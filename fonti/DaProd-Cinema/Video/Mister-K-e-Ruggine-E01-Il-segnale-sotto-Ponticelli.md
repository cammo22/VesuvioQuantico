---
tipo: video
sottotipo: episodio-serie
titolo: "Mister K e Ruggine — E01: Il terzo segnale"
serie: "Mister K e Ruggine"
episodio: 1
divisione: "[[DaProd-Cinema]]"
regista: "[[People/Cammo|Cammo]]"
autore: "[[People/Babbasone|Babbasone]]"
universo: "[[DaProd-Produzioni/DaProdUniverso|DaProdUniverso]]"
modello: "MiniMax H3 — WanGP"
variante: FL2VA
reference_images: false
durata_target: "30:00"
durata_clip: "15 s / 360 frame a 24 fps"
clip_totali: 120
clip_autonome: 115
dipendenze_video: 5
stato: pronto-da-generare
aggiornato: 2026-08-05
tags: [daprod, cinema, serie-tv, episodio-pilota, minimax-h3, wangp, fl2va, text-to-video, ponticelli, mister-k, ruggine]
---

# 🎬 Mister K e Ruggine — E01: Il terzo segnale

> [!abstract] Logline
> Un blackout impossibile costringe il metodico Mister K e il gigantesco Ruggine a inseguire un terzo segnale sotto Ponticelli. Un mariuolo, una funzionaria e un boss di quartiere finiscono nella stessa squadra quando una sfera cromata prova a trasformare la rete elettrica della città in una chiamata verso qualcosa che risponde.

> [!important] Questa è una puntata TV, non una catena tecnica
> **115 clip sono autonome e si generano solo da testo.** Soltanto **5 clip su 120** dipendono dal video immediatamente precedente, nei cinque raccordi fisici indicati come `DIPENDENZA N/5`. La storia evolve perché ogni prompt contiene il proprio momento di copione, non perché eredita automaticamente la generazione prima.

## ✅ Configurazione WanGP

| Campo | Valore |
|---|---|
| Modello | MiniMax H3 pruned 20B |
| Variante | **FL2VA — text-to-video** |
| Immagini in ingresso | **Nessuna** |
| Durata | 15 s / 360 frame / 24 fps |
| Step | 20 consigliati; minimo 15 |
| Write H3 Prompt | Disabled |
| Prompt box | un solo blocco per generazione |

> [!warning] Se WanGP resta a 294 frame
> 294 frame a 24 fps producono circa 12,2 s. Per ottenere i **30:00 stabiliti** usa 360 frame / 15 s; 120 clip da 15 s producono 1.800 secondi.

## 🎭 Cast dell’episodio

| Personaggio | Funzione TV | Identità visiva |
|---|---|---|
| **Mister K** | protagonista metodico; risolve con precisione | robot nero compatto, mantello carbone, luci ciano, antenna radio |
| **Ruggine** | coprotagonista letterale e gentile; risolve con massa | colosso arancione, pistoni esposti, pugni idraulici |
| **Gina Relè** | funzionaria municipale e coordinatrice | piccola robot turchese/crema, cornetta in rame, tre lampade analogiche |
| **Vico-9** | mariuolo nervoso che ottiene una seconda possibilità | robot sottile arrugginito, testa CRT verde, giacca blu, borsa rossa |
| **Prefetto Ottone** | potere del quartiere; antagonista ambiguo e alleato finale | robomafioso ottone/nero, due fessure ambrate, cappotto crema |

## 📺 Struttura televisiva

| Blocco | Timecode | Clip | Funzione |
|---|---:|---:|---|
| COLD OPEN | 00:00–02:00 | 001–008 | Presentazione immediata dei protagonisti e incidente scatenante |
| SIGLA | 02:00–03:00 | 009–012 | Presentazioni iconiche, mondo e identità della serie |
| ATTO I — La chiamata | 03:00–08:00 | 013–032 | Missione, mondo quotidiano e primi sospetti |
| ATTO II — Sotto la città | 08:00–13:00 | 033–052 | Inseguimento, alleanza forzata e verità sul furto |
| ATTO III — Il quartiere mente | 13:00–18:00 | 053–072 | Confronto con Ottone, ribaltamento e minaccia manifesta |
| ATTO IV — La torre | 18:00–23:00 | 073–092 | Viaggio, assedio della torre e blackout totale |
| ATTO V — La scelta | 23:00–28:00 | 093–112 | Decisione morale, piano corale, climax e risoluzione |
| EPILOGO E TITOLI | 28:00–30:00 | 113–120 | Payoff dei personaggi, chiusura emotiva, credits e cliffhanger |

## 🔗 Le sole 5 dipendenze ammesse

| Dipendenza | Clip | Usa | Motivo |
|---:|---:|---:|---|
| 1/5 | 006 | Clip 005 | stessa tazzina sospesa durante il blackout |
| 2/5 | 034 | Clip 033 | stessa saracinesca che sta cadendo |
| 3/5 | 057 | Clip 056 | stesso tavolo durante il crollo della piazza |
| 4/5 | 087 | Clip 086 | stesso mast spezzato dall’impulso |
| 5/5 | 112 | Clip 111 | stessa azione corale che genera l’onda finale |

## 📝 Registro generazioni

| Clip | Data | Seed | Esito | Correzione successiva |
|---:|---|---|---|---|
| 001/120 |  |  |  |  |

> [!tip] Metodo pratico
> Genera e valuta ogni clip da solo. Nei cinque raccordi dipendenti usa il video indicato soltanto se è stato approvato; se il raccordo non funziona, lo stesso prompt resta abbastanza completo da poter essere rigenerato autonomamente da testo.


---

## COLD OPEN · 00:00–02:00

### ☐ 001/120 · 00:00–00:15 · COLD OPEN — Il caffè delle sette

**In una riga:** Una sveglia meccanica avvia da sola il vecchio bar di Ponticelli.

**Funzione:** Presentazione immediata dei protagonisti e incidente scatenante

**Controlla:** Mister K appare preciso e rapido; il café è già un personaggio.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Mister K slaps a brass alarm clock silent, slides beneath a leaking espresso machine and catches the first boiling drop in a tiny cup as the camera follows the drop from pipe to saucer. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Café machinery, rain on sheet metal, espresso pressure, hydraulic footsteps, relay clicks and deep volcanic rumble. non_diegetic_music: N/A
```

### ☐ 002/120 · 00:15–00:30 · COLD OPEN — Quello che aggiusta tutto

**In una riga:** Mister K ripara la macchina prima che arrivi il cliente.

**Funzione:** Presentazione immediata dei protagonisti e incidente scatenante

**Controlla:** La personalità asciutta emerge da gesto e battuta.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Mister K tightens one copper valve with two narrow fingers, spins the pressure wheel and produces a perfect espresso while the camera pushes from the repaired joint to his cyan optical lights. <d>[Italian] Mister K: "Anche oggi non è esplosa."</d> Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Café machinery, rain on sheet metal, espresso pressure, hydraulic footsteps, relay clicks and deep volcanic rumble. non_diegetic_music: N/A
```

### ☐ 003/120 · 00:30–00:45 · COLD OPEN — Un cliente troppo grande

**In una riga:** Ruggine si presenta entrando nel modo peggiore possibile.

**Funzione:** Presentazione immediata dei protagonisti e incidente scatenante

**Controlla:** Ruggine è enorme ma prova davvero a essere delicato.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Ruggine bends sideways through the narrow café doorway, carefully lifts the lintel with one hand and places it back after entering while Mister K protects the espresso cup. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Café machinery, rain on sheet metal, espresso pressure, hydraulic footsteps, relay clicks and deep volcanic rumble. non_diegetic_music: N/A
```

### ☐ 004/120 · 00:45–01:00 · COLD OPEN — La sedia numero sette

**In una riga:** La prima gag mostra il rapporto tra i due.

**Funzione:** Presentazione immediata dei protagonisti e incidente scatenante

**Controlla:** Tempo comico secco, due silhouette nello stesso quadro.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Ruggine lowers onto a welded stool that compresses into a flat disk while Mister K calmly moves the cup ten centimeters away. <d>[Italian] Ruggine: "Era già bassa." Mister K: "Adesso è sincera."</d> Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Café machinery, rain on sheet metal, espresso pressure, hydraulic footsteps, relay clicks and deep volcanic rumble. non_diegetic_music: N/A
```

### ☐ 005/120 · 01:00–01:15 · COLD OPEN — Il battito sotto il pavimento

**In una riga:** Tre colpi interrompono la colazione.

**Funzione:** Presentazione immediata dei protagonisti e incidente scatenante

**Controlla:** I tre colpi devono essere distinti e fisici.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Mister K places the cup on the counter as three metallic knocks travel beneath the floor; Ruggine kneels and the tiles pulse cyan around one massive fist while the camera drops to ground level. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Café machinery, rain on sheet metal, espresso pressure, hydraulic footsteps, relay clicks and deep volcanic rumble. non_diegetic_music: N/A
```

### ☐ 006/120 · 01:15–01:30 · COLD OPEN — La tazzina sospesa

**In una riga:** Il blackout investe il bar nello stesso istante.

**Funzione:** Presentazione immediata dei protagonisti e incidente scatenante

**Controlla:** Dipendenza 1/5: stessa tazzina, stesso impulso e stessa posizione.

**Generazione:** **DIPENDENZA 1/5** — usa il video approvato del Clip 005 come continuazione sliding-window FL2VA.

```text
integrated_multimodal_description: [Shot 1] The cyan floor pulse lifts the espresso cup into the air as every café lamp shuts off; Ruggine catches the cup while Mister K catches the saucer, continuing directly from clip 005. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. Continue directly from the accepted final physical state of clip 005, preserving the stated object, character positions and ongoing motion. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Café machinery, rain on sheet metal, espresso pressure, hydraulic footsteps, relay clicks and deep volcanic rumble. non_diegetic_music: N/A
```

### ☐ 007/120 · 01:30–01:45 · COLD OPEN — La città si spegne

**In una riga:** Il problema supera subito il café.

**Funzione:** Presentazione immediata dei protagonisti e incidente scatenante

**Controlla:** Scala cittadina leggibile, niente confusione con un normale blackout.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Mister K opens the bent doorway and watches entire Ponticelli blocks lose power in a wave while Ruggine holds the rescued cup; orange lava becomes the only broad city light. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Café machinery, rain on sheet metal, espresso pressure, hydraulic footsteps, relay clicks and deep volcanic rumble. non_diegetic_music: N/A
```

### ☐ 008/120 · 01:45–02:00 · COLD OPEN — Il terzo segnale

**In una riga:** Un vecchio ricevitore indica qualcosa che non dovrebbe esistere.

**Funzione:** Presentazione immediata dei protagonisti e incidente scatenante

**Controlla:** Cold open chiude con domanda concreta e destinazione visibile.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Mister K connects a folding analog receiver to the floor cable; three bulbs ignite, the first two fade and the third points toward a distant antenna tower while Ruggine sets the cup down. <d>[Italian] Mister K: "Questo segnale non è della città."</d> Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Café machinery, rain on sheet metal, espresso pressure, hydraulic footsteps, relay clicks and deep volcanic rumble. non_diegetic_music: Original short mystery sting with one low metallic chord and three synchronized knocks.
```


---

## SIGLA · 02:00–03:00

### ☐ 009/120 · 02:00–02:15 · SIGLA — Mister K in quattro mosse

**In una riga:** La sigla presenta precisione, agilità e ironia di Mister K.

**Funzione:** Presentazioni iconiche, mondo e identità della serie

**Controlla:** Montaggio iconico; quattro azioni leggibili, nessuna trama da seguire.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Mister K swings beneath rusted tram cables, lands on wet cobblestones, repairs a sparking relay with one hand and catches an espresso cup with the other as the camera cuts on each precise impact. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Original television-theme sound design blended with volcanic booms, tram bells, analog relays and synchronized metallic impacts. non_diegetic_music: Original energetic Italian television opening theme with heroic rhythm, bright retro-futurist melody and industrial percussion.
```

### ☐ 010/120 · 02:15–02:30 · SIGLA — Ruggine sposta il quartiere

**In una riga:** La sigla presenta forza, peso e gentilezza di Ruggine.

**Funzione:** Presentazioni iconiche, mondo e identità della serie

