# VesuvioQuantico · Atlante DaProd

[![Apri l’atlante](https://img.shields.io/badge/Atlante-Pages_in_attivazione-grey)](https://cammo22.github.io/VesuvioQuantico/)

**GitHub Pages in attivazione: link non ancora verificato.** Repository pubblica su autorizzazione di Cammo. Il sito e le fonti creative incluse sono pubblici.

Atlante italiano con 27 schede del cast robotico e 6 ambientazioni. Ogni scheda espone un prompt fotografico FLUX 3 in inglese, modificabile, copiabile e salvato automaticamente. FLUX 3 è solo un’etichetta di destinazione: nessuna API o parametro del modello viene presunto. I dettagli visivi sono proposte da approvare, non aggiunte al canone. I prompt H3 e Pika rimangono studi copiabili nei dettagli.

## Dati personali e backup

Le immagini caricate, note e personalizzazioni dei prompt restano nell’**IndexedDB del browser**: **NON sono sincronizzati con GitHub**, non finiscono nei commit e non sono incorporati nell’HTML. Non esiste un backend. I visitatori non condividono un database.

Per trasferire i dati dal file locale al sito, o tra browser/dispositivi, usa **Esporta backup JSON**, poi **Importa backup JSON** nella destinazione. Il file locale e il sito hanno archivi distinti; spostare un file può separare il suo archivio. Conserva il backup privatamente. L’import verifica i dati prima di sostituirli, richiede conferma e scarica una copia preventiva. I vecchi backup senza prompt restano compatibili e utilizzano il prompt originale. «Ripristina originale» richiede conferma e non cancella immagine o note.

Non caricare backup, immagini private o profili browser nella repository. `.gitignore` esclude i risultati temporanei dei test e i backup.

## Esecuzione e sviluppo

Apri `index.html` nel browser oppure servi questa cartella con `python -m http.server 8000`. Per rigenerare l’HTML: `python crea_atlante.py`. Python 3, nessuna dipendenza aggiuntiva per il generatore. I link delle fonti sono relativi a `fonti/`.

Test reali Playwright, in contesti temporanei isolati:

```sh
python -m pip install -r requirements-dev.txt
python -m playwright install chromium
python crea_atlante.py
python verifica_atlante.py
python verifica_prompt_atlante.py
```

In alternativa al Chromium scaricato, imposta `PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH` sul percorso del tuo Chrome/Chromium. I test non aprono il profilo personale e non usano Computer Use. Verificano filtri, 33 editor foto, prompt differenti, copia immediata, modifica/reload/upload, export/import con immagini e note, backup legacy, rifiuto di prompt invalidi, conferma/annullamento del ripristino, layout mobile e assenza di errori JavaScript.

## Fonti selezionate e pubblicazione

Solo quattro documenti creativi sono inclusi: regole DaProdUniverso, cast Napoli 2077 e i due trattamenti narrativi richiamati nell’atlante. Nessuna Home, istruzione operativa CLAUDE, wiki personale integrale o dato browser. I wikilink interni ai documenti sono riferimenti alla wiki originale: le destinazioni non selezionate non sono incluse. I documenti sono copie di consultazione; le fonti canoniche esterne non sono state modificate.

Pages usa il branch `main`, cartella `/`. La repository pubblica può usare Pages con GitHub Free; la precedente configurazione privata non lo consentiva. Nessun contenuto privato del browser viene pubblicato automaticamente.
