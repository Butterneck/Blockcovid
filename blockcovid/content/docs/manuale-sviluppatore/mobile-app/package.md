---
title: "Package web app"
description: "Web app package diagrams."
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

Nella seguente immagine viene descritta la struttura dei package relativa all'**applicazione mobile**, le dipendenze principali tra di essi e le classi al loro interno.

<img src="../assets/packagemobile.png" alt="mobile-app package diagram" caption="<em></em>" class="border-0" width="100%">

- **http**: permette di effettuare connessioni tramite protocollo http;
- **openid_client**: effettua il login tramite protocollo openid;
- **meta**: abilita annotazioni per sviluppatori nel codice;
- **flutter_nfc_reader**: permette l'utilizzo dell'hardware NFC;
- **flutter_secure_storage**: salva i dati in locale;
- **intl**: permette di effettuare conversioni di tipo.
- **@Flutter**: package esterni forniti dal linguaggio di programmazione e dalla repository [pub.dev](https://pub.dev/);
- **dialogs**: package contenente tutti i dialog personalizzati creati;
- **cards**: package contenente tutte le card personalizzate create;
- **pages**: package contenente tutte le pagine dell'applicazione mobile;
- **Api**: package contenente tutte le Api utilizzate;
- **model**: package contenente i modelli usati nell'applicazione mobile.