**Controlla:** La forza serve a proteggere, non solo distruggere.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Ruggine lifts a collapsed balcony, lets three tiny service robots pass underneath, places the balcony back and gives them a careful wave while lava light rolls across rust-orange armor. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Original television-theme sound design blended with volcanic booms, tram bells, analog relays and synchronized metallic impacts. non_diegetic_music: Original energetic Italian television opening theme with heroic rhythm, bright retro-futurist melody and industrial percussion.
```

### ☐ 011/120 · 02:30–02:45 · SIGLA — Ponticelli ha ancora corrente

**In una riga:** La sigla mostra il cast e il mondo della serie.

**Funzione:** Presentazioni iconiche, mondo e identità della serie

**Controlla:** Presentazioni rapide ma visivamente diverse.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Gina Relè races through Ponticelli on a mint utility scooter, Vico-9 jumps across aqua market awnings, Prefetto Ottone watches from a brass balcony, and the mirror-chrome sphere rolls through their reflections as the erupting Vesuvius fills the skyline. Gina Relè is a petite turquoise municipal dispatcher robot with a cream enamel shell, a copper rotary-phone receiver mounted on one shoulder, three analog status lamps and brisk authoritative gestures. Vico-9 is a thin rusted street robot with a square green CRT display head, a patched blue jacket, a red satchel and quick nervous movements. Prefetto Ottone is a massive brass-and-black robomafioso robot with broad shoulders, two narrow amber optical slits, an immaculate cream overcoat and slow controlled movements. The signal entity appears only as a palm-sized flawless mirror-chrome sphere, physical, silent and highly reflective. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Original television-theme sound design blended with volcanic booms, tram bells, analog relays and synchronized metallic impacts. non_diegetic_music: Original energetic Italian television opening theme with heroic rhythm, bright retro-futurist melody and industrial percussion.
```

### ☐ 012/120 · 02:45–03:00 · SIGLA — Mister K e Ruggine

**In una riga:** La sigla chiude sull’immagine della coppia e sullo spazio per il titolo in post.

**Funzione:** Presentazioni iconiche, mondo e identità della serie

**Controlla:** Composizione pulita per aggiungere logo e titolo in montaggio.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Mister K and Ruggine stand back to back on a wet rooftop while a circular chrome plate with abstract embossed shapes rotates behind them; lightning strikes the Vesuvian antenna grid and both turn toward the same off-screen alarm. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Original television-theme sound design blended with volcanic booms, tram bells, analog relays and synchronized metallic impacts. non_diegetic_music: Original energetic Italian television opening theme reaching its main resolving hook.
```


---

## ATTO I — La chiamata · 03:00–08:00

### ☐ 013/120 · 03:00–03:15 · ATTO I — La chiamata — Gina Relè non bussa

**In una riga:** La responsabile municipale entra nel bar con una missione urgente.

**Funzione:** Missione, mondo quotidiano e primi sospetti

**Controlla:** Ingresso energico e design di Gina subito riconoscibile.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Gina Relè drives a mint utility scooter through the already bent café doorway, brakes beside Mister K and unfolds a physical three-bulb map from her cream enamel chest. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Gina Relè is a petite turquoise municipal dispatcher robot with a cream enamel shell, a copper rotary-phone receiver mounted on one shoulder, three analog status lamps and brisk authoritative gestures. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Rainy street ambience, utility scooter motors, analog radio chatter, tram wheels, market shutters and intermittent power relays. non_diegetic_music: N/A
```

### ☐ 014/120 · 03:15–03:30 · ATTO I — La chiamata — Tre quartieri al buio

**In una riga:** Gina spiega la posta in gioco con oggetti, non con una lezione.

**Funzione:** Missione, mondo quotidiano e primi sospetti

**Controlla:** Il mistero evolve tramite una dimostrazione fisica.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Gina Relè places three miniature district relays on the counter; two recover, the third drains power into a black cable while Mister K measures it and Ruggine holds the counter steady. <d>[Italian] Gina Relè: "Qualcuno non ruba corrente. La chiama."</d> Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. Gina Relè is a petite turquoise municipal dispatcher robot with a cream enamel shell, a copper rotary-phone receiver mounted on one shoulder, three analog status lamps and brisk authoritative gestures. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Rainy street ambience, utility scooter motors, analog radio chatter, tram wheels, market shutters and intermittent power relays. non_diegetic_music: N/A
```

### ☐ 015/120 · 03:30–03:45 · ATTO I — La chiamata — La tariffa di Mister K

**In una riga:** Mister K finge di non voler accettare.

**Funzione:** Missione, mondo quotidiano e primi sospetti

**Controlla:** Dialogo breve che stabilisce il ruolo di Mister K.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Mister K closes the meter, slides the untouched espresso toward Gina Relè and turns away while Ruggine silently lifts the entire tool rack. <d>[Italian] Mister K: "Io aggiusto macchine, non misteri." Gina Relè: "Stavolta sono la stessa cosa."</d> Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. Gina Relè is a petite turquoise municipal dispatcher robot with a cream enamel shell, a copper rotary-phone receiver mounted on one shoulder, three analog status lamps and brisk authoritative gestures. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Rainy street ambience, utility scooter motors, analog radio chatter, tram wheels, market shutters and intermittent power relays. non_diegetic_music: N/A
```

### ☐ 016/120 · 03:45–04:00 · ATTO I — La chiamata — Ruggine ha già accettato

**In una riga:** Ruggine rende inevitabile la missione.

**Funzione:** Missione, mondo quotidiano e primi sospetti

**Controlla:** Gag e decisione narrativa nello stesso gesto.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Ruggine clips a tiny municipal badge onto one enormous armor plate and tries to leave through the original doorway; the frame bends again. <d>[Italian] Ruggine: "Ho preso il distintivo." Mister K: "Quello era un gettone."</d> Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Rainy street ambience, utility scooter motors, analog radio chatter, tram wheels, market shutters and intermittent power relays. non_diegetic_music: N/A
```

### ☐ 017/120 · 04:00–04:15 · ATTO I — La chiamata — Il kit da indagine

**In una riga:** La coppia si prepara con metodi opposti.

**Funzione:** Missione, mondo quotidiano e primi sospetti

**Controlla:** Contrasto di carattere leggibile senza dipendenze.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Mister K selects a cable spool, brass meter and folding map while Ruggine loads a generator, ladder and entire steel cabinet onto one shoulder; the camera compares both loads. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Rainy street ambience, utility scooter motors, analog radio chatter, tram wheels, market shutters and intermittent power relays. non_diegetic_music: N/A
```

### ☐ 018/120 · 04:15–04:30 · ATTO I — La chiamata — Uscita di servizio

**In una riga:** La missione comincia davvero.

**Funzione:** Missione, mondo quotidiano e primi sospetti

**Controlla:** Uscita corale pulita, ritmo da inizio atto.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Mister K walks through the café door, Gina Relè exits on the scooter and Ruggine carefully uses the wall opening beside them while the restored bell rings once. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. Gina Relè is a petite turquoise municipal dispatcher robot with a cream enamel shell, a copper rotary-phone receiver mounted on one shoulder, three analog status lamps and brisk authoritative gestures. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Rainy street ambience, utility scooter motors, analog radio chatter, tram wheels, market shutters and intermittent power relays. non_diegetic_music: N/A
```

### ☐ 019/120 · 04:30–04:45 · ATTO I — La chiamata — La strada che beve luce

**In una riga:** Il trio vede l’anomalia in città.

**Funzione:** Missione, mondo quotidiano e primi sospetti

**Controlla:** Energia che si muove in direzione sbagliata.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Mister K touches the meter to a wet tram rail as cyan current flows backward into a storm drain; Gina Relè marks the route with a physical flag and Ruggine lifts the overhead cable. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. Gina Relè is a petite turquoise municipal dispatcher robot with a cream enamel shell, a copper rotary-phone receiver mounted on one shoulder, three analog status lamps and brisk authoritative gestures. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Rainy street ambience, utility scooter motors, analog radio chatter, tram wheels, market shutters and intermittent power relays. non_diegetic_music: N/A
```

### ☐ 020/120 · 04:45–05:00 · ATTO I — La chiamata — Il tram senza conducente

**In una riga:** Un tram riattivato da solo taglia loro la strada.

**Funzione:** Missione, mondo quotidiano e primi sospetti

**Controlla:** Azione urbana forte ma con traiettorie chiare.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] An empty aqua-and-rust tram accelerates through the intersection; Mister K jumps onto its side ladder while Ruggine plants both palms against the rear and Gina Relè follows on the scooter. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. Gina Relè is a petite turquoise municipal dispatcher robot with a cream enamel shell, a copper rotary-phone receiver mounted on one shoulder, three analog status lamps and brisk authoritative gestures. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Rainy street ambience, utility scooter motors, analog radio chatter, tram wheels, market shutters and intermittent power relays. non_diegetic_music: N/A
```

### ☐ 021/120 · 05:00–05:15 · ATTO I — La chiamata — Frenata municipale

**In una riga:** Mister K ferma il tram usando il circuito.

**Funzione:** Missione, mondo quotidiano e primi sospetti

**Controlla:** Mister K risolve con precisione; Ruggine con massa.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Mister K opens the exterior brake box, bridges two contacts with the brass meter and makes the tram stop exactly before a collapsed kiosk while Ruggine absorbs the final push. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Rainy street ambience, utility scooter motors, analog radio chatter, tram wheels, market shutters and intermittent power relays. non_diegetic_music: N/A
```

### ☐ 022/120 · 05:15–05:30 · ATTO I — La chiamata — Il biglietto impossibile

**In una riga:** Dentro il tram compare la prima traccia del colpevole.

**Funzione:** Missione, mondo quotidiano e primi sospetti

**Controlla:** Oggetto-indizio chiaro, nessuna scritta leggibile.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Gina Relè opens the tram validator and removes a fresh brass token stamped only with three raised circles while Mister K and Ruggine examine its warm edges. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. Gina Relè is a petite turquoise municipal dispatcher robot with a cream enamel shell, a copper rotary-phone receiver mounted on one shoulder, three analog status lamps and brisk authoritative gestures. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Rainy street ambience, utility scooter motors, analog radio chatter, tram wheels, market shutters and intermittent power relays. non_diegetic_music: N/A
```

### ☐ 023/120 · 05:30–05:45 · ATTO I — La chiamata — Archivio a schede

**In una riga:** Gina consulta la memoria fisica del municipio.

**Funzione:** Missione, mondo quotidiano e primi sospetti

**Controlla:** Tecnologia retro avanzata e informazione visiva.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Gina Relè feeds the three-circle token into a rotary card archive inside a street booth; one metal card slides out showing a route from the market to the old underpass. Gina Relè is a petite turquoise municipal dispatcher robot with a cream enamel shell, a copper rotary-phone receiver mounted on one shoulder, three analog status lamps and brisk authoritative gestures. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Rainy street ambience, utility scooter motors, analog radio chatter, tram wheels, market shutters and intermittent power relays. non_diegetic_music: N/A
```

### ☐ 024/120 · 05:45–06:00 · ATTO I — La chiamata — Il nome sul retro

**In una riga:** Un segno riconoscibile porta a Vico-9.

**Funzione:** Missione, mondo quotidiano e primi sospetti

**Controlla:** Prima apparizione del sospetto in profondità di campo.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Mister K turns the metal card over and finds a small square CRT-shaped punch mark; Ruggine points toward a distant market where a thin CRT-headed robot slips behind a shutter. <d>[Italian] Gina Relè: "Vico-9."</d> Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. Gina Relè is a petite turquoise municipal dispatcher robot with a cream enamel shell, a copper rotary-phone receiver mounted on one shoulder, three analog status lamps and brisk authoritative gestures. Vico-9 is a thin rusted street robot with a square green CRT display head, a patched blue jacket, a red satchel and quick nervous movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Rainy street ambience, utility scooter motors, analog radio chatter, tram wheels, market shutters and intermittent power relays. non_diegetic_music: N/A
```

### ☐ 025/120 · 06:00–06:15 · ATTO I — La chiamata — L’uomo che non esiste

**In una riga:** Mister K chiarisce cosa pensa dei mariuoli.

**Funzione:** Missione, mondo quotidiano e primi sospetti

**Controlla:** Dialogo da buddy series durante movimento concreto.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Mister K folds the card into the map while walking beside Ruggine through rain. <d>[Italian] Ruggine: "È un ladro?" Mister K: "È un commerciante che dimentica di pagare."</d> Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Rainy street ambience, utility scooter motors, analog radio chatter, tram wheels, market shutters and intermittent power relays. non_diegetic_music: N/A
```

### ☐ 026/120 · 06:15–06:30 · ATTO I — La chiamata — Il mercato chiude presto

**In una riga:** Le serrande si abbassano al loro arrivo.

**Funzione:** Missione, mondo quotidiano e primi sospetti

**Controlla:** Il quartiere reagisce alla loro presenza.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Market shutters slam down one after another as Mister K, Ruggine and Gina Relè enter the flooded square; the camera tracks backward through stalls lit by failing aqua lamps. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. Gina Relè is a petite turquoise municipal dispatcher robot with a cream enamel shell, a copper rotary-phone receiver mounted on one shoulder, three analog status lamps and brisk authoritative gestures. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Rainy street ambience, utility scooter motors, analog radio chatter, tram wheels, market shutters and intermittent power relays. non_diegetic_music: N/A
```

### ☐ 027/120 · 06:30–06:45 · ATTO I — La chiamata — Occhi dietro i vetri

**In una riga:** I robot del mercato osservano senza intervenire.

**Funzione:** Missione, mondo quotidiano e primi sospetti

**Controlla:** Popolazione robotica viva, solo macchine fisiche.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Small service robots and rusted workers peek through aqua shop glass while Ruggine lifts a fallen awning and Mister K follows the meter pulse beneath it. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Rainy street ambience, utility scooter motors, analog radio chatter, tram wheels, market shutters and intermittent power relays. non_diegetic_music: N/A
```

