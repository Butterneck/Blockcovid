---

resources:
  - name: Infra
    src: "Infra.png"
    title: "Schema dell'architettura generale del prodotto"
---
Il sistema ***BlockCOVID*** riguarda il *tracciamento* dell’utilizzo e dell’igienizzazione di postazioni di lavoro, da parte di utenti registrati, all’interno di relative stanze, nel contesto di un laboratorio informatico.</br>

## Componenti
Il prodotto si compone principalmente di:
- un ***backend*** su *server* dedicato, per la gestione operativa delle funzionalità;
- un'***applicazione web*** per permettere all'amministratore di interfacciarsi con il server;
- un'***applicazione mobile*** che permette agli utenti di usufruire dei servizi offerti.

## Architettura di base
Per realizzare un’architettura funzionale allo scopo del prodotto si è scelto di seguire un modello di architettura a *microservizi* che utilizza l’*API gateway* (come conseguenza dell’uso di questi). </br>
Tramite ciò è possibile gestire in modo centralizzato l’autenticazione e l’autorizzazione dei vari utilizzatori e si nasconde all’utente finale l’architettura dell’applicazione aggiungendo un ulteriore livello di astrazione.</br>

{{< img name="Infra" size="medium" lazy=false >}}