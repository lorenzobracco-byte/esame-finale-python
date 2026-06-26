### **Analizzatore di robustezza delle password**

# 

# Proposta di progetto

## Cosa fa il programma

Il programma analizza la robustezza di una password inserita dall'utente. Controlla la lunghezza, la presenza di lettere maiuscole e minuscole, numeri e caratteri speciali, verifica se contiene pattern comuni e se è presente in un dizionario di password compromesse. Al termine assegna un punteggio, stima l'entropia della password e fornisce un giudizio finale con eventuali suggerimenti per renderla più sicura.

## A chi serve e quale problema reale risolve

Il programma è utile a chi vuole verificare la sicurezza delle proprie password prima di utilizzarle. Aiuta a individuare password deboli o facilmente prevedibili, riducendo il rischio di accessi non autorizzati agli account.

## Competenze del corso utilizzate

* Programmazione orientata agli oggetti (OOP)  
* Ereditarietà e polimorfismo  
* Espressioni regolari (Regex)  
* Hashing  
* Gestione dei file (File I/O)  
* Interfaccia a riga di comando (CLI)

## Gerarchia di ereditarietà prevista

Classe base:

* Regola

Sottoclassi:

* RegolaLunghezza  
* RegolaVarietaCaratteri  
* RegolaDizionario  
* RegolaPattern

Metodo polimorfico:

* verifica(String password)

Il ValutatorePassword applicherà tutte le regole in modo polimorfico e calcolerà il punteggio finale.

## Piano di sviluppo

Fase 1

* Progettazione delle classi.  
* Implementazione delle regole principali.  
* Inserimento della password da CLI.

Fase 2

* Applicazione delle regole tramite polimorfismo.  
* Calcolo del punteggio e del giudizio finale.  
* Lettura del dizionario da file.

Fase 3

* Aggiunta della stima dell'entropia.  
* Controllo tramite hashing.  
* Suggerimenti per migliorare la password.  
* Test finali.

