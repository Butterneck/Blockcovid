---
title: "Descrizione web app"
description: "Web app description."
date: 2020-10-06T08:48:57+00:00
lastmod: 2020-10-06T08:48:57+00:00
draft: false
images: []
menu:
  docs:
    parent: "web-app"
weight: 410
toc: true
---


L'applicazione web rappresenta l'*interfaccia utente* per la gestione del server backend e mette a disposizione dell'amministratore (una volta autenticato) le seguenti funzionalità:
- **gestione degli utenti:** è possibile visualizzare e filtrare la lista di tutti gli utenti registrati; vederne ed in alcuni casi modificarne le informazioni principali; rimuovere utenti o aggiungerne di nuovi;
- **gestione di stanze e postazioni:** è possibile monitorare lo stato e l'occupazione delle stanze e delle postazioni al loro interno; disabilitare, riabilitare, rimuovere o aggiungerne di nuove; visualizzarne e modificarne le informazioni principali.


## Design pattern utilizzati
- **Comportamentali:**
  - **Observer:** viene fatto largo uso delle *reactive extensions* per garantire la responsività dell’applicazione anche sotto carico (ad esempio tutte le chiamate http al backend sono implementate utilizzando l’observer pattern) e per l’implementazione di *MVC*;
- **Creazionali:**
  - **Builder:** per l’implementazione dei *form*;
- **Strutturali:**
  - **Decorator:** il *framework* scelto fa largo uso di decorator per aggiungere funzionalità dinamicamente ad un oggetto in modo trasparente e generare documentazione;
- **Architetturali**:
  - **Dependency Injection:** per ridurre l’accoppiamento e il grado di dipendenza tra le classi;
  - **Model View Controller:** per realizzare la *GUI*.