## Requisiti di sistema
I requisiti di sitema sono gli stessi per 4.2 in più a seconda del ambiente di sviluppo potrebbero incorrere rallentamenti e lag.
<br>
    **minimi:** 8GB RAM, dual-core CPU.
<br>
    **consigliati:** 16GB RAM, quad-core(o più) CPU.
## Configurazione ambiente di sviluppo

1. Avere installato Flutter(e Dart), Android Studio ed il Backend(4.2).<br>
   
2. Installare i plugin per Android Studio(Flutter e Dart) via UI.
   
3. Creare un AVD in Android studio ed avviarlo(con versione SDK minimo attuale pari a 28) sempre via UI.
   
4. Se si usa Visual Studio Code installare i plugin Dart e Flutter che si trovano nel relativo store sempre via UI.

5. Eseguire da terminale(in qualsiasi directory) il comando `flutter doctor` per controllare se il tutto è andato a buon fine avremmo tutte le spunte verdi eccetto quella denominata Chrome extension(relativa allo sviluppo web) non necessaria.

6. Clonare la repo relativa allo sviluppo mobile: https://gitlab.com/sweleven/android-app

7. Essere connesso alla VPN dentro emulatore(o dispositivo) e da PC. 

8. Aprirlo dentro Visual Studio Code e se selezioniamo il file main.dart dentro alla subdirectory chiamata **lib** tramite la UI di VSC in alto a destra troviamo il bottone verde per poter compilare e creare l'app ed avviarla, nel emulatore o nel dispositivo fisico collegato.In alternativa eseguire il comando `flutter run` nella directory della repo appena creata.

9. Aprire la directory del backend in una nuova finestra di VSC ed eseguire il comando `make up` in modo da avere il backend attivo

10. Se tutto è andato a buon fine l'applicazione caricherà la UI relativa al Login da parte del utente, altrimenti si vedra nella UI un messaggio di errore relativo a cosa vada sistemato. 

## Linguaggi e strumenti utilizzati
- **Android Studio:** ambiente di sviluppo integrato per lo sviluppo per la piattaforma *Android*, utilizzato specialmente per utilizzare l’emulatore ed eseguire i test in locale, senza dover connettere e cambiare IP ogni volta; </br>
  [Dowload ed installazone Android Studio](https://developer.android.com/studio?gclid=CjwKCAjwkN6EBhBNEiwADVfya8SvC4b4m9-t22Bz0hnoOQlX6dYIvPFQ2LX7vF8ujLwz2wjw0e_veRoCgFIQAvD_BwE&gclsrc=aw.ds);
- **Flutter:** *framework* open-source creato da *Google* per la creazione di interfacce native per *iOS* e *Android*. Utilizzato per lo sviluppo dell'applicazione mobile tramite linguaggio di programmazione ***Dart***. </br>
  [Dowload ed installazone Flutter](https://flutter.dev/docs/get-started/install);
  [Documentazione Dart](https://dart.dev/guides);
  [Documentazione Material(UI)](https://flutter.dev/docs/development/ui/widgets/material);


