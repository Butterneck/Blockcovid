Il *sistema* ***BlockCOVID*** riguarda il *tracciamento* dell'utilizzo e dell'igienizzazione di postazioni di lavoro all'interno di relative stanze, nel contesto di un laboratorio informatico.

## Scopo e descrizione generale del prodotto

Il prodotto si compone principalmente di un'***applicazione web***, in comunicazione con un *server* su cui risiede il *backend*, per la gestione dell'intera piattaforma, e di un'***applicazione mobile*** che permetta di usufruire dei servizi offerti.

Sono garantite le seguenti funzionalità per tre principali categorie di *utenti*:

+ ***Amministratore:*** possiede le credenziali di accesso all'applicazione web ed attraverso essa, previa dovuta autenticazione, si può usufruire delle seguenti funzionalità:
    + **Visualizzazione degli utenti:** è possibile visualizzare la lista di tutti gli utenti registrati presso il sistema e le relative informazioni, tra cui nome, cognome, email, ruolo e storico degli accessi. E', inoltre, presente la funzionalità di filtraggio degli utenti dalla lista specificando nome, cognome, indirizzo email o ruolo;
    + **Gestione degli utenti:** è possibile aggiungere nuovi utenti al sistema, inserendo la relativa email univoca ed assegnandovi un ruolo; modificarne i dati o rimuoverli definitivamente dal sistema; 
    + **Visualizzazione delle stanze:** è possibile visualizzare la totalità delle stanze registrate presso il sistema con le relative informazioni. Per ogni stanza è possibile visualizzarne il codice identificativo univoco, lo *stato* di pulizia, gli utenti presenti e le postazioni al suo interno. Le stanze possono essere ricercate per codice identificativo o filtrate a seconda del relativo stato;
    + **Gestione delle stanze:** è possibile aggiungere nuove stanze, assegnandovi un codice identificativo univoco ed un relativo tag *RFID* per il *tracciamento*, o rimuoverne definitivamente dal sistema. Vi è inoltre la possibilità, all'occorrenza, di modificarne i dati, disabilitarle o riabilitarle;
    + **Visualizzazione delle postazioni:** è possibile visualizzare tutte le postazioni presenti nel sistema, ricercarle per relativo codice identificativo o filtrarle per stato. Per ogni postazione è possibile visualizzare il codice identificativo univoco, il tag *RFID* associato, lo stato di utilizzo e di pulizia;
    + **Gestione delle postazioni:** analogamente alle stanze, è possibile aggiungere nuove postazioni al sistema, selezionando la stanza di riferimento ed assegnandovi un codice identificativo univoco associato ad un relativo tag *RFID* per il tracciamento. Si può modificare i dati di una postazione, disabilitarla, riabilitarla o rimuoverla definitivamente dal sistema;
  
+ ***Dipendente:*** rappresenta un utente utilizzatore delle postazioni; autenticandosi presso l'applicazione mobile, attraverso di essa può:
    + **Prenotare una postazione:** l'utente può scegliere e prenotare una postazione selezionandola tra quelle disponibili, dopo aver indicato data, ora e durata prevista di utilizzo;
    + **Gestire le prenotazioni:** è possibile visualizzare un elenco delle prenotazioni effettuate e per ognuna di esse vedere codice identificativo della postazione, della stanza e della prenotazione stessa, la data, l'orario e la durata. Vi è inoltre la possibilità di cancellare una prenotazione futura precedentemente effettuata;
    + **Segnalare l'utilizzo di una postazione:** attraverso la scansione del relativo tag *RFID* tramite *smartphone*, il dipedente registra e *certifica* l'inizio dell'utilizzo di una postazione. Prima di ciò, attraverso la scansione, visualizza l'eventuale stato di disponibilità o di pulizia di questa e, tramite conferma, se possibile, ne avvia effettivamente l'utilizzo. La presenza fisica dell'utente all'interno della stanza viene monitorata in tempo reale attraverso segnale *GPS*; 
    + **Terminare l'utilizzo della postazione:** scansionando nuovmente il tag *RFID*, il dipendente registra e certifica di aver terminato di utilizzare la postazione. In questo processo può inoltre segnalare l'avvenuta igienizzazione individuale della postazione, la quale viene anch'essa eventualmente registrata e certificata;
  
+ ***Igienizzatore:*** l'utente igienizzatore rappresenta l'addetto alle pulizie che si occupa di igienizzare la stanza; autenticato presso l'applicazione mobile può:
    + **Visualizzare le stanze da igienizzare:** è possibile vedere una lista delle stanze che necessitano di igienizzazione. Risultano tali le stanze che hanno anche solo una postazione ancora da igienizzare;
    + **Segnalare l'igienizzazione:** attraverso la scansione del tag *RFID* associato alla stanza, viene registrata e certificata l'avvenuta igienizzazione di questa. Tutte le postazioni interne alla stanza acquisiranno lo stato di igienizzate;

+ Tutti gli utenti hanno inoltre accesso alle seguenti funzionalità dell'applicazione mobile: 

    + **Completamento della registrazione:** quando l'amministratore inserisce un nuovo utente, a questo viene inviata un'email contenente un *link* attraverso il quale viene completata la procedura di registrazione dello stesso, attraverso l'inserimento del proprio nome, cognome e la creazione di una nuova password personale;
    + **Recupero o modifica della password:** se l'utente è già autenticato può modificare la propria password creandone direttamente una nuova dopo aver prima inserito quella precedente. Se in fase di login ha dimenticato la propria password, tramite richiesta riceverà un *link* all'indirizzo email di registrazione per poterne creare una nuova in maniera similare alla fase di registrazione.








