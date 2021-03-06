---
title: "Descrizione mobile app"
description: "Mobile app description."
date: 2020-10-06T08:48:57+00:00
lastmod: 2020-10-06T08:48:57+00:00
draft: false
images: []
menu:
  docs:
    parent: "mobile-app"
weight: 510
toc: true
---

L'applicazione mobile, attraverso l'interazione col *backend* (tramite i servizi che quest'ultimo mette a disposizione), presenta determinate funzionalità, generalmente distinte per due tipi di utenza:
- Funzionalità per il **dipendente**:
  - **prenotare postazioni:** è possibile visualizzare una lista delle postazioni prenotabili in un determinato momento e prenotarne l'utilizzo;
  - **gestire prenotazioni:** è possibile visualizzare sia una lista delle prenotazioni attive che di quelle effettuate in passato;
  - **segnalare la propria presenza:** attraverso la scansione attiva di un tag *RFID* la presenza fisica dell'utente in una postazione (e quindi l'utilizzo della stessa) viene registrata. La presenza del dipendente all'interno della relativa stanza è inoltre monitorata tramite segnale GPS;
  - **segnalare l'igienizzazione:** al termine dell'utilizzo di una postazione, è possibile segnalarne l'avvenuta igienizzazione individuale effettuatavi;
- Funzionalità per l'**igienizzatore**:
  - **lista stanze:** è possibile visualizzare una lista delle stanze che necessitano di igienizzazione, così come una lista delle stanze che sono state igienizzate;
  - **segnalare igienizzazione:** attraverso la scansioe del relativo tag *RFID* l'utente igienizzatore può segnalare e registrare l'avvenuta igienizzazione della relativa stanza.

## Approccio e design pattern utilizzati
Seguendo la documentazione ed i tutorial ufficiali di *Flutter*, ci si è diretti verso l’utilizzo di un approccio in stile *Vanilla*.
In questo modo per ogni pagina dell’applicazione che dovrà essere aggiornata si deve implementare uno stato associato ad essa: questo permette di cambiarla più volte durante la sua stessa vita. Ad esempio, la chiamata del metodo `setState()`, infatti, notifica il *framework* che lo stato della pagina è cambiato e che potrebbe essere necessario ricreare la *UI*; ciò induce il framework stesso a pianificare una *build* per questo specifico stato.

**Pro:**
- facile da capire e imparare;
- nessuna dipendenza esterna richesta;
- utilizzato dai tutorial e guide ufficiale di *Flutter*;
- minore scrittura di codice.
  
**Contro:**
- l’intero albero dei widget mostrati viene ricreato;
- rompe il principio di singola responsabilità: il Widget (pagina) non è solo responsabile di creare l’interfaccia utente, ma deve anche gestire gli stati ed occuparsi dell’interazione col modello;
- la dichiarazione su come lo stato corrente debba essere visualizzato è scritta nella dichiarazione della *UI*, ciò potrebbe portare a scarsa leggibilità e riutilizzabilità del codice.

Il design pattern **dependency injection** è stato utilizzato per il modello, esso permette infatti di ridurre l’accoppiamento e la dipendenza tra le classi.
