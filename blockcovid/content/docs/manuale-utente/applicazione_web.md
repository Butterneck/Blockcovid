---
title: "Applicazione web"
description: "Web application."
date: 2020-10-06T08:48:57+00:00
lastmod: 2020-10-06T08:48:57+00:00
draft: false
images: []
menu:
  docs:
    parent: "manuale-utente"
weight: 100
toc: true
---

## Requisiti

L'applicazione Web rende disponibili una serie di funzionalità legate alla **gestione** ed al **monitoraggio** delle attività degli utenti, delle postazioni e delle stanze presenti nell'edificio. L'accesso al portale Web è pertanto riservato solamente all'utenza in possesso di credenziali con permessi di **amministratore**.

## Installazione

Per poter utilizzare l'applicazione, è necessario che il proprio _amministratore_ di sistema abbia installato con successo l'applicativo sul _server_. Per utilizzare l'applicazione appena installata, è sufficiente collegarsi tramite browser all'_indirizzo ip_ interno del _server_.

## Autenticazione

### Login

Le funzionalità fornite dall'applicazione Web sono disponibili solo dopo aver effettuato la procedura di login con le credenziali da _amministratore_. </br>
Per effettuare il login sarà sufficiente inserire le proprie credenziali (indirizzo email di registrazione e password personale) nei campi dati del form dedicato, che compare all'avvio del _portale_ web.

<img src="../assets/web/login.png" alt="schermata login" caption="<em>schermata login</em>" class="border-0" width="100%">

### Logout

Per effettuare la disconnessione dalla sessione attiva nell'applicazione, sarà sufficiente selezionare la funzionalità di logout presente come voce del menù a tendina che compare cliccando il pulsante per la visualizzazione del proprio profilo in alto a destra, come mostrato nella seguente immagine:

<img src="../assets/web/logout.png" alt="schermata visualizzazione stanze" caption="<em>schermata visualizzazione stanze</em>" class="border-0" width="100%">

## Gestione utenti

### Lista utenti

Nell'apposita sezione a sinistra dell'interfaccia, selezionando la voce **Users**, è possibile visualizzare una lista completa di tutti i profili registrati nel sistema. </br>
Per ogni voce è visibile direttamente il nome utente e la sua mail personale di registrazione.</br>

<img src="../assets/web/users.png" alt="schermata lista utenti" caption="<em>schermata lista utenti</em>" class="border-0" width="100%">

> Sempre nella medesima schermata, è inoltre possibile filtrare la lista inserendo nell'apposito spazio sotto la scritta "**Search user**" il nome, il cognome o l'indirizzo email, facendo così apparire a schermo soltanto i corrispondenti, qualora presenti.

### Dati utente

Selezionando un determinato utente dalla lista si accede alle informazioni più in dettaglio del singolo. </br>
Sono quindi visualizzabili le seguenti informazioni:

1. **nome**: il nome dell'utente registrato;
2. **cognome**: il cognome dell'utente registrato;
3. **indirizzo email**: l'indirizzo email di registrazione dell'utente;
4. **ruolo**: il ruolo dell'utente assegnato in fase di registrazione dall'amministratore;
5. **storico degli accessi effettuati**: uno storico relativo all'utilizzo delle postazioni registrate da parte dell'utente specifico.

La seguente schermata mostra le informazioni in dettaglio di un utente già censito nel sistema:

<img src="../assets/web/dettaglio_utenti.png" alt="schermata dettagli utente" caption="<em>schermata dettagli utente</em>" class="border-0" width="100%">

> Nella parte a destra dell'immagine è possibile vedere la sezione "**User history**", ovvero una lista a video relativa a tutti gli accessi effettuati dall'utente selezionato all'interno della struttura.

### Modifica

Per modificare i dati di un singolo utente, dalla schermata di visualizzazione della lista degli utenti censiti nel sistema, all'_amministratore_ basterà cliccare con il tasto sinistro del mouse sopra l'utente desiderato.
Dalla nuova schermata raggiunta, l'_amministratore_ potrà modificare in maniera semplice ed intuitiva le informazioni del singolo utente quali nome, cognome, indirizzo email ed il ruolo semplicemente interagendo con esse tramite selezione con il tasto sinistro del mouse.
Un esempio di visualizzazione in dettaglio dei dati di un singolo utente e di modifica degli stessi è visibile nella schermata sottostante:

