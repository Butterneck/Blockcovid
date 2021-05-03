## Requisiti di sistema
*TODO: requisiti minimi di sistema per far girare tutto correttamente (essenzialmente la potenza di calcolo minima richiesta e che problemi può dare ad esempio su windows)*

## Configurazione ambiente di sviluppo
Il *backend* fa ampio uso di *containerizzazione*. Ciò permette di virtualizzare i diversi servizi di cui è composto, evitando così di dover installare e configurare su ogni sistema tutti gli strumenti e le tecnologie di cui fa uso.</br>
I passi necessari da eseguire sono i seguenti:

1. Installare (o aver installato) sul proprio sistema lo strumento **Git** ([qui](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) la guida ufficiale), il quale permette il controllo e versionamento del codice sorgente;
   
2. Installare il motore per JavaScript **Node.js** (versione LTS), scaricando l'installer da [questo indirizzo](https://nodejs.org/it/download/), il quale include il relativo gestore di pacchetti **npm** anch'esso necessario;
   
3. Per la gestione delle applicazioni *containerizzate*, è necessario installare sul proprio sistema i software **Docker** e **Docker Compose**.
Di seguito le guide ufficiali per i diversi sitemi operativi: </br>
[Download e installazione Docker](https://docs.docker.com/get-docker/);
[Download e installazione Compose](https://docs.docker.com/compose/install/);

5. Clonare in locale la meta-repository da questo indirizzo: https://gitlab.com/sweleven/blockcovid ;

6. Posizionarsi da terminale dentro la suddetta repository clonata ed eseguire il comando `npm i` per installare il pacchetto `meta` https://www.npmjs.com/package/meta ;
   
7. Rimanendo da terminale sempre dentro la stessa repository eseguire il comando `npx meta git update` per scaricare automaticamente tutte le repository del progetto;
   
8. Se tutto è stato fatto correttamente, per eseguire il *backend* sarà sufficiente avviare **Docker** e successivamente digitare il comando `make up` da terminale all'interno della repository. Per il completamento del processo è necessario attendere almeno qualche minuto.
   >Se si utilizza **Windows**, `make up` non viene nativamente riconosciuto. Basterà installare il comodo gestore di pacchetti [chocolatey](https://chocolatey.org/install) ed eseguire poi, da terminale, il comando `choco install make`.



## Tecnologie utilizzate
- **Nestjs:** framework **Node.js** progressivo per la creazione di applicazioni lato server efficienti, affidabili e scalabili; utilizza la sintassi del linguaggio **Typescript** ed è stato utilizzato principalmente per sviluppare i divesi servizi messi a disposizione dal *backend*. </br>
  [Documentazione Nestjs](https://docs.nestjs.com/);
  [Documentazione Node.js](https://nodejs.org/it/docs/);
  [Documentazione Typescript](https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes.html);

- **Kubernetes:** sistema usato per *containerizzare* i servizi del prodotto; automatizza la distribuzione, la scalabilità e la gestione di questi. </br>
  [Documentazione ufficiale](https://kubernetes.io/docs/home/);

- **Keycloak:** *IAM provider* adottato per la gestione degli account registrati nel sistema. </br>
  [Documentazione ufficiale](https://www.keycloak.org/documentation);

- **Kong:** *API gateway* performante ed ottimizzato per i *microservizi*, adottato per gestire in modo centralizzato l'autenticazione e l'autorizzazione dei vari utilizzatori dell'applicativo. </br> 
  [Documentazione ufficiale](https://docs.konghq.com/?_ga=2.93577566.2121013021.1620045998-1484959525.1616409224&_gac=1.93528815.1616409224.CjwKCAjwgOGCBhAlEiwA7FUXkho9rTweO3FbOmCNUyXX7SyL0HWzMge4NZM3ilDQ3Znv9COIPgnjBxoCTmMQAvD_BwE);

- **MongoDB:** *DBMS* non relazionale, orientato a documenti di tipo **json** con schema dinamico. Viene utilizzato per l'archiviazione dei dati, in particolare sfruttando lo strumento di *object modeling* per Node.js, **Mongoose**. </br>
  [Documentazione MongoDB](https://docs.mongodb.com/manual/);
  [Documentazione Mongoose](https://mongoosejs.com/docs/guide.html);

- **Infura:** *nodo* che permette di processare informazioni in *Blockchain* tramite **Ethereum**. Viene utilizzato per salvare i dati richiesti in modo certificato ed immutabile. </br>
  [Documentazione ufficiale](https://infura.io/docs/ethereum);

- **RabbitMQ:** viene utilizzato come *message broker* per l'interazione con la *Blockchain*. </br>
  [Documentazione ufficiale](https://www.rabbitmq.com/documentation.html);




