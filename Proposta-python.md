# Analizzatore di robustezza delle password con verifica su database di leak reali

## Proposta di progetto

### Cosa fa il programma

Il programma analizza la robustezza di una password inserita dall'utente. Controlla la lunghezza, la presenza di lettere maiuscole e minuscole, numeri e caratteri speciali, verifica la presenza di pattern comuni e calcola una stima dell'entropia.  
Come elemento distintivo del progetto, il programma verifica se la password è presente in database di password compromesse utilizzando il servizio Have I Been Pwned (HIBP) tramite il protocollo k-anonymity. La password viene convertita in hash SHA-1 e viene inviato solo il prefisso dell'hash (range query), senza trasmettere la password completa, garantendo così la privacy dell'utente. Il programma confronta poi localmente il suffisso dell'hash con la risposta del servizio per stabilire se la password è stata compromessa.  
Al termine assegna un punteggio complessivo, fornisce un giudizio finale e suggerisce eventuali miglioramenti.

## A chi serve e quale problema reale risolve

Il programma è utile a chi desidera verificare la sicurezza delle proprie password prima di utilizzarle. Oltre a valutarne la robustezza, permette di sapere se una password è già comparsa in violazioni di dati reali, aiutando l'utente a scegliere credenziali più sicure e riducendo il rischio di accessi non autorizzati.

## Competenze del corso utilizzate

* Programmazione orientata agli oggetti (OOP)  
* Ereditarietà e polimorfismo  
* Espressioni regolari (Regex)  
* Hashing (SHA-1)  
* Comunicazione HTTP verso API REST  
* Gestione dei file (File I/O)  
* Interfaccia a riga di comando (CLI)

## Gerarchia di ereditarietà prevista

### Classe base

Regola

### Sottoclassi

* RegolaLunghezza  
* RegolaVarietaCaratteri  
* RegolaPattern  
* RegolaPasswordCompromessa

### Metodo polimorfico

verifica(String password)  
Il ValutatorePassword applicherà tutte le regole in modo polimorfico e calcolerà il punteggio finale.

## Piano di sviluppo

### Fase 1

* Progettazione delle classi.  
* Implementazione delle regole principali.  
* Inserimento della password da CLI.

### Fase 2

* Applicazione delle regole tramite polimorfismo.  
* Calcolo del punteggio e del giudizio finale.  
* Implementazione dell'hashing SHA-1.  
* Connessione HTTP al servizio HIBP tramite range query (k-anonymity).

### Fase 3

* Calcolo della stima dell'entropia.  
* Verifica delle password compromesse confrontando gli hash restituiti dal servizio.  
* Suggerimenti per migliorare la password.  
* Test finali e validazione del programma.