<img src="../assets/web/dettaglio_utenti.png" alt="schermata modifica dettagli utente" caption="<em>schermata modifica dettagli utente</em>" class="border-0" width="100%">

> La "**User history**" di un utente non è modificabile.

> Qualora le nuove informazioni inserite contengano caratteri non ammissibili o si inserisca un nuovo indirizzo email già presente nel sistema, verrà visualizzato un messaggio di errore auto-esplicativo.

### Aggiunta

Entrando nella sezione **Users**, visibile a sinistra dell'interfaccia, oltre a visualizzare la lista di tutti gli account registrati nel sistema, è possibile aggiungere un nuovo utente premendo sull’apposita funzionalità di aggiunta denotata dalla seguente icona: <img src="../assets/web/addbutton.png" alt="icona aggiungi" caption="<em>icona aggiungi</em>" class="border-0" width="10%"></br>

Una volta invocata la funzione di aggiunta, apparirà una nuova schermata a video dove sarà necessario inserire l'indirizzo email del nuovo utente e, dopo aver premuto sul pulsante recante la scritta "**next**", selezionare il ruolo da assegnarvi.<br>
<img src="../assets/web/adduser.png" alt="schermata aggiunta utente" caption="<em>schermata aggiunta utente</em>" class="border-0" width="100%"></br>

> Qualora l'indirizzo email inserito contenga caratteri non validi o sia già presente nel sistema, verrà visualizzato a video un messaggio di errore auto-esplicativo.

Una volta fatto ciò, e premuto sull'apposito tasto **Confirm**, verra' automaticamente inviata una email all'indirizzo email appena inserito contenente un link per permettere all'_utente_ di completare la procedura di registrazione.

La seguente schermata raffigura la richiesta di conferma di un inserimento di un nuovo utente nel sistema discussa precedentemente:

<img src="../assets/web/adduser2.png" alt="schermata finale aggiunta utente" caption="<em>schermata finale aggiunta utente</em>" class="border-0" width="100%">

### Rimozione

Entrando nella sezione **Users**, visibile a sinistra dell'interfaccia, è possibile visualizzare un elenco di tutti gli utenti registrati nel sistema. Per eliminare definitivamete un utente, basterà cliccare sopra la voce dell'utente desiderato e selezionare l'apposita voce di **rimozione utenza** contrassegnata dalla seguente icona: <img src="../assets/web/icona_rimozione.png" alt="icona aggiungi" caption="<em>icona aggiungi</em>" class="border-0" width="10%">.

Una volta selezionata l'apposita funzionalità di rimozione, l'_amministratore_ dovrà confermare la volontà di eliminare l'utente selezionato dalla successiva schermata premendo il tasto recante il testo "**delete**" come riportato nella seguente immagine:

<img src="../assets/web/deletion_confirm.png" alt="conferma rimozione" caption="<em>conferma rimozione</em>" class="border-0" width="100%">

> NB: un utente eliminato dal sistema non sarà più recuperabile.

## Gestione stanze

### Lista stanze

Tramite questa funzionalità, un dipendente può visualizzare una lista di tutte le stanze correntemente registrate nel sistema. Per accedere alla lista delle stanze, il dipendente dovrà accedere all'apposita funzionalità di **visualizzazione stanze** presente nella schermata principale, premendo sulla voce "**Rooms**" presente nel menu a sinistra.

Sempre da questa schermata, l'_amministratore_ può effettuare una ricerca e filtraggio di tutte le stanze censite nel sistema.
I possibili filtri applicabili per una stanza sono i seguenti:

1. **codice identificativo**: è un codice univoco che identifica una stanza nel sistema;
2. **stato**: identifica lo stato corrente di una stanza. Lo stato può essere "abilitato" o "disabilitato".

Una volta selezionato il filtro desiderato, rimarranno automaticamente a video la lista delle stanze che corrispondono ai criteri selezionati dall'_amministratore_.

> Per rimuovere un filtro basterà semplicemente de-selezionarlo cliccandoci sopra con il tasto sinistro del mouse.

Di seguito viene riportata una schermata di esempio relativa alla visualizzazione di tre stanze registate nel sistema:

