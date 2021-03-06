---
title: "Descrizione backend"
description: "Backend description."
date: 2020-10-06T08:48:57+00:00
lastmod: 2020-10-06T08:48:57+00:00
draft: false
images: []
menu:
  docs:
    parent: "backend"
weight: 310
toc: true
---


La struttura del *backend* segue un'architettura a ***microservizi***, decomposti per *sotto-domini*. </br>
Ogni servizio è quindi considerato come un modulo indipendente dedicato ad un relativo compito; viene utilizzato il pattern *database-per-service* per cui ogni servizio ha il proprio database con cui e' in grado di comunicare (ogni servizio puo' comunicare direttamente esclusivamente con il proprio database). I *microservizi*, gestiti in un *cluster Kubernetes*, sono in grado di comunicare tra di loro in modo sincrono tramite REST API e in modo asincrono attraverso lo scambio di messaggi utilizzando un *message broker* che implementa il pattern *publish-subscribe*. </br>


I dati generati dal sistema vengono salvati utilizzando database di tipo non-relazionale e poiché vi è necessità che una copia di alcuni di essi venga memorizzata in maniera certificata ed immutabile, viene fatto uso della *Blockchain Ethereum*.

## Design pattern utilizzati
- **Comportamentali:**
  - **Outbox:** per garantire la *at least once delivery* di *domain events* nel *message broker*. Il seguente design pattern è stato utilizzato per lo sviluppo delle seguenti parti dell'applicazione: TODO;
  - **Observer:** viene fatto largo uso delle *reactive extensions* per garantire la responsività dell’applicazione anche sotto carico. Il seguente design pattern è stato utilizzato per lo sviluppo delle seguenti parti dell'applicazione: TODO.

- **Creazionali:**
  - **Factory method:** viene utilizzato per fare il *bootstrap* dei vari microservizi, in particolare per permettere la loro configurazione in maniera dinamica. Il seguente design pattern è stato utilizzato per lo sviluppo delle seguenti parti dell'applicazione: TODO.
  
- **Strutturali:**
  - **Decorator:** il *framework* scelto fa largo uso del decorator pattern, per aggiungere funzionalità dinamicamente ad un oggetto in modo trasparente e generare in automatica documentazione e interfacce di supporto sia per lo sviluppatore che per il manutentore. Il seguente design pattern è stato utilizzato per lo sviluppo delle seguenti parti dell'applicazione: TODO;
  - **Façade:** per semplificare l’interazione con l’*IAM provider* utilizzato (*Keycloak*) è stato implementato un microservizio che implementa tale pattern. Il seguente design pattern è stato utilizzato per lo sviluppo delle seguenti parti dell'applicazione: TODO;
  - **Proxy:** viene utilizzato per fare in modo di interagire con il database, il message broker e gli altri microservizi come se fossero locali. Il seguente design pattern è stato utilizzato per lo sviluppo delle seguenti parti dell'applicazione: TODO.

- **Architetturali:**
  - **Sidecar:** la logica per la pubblicazione di domain events sul message broker è stata isolata in un servizio a sè che viene affiancato ad ogni database;
  - **Dependency Injection:** design pattern utilizzato per ridurre l’accoppiamento e il grado di dipendenza tra le classi.