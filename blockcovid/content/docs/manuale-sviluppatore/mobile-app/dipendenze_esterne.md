---
title: "Dipendenze esterne mobile app"
description: "Mobile app external dependencies."
date: 2020-10-06T08:48:57+00:00
lastmod: 2020-10-06T08:48:57+00:00
draft: false
images: []
menu:
  docs:
    parent: "mobile-app"
weight: 700
toc: true
---

Il servizio API **KeyCloak** viene utilizzato per l'autenticazione tramite web.<br>

## Package esterni utilizzati:

- **flutter_nfc_reader:** permette la lettura dei tag *RFID* tramite *NFC* (<https://pub.dev/packages/flutter_nfc_reader/install>);
- **cupertino_icons:** aggiunge delle icone utilizzate nell'applicazione (<https://pub.dev/packages/cupertino_icons>);
- **flutter_secure_storage:** permette la criptazione dei dati dell'utente (<https://pub.dev/packages/flutter_secure_storage>);
- **http:** per la comunicazione con il backend (<https://pub.dev/packages/http>); 
- **intl:** per la gestione del formato date (<https://pub.dev/packages/intl>);
- **openid_client:** utilizzato nella gestione dei token di autorizzazione lato client (<https://pub.dev/packages/openid_client>);
- **url_launcher:** per eseguire la Webview del servizio ApiKeyCLoack (<https://pub.dev/packages/url_launcher>).

  