<img src="../assets/web/room.png" alt="schermata visualizzazione stanze" caption="<em>schermata visualizzazione stanze</em>" class="border-0" width="100%">

### Dati stanza

Tramite questa funzionalità, un _dipendente_ può visualizzare le seguenti informazioni relative al dettaglio di una singola stanza selezionata registrata nel sistema:

1. **codice stanza**: è un codice univoco che identifica una stanza censita nel sistema;
2. **panoramica postazioni interne**: un elenco esplicativo relativo agli stati delle postazioni interne alla stanza selezionata;
3. **numero utenti presenti**: il totale degli utenti presenti all'interno della stanza selezionata.

Di seguito viene riportata una schermata di esempio relativa alla visualizzazione di tre stanze registate nel sistema:

<img src="../assets/web/postazioni_stanza.png" alt="schermata visualizzazione postazioni" caption="<em>schermata visualizzazione postazioni</em>" class="border-0" width="100%">

### Visualizzazione totalità utenti presenti

Una volta visualizzati i dettagli realtivi alla stanza selezionata, un _amministratore_ può visualizzarne in **real-time** il numero totale degli utenti attivi correntemente presenti nella stanza selezionata. La totalità degli utenti presenti apparirà in automatico nel momento in cui un amministratore visualizzaerà i dettagli relativi alla stanza desiderata.

### Modifica

Tramite questa funzionalità un _amministratore_ può modificare tutti i dettagli relativi ad una stanza precedentemente registrata nel sistema. I dettagli di una singola stanza modificabili, per scelta architetturale, sono solamente il codice identificativo.

### Modifica codice stanza

Per modificare il codice identificativo della nuova stanza, l'_amministratore_ dovrà accedere alla pagina relativa al dettaglio della stanza selezionata, ed invocare l'apposita funzionalità di rimozione contrassegnata dall'icona a forma di matita <img src="../assets/web/x_delete.png" alt="icona matita](../assets/web/matita.png). Una volta selezionata la funzionalità di modifica, apparirà una barra testuale dove si potrà assegnare il nuovo codice identificativo alla stanza selezionata. Per confermare l'effettivo cambiamento del codice identificativo, l'_amministratore_ dovrà confermare le modifiche effettuate premendo sull'apposita icona "![icona apporta modifica](../assets/web/v_confirm.png)", o annullarle premendo sull'icona denotata con il simbolo "![icona annulla modifica" caption="<em>icona matita](../assets/web/matita.png). Una volta selezionata la funzionalità di modifica, apparirà una barra testuale dove si potrà assegnare il nuovo codice identificativo alla stanza selezionata. Per confermare l'effettivo cambiamento del codice identificativo, l'_amministratore_ dovrà confermare le modifiche effettuate premendo sull'apposita icona "![icona apporta modifica](../assets/web/v_confirm.png)", o annullarle premendo sull'icona denotata con il simbolo "![icona annulla modifica</em>" class="border-0" width="100%">", come rappresentato nella seguente immagine:
<img src="../assets/web/modifica_c_s_eff.png" alt="modifica codice identificativo stanza" caption="<em>modifica codice identificativo stanza</em>" class="border-0" width="100%">

> In caso di codice identificativo mal formato, contenente quindi caratteri non validi, o già utilizzato da un'altra stanza, il sistema informerà a video l'_amministratore_ con un messaggio di avviso auto-esplicativo, e non permetterà la modifica del codice identificativo della stanza.

### Disabilita/riabilita stanza

Per contrassegnare la stanza come disabilitata, non permettendone quindi l'uso da parte di alcun dipendente, l'_amministratore_ dovrà accedere alla schermata riepilogativa del dettaglio della stanza, e selezionare la funzionalià di disabilitazione stanza contrassegnata dalla seguente icona: <img src="../assets/web/enable_disable_room_icon.png" alt="icona abilita-disabilita stanza" caption="<em>icona abilita-disabilita stanza</em>" class="border-0" width="10%">

> Per abilitare nuovamente una stanza segnata precedentemente disabilitata, l'_amministratore_ dovrà semplicemente cliccare sul cursore precedentemente rappresentato, facendolo tornare di colore verde.

> Una stanza abilitata nuovamente torna ad essere **servibile** dagli utenti registrati nell'applicazione.

### Aggiunta

