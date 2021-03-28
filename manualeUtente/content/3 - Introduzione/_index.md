Il prodotto di riferimento, descritto in questa sede, viene denominato ***BlockCOVID*** e si riferisce al capitolato **C1**, proposto dall'azienda *Imola Informatica*.

{{< toc >}}

## 3.1 Scopo del documento

Il presente documento ha lo scopo di illustrare e guidare, attraverso descrizioni testuali ed immagini, le diverse tipologie di *utente* nell'utilizzo e nella gestione della piattaforma ***BlockCOVID***. 

In appendice è possibile consultare un apposito glossario dei termini tecnici, o eventualmente ambigui, in questa sede rappresentati in *corsivo*.

## 3.2 Scopo del prodotto
Il *sistema* riguarda il *tracciamento* dell'utilizzo e dell'igienizzazione di postazioni di lavoro all'interno di relative stanze, nel contesto di un laboratorio informatico.

Il prodotto si compone principalmente di un'***applicazione web***, in comunicazione con un *server* centralizzato, per la gestione dell'intera piattaforma e di un'***applicazione mobile***, che permetta ai dipendenti di usufruire del servizio.

Sono garantite le seguenti funzionalità per tre principali categorie di utenti:

+ ***Amministratore:*** è l'unica tipologia di utente ad avere accesso all'applicazione web ed attraverso di essa, previa dovuta autenticazione, può:
    + **Visualizzare gli utenti:** è possibile visualizzare la lista di tutti gli utenti registrati presso il sistema e le relative informazioni, tra cui nome, cognome, email, ruolo e storico degli accessi; è possibile inoltre ricercare specifici utenti per nome, cognome, indirizzo email o filtrare la lista per relativo ruolo;
    + **Gestire gli utenti:** è possibile aggiungere nuovi utenti al sistema, inserendo la relativa email ed assegnandovi un ruolo; modificarne i dati; rimuovere definitivamente un utente dal sistema; 
    + **Visualizzare le stanze:** è possibile visualizzare la totalità delle stanze registrate presso il sistema e le relative informazioni; per ogni stanza è possibile visualizzarne il codice identificativo, lo *stato* di pulizia, gli utenti e le postazioni al suo interno; possono essere ricercate per codice identificativo o filtrate a seconda del relativo stato;
    + **Gestire le stanze:** è possibile aggiungere nuove stanze, assegnandovi un codice identificativo univoco ed un relativo tag *RFID*, o rimuoverne definitivamente dal sistema; all'occorrenza modificarne i dati, disabilitarle o riabilitarle;
    + **Visualizzare le postazioni:** è possibile visualizzare tutte le postazioni presentei nel sistema, ricercarle per relativo codice identificativo o filtrarle per stato; per ogni postazione è possibile visualizzare il codice identificativo, il tag RFID associato, lo stato di utilizzo e di pulizia;
    + **Gestire le postazioni:** allo stesso modo della stanze è possibile aggiungere nuove postazioni al sistema, selezionando la stanza di riferimento ed assegnandovi un codice identificativo univoco associato ad un relativo tag *RFID*; è possibile modificare i dati di una postazione, disabilitarla, riabilitarla o rimuoverla definitivamente dal sistema;
+ ***Dipendente:*** rappresenta un utente utilizzatore della postazioni; autenticandosi presso l'applicazione mobile, attraverso di essa può:
    + **Prenotare una postazione:** l'utente può scegliere una postazione selezionandola tra quelle diponibili, oppure ricercarne una in particolare; nella fase di prenotazione vengono specificate data, ora e durata prevista di questa;
    + **Gestire le prenotazioni:** è possibile visualizzare un elenco delle prenotazioni e per ognuna di esse è possibile vedere codice identificativo della prenotazione, della postazione e della stanza, la data, l'orario e la durata; è inoltre possibile cancellare una prenotazione precedentemente effettuata;
    + **Segnalare l'utilizzo di una postazione:** attraverso la scansione del relativo tag RFID tramite *smartphone*, il dipedente registra l'inizio dell'utilizzo della postazione; prima di ciò visualizza l'eventuale stato di disponibilità o di pulizia di questa e, tramite conferma, ne può avviare effettivamente l'utilizzo. La presenza fisica attiva dell'utente viene monitorata attraverso segnale *GPS*; 
    + **Terminare l'utilizzo della postazione:** ri-scansionando il tag RFID, il dipendente registra di aver terminato di utilizzare la postazione; in questo processo può inoltre segnalare l'avvenuta igienizzazione individuale della postazione;
+ ***Igienizzatore:*** l'utente igienizzatore, autenticato presso l'applicazione mobile, può:
    + **Visualizzare le stanze da igienizzare:** è possibile vedere una lista delle stanze che necessitano di igienizzazione; risultano tali le stanze che hanno anche solo una postazione da igienizzare;
    + **Segnalare l'igienizzazione:** attraverso la scansione del tag RFID associato alla stanza, viene registrata l'avvenuta igienizzazione di questa;

+ Tutti gli utenti hanno inoltre accesso alle seguenti funzionalità dell'applicazione mobile: 

    + **Completare la registrazione:** quando l'amministratore inserisce un nuovo utente, a questo viene inviata un'email contenente un link attraverso il quale viene completata la registrazione dello stesso, inserendo il proprio nome e cognome e creando una nuova password;
    + **Modificare la propria password:** se l'utente è già autenticato può creare direttamente una nuova password inserendo prima quella precedente; se in fase di login ha dimenticato la propria password riceverà un link all'indirizzo email di registrazione per permettere di crearne una nuova;








