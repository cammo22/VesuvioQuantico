from pathlib import Path
import os,json,base64,re
from html.parser import HTMLParser
from playwright.sync_api import sync_playwright
P=Path(__file__).parent
class Check(HTMLParser):
 def __init__(self): super().__init__();self.ids=[]
 def handle_starttag(self,t,a):
  for k,v in a:
   if k=='id':self.ids.append(v)
c=Check();c.feed((P/'index.html').read_text(encoding='utf-8'));assert len(c.ids)==len(set(c.ids))
with sync_playwright() as pw:
 browser=pw.chromium.launch(executable_path=os.environ.get('PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH'),headless=True)
 ctx=browser.new_context(accept_downloads=True,viewport={'width':1440,'height':1000});page=ctx.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto((P/'index.html').as_uri());page.wait_for_function('window.atlanteTest?.ready');assert page.locator('.card').count()==33;assert page.locator('.chapter').count()==16
 page.get_by_role('button',name='Ambientazioni',exact=True).click();assert page.locator('.card').count()==6
 page.get_by_role('button',name='Personaggi',exact=True).click();assert page.locator('.card').count()==27
 page.locator('#search').fill('Corriere veloce');page.wait_for_function("document.querySelectorAll('.card').length===1");assert page.locator('.card').count()==1
 page.locator('[data-note="cast-05"]').fill('Prova persistenza Cammo <test>');page.get_by_role('button',name='Salva note',exact=True).click()
 png=base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+j4n8AAAAASUVORK5CYII=')
 page.locator('[data-upload="cast-05"]').set_input_files({'name':'test.png','mimeType':'image/png','buffer':png});page.wait_for_selector('#cast-05 img')
 page.reload();page.wait_for_function('window.atlanteTest?.ready');assert page.locator('#cast-05 img').count()==1;assert page.locator('[data-note="cast-05"]').input_value()=='Prova persistenza Cammo <test>'
 with page.expect_download() as dl:page.locator('#export').click()
 path=P/'DaProd-Atlante-test-backup.json';dl.value.save_as(path);payload=json.loads(path.read_text());assert payload['records'][0]['image'].startswith('data:image/png')
 page.locator('[data-note="cast-05"]').fill('nota cambiata');page.locator('[data-save="cast-05"]').click()
 page.on('dialog',lambda d:d.accept());page.locator('#import').set_input_files(str(path));page.wait_for_function("document.querySelector('[data-note=\"cast-05\"]').value==='Prova persistenza Cammo <test>'")
 assert page.locator('#cast-05 img').count()==1
 page.locator('#import').set_input_files({'name':'bad.json','mimeType':'application/json','buffer':b'{invalid'});page.wait_for_function("document.querySelector('#status').textContent.includes('Importazione non eseguita')")
 assert page.locator('#cast-05 img').count()==1
 page.locator('#search').fill('nessuna-scheda');assert page.locator('#empty').is_visible();page.locator('#search').fill('')
 page.get_by_role('link',name='03 · Il libro').click();assert page.evaluate('location.hash')=='#libro'
 page.set_viewport_size({'width':390,'height':844});page.screenshot(path=str(P/'DaProd-Atlante-mobile.png'),full_page=False);assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
 page.get_by_role('link',name='02 · Esplora l’atlante').click();page.locator('#imagesOnly').check();assert page.locator('.card').count()==1
 page.set_viewport_size({'width':1440,'height':1000});page.screenshot(path=str(P/'DaProd-Atlante-desktop.png'),full_page=False)
 assert not errors,errors
 # All test data belong only to this isolated temporary browser context.
 print(json.dumps({'html_parser':'OK; ID statici univoci','schede':33,'capitoli':16,'filtri_ricerca_vuoto':'OK','upload_persistenza_reload':'OK','export_import_immagine_note':'OK','errore_json_senza_perdita':'OK','navigazione_hash':'OK','mobile_390_no_overflow':'OK','console_pageerrors':errors},ensure_ascii=False,indent=2))
 ctx.close();browser.close()