Tramite questa funzionalità un _amministratore_ può aggiungere una nuova stanza all'elenco delle stanze già censite nel sistema.
Per aggiungere una nuova stanza, l'_amministartore_ dovrà accedere alla pagina di gestione delle stanze premendo sull'apposita funzionalità di **aggiunta** denotata dalla seguente icona: <img src="../assets/web/addbutton.png" alt="schermata aggiunta stanza1" caption="<em>schermata aggiunta stanza1</em>" class="border-0" width="10%">

Per censire una nuova stanza nel sistema l'_amministratore_ dovrà inserire negli appositi spazi le seguenti informazioni:

1. **codice identificativo nuova stanza**: è un codice alfanumerico che identifica in maniera univoca la stanza all'interno del sistema. Questo codice non può contenere caratteri speciali;

<img src="../assets/web/nomestanza.png" alt="schermata aggiunta stanza1" caption="<em>schermata aggiunta stanza1</em>" class="border-0" width="100%">

1. **codice tag RFID**: questo codice serve al sistema per permettere la prenotazione e l'igienizzazione della stanza. Ogni codice RFID che contrassegna una stanza è univoco.

<img src="../assets/web/roomrfid.png" alt="schermata aggiunta stanza1" caption="<em>schermata aggiunta stanza1</em>" class="border-0" width="100%">

Una volta compilati correttamente tutti i campi di cui sopra, per **confermare l'aggiunta** di una nuova stanza, basterà premere il pulsante "**Confirm**" presente nella medesima schermata come nell'immagine:

<br><img src="../assets/web/roomconfirm.png" alt="schermata aggiunta stanza1" caption="<em>schermata aggiunta stanza1</em>" class="border-0" width="100%"></br>

> In caso di errore sui campi dati quali codice identificativo o codice tag RFID, il sistema mostrerà a video un messaggio di errore auto-esplicativo, che informerà l'_amministratore_ sui campi da risolvere per permettere un corretto inserimento della stanza.

### Rimozione

Tramite questa funzionalità un _amministratore_ può rimuovere definitivamente una stanza precedentemente censita nel sistema.
Per **rimuovere** una stanza registrata, dalla pagina di gestione delle stanze, l'_amministratore_ selezionerà la stanza desiderata per la rimozione e si invocherà la funzionalità di **rimozione definitiva** denotata dalla seguente icona: <img src="../assets/web/rimozione_stanza.png" alt="rimozione stanza" caption="<em>rimozione stanza</em>" class="border-0" width="10%">

Per confermare la volontà di rimuovere definitivamnte la stanza selezionata dal sistema, l'_amministratore_ dovrà confermare la scelta premendo il pulsante recante la scritta "**delete**" come rappresentato nella seguente immagine:

<img src="../assets/web/conferma_rimozione_stanza.png" alt="conferma rimozione stanza" caption="<em>conferma rimozione stanza</em>" class="border-0" width="100%">

> Una volta eliminata una stanza, questa sarà eliminata **definitivamente**, ed ogni postazione al suo interno, comprensive di eventuali prenotazioni, verranno automaticamente **cancellate**.

## Gestione postazioni

### Lista postazioni

Tramite questa funzionalità, un _amministratore_ può visualizare a video l'insieme delle postazioni registrate all'interno di una specifica stanza selezionata.
Per accedere alla lista delle postazioni, l'_amministratore_ dovrà selezionare con il tasto sinistro del mouse la stanza desiderata dalla schermata riepilogativa delle stanze registrate nel sistema. Una volta selezionata una stanza, apparirà a video la lista delle postazioni ad essa associate.

Di seguito, viene riportata una schermata illustrativa mostrante una lista di postazioni associate ad una determinata stanza:

<img src="../assets/web/listapostazioni.png" alt="schermata visualizzazione stanze" caption="<em>schermata visualizzazione stanze</em>" class="border-0" width="100%">

Un _amministratore_ può eseguire una ricerca con filtraggio delle postazioni. E' possibile filtrare le postazioni secondo i seguenti parametri:

