# Scelte 

## Perché l'ereditarietà (e non composizione/funzioni)

Il nucleo del sistema si basa sulla classe astratta Regola estesa da RegolaLunghezza, RegolaVarieta, RegolaPattern e RegolaPasswordCompromessa. La relazione is-a è reale: ogni sottoclasse è una regola di validazione.

* Perché non una classe unica con if/match? Avrebbe violato l'Open/Closed Principle (OCP). Aggiungere un nuovo controllo avrebbe significato modificare il codice esistente, aumentando la complessità e il rischio di regressioni.  
* Perché non la composizione? Le regole non sono composte da altri pezzi logici, ma condividono la stessa natura e lo stesso contratto. La composizione è usata correttamente un livello sopra: il Valutatore compone una lista di regole.  
* Uso concreto del polimorfismo: Nel ciclo principale di Valutatore (valutatore.py). Il valutatore scorre la lista ed esegue regola.valuta(password) senza sapere (né curarsi di) quale logica specifica ci sia dietro.

## Altre scelte non ovvie

* Oggetto Risultato vs Primitivi: Il metodo valuta() non restituisce un semplice bool o una tupla, ma un oggetto Risultato dedicato. Questo permette di incapsulare in modo pulito il punteggio, lo stato e il messaggio di feedback specifico per l'utente.  
* Resilienza della rete (hibp\_client.py): Le chiamate all'API di Have I Been Pwned sono isolate nel client. In caso di timeout o assenza di rete, l'eccezione viene gestita internamente restituendo un esito "Non verificabile", evitando il crash dell'intera applicazione.  
* Compromesso sincrono: Per ragioni di tempo, le chiamate HTTP sono sincrone. L'aver isolato il client permette comunque un futuro passaggio ad asyncio senza impattare il resto dell'architettura.

## Alternative scartate

* Logica HTTP dentro la Regola: Inizialmente la richiesta API era integrata direttamente in RegolaPasswordCompromessa. È stata abbandonata perché violava la separazione delle responsabilità e rendeva impossibile effettuare gli unit test senza colpire realmente i server esterni.  
* Dizionari di password locali massivi: Scartata l'idea di caricare in memoria file .txt con milioni di password comuni. Avrebbe appesantito l'applicazione, duplicando un controllo che l'API HIBP esegue già in modo più efficiente e aggiornato.

