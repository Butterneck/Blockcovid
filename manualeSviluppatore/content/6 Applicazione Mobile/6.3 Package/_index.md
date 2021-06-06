---

resources:
  - name: packagemobile
    src: "packagemobile.png"
    title: Diagramma dei package relativo all'applicazione mobile

---

Nella seguente immagine viene descritta la struttura dei package relativa all'**applicazione mobile**, le dipendenze principali tra di essi e le classi al loro interno.

{{< img name="packagemobile" size="large" lazy=true >}}

- **http**: permette di effettuare connessioni tramite protocollo http;
- **openid_client**: effettua il login tramite protocollo openid;
- **meta**: abilita annotazioni per sviluppatori nel codice;
- **flutter_nfc_reader**: permette l'utilizzo dell'hardware NFC;
- **flutter_secure_storage**: salva i dati in locale;
- **intl**: permette di effettuare conversioni di tipo.