1. **codice identificativo**: è un codice alfanumerico che identifica in maniera univoca una postazione all'interno del sistema. Questo codice non può contenere caratteri speciali;
2. **postazioni prenotate**: tramite attivazione di questo filtro verranno mostrate a video solamente le postazioni cui stato attuale è "prenotato";
3. **postazioni occupate**: tramite attivazione di questo filtro verranno mostrate a video solamente le postazioni cui stato attuale è "occupato";
4. **postazioni libere**: tramite attivazione di questo filtro verranno mostrate a video solamente le postazioni cui stato attuale è "libera";
5. **postazioni igienizzate**: tramite attivazione di questo filtro verranno mostrate a video solamente le postazioni cui stato attuale è "igienizzata";
6. **postazioni sporche**: tramite attivazione di questo filtro verranno mostrate a video solamente le postazioni cui stato attuale è "sporco";
7. **postazioni abilitate**: tramite attivazione di questo filtro verranno mostrate a video solamente le postazioni cui stato attuale è "abilitata";
8. **postazioni disabilitate**: tramite attivazione di questo filtro verranno mostrate a video solamente le postazioni cui stato attuale è "disabilitata".

### Dati postazione

Dalla pagina di visualizzazione delle postazioni interne ad una stanza, l'_amministratore_ ha la possibilità di visualizzare in dettaglio le informazioni specifiche di una singola postazione desiderata.
Le informazioni relative ad ogni postazione visibili da questa schermata sono le seguenti:

1. **codice identificativo postazione**: è un codice alfanumerico univoco che identifica la specifica postazione all'interno del sistema. Questo codice non può contenere caratteri speciali.
2. **stato della postazione**: questa voce identifica lo stato attuale della postazione, che può essere uno tra i seguenti:
   1. _libera_: identifica una postazione fruibile da un utente;
   2. _occupata_: identifica una postazione attualmente occupata da un utente;
   3. _disabilitata_: identifica una postazione non prenotabile né servibile da un utente in quanto disabilitata da un _amministratore_.
3. **stato della pulizia della postazione**: questa voce identifica appunto lo stato di pulizia della postazione, che può essere uno tra i seguenti:
   1. _sporca_: identifica una postazione precedentemente utilizzata da un utente e non più servibile fino a nuova igienizzazione;
   2. _igienizzata_: identifica una postazione pulita e servibile da un altro utente.

> Per permettere all'amministratore di visualizzare a video in maniera più semplice e veloce le postazioni libere od occupate, si è deciso di implementare una semplice icona nella schermata corrente. Le icone contrassegnanti le postazioni possono essere le seguenti:

1. <img src="../assets/web/icona_postazione_libera.png" alt="icona postazione libera" caption="<em>icona postazione libera</em>" class="border-0" width="10%"> per identificare una postazione attualmente libera;
2. <img src="../assets/web/icona_postazione_occupata.png" alt="icona postazione occupata" caption="<em>icona postazione occupata</em>" class="border-0" width="10%"> per identificare una postazione attualmente occupata;

### Modifica

Tramite questa funzionalità un _amministratore_ può modificare tutti i dettagli relativi ad una postazione abbinata ad una stanza. I dettagli di una singola postazione modificabili sono i seguenti:

1. **codice identificativo postazione**;
2. **codice tag RFID**.

### Modifica codice postazione

Ogni postazione è contrassegnata con un codice identificativo, che la identitica **univocamente** tra tutte le altre postazioni registrate nel sistema. Il codice identificativo permette, inoltre, alla postazione di essere prenotabile ed igienizzabile dagli utenti.
Nel caso in cui l'_amministratore_ volesse modificare il codice identificativo relativo ad una determinata postazione, dovrà prima accedere alla pagina di gestione delle postazioni da applicativo web.
Per modificare il codice postazione, l'_amministratore_ utilizza la funzionalità di modifica situata nella medesima schermata denotata dalla seguente icona: <img src="../assets/web/modifica.png" alt="schermata modifica stanza" caption="<em>schermata modifica stanza</em>" class="border-0" width="10%">

Una volta terminata la modifica del codice, l'_amministratore_ deve confermare i cambiamenti eseguiti premendo l'apposito pulsante di conferma identificato dalla seguente icona: <img src="../assets/web/modifica_ok.png" alt="schermata modifica_ok" caption="<em>schermata modifica_ok</em>" class="border-0" width="10%">.

> Nel caso in cui il sistema mostri un messaggio di errore relativo al codice identificativo appena inserito, verificare che il codice sia composto solamente caratteri alfanumerici e non da caratteri speciali.

