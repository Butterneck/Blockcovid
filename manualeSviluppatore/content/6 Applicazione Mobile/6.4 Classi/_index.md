---

resources:
  - name: classmobile
    src: "classmobile.png"
    title: Diagramma delle classi relativo all'applicazione mobile

---

Nelle seguenti immagini vengono distinte e descritte la struttura e le relazioni principali delle classi che compongono la parte di utilizzo Igienizzatore (sopra) ed utilizzo Dipendente (sotto), dell'**applicazione mobile**.</br>

{{< img name="classmobile" size="large" lazy=false >}}

- **DialogNfcReadIgienizzatore**: Dialog per avvisare della lettura in corso del tag NFC;
- **DialogDeleteStanza**: Dialog per chiedere conferma prima della scansione NFC;
- **HomeStanzeDaPulire**: Schermata principale contenente le stanze sporche;
- **StanzaCleaner**: Classe che rappresenta le stanze;
- **DialogRisultatoIginizzatore**: Dialog per mostrare il risultato di una igienizzazione;
- **HomeStanzePulite**: Schermata contenente una lista di stanze pulite oggi;
- **ApiServiceCleaner**: Classe per interagire col backend;
- **HomeCleaner**: Classe che gestisce le schermate dell'utente cleaner;
- **Login**: Classe che gestisce il login interfacciandosi col backend;
- **DialogSiNo**: Dialog con pulsanti *Si* e *No*;
- **ApiKeycloak**: Classe per interfacciarsi con il backend;
- **ApiStorage**: Classe per gestire il salvataggio di informazioni dul dispositivo;
- **HomeListaPrenotazioni**: Schermata contenente la lista di prenotazioni attive o comprensive di quelle passate ed eliminate;
- **DialogNfcRead**: Dialog per leggere il tag NFC;
- **Home**: Classe che gestisce le schermate di un utente employee;
- **ApiService**: Classe per interagire col backend;
- **Stanza**: Classe che rappresenta una stanza;
- **DialogNfcPostRead**: Dialog contenente l'esito della scansione del tag NFC;
- **DialogSelezionaOraFine**: Dialog per selezionare l'ora di fine;
- **CreaPrenotazione**: Scehrmata per creare una nuova prenotazione;
- **DialogDeletePrenotazione**: Dialog di conferma per l'eliminazione di una prenotazione;
- **ListViewDialogGenerale**: Dialog con ListView incorporata;
- **Prenotazione**: Classe che rappresenta una prenotazione;
- **Postazione**: Classe che rappresenta una postazione;
- **DialogConfermaPrenotazione**: Dialog contenente la richiesta di conferma per creare una prenotazione;
- **PreviewPrenotazione**: Schermata contenente i dettagli della prenotazione che si sta per effettuare;
- **DialogRisultato**: Dialog contenente una stringa di testo.
