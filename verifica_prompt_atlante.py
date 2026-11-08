from pathlib import Path
import os,json,base64
from playwright.sync_api import sync_playwright
P=Path(__file__).parent
with sync_playwright() as pw:
 b=pw.chromium.launch(executable_path=os.environ.get('PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH'),headless=True)
 ctx=b.new_context(accept_downloads=True);p=ctx.new_page();errors=[];p.on('pageerror',lambda e:errors.append(str(e)))
 p.goto((P/'index.html').as_uri());p.wait_for_function('window.atlanteTest?.ready')
 assert p.locator('[data-photo]').count()==33
 prompts=p.locator('[data-photo]').evaluate_all('(els)=>els.map(e=>e.value)')
 assert len(set(prompts))==33
 assert p.locator('[data-photo]').evaluate_all('(els)=>els.every(e=>!e.closest("details"))')
 cards=p.evaluate('window.atlanteTest.cards');assert len(cards)==33
 for c in cards:
  assert c['title'] in c['prompts']['FLUX 3'] or c['kind']=='Ambientazioni' or c['id'].startswith('cast-')
  if c['kind']=='Ambientazioni':assert 'unoccupied foreground' in c['prompts']['FLUX 3'] and 'maintenance android' not in c['prompts']['FLUX 3']
 # Intercept clipboard to verify copy uses live field, without waiting for save.
 p.evaluate('window.copied="";Object.defineProperty(navigator,"clipboard",{value:{writeText:async text=>{window.copied=text}},configurable:true})')
 p.locator('[data-photo="cast-05"]').fill('Custom courier photo <Cammo> & mint scooter')
 p.locator('[data-copy="cast-05"][data-model="FLUX 3"]').click()
 assert p.evaluate('window.copied')=='Custom courier photo <Cammo> & mint scooter'
 p.locator('[data-photo="cast-21"]').fill('Custom guard dog photo with bronze paws')
 p.get_by_role('button',name='Ambientazioni',exact=True).click();assert p.locator('[data-photo]').count()==6
 p.locator('[data-photo="porto"]').fill('Custom harbour photograph, empty quay')
 p.get_by_role('button',name='Tutti',exact=True).click()
 p.reload();p.wait_for_function('window.atlanteTest?.ready')
 assert p.locator('[data-photo="cast-05"]').input_value()=='Custom courier photo <Cammo> & mint scooter'
 assert p.locator('[data-photo="cast-21"]').input_value()=='Custom guard dog photo with bronze paws'
 assert p.locator('[data-photo="porto"]').input_value()=='Custom harbour photograph, empty quay'
 p.locator('[data-note="cast-05"]').fill('Keep existing note')
 png=base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+j4n8AAAAASUVORK5CYII=')
 p.locator('[data-photo="cast-05"]').fill('Immediate upload prompt')
 p.locator('[data-upload="cast-05"]').set_input_files({'name':'pixel.png','mimeType':'image/png','buffer':png});p.wait_for_selector('#cast-05 img')
 assert p.locator('[data-photo="cast-05"]').input_value()=='Immediate upload prompt'
 with p.expect_download() as dl:p.locator('#export').click()
 path=P/'DaProd-Atlante-test-prompts.json';dl.value.save_as(path);payload=json.loads(path.read_text())
 row=next(r for r in payload['records'] if r['id']=='cast-05');assert row['prompt']=='Immediate upload prompt' and row['note']=='Keep existing note' and row['image']
 p.locator('[data-photo="cast-05"]').fill('Changed after export')
 accept=lambda d:d.accept()
 p.on('dialog',accept);p.locator('#import').set_input_files(str(path));p.wait_for_function('document.querySelector("[data-photo=cast-05]").value==="Immediate upload prompt"')
 assert p.locator('#cast-05 img').count()==1
 # Reject each invalid prompt type/size without altering data.
 for invalid in ['',42,'x'*20001,'bad\x00prompt',{}]:
  bad=json.loads(json.dumps(payload));bad['records'][0]['prompt']=invalid
  result=p.evaluate('async v=>{try{await atlanteTest.importBackup(v);return false}catch{return true}}',bad);assert result
 assert p.locator('[data-photo="cast-05"]').input_value()=='Immediate upload prompt'
 old=json.loads(json.dumps(payload))
 for r in old['records']:r.pop('prompt',None)
 p.locator('#import').set_input_files({'name':'legacy.json','mimeType':'application/json','buffer':json.dumps(old).encode()})
 p.wait_for_function('document.querySelector("[data-photo=cast-05]").value.startsWith("PROPOSED")')
 assert p.locator('#cast-05 img').count()==1 and p.locator('[data-note="cast-05"]').input_value()=='Keep existing note'
 original=p.locator('[data-photo="cast-05"]').input_value()
 p.locator('[data-photo="cast-05"]').fill('Reset me')
 # Replace accepting handler with a one-shot dismissal to verify cancellation.
 p.remove_listener('dialog',accept);p.once('dialog',lambda d:d.dismiss());p.locator('[data-reset-photo="cast-05"]').click();assert p.locator('[data-photo="cast-05"]').input_value()=='Reset me'
 p.once('dialog',lambda d:d.accept());p.locator('[data-reset-photo="cast-05"]').click();p.wait_for_function('document.querySelector("[data-photo=cast-05]").value.startsWith("PROPOSED")');assert p.locator('[data-photo="cast-05"]').input_value()==original
 assert not errors,errors
 report={'editor_foto_visibili':33,'prompt_individualizzati_unici':33,'ambientazioni_senza_robot_foreground':6,'copia_testo_immediato':'OK','edit_reload_filtri_upload':'OK','export_import_prompt_note_immagini':'OK','backup_precedente_senza_prompt':'OK','validazione_5_prompt_invalidi':'OK','ripristino_conferma_annulla':'OK','pageerrors':errors}
 (P/'DaProd-Atlante-test-prompts-risultati.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(report,ensure_ascii=False,indent=2));ctx.close();b.close()
