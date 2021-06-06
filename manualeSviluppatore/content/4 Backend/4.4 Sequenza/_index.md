---

resources:

  - name: Blockchain
    src: "Blockchain.png"
    title: Diagramma di sequenza relativo al salvataggio delle informazioni in Blockchain

  - name: Facade
    src: "Facade.png"
    title: Diagramma di sequenza relativo al funzionamento dell'identity provider (facade pattern)

  - name: IAM
    src: "IAM.png"
    title: Diagramma di sequenza relativo al funzionamento delle chiamate http da parte dell’API gateway

  - name: Transaction
    src: "Transaction.png"
    title: Diagramma di sequenza che descrive una transazione multicollection (outbox pattern)

  - name: Message-relay
    src: "Message-relay.png"
    title: Diagramma di sequenza relativo alla pubblicazione di domain events sul message broker

---
Di seguito vengono mostrati i diagrammi di sequenza di alcune tra le funzioni principali riguardanti il backend.

### Salvataggio in Blockchain
Il seguente diagramma descrive il salvataggio in Blockchain degli eventi di prenotazione, check-in, check-out e pulizia; In particolar modo, viene mostrato come sia garantita l'idempotenza del servizio Blockchain Interactor e descrive il processo di salvataggio dei dettagli dell'evento nell'object-storage utilizzato e i riferimenti alla transazione in Blockchain nel database.

{{< img name="Blockchain" size="large" lazy=true >}}

### Funzionamento identity provider
Il design pattern utilizzato è "**Facade**". Viene descritto il funzionamento del micro-servizio identities che funge da interfaccia semplificata per l'interazione con IAM Provider (Keycloak).
{{< img name="Facade" size="small" lazy=false >}}

### Chiamate http
Viene descritto come l'API gateway gestisce le chiamate *http* ricevute dai client. In particolar modo viene descritto il processo di autenticazione che utilizza lo standard **OpenID Connect** per comunicare con Keycloak. 
{{< img name="IAM" size="large" lazy=true >}}

### Transazione
Viene descritto come avviene una transazione multi-collection nella collection di destinazione e nell'outbox-collection.
{{< img name="Transaction" size="small" lazy=true >}}

### Pubblicazione domain events
Implementazione dell'outbox pattern e viene descritto il funzionamento del servizio "message-relay" che si occupa di garantire la *at-least-once Delivery* dei domain events, salvati nell'outbox-collection, nel message-broker.
{{< img name="Message-relay" size="small" lazy=true >}}


