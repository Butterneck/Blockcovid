---

resources:

  - name: diagramma_sequenza1
    src: "diagramma_sequenza1.png"
    title: Diagramma di sequenza relativo alla scannerizzazione di una postazione libera e conseguente prenotazione istantanea

  - name: diagramma_sequenza2
    src: "diagramma_sequenza2.png"
    title: Diagramma di sequenza relativo alla creazione di una nuova prenotazione

  - name: diagramma_sequenza3
    src: "diagramma_sequenza3.png"
    title: Diagramma di sequenza relativo all'igienizzazione di una stanza

  - name: diagramma_sequenza4
    src: "diagramma_sequenza4.png"
    title: Diagramma di sequenza relativo alla conclusione dell'utilizzo di una postazione e pulizia della stessa

---
Di seguito vengono mostrati i diagrammi di sequenza che modellano alcune tra le operazioni principali legate all'applicazione mobile.

### Scannerizzazione ed utilizzo

{{< img name="diagramma_sequenza1" size="large" lazy=true >}}
Il diagramma mostra la sequenza di interazioni tra le classi quando viene eseguita una scannerizzazione di una postazione per indicare la volontà di iniziare ad usarla.

- l'evento scatenante è il tap da parte dell'utente sul pulsante di scansione NFC, questo porta al push da parte della classe *Home* del dialog *DialogNfcRead*;
- *DialogNfcRead* invoca la funzione `readNfc()` restando in ascolto del tag. Quando Il tag viene rilevato, `readNfc()` ne cattura il contenuto e lo ritorna ad *Home*;
- *Home* si serve del metodo `getPostazioneFromTag(String t)` fornito da *ApiService* per ottenere i dati dal backend della postazione appena scannerizzata;
- viene mostrata a video la schermata *DialogNfcPostRead* tramite il metodo `push()`;
- quando l'utente tappa sul pulsante di conferma, *DialogNfcPostRead* mostra a video *PreviewPrenotazione* tramite il metodo `push()`;
- quando l'utente tappa sulla data mostrata a video, viene invocato il metodo `selectDurata()`;
- una volta selezionata la durata da parte dell'utente, viene invocato il metodo `prenota(Prenotazione p)` fornito dalla classe *ApiService*;
- il valore di ritorno viene catturato e tutti i dialog pushati precedentemente cessano di esistere, rilasciando il controllo a *Home*.

### Prenotazione

{{< img name="diagramma_sequenza2" size="large" lazy=true >}}
Il diagramma mostra la sequenza di interazioni tra le classi quando viene eseguita una prenotazione dalla shchermata di creazione di una prenotazione.

- l'evento scatenante è il tap da parte dell'utente sul tab mostrante la pagina *HomeCreaPrenotazione*;
- *HomeCreaPrenotazione* interagisce con *ApiServiceEmployee* tramite il metodo `getFreeRooms()`, ottenendo come risposta una `List<Rooms>`;
- l'utente inserisce i dati nei campi della form;
- l'utente preme sul pulsante prenota, invocando il metodo `validateDati()`;
- superata la validazione dei dati immessi, grazie al metodo `push()` viene mostrata a video la schermata rappresentata dalla classe *PreviewPrenotazione*;
- cliccando il pulsante prenota mostrato a video, viene invocato il metodo `createreservation(Prenotazione p)` fornito dalla classe *ApiServiceEmployee*;
- viene ritornato la risposta a *PreviewRisultato*, che grazie al metodo `build(String ris)` della classe *DialogRisultato* mostra a video la conferma dell'avvenuta prenotazione.

### Igienizzazione

{{< img name="diagramma_sequenza3" size="large" lazy=true >}}
Il diagramma mostra la sequenza di interazioni tra le classi quando viene eseguita una igienizzazione delle stanze.

- l'evento scatenante è il login da parte di un utente *igienizzatore*;
- la classe *HomeStanzeDaPulire* interagisce con *ApiCleaner* tramite il metodo `getStanzeSporche()` per ottenere una `List<Stanza>` contenente le stanze da igienizzare;
- la classe *HomeStanzeDaPulire* mostra a video le stanze sporche e cattura il tap dell'utente;
- grazie al metodo `push(Stanza s)` viene mostrata a video la schermata *DialogDeleteStanza*, che cattura l'imput utente e viene chiusa;
- l'input utente viene ritornato a *HomeStanzeDaPulire*, che grazie al metodo `push(Stanza s)` mostra a video il dialog *LetturaNfcStanza*;
- il dialog sopracitato resta in ascolto di una scansione di un tag NFC, tramite il metodo `readNfc()`;
- quando il tag NFC viene scansionato il dialog ritorna il valore letto a *HomeStanzeDaPulire*, che interagisce con *ApiCleaner* grazie al metodo `pulisciStanza(Stanza s)`;
- una volta ricetuo il valore di ritorno, *HomeStanzeDaPulire* mostra la scehrmata rappresentata da *DialogRisultato*;
- una volta premuto il pulsante *exit* mostrato a video, la schermata *DialogRisultato* è chiusa.

### Terminazione e igienizzazione

{{< img name="diagramma_sequenza4" size="large" lazy=true >}}
Il diagramma mostra la sequenza di interazioni tra le classi quando viene eseguito un check-out della postazione con pulizia della stessa.

- l'evento scatenante è il tap da parte dell'utente sul pulsante di scansione NFC mostrato a video;
- la classe *Home*, catturato l'evento scatenante, presenta il dialog *DialogNfcRead*, grazie al metodo `push()`;
- il dialog sopracitato rimane in attesa di una scansione di un tag NFC, servendosi del metodo `readNfc()`;
- una volta scansionato il tag, il valore letto viene ritornato a *Home*;
- viene invocato il metodo `getPostazioneFromTag(Tag t)` della classe *ApiService*;
- il metodo ritorna la postazione in oggetto;
- *Home* mostra a video il dialog *DialogNfcPostRead*, che cattura il tap dell'utente sul pulsante di conferma;
- il dialog quindi si serve del metodo `fineUso(Postazione p, Bool pulizia)` con campo pulizia=true, fornito da *ApiService*;
- il dialog cattura la risposta e la ritorna a *Home*.