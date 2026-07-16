# Analizzatore di robustezza delle password

## Proposta di progetto

### Cosa fa il programma

Il programma analizza la robustezza di una password inserita dall'utente. Controlla la lunghezza, la presenza di lettere maiuscole e minuscole, numeri e caratteri speciali, individua pattern comuni e stima l'entropia della password.  
Come funzionalità aggiuntiva, verifica se la password è presente in un database di password compromesse utilizzando il servizio Have I Been Pwned (HIBP). Al termine assegna un punteggio, fornisce un giudizio sulla sicurezza della password e suggerisce eventuali miglioramenti.

### A chi serve e quale problema reale risolve

Il programma è utile a chi desidera verificare la sicurezza delle proprie password prima di utilizzarle. Permette di individuare password deboli o già compromesse in violazioni di dati, aiutando l'utente a scegliere credenziali più sicure e a ridurre il rischio di accessi non autorizzati.

### Competenze del corso utilizzate

* Programmazione orientata agli oggetti (OOP)  
* Ereditarietà e polimorfismo  
* Espressioni regolari (Regex)  
* Hashing (SHA-1)  
* Richieste HTTP verso API REST  
* Gestione di file JSON per la configurazione e il salvataggio dei risultati  
* Interfaccia a riga di comando (CLI)

### Gerarchia di ereditarietà prevista

Classe base

* Regola

Sottoclassi

* RegolaLunghezza  
* RegolaVarietaCaratteri  
* RegolaPattern  
* RegolaPasswordCompromessa

Ogni sottoclasse implementa il metodo polimorfico:  
Il ValutatorePassword applicherà tutte le regole senza conoscere il tipo specifico di ciascuna, calcolando il punteggio finale e il giudizio complessivo.

### Piano di sviluppo

#### Fase 1

* Progettazione delle classi.  
* Implementazione delle regole principali.  
* Inserimento della password da terminale.

#### Fase 2

* Calcolo del punteggio e del giudizio finale.  
* Stima dell'entropia.  
* Salvataggio dei risultati in un file JSON.

#### Fase 3

* Verifica della password tramite il servizio Have I Been Pwned.  
* Suggerimenti per migliorare la password.  
* Test finali e documentazione del progetto.

