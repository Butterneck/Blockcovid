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
{{< img name="Blockchain" size="large" lazy=true >}}

### Funzionamento identity provider
{{< img name="Facade" size="small" lazy=false >}}

### Chiamate http
{{< img name="IAM" size="large" lazy=true >}}

### Transazione
{{< img name="Transaction" size="small" lazy=true >}}

### Pubblicazione domain events
{{< img name="Message-relay" size="small" lazy=true >}}


