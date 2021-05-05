## Requisiti di sistema
*TODO: requisiti minimi di sistema per far girare tutto correttamente (essenzialmente la potenza di calcolo minima richiesta e che problemi può dare ad esempio su windows)*

## Configurazione ambiente di sviluppo
Ogni servizio del *backend* è distribuito sotto forma di *container docker*. Ciò permette di rendere lo sviluppo agnostico rispetto al sistema operativo utilizzato, di evitare conflitti con componenti esterne in quanto ogni container è **autocontenuto**.</br>
I passi necessari da eseguire per il setup del backend sono i seguenti:

1. Installare (o aver installato) sul proprio sistema **Git** ([qui](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) la guida ufficiale), attraverso il quale e' possibile scaricare codice sorgente;
   
2. Installare il motore per JavaScript **Node.js** (versione LTS) e il gestore di pacchetti **npm** ([qui](https://nodejs.org/it/download/) la guida ufficiale);
   
3. Installare (o aver installato) sul proprio sistema l'utility **make**:
   > Su **Linux** è sufficiente eseguire da terminale il comando `sudo make install`;</br> 

   > Se si utilizza **Windows**, è possibile utilizzando il comodo gestore di pacchetti [chocolatey](https://chocolatey.org/install) ed eseguire poi, da terminale, il comando `choco install make`;</br>

   > Su **macOS** è possibile anch'esso da terminale installando prima **brew**, attraverso il comando `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`, e successivamente digitando `brew install make`.
   
4. Per la gestione delle applicazioni *containerizzate*, è necessario installare sul proprio sistema i software **Docker** e **Docker Compose**.
Di seguito le guide ufficiali per i diversi sitemi operativi: </br>
[Download e installazione Docker](https://docs.docker.com/get-docker/);
[Download e installazione Compose](https://docs.docker.com/compose/install/);

5. Clonare in locale la meta-repository da questo indirizzo: https://gitlab.com/sweleven/blockcovid con il comando ```git clone https://gitlab.com/sweleven/blockcovid``` ;

6. Posizionarsi da terminale dentro la suddetta repository clonata ed installare il pacchetto `meta` (https://www.npmjs.com/package/meta) con il comando ```cd blockcovid && npm i``` ;
   
7. Rimanendo da terminale sempre dentro la stessa repository eseguire il comando `npx meta git update` per scaricare automaticamente tutte le repository del progetto;
   
8. Se tutto è stato fatto correttamente, per eseguire il *backend* sarà sufficiente avviare **Docker** e successivamente digitare il comando `make up` da terminale all'interno della repository precedentemente clonata. Per il completamento del processo è necessario attendere qualche minuto.

   
## Tecnologie utilizzate
- **Nestjs:** framework **Node.js** progressivo per la creazione di applicazioni lato server efficienti, affidabili e scalabili; utilizza il linguaggio **Typescript** ed è stato utilizzato principalmente per sviluppare i divesi servizi messi a disposizione dal *backend*. </br>
  [Documentazione Nestjs](https://docs.nestjs.com/);
  [Documentazione Node.js](https://nodejs.org/it/docs/);
  [Documentazione Typescript](https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes.html);

- **Kubernetes:** sistema usato per l'*orchestrazione* dei continaer del prodotto; automatizza la distribuzione, la scalabilità e la gestione di questi. </br>
  [Documentazione ufficiale](https://kubernetes.io/docs/home/);

- **Keycloak:** *IAM provider* adottato per la gestione degli utenti registrati nel sistema e dei loro ruoli. </br>
  [Documentazione ufficiale](https://www.keycloak.org/documentation);

- **Kong:** *API gateway* performante ed ottimizzato per i *microservizi*, adottato per gestire in modo centralizzato l'autenticazione e l'autorizzazione dei vari utilizzatori dell'applicativo in sinergia con l'*IAM provider* utilizzando il protocollo *OpenID Connect*. </br> 
  [Documentazione ufficiale](https://docs.konghq.com/?_ga=2.93577566.2121013021.1620045998-1484959525.1616409224&_gac=1.93528815.1616409224.CjwKCAjwgOGCBhAlEiwA7FUXkho9rTweO3FbOmCNUyXX7SyL0HWzMge4NZM3ilDQ3Znv9COIPgnjBxoCTmMQAvD_BwE);

- **MongoDB:** *DBMS* non relazionale, orientato a documenti di tipo **json** con schema dinamico. Viene utilizzato per l'archiviazione dei dati, in particolare sfruttando lo strumento di *object modeling* per Node.js, **Mongoose**. </br>
  [Documentazione MongoDB](https://docs.mongodb.com/manual/);
  [Documentazione Mongoose](https://mongoosejs.com/docs/guide.html);

- **Infura:** *nodo* che permette di eseguire transazioni sulla *Blockchain **Ethereum*** utilizzata. </br>
  [Documentazione ufficiale](https://infura.io/docs/ethereum);

- **RabbitMQ:** viene utilizzato come *message broker* per la comunicazione asincrona tra i servizi. </br>
  [Documentazione ufficiale](https://www.rabbitmq.com/documentation.html);




