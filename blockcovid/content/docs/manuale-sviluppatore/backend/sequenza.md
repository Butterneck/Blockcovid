---
title: "Diagrammi di sequenza"
description: "Sequence diagrams."
date: 2020-10-06T08:48:57+00:00
lastmod: 2020-10-06T08:48:57+00:00
draft: false
images: []
menu:
  docs:
    parent: "backend"
weight: 700
toc: true
---


Di seguito vengono mostrati i diagrammi di sequenza di alcune tra le funzioni principali riguardanti il backend.

### Salvataggio in Blockchain
Il seguente diagramma descrive il salvataggio in Blockchain degli eventi di prenotazione, check-in, check-out e pulizia; In particolar modo, viene mostrato come sia garantita l'idempotenza del servizio Blockchain Interactor e descrive il processo di salvataggio dei dettagli dell'evento nell'object-storage utilizzato e i riferimenti alla transazione in Blockchain nel database.

<img src="../assets/Blockchain.png" alt="blockchain sequence diagram" caption="<em>diagramma di sequenza blockchain</em>" class="border-0" width="100%">

### Funzionamento identity provider
Il design pattern utilizzato è "**Facade**". Viene descritto il funzionamento del micro-servizio identities che funge da interfaccia semplificata per l'interazione con IAM Provider (Keycloak).

<img src="../assets/Facade.png" alt="Facade sequence diagram" caption="<em></em>" class="border-0" width="100%">

### Chiamate http
Viene descritto come l'API gateway gestisce le chiamate *http* ricevute dai client. In particolar modo viene descritto il processo di autenticazione che utilizza lo standard **OpenID Connect** per comunicare con Keycloak. 
<img src="../assets/IAM.png" alt="IAM sequence diagram" caption="<em></em>" class="border-0" width="100%">


### Transazione
Viene descritto come avviene una transazione multi-collection nella collection di destinazione e nell'outbox-collection.
<img src="../assets/Transaction.png" alt="Transaction sequence diagram" caption="<em></em>" class="border-0" width="100%">

### Pubblicazione domain events
Implementazione dell'outbox pattern e viene descritto il funzionamento del servizio "message-relay" che si occupa di garantire la *at-least-once Delivery* dei domain events, salvati nell'outbox-collection, nel message-broker.
<img src="../assets/Message-relay.png" alt="Message-relay sequence diagram" caption="<em></em>" class="border-0" width="100%">


