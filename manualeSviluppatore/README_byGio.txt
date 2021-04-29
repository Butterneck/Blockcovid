ALCUNE ISTRUZIONI BASE BASE PER TUTTI, PER POTER INIZIARE FACILMENTE A SPIPPOLARE SUI MANUALI
per ulteriori necessità rifarsi alla documentazione (che vi ho linkato a seguire)...o al buon vecchio google

1. Innanzitutto installare Hugo (allo stesso indirizzo ci sono anche info ed istruzioni per usarlo):

    https://gohugo.io/getting-started/installing/


2. Se non già fatto eseguire anche (da terminale):

    npm install

    npm install gulp (se non già fatto precedentemente)

    npx gulp default


3. Per avviare il server locale posizionarsi da terminale nella cartella "manualeSviluppatore" e digitare:

    hugo server -D


4. Se tutto è andato liscio entrare da browser su "localhost:1313/blockcovid" (vedrete l'indirizzo anche nella penultima riga che vi è uscita sul terminale) per visualizzare il documento in locale

5. Per scrivere si usa Markdown (se non lo conoscete, tranqui è molto easy): https://www.markdownguide.org/basic-syntax
la struttura ed il contenuto del doc è tutto nella cartella "content"

6. Qui documentazione generale con le funzionalità principali per usare il template Geekdoc che abbiamo usato: 
https://geekdocs.de/usage/getting-started/

7. Per modificare elementi dell'aspetto grafico basta aggiungere regole css sul file "custom.css" dentro la cartella static 
(per identificare l'elemento da modificare potete usare "analizza elemento" sul doc aperto nel browser)

8. Se dovesse servirvi, qui c'è un utility per generare velocemente tabelle in markdown senza sbattersi a scriverle a mano:
https://www.tablesgenerator.com/markdown_tables


Ps. Se non vedete subito le modifiche o a seguito di queste vedete strani pasticci sul documento, non spaventatevi: chiudete il server locale e riavviatelo (refreshando poi il browser) e dovrebbe tornare tutto a posto


