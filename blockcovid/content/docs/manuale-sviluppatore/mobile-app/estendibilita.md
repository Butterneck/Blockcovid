---
title: "Estendibilità mobile app"
description: "Extensibility."
date: 2020-10-06T08:48:57+00:00
lastmod: 2020-10-06T08:48:57+00:00
draft: false
images: []
menu:
  docs:
    parent: "mobile-app"
weight: 570
toc: true
---

# Aggiungere un nuovo sottosistema

Per aggiungere un nuovo sottosistema specifico per un determinato ruolo è necessario controllare/modificare l'algoritmo di selezione aggiungendolo tra le scelte possibili. Per fare ciò è sufficiente modificare la classe **Login**, la quale avvierà il relativo sottosistema a seconda dei permessi e del tipo di utenza che effettuerà il login.

# Aggiungere una nuova funzionalità ai sottosistemi presenti

- per impaginare un dato con il suo valore testuale servirsi della classe **CardDoppia**;
- in caso di una ListView creata in modo dinamico, servirsi del widget **ListaVuotaRicarica** in caso di lista vuota;
- per servirsi della tecnologia GPS per tracciare gli utenti dentro ad un recinto geografico, servirsi della classe **GpsManager**;
- per servirsi delle funzionalità di invio di notifiche da parte dell'applicazione mobile, uilizzare i metodi nella classe **NotificheManager**.

## Sottosistema Employee

- nel caso di funzionalità che utilizzino l'NFC è consigliabile utilizzare le classi **DialogNFCRead** e **DialogNFCPostRead**;
- se si vuole aggiungere nuovi campi dati relativi alla form di prenotazione, è possibilie utilizzare la classe **CreaPrenotazione** o modificarla direttamente;
- per mostrare dei dialog di conferme, errori o richieste utilizzare le classi **DialogRisultato**, **DialogErrore** e **DialogSiNo**;
- in caso di utilizzo di una ListView per mostrare prenotazioni, servirsi della calsse **CardPrenotazioni** per una correta impaginazione;
- per aggiungere una nuova funzionalità che consista nel visualizzare dati è sufficiente aggiungere la pagina desiderata nel campo dati `body` della classe **HomeEmployee**.

## Sottosistema Cleaner

- per aggiungere nuove funzionalità che consistano nel visualizzare dati, aggiungere i relativi widget desiderati nel campo dati `body` della classe **HomeCleaner**, e aggiungere una nuova Tab nel campo `tabs` della TabBar;
- nel caso di funzionalità che utilizzino l'NFC utilizzare le relative classi **DialogNFCRead** e **DialogNFCPostRead**.