Un esempio di funzionalità di modifica del codice identificativo della postazione può essere quanto segue:

<img src="../assets/web/modifica_codice.png" alt="schermata modifica codice postazione" caption="<em>schermata modifica codice postazione</em>" class="border-0" width="100%">

### Modifica codice RFID

Il codice RFID permette alla postazione di essere prenotabile ed igienizzabile dagli utenti dell'applicazione.
Nel caso in cui l'_amministratore_ volesse modificare il codice RFID relativo ad una determinata postazione, dovrà prima accedere alla pagina di gestione delle postazioni da applicativo web.
Per modificare il codice postazione, l'_amministratore_ utilizza la funzionalità di modifica situata nella medesima schermata denotata dalla seguente icona: <img src="../assets/web/modifica.png" alt="schermata modifica codice RFID" caption="<em>schermata modifica codice RFID</em>" class="border-0" width="10%">

Una volta terminata la modifica del codice, l'_amministratore_ deve confermare i cambiamenti eseguiti premendo l'apposito pulsante di conferma identificato dalla seguente icona: <img src="../assets/web/modifica_ok.png" alt="schermata modifica_ok" caption="<em>schermata modifica_ok</em>" class="border-0" width="10%">

Un esempio di funzionalità di modifica del codice RFID della postazione può essere quanto segue:

<img src="../assets/web/modifica_rfid.png" alt="schermata modifica" caption="<em>schermata modifica</em>" class="border-0" width="100%">

### Disabilita/riabilita postazione

Per interrompere la possibilità di uso e prenotazione di una postazione da parte di un qualsiasi utente, l'_amministratore_ può marcare una specifica postazione come disabilitata.
Per fare ciò, l'_amministratore_ dovrà accedere alla pagina di visualizzazione dei dettagli relativa ad una postazione precedentemente selezionata e, successivamente, si dovrà cliccare sull'apposita funzionalità di disabilitazione di una postazione, denotata dal bottone con la scritta "**disabilita postazione**".
Una volta premuto il pulsante, la postazione aggiornerà il suo stato in "disabilitata", e tutte le prenotazioni pendenti per quella specifica postazione saranno **automaticamente cancellate** dal sistema.

> Per riabilitare nuovamente una postazione precedentemente contrassegnata come disabilitata, un _amministratore_ dovrà entrare nella pagina del dettaglio relativa alla postazione disabilitata e riattivare la postazione premendo sull'apposita funzionalità di ri-abilitazione di una postazione denotata dal bottone recante la scritta "riabilita la postazione".

Una postazione **abilitata** sarà nuovamente **prenotabile** e **servibile** da tutti gli utenti registrati nel sistema.

### Aggiunta

Tramite questa funzionalità un _amministratore_ può aggiungere una nuova postazione da una stanza censita nel sistema.
Per aggiungere una nuova postazione, l'_amministratore_ dovrà accedere alla pagina di gestione delle stanze, e selezionare con il tasto sinistro del mouse la stanza dove si desidera aggiungere una nuova postazione.
Per aggiungere una nuova postazione alla stanza precedentemente selezionata, basterà premere sull'apposito pulsante di **aggiunta** denotato dalla seguente icona: <img src="../assets/web/addbutton.png" alt="schermata aggiunta stanza1" caption="<em>schermata aggiunta stanza1</em>" class="border-0" width="10%">

Per registrare una nuova postazione nel sistema l'_amministratore_ dovrà inserire negli appositi spazi le seguenti informazioni:

1. **codice identificativo postazione**: è un codice alfanumerico univoco che identifica la specifica postazione all'interno del sistema. Questo codice non può contenere caratteri speciali;
2. **codice tag RFID**: questo codice serve al sistema per permettere la prenotazione e l'igienizzazione da parte di un utente della postazione. Ogni codice RFID che contrassegna una postazione è univoco.

Una volta compilati correttamente tutti i campi di cui sopra, per confermare l'aggiunta di una nuova postazione, basterà premere il pulsante "**confirm**" presente nella medesima schermata come nella seguente immagine:

<img src="../assets/web/creapostazione.png" alt="schermata visualizzazione stanze" caption="<em>schermata visualizzazione stanze</em>" class="border-0" width="100%">