### ☐ 028/120 · 06:45–07:00 · ATTO I — La chiamata — Il banco vuoto

**In una riga:** Vico-9 ha lasciato una trappola semplice.

**Funzione:** Missione, mondo quotidiano e primi sospetti

**Controlla:** Tono leggero, trappola concreta.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Mister K opens an abandoned market crate and a spring-loaded chrome spoon strikes the meter from his hand; Ruggine catches the meter before it hits water. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Rainy street ambience, utility scooter motors, analog radio chatter, tram wheels, market shutters and intermittent power relays. non_diegetic_music: N/A
```

### ☐ 029/120 · 07:00–07:15 · ATTO I — La chiamata — La voce dal tombino

**In una riga:** Vico provoca la coppia da sotto la strada.

**Funzione:** Missione, mondo quotidiano e primi sospetti

**Controlla:** Vico è agile, nervoso e riconoscibile.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Vico-9 lifts a storm-drain cover just enough to show the green CRT head, rings a stolen tram bell and disappears as Mister K turns. <d>[Italian] Vico-9: "State seguendo il cavo sbagliato."</d> Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Vico-9 is a thin rusted street robot with a square green CRT display head, a patched blue jacket, a red satchel and quick nervous movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Rainy street ambience, utility scooter motors, analog radio chatter, tram wheels, market shutters and intermittent power relays. non_diegetic_music: N/A
```

### ☐ 030/120 · 07:15–07:30 · ATTO I — La chiamata — Ruggine prende la misura

**In una riga:** Ruggine prova a passare dal tombino.

**Funzione:** Missione, mondo quotidiano e primi sospetti

**Controlla:** Gag fisica che apre la discesa.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Ruggine measures the circular storm drain against one hydraulic fist, then lifts the entire surrounding paving slab instead while Mister K steps onto the exposed stair. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Rainy street ambience, utility scooter motors, analog radio chatter, tram wheels, market shutters and intermittent power relays. non_diegetic_music: N/A
```

### ☐ 031/120 · 07:30–07:45 · ATTO I — La chiamata — La scala sotto il mercato

**In una riga:** La squadra entra nel sottosuolo.

**Funzione:** Missione, mondo quotidiano e primi sospetti

**Controlla:** Passaggio d’ambiente chiaro e autonomo.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Mister K descends the wet service stair with the meter, Gina Relè follows with three status lamps glowing and Ruggine lowers the paving slab behind them before climbing down. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. Gina Relè is a petite turquoise municipal dispatcher robot with a cream enamel shell, a copper rotary-phone receiver mounted on one shoulder, three analog status lamps and brisk authoritative gestures. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Rainy street ambience, utility scooter motors, analog radio chatter, tram wheels, market shutters and intermittent power relays. non_diegetic_music: N/A
```

### ☐ 032/120 · 07:45–08:00 · ATTO I — La chiamata — Il segnale respira

**In una riga:** L’atto chiude con una presenza meccanica viva.

**Funzione:** Missione, mondo quotidiano e primi sospetti

**Controlla:** Fine atto su movimento concreto che arriva verso i protagonisti.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] At the bottom of the underpass, Mister K raises the meter as three cyan pulses move through black floodwater toward them; Ruggine braces and Gina Relè's lamps answer in the same rhythm. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. Gina Relè is a petite turquoise municipal dispatcher robot with a cream enamel shell, a copper rotary-phone receiver mounted on one shoulder, three analog status lamps and brisk authoritative gestures. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Rainy street ambience, utility scooter motors, analog radio chatter, tram wheels, market shutters and intermittent power relays. non_diegetic_music: Original brief suspense sting ending on three low metallic knocks.
```


---

## ATTO II — Sotto la città · 08:00–13:00

### ☐ 033/120 · 08:00–08:15 · ATTO II — Sotto la città — La corsa nell’acqua

**In una riga:** Vico fugge lungo il sottopasso allagato.

**Funzione:** Inseguimento, alleanza forzata e verità sul furto

**Controlla:** Inseguimento autonomo con soggetti e direzione chiari.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Vico-9 sprints along a narrow maintenance rail carrying a red satchel while Mister K follows with magnetic feet and Ruggine wades through black water behind them. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. Vico-9 is a thin rusted street robot with a square green CRT display head, a patched blue jacket, a red satchel and quick nervous movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Floodwater, chain echoes, magnetic footsteps, pump pistons, CRT buzz, relay knocks and subterranean volcanic vibration. non_diegetic_music: N/A
```

### ☐ 034/120 · 08:15–08:30 · ATTO II — Sotto la città — Il soffitto viene giù

**In una riga:** La fuga attiva un vecchio sistema di difesa.

**Funzione:** Inseguimento, alleanza forzata e verità sul furto

**Controlla:** Pericolo fisico leggibile, prepara la sola continuità.

**Generazione:** **DIPENDENZA 2/5** — usa il video approvato del Clip 033 come continuazione sliding-window FL2VA.

```text
integrated_multimodal_description: [Shot 1] Vico-9 pulls a rusted lever and concrete shutters begin dropping across the flooded tunnel as Mister K dives beneath the first barrier and Ruggine reaches for the second. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. Vico-9 is a thin rusted street robot with a square green CRT display head, a patched blue jacket, a red satchel and quick nervous movements. Continue directly from the accepted final physical state of clip 033, preserving the stated object, character positions and ongoing motion. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Floodwater, chain echoes, magnetic footsteps, pump pistons, CRT buzz, relay knocks and subterranean volcanic vibration. non_diegetic_music: N/A
```

### ☐ 035/120 · 08:30–08:45 · ATTO II — Sotto la città — La mano sotto la saracinesca

**In una riga:** Ruggine salva Mister K nello stesso movimento.

**Funzione:** Inseguimento, alleanza forzata e verità sul furto

**Controlla:** Dipendenza 2/5: posizione della saracinesca e dei personaggi.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Ruggine catches the falling concrete shutter inches above Mister K, continuing directly from clip 033, while Vico-9 slips through the next gate and Gina Relè drags the brass meter clear. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. Gina Relè is a petite turquoise municipal dispatcher robot with a cream enamel shell, a copper rotary-phone receiver mounted on one shoulder, three analog status lamps and brisk authoritative gestures. Vico-9 is a thin rusted street robot with a square green CRT display head, a patched blue jacket, a red satchel and quick nervous movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Floodwater, chain echoes, magnetic footsteps, pump pistons, CRT buzz, relay knocks and subterranean volcanic vibration. non_diegetic_music: N/A
```

### ☐ 036/120 · 08:45–09:00 · ATTO II — Sotto la città — Una domanda pesante

**In una riga:** Ruggine pretende una spiegazione da Vico.

**Funzione:** Inseguimento, alleanza forzata e verità sul furto

**Controlla:** Dialogo comico durante azione utile.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Ruggine lifts the next gate with both hands while Mister K aims the meter through the gap at Vico-9. <d>[Italian] Ruggine: "Perché corri?" Vico-9: "Perché tu cammini forte."</d> Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. Vico-9 is a thin rusted street robot with a square green CRT display head, a patched blue jacket, a red satchel and quick nervous movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Floodwater, chain echoes, magnetic footsteps, pump pistons, CRT buzz, relay knocks and subterranean volcanic vibration. non_diegetic_music: N/A
```

### ☐ 037/120 · 09:00–09:15 · ATTO II — Sotto la città — Il sacco rosso

**In una riga:** La chiave rubata si vede per la prima volta.

**Funzione:** Inseguimento, alleanza forzata e verità sul furto

**Controlla:** Chiave chiaramente visibile, nuova posta immediata.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Vico-9 jumps onto a floating maintenance trolley; the red satchel opens and a three-toothed brass relay key slides across the deck while Mister K reaches from the rail. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Vico-9 is a thin rusted street robot with a square green CRT display head, a patched blue jacket, a red satchel and quick nervous movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Floodwater, chain echoes, magnetic footsteps, pump pistons, CRT buzz, relay knocks and subterranean volcanic vibration. non_diegetic_music: N/A
```

### ☐ 038/120 · 09:15–09:30 · ATTO II — Sotto la città — Il tuffo della chiave

**In una riga:** L’indizio cade nell’acqua nera.

**Funzione:** Inseguimento, alleanza forzata e verità sul furto

**Controlla:** Un singolo oggetto guida l’inquadratura.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] The brass relay key slips from the trolley and sinks between submerged cables; Vico-9, Mister K and Ruggine all reach toward the same expanding ripple. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. Vico-9 is a thin rusted street robot with a square green CRT display head, a patched blue jacket, a red satchel and quick nervous movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Floodwater, chain echoes, magnetic footsteps, pump pistons, CRT buzz, relay knocks and subterranean volcanic vibration. non_diegetic_music: N/A
```

### ☐ 039/120 · 09:30–09:45 · ATTO II — Sotto la città — Chi arriva prima

**In una riga:** Mister K recupera la chiave con il cavo.

**Funzione:** Inseguimento, alleanza forzata e verità sul furto

**Controlla:** Azione precisa, nessun riferimento necessario.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Mister K launches the blue cable into the flood, hooks the brass key and pulls it onto the rail while Vico-9 tries to catch the returning line. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Vico-9 is a thin rusted street robot with a square green CRT display head, a patched blue jacket, a red satchel and quick nervous movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Floodwater, chain echoes, magnetic footsteps, pump pistons, CRT buzz, relay knocks and subterranean volcanic vibration. non_diegetic_music: N/A
```

### ☐ 040/120 · 09:45–10:00 · ATTO II — Sotto la città — La corrente sbagliata

**In una riga:** La chiave alimenta il tunnel invece di aprirlo.

**Funzione:** Inseguimento, alleanza forzata e verità sul furto

**Controlla:** Conseguenza sorprendente ma fisicamente causata.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Mister K inserts the key into a wall socket; cyan current races through transparent pipes and activates pumps in reverse, raising the water around Ruggine. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Floodwater, chain echoes, magnetic footsteps, pump pistons, CRT buzz, relay knocks and subterranean volcanic vibration. non_diegetic_music: N/A
```

### ☐ 041/120 · 10:00–10:15 · ATTO II — Sotto la città — Ruggine fa diga

**In una riga:** Il gigante protegge gli altri dalla piena.

**Funzione:** Inseguimento, alleanza forzata e verità sul furto

**Controlla:** Ruggine eroico, scala leggibile.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Ruggine plants both feet between tunnel walls and forms a barrier with a steel maintenance panel while Mister K, Gina Relè and Vico-9 climb onto the dry side. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. Gina Relè is a petite turquoise municipal dispatcher robot with a cream enamel shell, a copper rotary-phone receiver mounted on one shoulder, three analog status lamps and brisk authoritative gestures. Vico-9 is a thin rusted street robot with a square green CRT display head, a patched blue jacket, a red satchel and quick nervous movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Floodwater, chain echoes, magnetic footsteps, pump pistons, CRT buzz, relay knocks and subterranean volcanic vibration. non_diegetic_music: N/A
```

### ☐ 042/120 · 10:15–10:30 · ATTO II — Sotto la città — Gina conta i secondi

**In una riga:** La responsabile trova il comando delle pompe.

**Funzione:** Inseguimento, alleanza forzata e verità sul furto

**Controlla:** Tensione da procedura, non monologo.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Gina Relè opens a floor cabinet, rotates three analog timers and synchronizes their needles while water rises against Ruggine's shield. <d>[Italian] Gina Relè: "Quando dico tre, gira tutto."</d> Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. Gina Relè is a petite turquoise municipal dispatcher robot with a cream enamel shell, a copper rotary-phone receiver mounted on one shoulder, three analog status lamps and brisk authoritative gestures. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Floodwater, chain echoes, magnetic footsteps, pump pistons, CRT buzz, relay knocks and subterranean volcanic vibration. non_diegetic_music: N/A
```

### ☐ 043/120 · 10:30–10:45 · ATTO II — Sotto la città — Tre ruote insieme

**In una riga:** I quattro devono collaborare.

**Funzione:** Inseguimento, alleanza forzata e verità sul furto

