## Requisiti di sistema
I requisiti minimi di sistema per poter sviluppare sul *frontend* web sono i medesimi relativi allo sviluppo sul *backend*, descritti nella sezione **4.2**.

## Linguaggi e strumenti utilizzati
- **Android Studio:** ambiente di sviluppo integrato per lo sviluppo per la piattaforma *Android*, utilizzato specialmente per utilizzare l’emulatore ed eseguire i test in locale, senza dover connettere e cambiare IP ogni volta; </br>
  [Download ed installazione Android Studio](https://developer.android.com/studio?gclid=CjwKCAjwkN6EBhBNEiwADVfya8SvC4b4m9-t22Bz0hnoOQlX6dYIvPFQ2LX7vF8ujLwz2wjw0e_veRoCgFIQAvD_BwE&gclsrc=aw.ds);
- **Flutter:** *framework* open-source creato da *Google* per la creazione di interfacce native per *iOS* e *Android*. Utilizzato per lo sviluppo dell'applicazione mobile tramite linguaggio di programmazione ***Dart***. </br>
  [Download ed installazione Flutter](https://flutter.dev/docs/get-started/install);
  [Documentazione Dart](https://dart.dev/guides);
  [Documentazione Material(UI)](https://flutter.dev/docs/development/ui/widgets/material);

## Configurazione ambiente di sviluppo

1. Installare sul proprio sistema *Flutter*, *Dart*, *Android Studio* (come indicato nel paragrafo soprastante) ed essere in grado di eseguire il backend (sezione **4.2**);
   
2. [Installare](https://flutter.dev/docs/get-started/editor) i plugin per *Flutter* e *Dart* su Android Studio via *UI* (sei si volesse usare Visual Studio Code, in alternativa, è possibile installare i relativi plugin in maniera analoga);
   
3. Creare una [AVD](https://developer.android.com/studio/run/managing-avds) tramite *Android Studio* ed avviarlo (la versione minima richiesta dell'*SDK* è **28**);

4. Eseguire da terminale (in qualsiasi directory) il comando `flutter doctor` per controllare se il tutto è andato a buon fine: tutte le voci presenti dovranno avere delle spunte verdi, eccetto quella denominata "Chrome extension" (relativa allo sviluppo web, non necessaria);

5. Clonare la repository relativa al frontend mobile dal seguente indirizzo: https://gitlab.com/sweleven/android-app;
   
### Per eseguire e testare l'applicativo sarà quindi necessario:

1. Essere connesso alla VPN dentro emulatore (o dispositivo fisico) oppure da PC; 

2. Aprire la repository da *Visual Studio Code* e compilare il file `main.dart` (all'interno della sotto-cartella chiamata **lib**) per creare l'applicazione mobile ed avviarla nell'emulatore o nel dispositivo fisico collegato. In alternativa è possibile eseguire da terminale il comando `flutter run` all'interno della repository appena clonata;

3. Eseguire il *backend* tramite comando `make up` (vedasi sezione **4.2** per ulteriori dettagli);

4. Se tutto è andato a buon fine l'applicazione avvierà la *UI* relativa al Login da parte dell'utente, altrimenti sarà visualizzato un messaggio di errore relativo alle correzioni da apportare. 




