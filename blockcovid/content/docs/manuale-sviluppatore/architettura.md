---
title: "Architettura"
description: "Architecture."
date: 2020-10-06T08:48:57+00:00
lastmod: 2020-10-06T08:48:57+00:00
draft: false
images: []
menu:
  docs:
    parent: "manuale-sviluppatore"
weight: 210
toc: true
---
Il prodotto si compone principalmente di:
- un ***backend*** su *server* dedicato, per la gestione operativa delle funzionalità;
- un'***applicazione web*** per permettere all'amministratore di interfacciarsi con il server;
- un'***applicazione mobile*** che permette agli utenti di usufruire dei servizi offerti.

Il prodotto e' stato sviluppato utilizzando un'architettura a microservizi.

Per realizzare un’architettura funzionale allo scopo del prodotto si è scelto di seguire un modello di architettura a *microservizi* che utilizza l’*API gateway* (come conseguenza dell’uso di questi). </br>
Tramite ciò è possibile gestire in modo centralizzato l’autenticazione e l’autorizzazione dei vari utilizzatori e si nasconde all’utente finale l’architettura dell’applicazione aggiungendo un ulteriore livello di astrazione.</br>

<img src="../assets/Infra.png" alt="Infra" caption="<em>Architettura</em>" class="border-0" width="100%">