**Controlla:** Prima azione davvero corale.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Mister K, Gina Relè and Vico-9 each turn one brass pump wheel as Ruggine releases the shield; the flood drops suddenly through grated channels. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. Gina Relè is a petite turquoise municipal dispatcher robot with a cream enamel shell, a copper rotary-phone receiver mounted on one shoulder, three analog status lamps and brisk authoritative gestures. Vico-9 is a thin rusted street robot with a square green CRT display head, a patched blue jacket, a red satchel and quick nervous movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Floodwater, chain echoes, magnetic footsteps, pump pistons, CRT buzz, relay knocks and subterranean volcanic vibration. non_diegetic_music: N/A
```

### ☐ 044/120 · 10:45–11:00 · ATTO II — Sotto la città — Il tunnel asciutto

**In una riga:** Il fondo rivela una pista nascosta.

**Funzione:** Inseguimento, alleanza forzata e verità sul furto

**Controlla:** Traccia della sfera visibile senza mostrarla ancora.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] As water drains, a trail of polished circular marks appears across the black stone floor; Mister K kneels beside them while Vico-9 closes the satchel. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Vico-9 is a thin rusted street robot with a square green CRT display head, a patched blue jacket, a red satchel and quick nervous movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Floodwater, chain echoes, magnetic footsteps, pump pistons, CRT buzz, relay knocks and subterranean volcanic vibration. non_diegetic_music: N/A
```

### ☐ 045/120 · 11:00–11:15 · ATTO II — Sotto la città — La moneta di Ottone

**In una riga:** Vico porta addosso il segno del mandante.

**Funzione:** Inseguimento, alleanza forzata e verità sul furto

**Controlla:** Indizio materiale, design coerente.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Ruggine picks a heavy brass coin from the drained channel and places it beside the three-toothed key; both carry the same two narrow amber grooves associated with Prefetto Ottone. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. Prefetto Ottone is a massive brass-and-black robomafioso robot with broad shoulders, two narrow amber optical slits, an immaculate cream overcoat and slow controlled movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Floodwater, chain echoes, magnetic footsteps, pump pistons, CRT buzz, relay knocks and subterranean volcanic vibration. non_diegetic_music: N/A
```

### ☐ 046/120 · 11:15–11:30 · ATTO II — Sotto la città — Vico non è il ladro giusto

**In una riga:** Il sospetto ammette solo metà della verità.

**Funzione:** Inseguimento, alleanza forzata e verità sul furto

**Controlla:** Confessione semplice con mistero ancora aperto.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Vico-9 sits on the trolley with both thin hands raised while Mister K holds the coin. <d>[Italian] Vico-9: "La chiave l'ho presa io. Il segnale mi ha trovato dopo."</d> Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Vico-9 is a thin rusted street robot with a square green CRT display head, a patched blue jacket, a red satchel and quick nervous movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Floodwater, chain echoes, magnetic footsteps, pump pistons, CRT buzz, relay knocks and subterranean volcanic vibration. non_diegetic_music: N/A
```

### ☐ 047/120 · 11:30–11:45 · ATTO II — Sotto la città — Il lavoro di Ottone

**In una riga:** Vico racconta il mandato ricevuto.

**Funzione:** Inseguimento, alleanza forzata e verità sul furto

**Controlla:** Esposizione visuale, niente testo generato.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Vico-9 projects a crude physical flipbook from the satchel showing Prefetto Ottone, the market generator and the relay key while Gina Relè turns each metal page by hand. Gina Relè is a petite turquoise municipal dispatcher robot with a cream enamel shell, a copper rotary-phone receiver mounted on one shoulder, three analog status lamps and brisk authoritative gestures. Vico-9 is a thin rusted street robot with a square green CRT display head, a patched blue jacket, a red satchel and quick nervous movements. Prefetto Ottone is a massive brass-and-black robomafioso robot with broad shoulders, two narrow amber optical slits, an immaculate cream overcoat and slow controlled movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Floodwater, chain echoes, magnetic footsteps, pump pistons, CRT buzz, relay knocks and subterranean volcanic vibration. non_diegetic_music: N/A
```

### ☐ 048/120 · 11:45–12:00 · ATTO II — Sotto la città — Proteggere il quartiere

**In una riga:** Il presunto cattivo aveva una motivazione concreta.

**Funzione:** Inseguimento, alleanza forzata e verità sul furto

**Controlla:** Motivazione ambigua, non villain piatto.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Vico-9 points to a miniature market generator on the flipbook as its lamps go dark. <d>[Italian] Vico-9: "Ottone voleva luce per il mercato. Solo per il mercato."</d> Vico-9 is a thin rusted street robot with a square green CRT display head, a patched blue jacket, a red satchel and quick nervous movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Floodwater, chain echoes, magnetic footsteps, pump pistons, CRT buzz, relay knocks and subterranean volcanic vibration. non_diegetic_music: N/A
```

### ☐ 049/120 · 12:00–12:15 · ATTO II — Sotto la città — I tre colpi tornano

**In una riga:** La sfera interrompe l’interrogatorio.

**Funzione:** Inseguimento, alleanza forzata e verità sul furto

**Controlla:** Ritorno del motivo sonoro, causa visibile.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Three metallic knocks sound beneath the drained tunnel and the brass coin rotates by itself toward a side conduit while Mister K raises the meter. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Floodwater, chain echoes, magnetic footsteps, pump pistons, CRT buzz, relay knocks and subterranean volcanic vibration. non_diegetic_music: N/A
```

### ☐ 050/120 · 12:15–12:30 · ATTO II — Sotto la città — Il riflesso che manca

**In una riga:** La sfera appare solo nell’acqua rimasta.

**Funzione:** Inseguimento, alleanza forzata e verità sul furto

**Controlla:** Prima apparizione inquietante ma concreta.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] A palm-sized mirror-chrome sphere rolls behind the group; its reflection crosses a shallow puddle before the physical sphere disappears into a pipe while Ruggine turns too late. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. The signal entity appears only as a palm-sized flawless mirror-chrome sphere, physical, silent and highly reflective. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Floodwater, chain echoes, magnetic footsteps, pump pistons, CRT buzz, relay knocks and subterranean volcanic vibration. non_diegetic_music: N/A
```

### ☐ 051/120 · 12:30–12:45 · ATTO II — Sotto la città — Il patto provvisorio

**In una riga:** Mister K include Vico nella squadra.

**Funzione:** Inseguimento, alleanza forzata e verità sul furto

**Controlla:** Nuova alleanza definita in una battuta.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Mister K returns the red satchel to Vico-9 but keeps the brass key. <d>[Italian] Mister K: "Ci porti da Ottone." Vico-9: "E poi?" Ruggine: "Poi corriamo meno."</d> Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. Vico-9 is a thin rusted street robot with a square green CRT display head, a patched blue jacket, a red satchel and quick nervous movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Floodwater, chain echoes, magnetic footsteps, pump pistons, CRT buzz, relay knocks and subterranean volcanic vibration. non_diegetic_music: N/A
```

### ☐ 052/120 · 12:45–13:00 · ATTO II — Sotto la città — La porta del mercato

**In una riga:** Il gruppo riemerge direttamente nel territorio di Ottone.

**Funzione:** Inseguimento, alleanza forzata e verità sul furto

**Controlla:** Fine atto con destinazione e nuovo tono visivo.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Ruggine turns a giant wheel and opens a floodgate onto the underside of the market square while Mister K, Gina Relè and Vico-9 climb toward warm brass light. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. Gina Relè is a petite turquoise municipal dispatcher robot with a cream enamel shell, a copper rotary-phone receiver mounted on one shoulder, three analog status lamps and brisk authoritative gestures. Vico-9 is a thin rusted street robot with a square green CRT display head, a patched blue jacket, a red satchel and quick nervous movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Floodwater, chain echoes, magnetic footsteps, pump pistons, CRT buzz, relay knocks and subterranean volcanic vibration. non_diegetic_music: Original act-ending mystery sting with muted industrial pulse.
```


---

## ATTO III — Il quartiere mente · 13:00–18:00

### ☐ 053/120 · 13:00–13:15 · ATTO III — Il quartiere mente — Il salotto in piazza

**In una riga:** Prefetto Ottone riceve tutti in mezzo al mercato.

**Funzione:** Confronto con Ottone, ribaltamento e minaccia manifesta

**Controlla:** Ottone imponente ma inserito nella vita del quartiere.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Prefetto Ottone sits at a heavy brass table beneath a cream awning while robot vendors continue working around him; Mister K, Ruggine, Gina Relè and Vico-9 approach through rain. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. Gina Relè is a petite turquoise municipal dispatcher robot with a cream enamel shell, a copper rotary-phone receiver mounted on one shoulder, three analog status lamps and brisk authoritative gestures. Vico-9 is a thin rusted street robot with a square green CRT display head, a patched blue jacket, a red satchel and quick nervous movements. Prefetto Ottone is a massive brass-and-black robomafioso robot with broad shoulders, two narrow amber optical slits, an immaculate cream overcoat and slow controlled movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Market generators, brass mechanisms, awning rain, low crowd murmurs, heavy armor steps and intermittent signal knocks. non_diegetic_music: N/A
```

### ☐ 054/120 · 13:15–13:30 · ATTO III — Il quartiere mente — Due fessure ambrate

**In una riga:** Il boss si presenta con calma assoluta.

**Funzione:** Confronto con Ottone, ribaltamento e minaccia manifesta

**Controlla:** Minaccia ottenuta con immobilità e controllo.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Prefetto Ottone folds an immaculate cream overcoat across broad brass-and-black armor and places four espresso cups on the table without rising. <d>[Italian] Prefetto Ottone: "Siete in ritardo. La corrente pure."</d> Prefetto Ottone is a massive brass-and-black robomafioso robot with broad shoulders, two narrow amber optical slits, an immaculate cream overcoat and slow controlled movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Market generators, brass mechanisms, awning rain, low crowd murmurs, heavy armor steps and intermittent signal knocks. non_diegetic_music: N/A
```

### ☐ 055/120 · 13:30–13:45 · ATTO III — Il quartiere mente — La chiave sul tavolo

**In una riga:** Mister K mette l’indizio tra loro.

**Funzione:** Confronto con Ottone, ribaltamento e minaccia manifesta

**Controlla:** Composizione da confronto TV, oggetti centrali.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Mister K places the three-toothed relay key beside Ottone's brass coin while Ruggine stands behind him and Vico-9 avoids the amber optical slits. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. Vico-9 is a thin rusted street robot with a square green CRT display head, a patched blue jacket, a red satchel and quick nervous movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Market generators, brass mechanisms, awning rain, low crowd murmurs, heavy armor steps and intermittent signal knocks. non_diegetic_music: N/A
```

### ☐ 056/120 · 13:45–14:00 · ATTO III — Il quartiere mente — Il conto del mercato

**In una riga:** Ottone mostra perché voleva il relay.

**Funzione:** Confronto con Ottone, ribaltamento e minaccia manifesta

**Controlla:** Motivazione concreta, nessuna scritta.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Prefetto Ottone opens a mechanical ledger made of rotating power dials; each market stall loses one lamp as the central generator needle falls. <d>[Italian] Prefetto Ottone: "Lo Stato conta i quartieri. Io conto chi resta al buio."</d> Prefetto Ottone is a massive brass-and-black robomafioso robot with broad shoulders, two narrow amber optical slits, an immaculate cream overcoat and slow controlled movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Market generators, brass mechanisms, awning rain, low crowd murmurs, heavy armor steps and intermittent signal knocks. non_diegetic_music: N/A
```

### ☐ 057/120 · 14:00–14:15 · ATTO III — Il quartiere mente — Gina non arretra

**In una riga:** La responsabile contesta il metodo di Ottone.

**Funzione:** Confronto con Ottone, ribaltamento e minaccia manifesta

**Controlla:** Conflitto istituzionale breve e fisico.

**Generazione:** **DIPENDENZA 3/5** — usa il video approvato del Clip 056 come continuazione sliding-window FL2VA.

```text
integrated_multimodal_description: [Shot 1] Gina Relè slams a municipal seal onto the dial box while Prefetto Ottone stops it with one brass finger. <d>[Italian] Gina Relè: "Hai rubato una chiave pubblica." Prefetto Ottone: "L'ho fatta lavorare."</d> Gina Relè is a petite turquoise municipal dispatcher robot with a cream enamel shell, a copper rotary-phone receiver mounted on one shoulder, three analog status lamps and brisk authoritative gestures. Prefetto Ottone is a massive brass-and-black robomafioso robot with broad shoulders, two narrow amber optical slits, an immaculate cream overcoat and slow controlled movements. Continue directly from the accepted final physical state of clip 056, preserving the stated object, character positions and ongoing motion. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Market generators, brass mechanisms, awning rain, low crowd murmurs, heavy armor steps and intermittent signal knocks. non_diegetic_music: N/A
```

### ☐ 058/120 · 14:15–14:30 · ATTO III — Il quartiere mente — Il tavolo si spacca

**In una riga:** Il terzo segnale irrompe nel confronto.

**Funzione:** Confronto con Ottone, ribaltamento e minaccia manifesta