> In caso di errore sui campi dati quali stanza, codice identificativo o codice tag RFID, il sistema mostrerà a video un messaggio di errore auto-esplicativo, che informerà l'amministratore sui campi da risolvere per permettere un corretto inserimento della nuova postazione a sistema.

### Rimozione

Tramite questa funzionalità un _amministratore_ può rimuovere una postazione presente in una stanza censita nel sistema.
Per rimuovere una postazione, l'_amministratore_ dovrà accedere alla pagina di gestione delle postazioni, e selezionare con il tasto sinistro del mouse la postazione desiderata.

Per **rimuovere** la postazione precedentemente selezionata dal sistema, l'_amministratore_ invocherà l'apposita funzionalità di rimozione dell'applicazione denotata dalla seguente icona: <img src="../assets/web/rimozione.png" alt="rimozione postazione" caption="<em>rimozione postazione</em>" class="border-0" width="10%">

Una volta confermata la volontà di eliminare la postazione tramite finestra di dialogo, la postazione verrà **completamente eliminata** dal sistema.

> Eventuali prenotazioni attive su una postazione eliminata verranno **automaticamente cancellate**.

## Scaricamento report

Tramite applicazione web, premendo sull'apposita voce "**Reports**" presente nel menu, è possibile accedere alla sezione di reportistica.
Da questa schermata, un _amministratore_ autenticato avrà la possibilità di **consultare** e **scaricare** report di prenotazione ed igienizzazione delle postazioni registrate nel sistema.

Per generare e scaricare un report l'_amministratore_ dovrà eseguire i seguenti passaggi:

### Selezione data

Da apposito widget a calendario _evidenziato in rosso_, l'amministratore può **selezionare la data** desiderata nel quale si desidera consultare lo storico di utilizzo ed igienizzazione delle postazioni, come nella seguente immagine:

<img src="../assets/web/report1.png" alt="schermata report - data" caption="<em>schermata report - data</em>" class="border-0" width="100%">

### Selezione postazioni

Una volta selezionata la data, apparirà a video la **lista di postazioni** nelle relative stanze censite nel sistema. Per avere un report di una specifica postazione, l'_amministratore_ dovrà selezionare la postazione, o gruppo di postazioni desiderate, tramite _click_ sinistro del mouse.

<img src="../assets/web/report2.png" alt="schermata report - postazioni" caption="<em>schermata report - postazioni</em>" class="border-0" width="100%">

### Selezione utenti

Una volta selezionate le postazioni desiderate, il sistema mostrerà a video la **lista degli utenti** censiti ed attualmente registrati, in questa schermata evidenziati in rosso. Affinchè il report contenga informazioni dettagliate su un singolo o gruppo di utenti relativo allo storico di utilizzo ed igienizzazioni delle postazioni precedentemente selezionate, l'_amministratore_ dovrà selezionare, con il tasto sinistro del mouse, la lista di utenti desiderati.

<img src="../assets/web/report3.png" alt="schermata report - utenti" caption="<em>schermata report - utenti</em>" class="border-0" width="100%">

### Tipo report

Terminata la selezione di utenti e stanze, l'_amministratore_ avrà la possibilità di selezionare **due** tipi di reportistica offerti dall'applicazione:

1. **Cleanings history**, ovvero lo storico delle igienizzazioni effettuate dagli utenti selezionati;
2. **Bookings history**, ovvero lo storico delle prenotazioni effettuate dagli utenti selezionati.
   <img src="../assets/web/report4.png" alt="schermata report - tipo report" caption="<em>schermata report - tipo report</em>" class="border-0" width="100%">

### Conferma

Inseriti tutti i dati richiesti, il sistema, prima di generare il report, chiederà **conferma all'_amministratore_** circa i dati precedentemente inseriti.
Se i dati inseriti sono corretti, l'_amministratore_ potrà confermare la creazione del report premendo sul pulsante "**DOWNLOAD**" cerchiato in rosso nell'immagine, altrimenti, per modificare i dati inseriti, basterà premere sul pulsante "**PREV**".

<img src="../assets/web/report5.png" alt="schermata report - tipo report" caption="<em>schermata report - tipo report</em>" class="border-0" width="100%">

<img src="../assets/web/report5.png" alt="Rectangle" caption="<em>Rectangle</em>" class="border-0" width="100%">
