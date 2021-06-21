---
title: "Estendibilità web app"
description: "Extensibility."
date: 2020-10-06T08:48:57+00:00
lastmod: 2020-10-06T08:48:57+00:00
draft: false
images: []
menu:
  docs:
    parent: "web-app"
weight: 700
toc: true
---

In questa pagina sono indicate tutte le possibili modifiche effettuabili secondo alcuni criteri che crediamo necessari evidenziare (per esempio la sostituzione di Keycloak con un altro Identity and Access Management provider) oppure punti non sviluppati dal prodotto software rilasciato e che si ritengono utili da implementare per rendere ancora più robusto il sistema.

## Sostituire Keycloak
Il backend attualmente utilizza Keycloak come IAM provider, ma è possibile sostituirlo con un qualsiasi altro sistema di autenticazione che rispetti lo standard [OpenID Connect](https://openid.net/connect/).

L'architettura del sistema rende semplice la sostituzione. È infatti sufficiente modificare il microservizio `Identities` in modo che non interagisca più con keycloak ma con il nuovo provider scelto. In particolare sarà necessario:

- creare una nuova classe (`src/http/<providerName>.http.interceptor.ts`) che implementi l'interfaccia `HttpInterceptor` che si occupa di autenticare le chiamate alle API esposte dal provider;
- creare una nuova classe (`src/users/services/<providerName>.users.service.ts`) che implementi l'interfaccia `UserService`;
- creare una nuova classe (`src/profile/services/<providerName>.profile.service.ts`) che implementi l'interfaccia `ProfileService`;
- aggiornare gli `imports` in `src/users/users.module.ts` e in `src/profile/profile.module.ts` facendo riferimento alle nuove classi create.

## Sostituire network Ethereum
Per il tracciamento immutabile delle pulizie e delle presenze viene utilizzata la test network Ethereum Rinkeby, ma è possibile utilizzare una qualsiasi altra network ethereum. Per cambiare la network è sufficiente:

- aggiungere la configurazione delle nuova network all'oggetto `module.exports.networks` nel file `truffle-config.js` nel progetto truffle che contiene gli smart contracts;
- fare il deploy degli smart contracts nella nuova network con il comando `truffle deploy --network <network_name>`;
- impostare le variabili d'ambiente `INFURA_URL=https://<network_name>.infura.io/v3` e `ETHERSCAN_URL=https://<network_name>.etherscan.io/tx` nel microservizio `blockchain-interactor`.

## Sostituire Minio
Per questioni di privacy in blockchain viene salvata esclusivamente una prova crittografica delle presenze e delle pulizie. I riferimenti (contententi dati sensibili) vengono salvati sotto forma di file `.json` in un Object Storage System. Attualmente il prodotto utilizzato è `Minio`, che per sua natura è compatibile con `S3`, per cui nel caso in cui si volesse utilizzare un qualsiasi altro prodotto compatibile con `S3` non sarebbe necessaria nessuna modifica. Nel caso in cui, invece, si volesse utilizzare un altro prodotto per lo storage dei file, sarebbe sufficiente modificare il servizio `blockchain-interactor`:

- creare una nuova classe (`src/ObjectStorageClient/<productName>.client.ts`) che implementi l'interfaccia `ObjectStorageClient`;
- aggiornare gli `imports` in `src/app.module.ts` facendo riferimento alla nuova classe creata.

## Sostituire RabbitMQ
Il backend attualmente utilizza `RabbitMQ` come Message Broker, ma è possibile sostituirlo con un qualiasi altro message broker che implementa lo standard `MQTT`. È sufficiente, ogni servizio che fa uso del message broker:

- cambiare le variabili d'ambiente `MESSAGE_BROKER_USER`, `MESSAGE_BROKER_PASSWORD`, `MESSAGE_BROKER_HOST`, `MESSAGE_BROKER_PORT`,`MESSAGE_BROKER_QUEUE_NAME`