**Controlla:** Incidente forte e direzione del crollo chiara.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Three knocks rise through the square and a cyan line splits the paving beneath the brass table; Mister K pulls the key away as the floor begins to drop. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Market generators, brass mechanisms, awning rain, low crowd murmurs, heavy armor steps and intermittent signal knocks. non_diegetic_music: N/A
```

### ☐ 059/120 · 14:30–14:45 · ATTO III — Il quartiere mente — La piazza senza fondo

**In una riga:** Ruggine e Ottone salvano il gruppo insieme.

**Funzione:** Confronto con Ottone, ribaltamento e minaccia manifesta

**Controlla:** Dipendenza 3/5: stesso tavolo, stesso crollo, stessa disposizione.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Ruggine catches one side of the collapsing brass table while Prefetto Ottone catches the other, continuing directly from clip 056; Mister K, Gina Relè and Vico-9 cross between them as the fissure opens. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. Gina Relè is a petite turquoise municipal dispatcher robot with a cream enamel shell, a copper rotary-phone receiver mounted on one shoulder, three analog status lamps and brisk authoritative gestures. Vico-9 is a thin rusted street robot with a square green CRT display head, a patched blue jacket, a red satchel and quick nervous movements. Prefetto Ottone is a massive brass-and-black robomafioso robot with broad shoulders, two narrow amber optical slits, an immaculate cream overcoat and slow controlled movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Market generators, brass mechanisms, awning rain, low crowd murmurs, heavy armor steps and intermittent signal knocks. non_diegetic_music: N/A
```

### ☐ 060/120 · 14:45–15:00 · ATTO III — Il quartiere mente — Il nemico non era seduto

**In una riga:** Ottone prova di non controllare il segnale.

**Funzione:** Confronto con Ottone, ribaltamento e minaccia manifesta

**Controlla:** Ribaltamento leggibile, Ottone non assolto ma non responsabile.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Prefetto Ottone releases the stabilized table and shows both empty hands as the cyan fissure travels away from him toward the tower. <d>[Italian] Prefetto Ottone: "Se fosse mio, resterebbe qui."</d> Prefetto Ottone is a massive brass-and-black robomafioso robot with broad shoulders, two narrow amber optical slits, an immaculate cream overcoat and slow controlled movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Market generators, brass mechanisms, awning rain, low crowd murmurs, heavy armor steps and intermittent signal knocks. non_diegetic_music: N/A
```

### ☐ 061/120 · 15:00–15:15 · ATTO III — Il quartiere mente — La sfera tra le tazze

**In una riga:** L’entità si manifesta davanti a tutti.

**Funzione:** Confronto con Ottone, ribaltamento e minaccia manifesta

**Controlla:** Icona centrale pulita, suspense da serie.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] The mirror-chrome sphere rolls across the brass table, circles the four espresso cups and stops beside the relay key while every robot remains motionless.  The signal entity appears only as a palm-sized flawless mirror-chrome sphere, physical, silent and highly reflective. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Market generators, brass mechanisms, awning rain, low crowd murmurs, heavy armor steps and intermittent signal knocks. non_diegetic_music: N/A
```

### ☐ 062/120 · 15:15–15:30 · ATTO III — Il quartiere mente — Il quartiere la riconosce

**In una riga:** Gli abitanti reagiscono come a qualcosa di proibito.

**Funzione:** Confronto con Ottone, ribaltamento e minaccia manifesta

**Controlla:** Mostra la paura sociale senza spiegone.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Market robots close shutters, cover analog radios and pull small service automatons inside as the mirror-chrome sphere reflects their movement.  The signal entity appears only as a palm-sized flawless mirror-chrome sphere, physical, silent and highly reflective. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Market generators, brass mechanisms, awning rain, low crowd murmurs, heavy armor steps and intermittent signal knocks. non_diegetic_music: N/A
```

### ☐ 063/120 · 15:30–15:45 · ATTO III — Il quartiere mente — Ottone dice il nome

**In una riga:** Il boss collega la sfera a vecchie storie.

**Funzione:** Confronto con Ottone, ribaltamento e minaccia manifesta

**Controlla:** Dialogo breve che amplia il mistero.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Prefetto Ottone slowly removes one brass glove while watching the sphere. <d>[Italian] Prefetto Ottone: "Quella non porta corrente. Porta attenzione." Mister K: "Di chi?"</d> Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Prefetto Ottone is a massive brass-and-black robomafioso robot with broad shoulders, two narrow amber optical slits, an immaculate cream overcoat and slow controlled movements. The signal entity appears only as a palm-sized flawless mirror-chrome sphere, physical, silent and highly reflective. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Market generators, brass mechanisms, awning rain, low crowd murmurs, heavy armor steps and intermittent signal knocks. non_diegetic_music: N/A
```

### ☐ 064/120 · 15:45–16:00 · ATTO III — Il quartiere mente — Il primo comando

**In una riga:** La sfera usa la chiave a distanza.

**Funzione:** Confronto con Ottone, ribaltamento e minaccia manifesta

**Controlla:** Azione fisica e soprannaturale solo tramite magnetismo/meccanica.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] The mirror-chrome sphere strikes the table once; the three-toothed key lifts, rotates and inserts itself into the market generator socket while Mister K lunges toward it. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. The signal entity appears only as a palm-sized flawless mirror-chrome sphere, physical, silent and highly reflective. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Market generators, brass mechanisms, awning rain, low crowd murmurs, heavy armor steps and intermittent signal knocks. non_diegetic_music: N/A
```

### ☐ 065/120 · 16:00–16:15 · ATTO III — Il quartiere mente — Una strada accesa

**In una riga:** Il mercato riceve troppa energia.

**Funzione:** Confronto con Ottone, ribaltamento e minaccia manifesta

**Controlla:** Effetto morale visibile: un quartiere acceso, altri spenti.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] A wave of aqua lamps ignites across one market street while adjacent blocks go completely dark; Ruggine shields small robots from exploding bulbs. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Market generators, brass mechanisms, awning rain, low crowd murmurs, heavy armor steps and intermittent signal knocks. non_diegetic_music: N/A
```

### ☐ 066/120 · 16:15–16:30 · ATTO III — Il quartiere mente — Il prezzo della luce

**In una riga:** Ottone vede il costo della propria richiesta.

**Funzione:** Confronto con Ottone, ribaltamento e minaccia manifesta

**Controlla:** Scelta del personaggio mostrata senza redenzione facile.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Prefetto Ottone watches his stalls glow while distant Ponticelli rooftops die one by one; he closes the power ledger with both hands. <d>[Italian] Prefetto Ottone: "Non così."</d> Prefetto Ottone is a massive brass-and-black robomafioso robot with broad shoulders, two narrow amber optical slits, an immaculate cream overcoat and slow controlled movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Market generators, brass mechanisms, awning rain, low crowd murmurs, heavy armor steps and intermittent signal knocks. non_diegetic_music: N/A
```

### ☐ 067/120 · 16:30–16:45 · ATTO III — Il quartiere mente — La presa di Ruggine

**In una riga:** Ruggine tenta la soluzione più semplice.

**Funzione:** Confronto con Ottone, ribaltamento e minaccia manifesta

**Controlla:** Forza bruta chiara, prepara il fallimento.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Ruggine slams one hydraulic palm over the mirror-chrome sphere, trapping it against the brass table, while Mister K reaches for the key. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. The signal entity appears only as a palm-sized flawless mirror-chrome sphere, physical, silent and highly reflective. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Market generators, brass mechanisms, awning rain, low crowd murmurs, heavy armor steps and intermittent signal knocks. non_diegetic_music: N/A
```

### ☐ 068/120 · 16:45–17:00 · ATTO III — Il quartiere mente — La sfera passa attraverso

**In una riga:** L’entità sfugge usando il tavolo stesso.

**Funzione:** Confronto con Ottone, ribaltamento e minaccia manifesta

**Controlla:** Fuga fisica plausibile, non intangibile.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] The mirror-chrome sphere rolls through a narrow drainage groove beneath Ruggine's palm and exits from the table edge while sparks trace its path. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. The signal entity appears only as a palm-sized flawless mirror-chrome sphere, physical, silent and highly reflective. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Market generators, brass mechanisms, awning rain, low crowd murmurs, heavy armor steps and intermittent signal knocks. non_diegetic_music: N/A
```

### ☐ 069/120 · 17:00–17:15 · ATTO III — Il quartiere mente — Vico ruba al ladro

**In una riga:** Vico intercetta la sfera con il sacco rosso.

**Funzione:** Confronto con Ottone, ribaltamento e minaccia manifesta

**Controlla:** Redenzione attiva di Vico.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Vico-9 opens the red satchel beneath the falling sphere, catches it and sprints across aqua awnings while Mister K shouts from the square. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Vico-9 is a thin rusted street robot with a square green CRT display head, a patched blue jacket, a red satchel and quick nervous movements. The signal entity appears only as a palm-sized flawless mirror-chrome sphere, physical, silent and highly reflective. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Market generators, brass mechanisms, awning rain, low crowd murmurs, heavy armor steps and intermittent signal knocks. non_diegetic_music: N/A
```

### ☐ 070/120 · 17:15–17:30 · ATTO III — Il quartiere mente — Il mercato insegue

**In una riga:** Tutti partono verso la torre.

**Funzione:** Confronto con Ottone, ribaltamento e minaccia manifesta

**Controlla:** Ensemble action con percorsi separati.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Mister K swings onto a tram cable, Gina Relè starts the scooter, Ruggine runs through the broad avenue and Prefetto Ottone clears stalls aside as Vico-9 escapes with the satchel. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. Gina Relè is a petite turquoise municipal dispatcher robot with a cream enamel shell, a copper rotary-phone receiver mounted on one shoulder, three analog status lamps and brisk authoritative gestures. Vico-9 is a thin rusted street robot with a square green CRT display head, a patched blue jacket, a red satchel and quick nervous movements. Prefetto Ottone is a massive brass-and-black robomafioso robot with broad shoulders, two narrow amber optical slits, an immaculate cream overcoat and slow controlled movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Market generators, brass mechanisms, awning rain, low crowd murmurs, heavy armor steps and intermittent signal knocks. non_diegetic_music: N/A
```

### ☐ 071/120 · 17:30–17:45 · ATTO III — Il quartiere mente — Il tram delle undici

**In una riga:** Vico salta sul mezzo che porta alla torre.

**Funzione:** Confronto con Ottone, ribaltamento e minaccia manifesta

**Controlla:** Veicolo e direzione chiari.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Vico-9 lands on the roof of a moving cargo tram with the red satchel while Mister K catches the rear ladder and Gina Relè rides beside the wheels. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Gina Relè is a petite turquoise municipal dispatcher robot with a cream enamel shell, a copper rotary-phone receiver mounted on one shoulder, three analog status lamps and brisk authoritative gestures. Vico-9 is a thin rusted street robot with a square green CRT display head, a patched blue jacket, a red satchel and quick nervous movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Market generators, brass mechanisms, awning rain, low crowd murmurs, heavy armor steps and intermittent signal knocks. non_diegetic_music: N/A
```

### ☐ 072/120 · 17:45–18:00 · ATTO III — Il quartiere mente — Ottone sale a bordo

**In una riga:** Il boss decide di aiutare apertamente.

**Funzione:** Confronto con Ottone, ribaltamento e minaccia manifesta

**Controlla:** Fine atto: l’ensemble è formato.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Prefetto Ottone steps from a balcony onto the cargo platform as Ruggine grabs the rear coupling and pulls himself aboard. <d>[Italian] Prefetto Ottone: "Il mercato viene con voi."</d> Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. Prefetto Ottone is a massive brass-and-black robomafioso robot with broad shoulders, two narrow amber optical slits, an immaculate cream overcoat and slow controlled movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Market generators, brass mechanisms, awning rain, low crowd murmurs, heavy armor steps and intermittent signal knocks. non_diegetic_music: Original ensemble action sting with a rising unresolved final chord.
```


---

## ATTO IV — La torre · 18:00–23:00

### ☐ 073/120 · 18:00–18:15 · ATTO IV — La torre — Cinque sullo stesso tram

**In una riga:** La squadra improvvisata viaggia verso la torre.

**Funzione:** Viaggio, assedio della torre e blackout totale

**Controlla:** Ricomposizione del gruppo, mistero contenuto nel sacco.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Mister K studies the folding map on a cargo crate while Ruggine, Gina Relè, Vico-9 and Prefetto Ottone surround the red satchel vibrating with three knocks. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. Gina Relè is a petite turquoise municipal dispatcher robot with a cream enamel shell, a copper rotary-phone receiver mounted on one shoulder, three analog status lamps and brisk authoritative gestures. Vico-9 is a thin rusted street robot with a square green CRT display head, a patched blue jacket, a red satchel and quick nervous movements. Prefetto Ottone is a massive brass-and-black robomafioso robot with broad shoulders, two narrow amber optical slits, an immaculate cream overcoat and slow controlled movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Cargo-tram wheels, rooftop wind, antenna motors, defense-drone tracks, electrical arcs and increasingly violent volcanic thunder. non_diegetic_music: N/A
```

### ☐ 074/120 · 18:15–18:30 · ATTO IV — La torre — La regola del sacco

