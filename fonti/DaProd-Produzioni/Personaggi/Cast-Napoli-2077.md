---
tipo: personaggi
titolo: "Cast di Napoli 2077"
universo: "[[DaProd-Produzioni/DaProdUniverso|DaProdUniverso]]"
produttore: "[[People/Cammo|Cammo]]"
tags: [daprod, lore, personaggi, gamedev, ponticelli, napoli2077]
aggiornato: 2026-08-11
---

# Cast di Napoli 2077 — Robot e Rovine

> Il Vesuvio erutta senza sosta. L'energia è tutto. La legge è un ricordo.
> L'acciaio è la realtà.

Ventisette personaggi fissati da Cammo nel roster "Napoli 2077 — Roboti e Rovine".
È la prima volta che [[DaProd-Produzioni/DaProdUniverso|DaProdUniverso]] ha un **cast
stabile** invece di robot generati di volta in volta: la regola del 2026-07-09 diceva
"nessun cast fisso salvo eccezioni dichiarate", e questa è l'eccezione, dichiarata qui.

Il motto del roster — *"A Napoli, anche i robot hanno un codice"* — è coerente con la
regola psicologica dell'universo: questi robot **si comportano da napoletani**, non da
macchine, ed è dalla scrittura che deve emergere, non da volti umani nei prompt visivi.

## Alleati

| # | Nome | Cifra |
|---|---|---|
| 01 | 'O Meccanico | Ripara, non giudica |
| 02 | La Lavandaia | Ti pulisce dentro e fuori |
| 03 | Don Circuito | Ex prete, ora guida |
| 04 | Lucy Ferrara | Hacker con cuore |
| 05 | Pacco | Corriere veloce |
| 06 | Zia Rosetta | Sa tutti i segreti |
| 07 | Gianni il Muto | Parla con gli occhi |

## Nemici

| # | Nome | Cifra |
|---|---|---|
| 08 | Il Capitano | Regna con il terrore |
| 09 | Bomba | Esplode, poi parla |
| 10 | La Vipera | Tradisce sempre |
| 11 | Mister K | Nessuno conosce il suo volto |
| 12 | I Gemelli | Due menti, una pistola |
| 13 | Madonnina Nera | Vende dolore |
| 14 | Ruggine | Vive solo per distruggere |

## Neutrali

| # | Nome | Cifra |
|---|---|---|
| 15 | Il Mercante | Ha tutto, per un prezzo |
| 16 | Il Barista | Caffè e informazioni |
| 17 | L'Artista | Crea bellezza dal nulla |
| 18 | Il Pescatore | Conosce il mare |
| 19 | La Cartomante | Le carte non mentono |
| 20 | Lo Spacciatore | O parti, o paghi |

## Animali robotici

| # | Nome | Cifra |
|---|---|---|
| 21 | Zamp | Cane da guardia |
| 22 | Gatto | Vede tutto |
| 23 | Gabbiano | Ruba e sopravvive |
| 24 | Polpo | Re delle profondità |
| 25 | Squalo | Cacciatore del golfo |
| 26 | Delfino | Veloce e intelligente |
| 27 | Granchio | Duro a morire |

## Nel gioco

Il cast è codificato in `Assets/Ponticelli/Scripts/RobotRoster.cs` e alimenta la
schermata **Personaggio** del menu iniziale: alleati e neutrali sono selezionabili,
nemici e animali popolano il quartiere. Tenerlo come dato unico serve a far combaciare
menu, futuri dialoghi e questa pagina.

## Domande aperte per Cammo

- **Il Barista** (16): per ora è un ruolo del roster, non va identificato automaticamente con Robo-Peppe finché il progetto Unity non lo stabilisce.
- Gli animali robotici marini (Polpo, Squalo, Delfino) restano parte del mondo e del roster; la loro presenza nella mappa giocabile dipende dall'area costiera prevista, non è ancora un requisito della prima zona.
- L'apertura del gioco non ha ancora un personaggio iniziale stabilito: la schermata consente la scelta del roster prima dell'avvio.

## Collegamenti

- [[DaProd-Produzioni/DaProdUniverso|DaProdUniverso]] — le regole dell'universo
- [[DaProd-Produzioni/Personaggi/Tipi-di-Robot|Tipi di Robot]] — la tassonomia generale
- [[DaProd-Produzioni/Personaggi/Salvo-il-Resiliente|Salvo il Resiliente]] — personaggio dell'era Godot, da ricollocare nel cast
- [[DaProd-GameStudio/Progetti/Ponticelli-Unity-Stato|Ponticelli — reboot Unity]]
