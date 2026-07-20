Devlog
Settimana 1 — 29/06/2026
Durante questa settimana abbiamo definito la struttura del progetto e iniziato lo sviluppo del valutatore di password. Abbiamo deciso di organizzare il codice in più classi invece di inserire tutti i controlli nello stesso file. Abbiamo creato la classe astratta Regola, dalla quale derivano le varie verifiche (lunghezza, varietà dei caratteri e pattern comuni). La parte che ci ha richiesto più tempo è stata capire come rendere il codice facilmente estendibile senza dover modificare continuamente il valutatore principale. Ci siamo divisi il lavoro tra progettazione delle classi e implementazione delle prime regole.

Settimana 2 — 06/07/2026
Abbiamo completato il sistema di valutazione aggiungendo il calcolo dell'entropia della password e il punteggio finale. Successivamente abbiamo iniziato a integrare il controllo delle password compromesse utilizzando l'API di Have I Been Pwned. Abbiamo studiato il funzionamento del protocollo K-Anonymity e deciso di utilizzare l'hash SHA-1 per non inviare mai la password in chiaro. Durante i test abbiamo corretto alcuni errori nel calcolo dei punteggi e nella gestione dei messaggi restituiti all'utente.

Settimana 3 — 13/07/2026 - 18/07/2026
Negli ultimi giorni abbiamo rifinito il progetto e verificato che tutti i moduli funzionassero insieme. Abbiamo eseguito diversi test con password differenti per controllare il comportamento delle varie regole e correggere gli ultimi bug. Infine abbiamo sistemato il codice, migliorato l'organizzazione dei file e preparato il progetto per la consegna.

Bilancio finale
Il progetto ci ha permesso di applicare i principi della programmazione orientata agli oggetti realizzando un'applicazione modulare e facilmente estendibile. La parte più interessante è stata l'integrazione con Have I Been Pwned, perché abbiamo imparato come verificare se una password è stata compromessa senza compromettere la privacy dell'utente grazie al protocollo K-Anonymity. Siamo soddisfatti della struttura raggiunta e, con più tempo, avremmo aggiunto altre regole di controllo, una semplice interfaccia grafica e una suite di test automatizzati più completa.