**In una riga:** Mister K impone di non aprire la sfera.

**Funzione:** Viaggio, assedio della torre e blackout totale

**Controlla:** Dialogo da squadra, oggetto sempre centrale.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Mister K tightens three physical clamps around Vico-9's red satchel. <d>[Italian] Mister K: "Non la tocchi nessuno." Ruggine: "Io l'ho già toccata."</d> Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. Vico-9 is a thin rusted street robot with a square green CRT display head, a patched blue jacket, a red satchel and quick nervous movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Cargo-tram wheels, rooftop wind, antenna motors, defense-drone tracks, electrical arcs and increasingly violent volcanic thunder. non_diegetic_music: N/A
```

### ☐ 075/120 · 18:30–18:45 · ATTO IV — La torre — Il ponte interrotto

**In una riga:** La linea del tram finisce davanti a un cratere.

**Funzione:** Viaggio, assedio della torre e blackout totale

**Controlla:** Ostacolo geografico leggibile.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] The cargo tram brakes at a collapsed rail bridge above a lava channel while Gina Relè points toward the tower on the far side. Gina Relè is a petite turquoise municipal dispatcher robot with a cream enamel shell, a copper rotary-phone receiver mounted on one shoulder, three analog status lamps and brisk authoritative gestures. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Cargo-tram wheels, rooftop wind, antenna motors, defense-drone tracks, electrical arcs and increasingly violent volcanic thunder. non_diegetic_music: N/A
```

### ☐ 076/120 · 18:45–19:00 · ATTO IV — La torre — Ruggine fa da ponte

**In una riga:** Il gigante crea il passaggio per gli altri.

**Funzione:** Viaggio, assedio della torre e blackout totale

**Controlla:** Forza usata come infrastruttura.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Ruggine plants one foot on each side of the broken span and lowers a steel beam across his forearms while Mister K, Gina Relè, Vico-9 and Prefetto Ottone cross. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. Gina Relè is a petite turquoise municipal dispatcher robot with a cream enamel shell, a copper rotary-phone receiver mounted on one shoulder, three analog status lamps and brisk authoritative gestures. Vico-9 is a thin rusted street robot with a square green CRT display head, a patched blue jacket, a red satchel and quick nervous movements. Prefetto Ottone is a massive brass-and-black robomafioso robot with broad shoulders, two narrow amber optical slits, an immaculate cream overcoat and slow controlled movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Cargo-tram wheels, rooftop wind, antenna motors, defense-drone tracks, electrical arcs and increasingly violent volcanic thunder. non_diegetic_music: N/A
```

### ☐ 077/120 · 19:00–19:15 · ATTO IV — La torre — L’ordine di Ottone

**In una riga:** Ottone apre il posto di blocco senza combattere.

**Funzione:** Viaggio, assedio della torre e blackout totale

**Controlla:** Potere sociale mostrato in un gesto.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Prefetto Ottone raises the brass coin toward a line of armored patrol robots; they rotate their barriers and reveal the tower road while Mister K watches him. <d>[Italian] Mister K: "Comodo." Prefetto Ottone: "Costoso."</d> Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Prefetto Ottone is a massive brass-and-black robomafioso robot with broad shoulders, two narrow amber optical slits, an immaculate cream overcoat and slow controlled movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Cargo-tram wheels, rooftop wind, antenna motors, defense-drone tracks, electrical arcs and increasingly violent volcanic thunder. non_diegetic_music: N/A
```

### ☐ 078/120 · 19:15–19:30 · ATTO IV — La torre — La cenere orizzontale

**In una riga:** La tempesta rende la torre quasi invisibile.

**Funzione:** Viaggio, assedio della torre e blackout totale

**Controlla:** Atmosfera forte, direzione sempre leggibile.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Mister K anchors the blue cable between rusted poles while the group advances bent against sideways ash and Ruggine shields the red satchel. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Cargo-tram wheels, rooftop wind, antenna motors, defense-drone tracks, electrical arcs and increasingly violent volcanic thunder. non_diegetic_music: N/A
```

### ☐ 079/120 · 19:30–19:45 · ATTO IV — La torre — Gina trova la frequenza

**In una riga:** La municipale sente il segnale dentro i suoi relay.

**Funzione:** Viaggio, assedio della torre e blackout totale

**Controlla:** Gina ha competenza propria e utile.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Gina Relè stops the scooter, opens her chest panel and aligns three analog lamps with the tower pulse while the others form a circle around her. Gina Relè is a petite turquoise municipal dispatcher robot with a cream enamel shell, a copper rotary-phone receiver mounted on one shoulder, three analog status lamps and brisk authoritative gestures. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Cargo-tram wheels, rooftop wind, antenna motors, defense-drone tracks, electrical arcs and increasingly violent volcanic thunder. non_diegetic_music: N/A
```

### ☐ 080/120 · 19:45–20:00 · ATTO IV — La torre — Il sentiero delle antenne

**In una riga:** Le antenne indicano una scala sicura.

**Funzione:** Viaggio, assedio della torre e blackout totale

**Controlla:** Investigazione fisica, niente interfaccia astratta.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Mister K taps successive antenna bases with the brass meter; each dish rotates toward a maintenance staircase while Ruggine clears loose cables. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Cargo-tram wheels, rooftop wind, antenna motors, defense-drone tracks, electrical arcs and increasingly violent volcanic thunder. non_diegetic_music: N/A
```

### ☐ 081/120 · 20:00–20:15 · ATTO IV — La torre — Vico apre il sacco

**In una riga:** La sfera forza il contenitore dall’interno.

**Funzione:** Viaggio, assedio della torre e blackout totale

**Controlla:** Errore non volontario, sfera sempre materiale.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Vico-9 braces both feet as the red satchel buckles, tears one clamp and releases the mirror-chrome sphere onto the tower stairs. Vico-9 is a thin rusted street robot with a square green CRT display head, a patched blue jacket, a red satchel and quick nervous movements. The signal entity appears only as a palm-sized flawless mirror-chrome sphere, physical, silent and highly reflective. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Cargo-tram wheels, rooftop wind, antenna motors, defense-drone tracks, electrical arcs and increasingly violent volcanic thunder. non_diegetic_music: N/A
```

### ☐ 082/120 · 20:15–20:30 · ATTO IV — La torre — La corsa verticale

**In una riga:** La sfera sale e la squadra la segue.

**Funzione:** Viaggio, assedio della torre e blackout totale

**Controlla:** Tre traiettorie verticali chiare.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] The mirror-chrome sphere rolls up a spiral magnetic rail while Mister K runs on the inner stairs, Vico-9 climbs the handrail and Ruggine ascends the outer ladder. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. Vico-9 is a thin rusted street robot with a square green CRT display head, a patched blue jacket, a red satchel and quick nervous movements. The signal entity appears only as a palm-sized flawless mirror-chrome sphere, physical, silent and highly reflective. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Cargo-tram wheels, rooftop wind, antenna motors, defense-drone tracks, electrical arcs and increasingly violent volcanic thunder. non_diegetic_music: N/A
```

### ☐ 083/120 · 20:30–20:45 · ATTO IV — La torre — Ottone resta sotto

**In una riga:** Il boss difende l’accesso dai droni.

**Funzione:** Viaggio, assedio della torre e blackout totale

**Controlla:** Ottone entra nell’azione mantenendo stile e peso.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Prefetto Ottone removes the cream overcoat, wraps it around one arm and blocks a wave of armored maintenance drones at the tower entrance. Prefetto Ottone is a massive brass-and-black robomafioso robot with broad shoulders, two narrow amber optical slits, an immaculate cream overcoat and slow controlled movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Cargo-tram wheels, rooftop wind, antenna motors, defense-drone tracks, electrical arcs and increasingly violent volcanic thunder. non_diegetic_music: N/A
```

### ☐ 084/120 · 20:45–21:00 · ATTO IV — La torre — Gina collega il piano terra

**In una riga:** La responsabile riattiva il relay inferiore.

**Funzione:** Viaggio, assedio della torre e blackout totale

**Controlla:** Azione tecnica sotto pressione.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Gina Relè inserts one municipal cable into the lowest tower socket and turns two analog wheels while drones strike the metal door behind her. Gina Relè is a petite turquoise municipal dispatcher robot with a cream enamel shell, a copper rotary-phone receiver mounted on one shoulder, three analog status lamps and brisk authoritative gestures. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Cargo-tram wheels, rooftop wind, antenna motors, defense-drone tracks, electrical arcs and increasingly violent volcanic thunder. non_diegetic_music: N/A
```

### ☐ 085/120 · 21:00–21:15 · ATTO IV — La torre — Il socket del terzo segnale

**In una riga:** Mister K raggiunge il punto d’arrivo.

**Funzione:** Viaggio, assedio della torre e blackout totale

**Controlla:** Obiettivo fisico finalmente rivelato.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Mister K arrives at the upper platform and opens a circular beacon socket with three empty clamps as the mirror-chrome sphere circles the rim. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. The signal entity appears only as a palm-sized flawless mirror-chrome sphere, physical, silent and highly reflective. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Cargo-tram wheels, rooftop wind, antenna motors, defense-drone tracks, electrical arcs and increasingly violent volcanic thunder. non_diegetic_music: N/A
```

### ☐ 086/120 · 21:15–21:30 · ATTO IV — La torre — La chiave vola

**In una riga:** Il relay viene strappato dalla cintura di Mister K.

**Funzione:** Viaggio, assedio della torre e blackout totale

**Controlla:** Oggetto già noto al centro dell’azione.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] The three-toothed brass key lifts from Mister K's belt and spins toward the beacon socket while Vico-9 jumps from the handrail to catch it. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Vico-9 is a thin rusted street robot with a square green CRT display head, a patched blue jacket, a red satchel and quick nervous movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Cargo-tram wheels, rooftop wind, antenna motors, defense-drone tracks, electrical arcs and increasingly violent volcanic thunder. non_diegetic_music: N/A
```

### ☐ 087/120 · 21:30–21:45 · ATTO IV — La torre — Vico la manca

**In una riga:** La chiave entra nel socket.

**Funzione:** Viaggio, assedio della torre e blackout totale

**Controlla:** Fallimento preciso, non caotico.

**Generazione:** **DIPENDENZA 4/5** — usa il video approvato del Clip 086 come continuazione sliding-window FL2VA.

```text
integrated_multimodal_description: [Shot 1] Vico-9's fingers close one centimeter late as the brass key locks into the beacon; the mirror-chrome sphere strikes it and cyan power erupts upward. Vico-9 is a thin rusted street robot with a square green CRT display head, a patched blue jacket, a red satchel and quick nervous movements. The signal entity appears only as a palm-sized flawless mirror-chrome sphere, physical, silent and highly reflective. Continue directly from the accepted final physical state of clip 086, preserving the stated object, character positions and ongoing motion. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Cargo-tram wheels, rooftop wind, antenna motors, defense-drone tracks, electrical arcs and increasingly violent volcanic thunder. non_diegetic_music: N/A
```

### ☐ 088/120 · 21:45–22:00 · ATTO IV — La torre — Il colpo sulla torre

**In una riga:** L’attivazione spezza il mast principale.

**Funzione:** Viaggio, assedio della torre e blackout totale

**Controlla:** Impatto iniziale chiaro, prepara la continuità.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] The sphere drives a cyan pulse through the key, bending the lightning mast and throwing Mister K and Vico-9 across the platform while Ruggine reaches the top ladder. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. Vico-9 is a thin rusted street robot with a square green CRT display head, a patched blue jacket, a red satchel and quick nervous movements. The signal entity appears only as a palm-sized flawless mirror-chrome sphere, physical, silent and highly reflective. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Cargo-tram wheels, rooftop wind, antenna motors, defense-drone tracks, electrical arcs and increasingly violent volcanic thunder. non_diegetic_music: N/A
```

### ☐ 089/120 · 22:00–22:15 · ATTO IV — La torre — Il mast cade

**In una riga:** Ruggine afferra la torre prima del collasso.

**Funzione:** Viaggio, assedio della torre e blackout totale

**Controlla:** Dipendenza 4/5: stesso impulso, stesso mast e stessa piattaforma.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Ruggine catches the falling lightning mast with both hydraulic hands, continuing directly from clip 086, while Mister K slides toward the edge and Vico-9 grips the beacon rail. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. Vico-9 is a thin rusted street robot with a square green CRT display head, a patched blue jacket, a red satchel and quick nervous movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Cargo-tram wheels, rooftop wind, antenna motors, defense-drone tracks, electrical arcs and increasingly violent volcanic thunder. non_diegetic_music: N/A
```

### ☐ 090/120 · 22:15–22:30 · ATTO IV — La torre — Il cavo di Mister K

**In una riga:** Mister K evita la caduta e torna al beacon.

**Funzione:** Viaggio, assedio della torre e blackout totale

**Controlla:** Azione eroica precisa.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Mister K fires the blue cable around Ruggine's forearm, swings beneath the platform and lands beside the locked key while the giant holds the mast. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Cargo-tram wheels, rooftop wind, antenna motors, defense-drone tracks, electrical arcs and increasingly violent volcanic thunder. non_diegetic_music: N/A
```

