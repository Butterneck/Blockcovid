---
title: "Configurazione web app"
description: "Web app configuration."
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

## Requisiti di sistema
I requisiti minimi di sistema per poter sviluppare sul *frontend* web sono i medesimi relativi allo sviluppo sul *backend*, descritti nella sezione **4.2**.

## Configurazione ambiente di sviluppo
L'applicazione web rappresenta la *UI* per la gestione delle funzionalità offerte dal server. Per configurare l'ambiente di sviluppo è innanzitutto necessario aver configurato il proprio sistema ed essere in grado id eseguire il *backend*, (si veda anche in questo caso la sezione **4.2**).

In aggiunta a ciò sarà necessario scaricare ed installare il *framework* principale utilizzato per lo sviluppo dell'applicazione:
- **Angular:** chiamato anche "Angular 2+"  è un *framework* open source con licenza *MIT* sviluppato principalmente da *Google*, per lo sviluppo di siti ed applicazioni web.</br>
  [Documentazione e configurazione di Angular](https://angular.io/guide/setup-local).

I passi successivi per completare la configurazione del sistema sono:
1. Clonare in locale la repository `https://gitlab.com/sweleven/web-interface`;
2. Posizionarsi con una linea di comando dentro la suddetta repository ed eseguire il comando `docker build -t web-interface:local -f docker/dockerfile.develop .`;
3. Sempre all'interno della stessa, eseguire il comando `docker run --rm -p 4200:4200 -v $(pwd):/app web-interface:local` per eseguire l'applicazione;
4. Entrando con un *browser* alla pagina `localhost:4200` sarà possibile vedere ed utilizzare in locale l'interfaccia.
