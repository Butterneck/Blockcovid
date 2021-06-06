---

resources:
  - name: packagemobile
    src: "packagemobile.png"
    title: Diagramma dei package relativo all'applicazione mobile

---

Nella seguente immagine viene descritta la struttura dei package relativa all'**applicazione mobile**, le dipendenze principali tra di essi e le classi al loro interno.

{{< img name="packagemobile" size="large" lazy=true >}}

- **@Flutter**: package esterni forniti dal linguaggio di programmazione e dalla repository [pub.dev](https://pub.dev/);
- **dialogs**: package contenente tutti i dialog personalizzati creati;
- **cards**: package contenente tutte le card personalizzate create;
- **pages**: package contenente tutte le pagine dell'applicazione mobile;
- **Api**: package contenente tutte le Api utilizzate;
- **model**: package contenente i modelli usati nell'applicazione mobile.