### ☐ 091/120 · 22:30–22:45 · ATTO IV — La torre — La scelta di Vico

**In una riga:** Vico torna indietro invece di fuggire.

**Funzione:** Viaggio, assedio della torre e blackout totale

**Controlla:** Completa l’arco di Vico con azione concreta.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Vico-9 climbs back onto the shaking platform and clamps the red satchel around the mirror-chrome sphere while Mister K works on the key. <d>[Italian] Vico-9: "Questa volta rubo per restituire."</d> Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Vico-9 is a thin rusted street robot with a square green CRT display head, a patched blue jacket, a red satchel and quick nervous movements. The signal entity appears only as a palm-sized flawless mirror-chrome sphere, physical, silent and highly reflective. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Cargo-tram wheels, rooftop wind, antenna motors, defense-drone tracks, electrical arcs and increasingly violent volcanic thunder. non_diegetic_music: N/A
```

### ☐ 092/120 · 22:45–23:00 · ATTO IV — La torre — Ponticelli al buio

**In una riga:** L’atto chiude sulla vittoria apparente della sfera.

**Funzione:** Viaggio, assedio della torre e blackout totale

**Controlla:** Blackout totale a colori, stato nuovo e definitivo.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] The tower emits three broad pulses and every lamp across Ponticelli shuts off, leaving only orange lava and the mirror-chrome sphere reflecting orange lava light as the team holds the collapsing structure.  The signal entity appears only as a palm-sized flawless mirror-chrome sphere, physical, silent and highly reflective. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Cargo-tram wheels, rooftop wind, antenna motors, defense-drone tracks, electrical arcs and increasingly violent volcanic thunder. non_diegetic_music: Original dark act-ending sting built around the three-knock motif.
```


---

## ATTO V — La scelta · 23:00–28:00

### ☐ 093/120 · 23:00–23:15 · ATTO V — La scelta — Il silenzio dopo la corrente

**In una riga:** La città resta viva ma completamente spenta.

**Funzione:** Decisione morale, piano corale, climax e risoluzione

**Controlla:** Quadro corale e conseguenza del blackout.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Mister K stands beside the locked beacon while Ruggine holds the bent mast, Gina Relè watches dead status lamps, Vico-9 grips the satchel and Prefetto Ottone reaches the upper platform. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. Gina Relè is a petite turquoise municipal dispatcher robot with a cream enamel shell, a copper rotary-phone receiver mounted on one shoulder, three analog status lamps and brisk authoritative gestures. Vico-9 is a thin rusted street robot with a square green CRT display head, a patched blue jacket, a red satchel and quick nervous movements. Prefetto Ottone is a massive brass-and-black robomafioso robot with broad shoulders, two narrow amber optical slits, an immaculate cream overcoat and slow controlled movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Near-silence after blackout, strained tower steel, manual gears, cable tension, synchronized relay impacts and returning city ambience. non_diegetic_music: N/A
```

### ☐ 094/120 · 23:15–23:30 · ATTO V — La scelta — La proposta di Ottone

**In una riga:** Ottone vuole salvare almeno il mercato.

**Funzione:** Decisione morale, piano corale, climax e risoluzione

**Controlla:** Scelta comprensibile ma egoista.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Prefetto Ottone places his brass coin into a side selector aimed at the market circuit. <d>[Italian] Prefetto Ottone: "Una strada accesa è meglio di una città cieca."</d> Prefetto Ottone is a massive brass-and-black robomafioso robot with broad shoulders, two narrow amber optical slits, an immaculate cream overcoat and slow controlled movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Near-silence after blackout, strained tower steel, manual gears, cable tension, synchronized relay impacts and returning city ambience. non_diegetic_music: N/A
```

### ☐ 095/120 · 23:30–23:45 · ATTO V — La scelta — La risposta di Gina

**In una riga:** Gina difende la rete comune.

**Funzione:** Decisione morale, piano corale, climax e risoluzione

**Controlla:** Conflitto morale in gesto e battuta.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Gina Relè removes Ottone's coin and places it on the neutral center slot. <d>[Italian] Gina Relè: "Una città divisa è già spenta."</d> Gina Relè is a petite turquoise municipal dispatcher robot with a cream enamel shell, a copper rotary-phone receiver mounted on one shoulder, three analog status lamps and brisk authoritative gestures. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Near-silence after blackout, strained tower steel, manual gears, cable tension, synchronized relay impacts and returning city ambience. non_diegetic_music: N/A
```

### ☐ 096/120 · 23:45–24:00 · ATTO V — La scelta — Mister K legge il trucco

**In una riga:** Il protagonista capisce che la sfera vuole una risposta.

**Funzione:** Decisione morale, piano corale, climax e risoluzione

**Controlla:** Rivelazione visiva semplice.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Mister K rotates the brass meter around the beacon and sees each of the three tower pulses followed by an empty fourth position. <d>[Italian] Mister K: "Non sta trasmettendo. Sta aspettando."</d> Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Near-silence after blackout, strained tower steel, manual gears, cable tension, synchronized relay impacts and returning city ambience. non_diegetic_music: N/A
```

### ☐ 097/120 · 24:00–24:15 · ATTO V — La scelta — Il quarto colpo

**In una riga:** Ruggine propone la soluzione letterale.

**Funzione:** Decisione morale, piano corale, climax e risoluzione

**Controlla:** Humor e intuizione del gigante.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Ruggine taps the mast once with one knuckle, producing a deep fourth knock that makes the sphere stop rotating. <d>[Italian] Ruggine: "Adesso ha una risposta."</d> Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. The signal entity appears only as a palm-sized flawless mirror-chrome sphere, physical, silent and highly reflective. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Near-silence after blackout, strained tower steel, manual gears, cable tension, synchronized relay impacts and returning city ambience. non_diegetic_music: N/A
```

### ☐ 098/120 · 24:15–24:30 · ATTO V — La scelta — La finestra di tre secondi

**In una riga:** Gina misura il momento per invertire la rete.

**Funzione:** Decisione morale, piano corale, climax e risoluzione

**Controlla:** Countdown fisico leggibile.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Gina Relè restarts her three analog lamps and aligns them with the sphere's next pulse while Mister K positions the key release lever. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Gina Relè is a petite turquoise municipal dispatcher robot with a cream enamel shell, a copper rotary-phone receiver mounted on one shoulder, three analog status lamps and brisk authoritative gestures. The signal entity appears only as a palm-sized flawless mirror-chrome sphere, physical, silent and highly reflective. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Near-silence after blackout, strained tower steel, manual gears, cable tension, synchronized relay impacts and returning city ambience. non_diegetic_music: N/A
```

### ☐ 099/120 · 24:30–24:45 · ATTO V — La scelta — La chiave restituita

**In una riga:** Vico consegna ciò che aveva rubato.

**Funzione:** Decisione morale, piano corale, climax e risoluzione

**Controlla:** Payoff del furto e fiducia incompleta.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Vico-9 removes a hidden second relay tooth from the red satchel and places it into Mister K's palm. <d>[Italian] Vico-9: "Mancava questo." Mister K: "Lo sapevo."</d> Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Vico-9 is a thin rusted street robot with a square green CRT display head, a patched blue jacket, a red satchel and quick nervous movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Near-silence after blackout, strained tower steel, manual gears, cable tension, synchronized relay impacts and returning city ambience. non_diegetic_music: N/A
```

### ☐ 100/120 · 24:45–25:00 · ATTO V — La scelta — Il piano sul pavimento

**In una riga:** Mister K assegna i ruoli con oggetti reali.

**Funzione:** Decisione morale, piano corale, climax e risoluzione

**Controlla:** Briefing visuale, niente monologo lungo.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Mister K arranges the brass key, Ottone's coin, Gina's cable and Ruggine's wrench around a circular maintenance plate, pointing each tool toward one tower mechanism. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Near-silence after blackout, strained tower steel, manual gears, cable tension, synchronized relay impacts and returning city ambience. non_diegetic_music: N/A
```

### ☐ 101/120 · 25:00–25:15 · ATTO V — La scelta — Ruggine alla ruota

**In una riga:** Il gigante prende il carico principale.

**Funzione:** Decisione morale, piano corale, climax e risoluzione

**Controlla:** Sforzo fisico centrale.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Ruggine locks the bent mast into a giant manual flywheel and begins one slow rotation while tower gears move for the first time without power. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Near-silence after blackout, strained tower steel, manual gears, cable tension, synchronized relay impacts and returning city ambience. non_diegetic_music: N/A
```

### ☐ 102/120 · 25:15–25:30 · ATTO V — La scelta — Ottone tiene la linea

**In una riga:** Il boss usa la propria armatura per il quartiere intero.

**Funzione:** Decisione morale, piano corale, climax e risoluzione

**Controlla:** Arco di Ottone mostrato tramite sacrificio materiale.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Prefetto Ottone wraps a high-voltage cable around both brass forearms and holds it away from the market-only selector while sparks travel across the overcoat. Prefetto Ottone is a massive brass-and-black robomafioso robot with broad shoulders, two narrow amber optical slits, an immaculate cream overcoat and slow controlled movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Near-silence after blackout, strained tower steel, manual gears, cable tension, synchronized relay impacts and returning city ambience. non_diegetic_music: N/A
```

### ☐ 103/120 · 25:30–25:45 · ATTO V — La scelta — Vico sopra il beacon

**In una riga:** Il mariuolo raggiunge il morsetto impossibile.

**Funzione:** Decisione morale, piano corale, climax e risoluzione

**Controlla:** Agilità utile, obiettivo preciso.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Vico-9 climbs the rotating beacon frame, slips the missing relay tooth into the upper clamp and hangs from it as the tower shakes. Vico-9 is a thin rusted street robot with a square green CRT display head, a patched blue jacket, a red satchel and quick nervous movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Near-silence after blackout, strained tower steel, manual gears, cable tension, synchronized relay impacts and returning city ambience. non_diegetic_music: N/A
```

### ☐ 104/120 · 25:45–26:00 · ATTO V — La scelta — Gina sincronizza la città

**In una riga:** La municipale riallinea i tre distretti.

**Funzione:** Decisione morale, piano corale, climax e risoluzione

**Controlla:** Competenza e posta cittadina visibili.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Gina Relè turns three analog district wheels together; physical relay lamps across a miniature Ponticelli map begin blinking in one rhythm. Gina Relè is a petite turquoise municipal dispatcher robot with a cream enamel shell, a copper rotary-phone receiver mounted on one shoulder, three analog status lamps and brisk authoritative gestures. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Near-silence after blackout, strained tower steel, manual gears, cable tension, synchronized relay impacts and returning city ambience. non_diegetic_music: N/A
```

### ☐ 105/120 · 26:00–26:15 · ATTO V — La scelta — Mister K gira la chiave

**In una riga:** Il piano entra nella fase irreversibile.

**Funzione:** Decisione morale, piano corale, climax e risoluzione

**Controlla:** Climax tecnico, oggetti noti.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Mister K inserts the completed three-toothed key into the central socket and turns it halfway while the mirror-chrome sphere pushes against the red satchel clamp. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. The signal entity appears only as a palm-sized flawless mirror-chrome sphere, physical, silent and highly reflective. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Near-silence after blackout, strained tower steel, manual gears, cable tension, synchronized relay impacts and returning city ambience. non_diegetic_music: N/A
```

### ☐ 106/120 · 26:15–26:30 · ATTO V — La scelta — La sfera resiste

**In una riga:** L’entità tenta di riprendere il controllo.

**Funzione:** Decisione morale, piano corale, climax e risoluzione

**Controlla:** Antagonista agisce senza dialogo.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] The mirror-chrome sphere spins inside the satchel clamp, pulling the key backward and reversing one district wheel while Mister K braces both feet. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. The signal entity appears only as a palm-sized flawless mirror-chrome sphere, physical, silent and highly reflective. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Near-silence after blackout, strained tower steel, manual gears, cable tension, synchronized relay impacts and returning city ambience. non_diegetic_music: N/A
```

### ☐ 107/120 · 26:30–26:45 · ATTO V — La scelta — Il primo tentativo fallisce

**In una riga:** La torre scarica l’energia contro la squadra.

**Funzione:** Decisione morale, piano corale, climax e risoluzione

**Controlla:** Fallimento corale leggibile.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] A cyan arc throws Mister K away from the socket, snaps Gina Relè's cable and forces Ruggine's flywheel backward while Vico-9 remains attached above. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. Gina Relè is a petite turquoise municipal dispatcher robot with a cream enamel shell, a copper rotary-phone receiver mounted on one shoulder, three analog status lamps and brisk authoritative gestures. Vico-9 is a thin rusted street robot with a square green CRT display head, a patched blue jacket, a red satchel and quick nervous movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Near-silence after blackout, strained tower steel, manual gears, cable tension, synchronized relay impacts and returning city ambience. non_diegetic_music: N/A
```

### ☐ 108/120 · 26:45–27:00 · ATTO V — La scelta — Il segno sulla moneta

**In una riga:** Ottone scopre che il proprio token completa il circuito.

**Funzione:** Decisione morale, piano corale, climax e risoluzione

**Controlla:** Indizio precedente diventa soluzione.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Prefetto Ottone sees the two amber grooves on his brass coin align with the broken cable ends and presses the coin between them, restoring the circuit. Prefetto Ottone is a massive brass-and-black robomafioso robot with broad shoulders, two narrow amber optical slits, an immaculate cream overcoat and slow controlled movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Near-silence after blackout, strained tower steel, manual gears, cable tension, synchronized relay impacts and returning city ambience. non_diegetic_music: N/A
```

### ☐ 109/120 · 27:00–27:15 · ATTO V — La scelta — Ruggine ha paura

**In una riga:** Il gigante ammette il rischio prima del colpo finale.

**Funzione:** Decisione morale, piano corale, climax e risoluzione

**Controlla:** Momento umano attraverso linguaggio e postura meccanica.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Ruggine stops the flywheel for one second as the mast groans overhead. <d>[Italian] Ruggine: "Se la giro, cade tutto." Mister K: "Allora girala piano."</d> Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Near-silence after blackout, strained tower steel, manual gears, cable tension, synchronized relay impacts and returning city ambience. non_diegetic_music: N/A
```

### ☐ 110/120 · 27:15–27:30 · ATTO V — La scelta — Il secondo piano

**In una riga:** La squadra riparte senza spiegazioni.

**Funzione:** Decisione morale, piano corale, climax e risoluzione

**Controlla:** Preparazione corale sintetica.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Mister K grabs the key, Gina Relè reconnects the cable through Ottone's coin, Vico-9 locks the upper tooth and Ruggine sets both hands on the flywheel. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. Gina Relè is a petite turquoise municipal dispatcher robot with a cream enamel shell, a copper rotary-phone receiver mounted on one shoulder, three analog status lamps and brisk authoritative gestures. Vico-9 is a thin rusted street robot with a square green CRT display head, a patched blue jacket, a red satchel and quick nervous movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Near-silence after blackout, strained tower steel, manual gears, cable tension, synchronized relay impacts and returning city ambience. non_diegetic_music: N/A
```

### ☐ 111/120 · 27:30–27:45 · ATTO V — La scelta — Tutti al quarto battito

**In una riga:** Il colpo finale viene eseguito nello stesso istante.

**Funzione:** Decisione morale, piano corale, climax e risoluzione

**Controlla:** Climax simultaneo con cinque azioni distinguibili.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] On the fourth metallic knock, Ruggine turns the flywheel, Mister K rotates the key, Gina Relè closes all three district switches, Vico-9 locks the upper clamp and Prefetto Ottone holds the live cable. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. Gina Relè is a petite turquoise municipal dispatcher robot with a cream enamel shell, a copper rotary-phone receiver mounted on one shoulder, three analog status lamps and brisk authoritative gestures. Vico-9 is a thin rusted street robot with a square green CRT display head, a patched blue jacket, a red satchel and quick nervous movements. Prefetto Ottone is a massive brass-and-black robomafioso robot with broad shoulders, two narrow amber optical slits, an immaculate cream overcoat and slow controlled movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Near-silence after blackout, strained tower steel, manual gears, cable tension, synchronized relay impacts and returning city ambience. non_diegetic_music: N/A
```

### ☐ 112/120 · 27:45–28:00 · ATTO V — La scelta — La risposta attraversa Napoli

**In una riga:** Il segnale corretto riaccende la città.

**Funzione:** Decisione morale, piano corale, climax e risoluzione

**Controlla:** Dipendenza 5/5: stesso gesto corale e onda che ne consegue.

**Generazione:** **DIPENDENZA 5/5** — usa il video approvato del Clip 111 come continuazione sliding-window FL2VA.

```text
integrated_multimodal_description: [Shot 1] A controlled aqua pulse leaves the tower and travels across Ponticelli rooftop relays while Mister K, Ruggine, Gina Relè, Vico-9 and Prefetto Ottone hold their final positions and orange lava reflections return to wet streets. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. Gina Relè is a petite turquoise municipal dispatcher robot with a cream enamel shell, a copper rotary-phone receiver mounted on one shoulder, three analog status lamps and brisk authoritative gestures. Vico-9 is a thin rusted street robot with a square green CRT display head, a patched blue jacket, a red satchel and quick nervous movements. Prefetto Ottone is a massive brass-and-black robomafioso robot with broad shoulders, two narrow amber optical slits, an immaculate cream overcoat and slow controlled movements. Continue directly from the accepted final physical state of clip 111, preserving the stated object, character positions and ongoing motion. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Near-silence after blackout, strained tower steel, manual gears, cable tension, synchronized relay impacts and returning city ambience. non_diegetic_music: Original restrained heroic resolution theme with analog pulse and warm orchestral lift.
```


---

## EPILOGO E TITOLI · 28:00–30:00

### ☐ 113/120 · 28:00–28:15 · EPILOGO E TITOLI — Le prime finestre

**In una riga:** La vita robotica torna nei quartieri.

**Funzione:** Payoff dei personaggi, chiusura emotiva, credits e cliffhanger

**Controlla:** Risoluzione ampia e colorata.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Aqua lamps illuminate one building at a time as small service robots roll onto balconies and workers restart analog machines beneath the erupting Vesuvius.  The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Returning market bustle, café machinery, distant tram bells, gentle relay hum and the recurring three-knock motif. non_diegetic_music: N/A
```

### ☐ 114/120 · 28:15–28:30 · EPILOGO E TITOLI — Il mercato non è speciale

**In una riga:** Ottone accetta che la corrente venga condivisa.

**Funzione:** Payoff dei personaggi, chiusura emotiva, credits e cliffhanger

**Controlla:** Tregua, non redenzione completa.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Prefetto Ottone returns the brass coin to Gina Relè beside the evenly powered market generator. <d>[Italian] Prefetto Ottone: "Domani ne riparliamo." Gina Relè: "Domani paghi."</d> Gina Relè is a petite turquoise municipal dispatcher robot with a cream enamel shell, a copper rotary-phone receiver mounted on one shoulder, three analog status lamps and brisk authoritative gestures. Prefetto Ottone is a massive brass-and-black robomafioso robot with broad shoulders, two narrow amber optical slits, an immaculate cream overcoat and slow controlled movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Returning market bustle, café machinery, distant tram bells, gentle relay hum and the recurring three-knock motif. non_diegetic_music: N/A
```

### ☐ 115/120 · 28:30–28:45 · EPILOGO E TITOLI — Un lavoro per Vico

**In una riga:** Gina trasforma il mariuolo in manutentore sorvegliato.

**Funzione:** Payoff dei personaggi, chiusura emotiva, credits e cliffhanger

**Controlla:** Arco di Vico chiuso con gag.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Gina Relè clips a mint municipal tool badge onto Vico-9's patched blue jacket while Mister K checks that the red satchel is empty. <d>[Italian] Vico-9: "È un arresto?" Gina Relè: "Con orari."</d> Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Gina Relè is a petite turquoise municipal dispatcher robot with a cream enamel shell, a copper rotary-phone receiver mounted on one shoulder, three analog status lamps and brisk authoritative gestures. Vico-9 is a thin rusted street robot with a square green CRT display head, a patched blue jacket, a red satchel and quick nervous movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Returning market bustle, café machinery, distant tram bells, gentle relay hum and the recurring three-knock motif. non_diegetic_music: N/A
```

### ☐ 116/120 · 28:45–29:00 · EPILOGO E TITOLI — La strada di casa

**In una riga:** Mister K e Ruggine tornano al café.

**Funzione:** Payoff dei personaggi, chiusura emotiva, credits e cliffhanger

**Controlla:** Respiro dopo il climax.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Mister K walks under restored aqua street lamps while Ruggine carries the flattened stool beneath one arm; the camera follows them through calm rain toward the bent café doorway. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Returning market bustle, café machinery, distant tram bells, gentle relay hum and the recurring three-knock motif. non_diegetic_music: N/A
```

### ☐ 117/120 · 29:00–29:15 · EPILOGO E TITOLI — Il caffè promesso

**In una riga:** La gag iniziale ottiene finalmente il payoff.

**Funzione:** Payoff dei personaggi, chiusura emotiva, credits e cliffhanger

**Controlla:** Chiusura calda, oggetti del cold open.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Mister K fills the tiny espresso cup while Ruggine reshapes the flattened stool into a standing tray. <d>[Italian] Ruggine: "Adesso posso berlo?" Mister K: "Se entra."</d> Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Returning market bustle, café machinery, distant tram bells, gentle relay hum and the recurring three-knock motif. non_diegetic_music: N/A
```

### ☐ 118/120 · 29:15–29:30 · EPILOGO E TITOLI — La tazza grande

**In una riga:** Ruggine risolve il problema a modo suo.

**Funzione:** Payoff dei personaggi, chiusura emotiva, credits e cliffhanger

**Controlla:** Ultima gag autonoma e visivamente pulita.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Ruggine places a massive steel measuring cup on the counter; Mister K silently pours the tiny espresso into it and the liquid disappears at the bottom. Mister K is a compact hooded black robot with a charcoal cloak, cyan optical lights, narrow mechanical hands, a radio antenna and quick precise movements. Ruggine is a colossal rust-orange robot with layered armor, exposed pistons, cable bundles, amber optical lights, massive hydraulic fists and slow heavy movements. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Returning market bustle, café machinery, distant tram bells, gentle relay hum and the recurring three-knock motif. non_diegetic_music: N/A
```

### ☐ 119/120 · 29:30–29:45 · EPILOGO E TITOLI — Titoli sulla città

**In una riga:** La sigla ritorna durante i credits aggiunti in post.

**Funzione:** Payoff dei personaggi, chiusura emotiva, credits e cliffhanger

**Controlla:** Montaggio finale, nessuna scritta generata.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] A smooth aerial montage crosses the restored underpass, market, tram bridge, turbine plant and antenna tower while physical robots resume daily work and blank chrome panels provide clean space for credits added in post.  The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Returning market bustle, café machinery, distant tram bells, gentle relay hum and the recurring three-knock motif. non_diegetic_music: Original opening-theme reprise for end credits, energetic but lighter.
```

### ☐ 120/120 · 29:45–30:00 · EPILOGO E TITOLI — Dopo i titoli: qualcuno risponde

**In una riga:** Il cliffhanger apre l’episodio successivo.

**Funzione:** Payoff dei personaggi, chiusura emotiva, credits e cliffhanger

**Controlla:** Cliffhanger fisico, chiaro e non spiegato.

**Generazione:** **AUTONOMA — SOLO TESTO** — nessun video e nessuna immagine in ingresso.

```text
integrated_multimodal_description: [Shot 1] Inside a distant rusted relay station beyond Ponticelli, the mirror-chrome sphere rolls into an empty brass socket, emits three metallic knocks and receives a fourth knock from deep beneath the floor as the camera pushes toward its reflection.  The signal entity appears only as a palm-sized flawless mirror-chrome sphere, physical, silent and highly reflective. The setting is robot-inhabited Ponticelli, Naples: wet black cobblestones, damaged Neapolitan buildings, rusted military-industrial structures, aqua translucent plastic, mirror chrome and Y2K water-glass reflections beneath the continuously erupting Mount Vesuvius, active orange lava and suspended ash. Physical robots and analog machines populate the world, with abstract colored symbols on signs and controls. vivid saturated full color, ultra high resolution. overall_soundscape: Returning market bustle, café machinery, distant tram bells, gentle relay hum and the recurring three-knock motif. non_diegetic_music: Original very low unresolved metallic drone ending after the fourth knock.
```

---

## ✂️ Montaggio

1. Aggiungi logo, titolo episodio e nomi della sigla in post: i pannelli generati restano grafici e senza testo leggibile.
2. Conserva il suono H3 per dialoghi provvisori, impatti, macchine e vulcano; rifai in post le battute che non escono pulite.
3. La sigla occupa i Clip 009–012; il reprise dei credits è nel Clip 119.
4. Il Clip 120 è una scena dopo i titoli e apre il mistero dell’episodio successivo.
5. Le cinque dipendenze sono opportunità di raccordo, non una catena obbligatoria.

## 🔗 Riferimenti

- [[DaProd-Cinema/Guida-MiniMax-H3-WanGP|Guida MiniMax H3 / WanGP]]
- [[DaProd-Produzioni/DaProdUniverso|DaProdUniverso]]
- [[DaProd-Produzioni/Personaggi/sinteticoMC|sinteticoMC]]
- [[DaProd-Cinema/Prompt-H3-MisterK-Ruggine-Sitcom|Mister K e Ruggine — scenette sitcom]]
