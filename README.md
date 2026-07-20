# Password Evaluator & Analyzer Engine

Sistema modulare ed estensibile in Python per l'analisi avanzata, la validazione e il calcolo della robustezza delle password. Il sistema combina regole metriche locali (lunghezza, varietà di caratteri, pattern ripetitivi), analisi dell'entropia di Shannon ed estensioni cloud-native tramite l'API di *Have I Been Pwned* (HIBP) con protocollo di K-Anonimato.

---

## Istruzioni per l'Avvio (Clone Pulito)

Segui questi passaggi per configurare ed eseguire il progetto da zero:

### 1. Prerequisiti
Assicurati di avere installato **Python 3.10** o superiore e il gestore di pacchetti `pip`.

### 2. Clonare il Repository ed entrare nella cartella
```bash
git clone <https://github.com/lorenzobracco-byte/esame-finale-python> password-evaluator
cd password-evaluator
```

### 3. Installazione delle Dipendenze
Il progetto utilizza la libreria standard di Python per quasi tutte le funzionalità, ad eccezione del client HIBP che richiede il modulo `requests` per le chiamate HTTP. Installa le dipendenze tramite il file `requirements.txt` (oppure direttamente):
```bash
pip install -r requirements.txt
# Alternativamente: pip install requests
```

### 4. Esecuzione del Programma
Per avviare l'interfaccia a riga di comando (CLI) principale e testare il valutatore in modalità interattiva:
```bash
python main.py
```

### 5. Esecuzione dei Test Unitari
Per verificare che tutti i criteri di validazione funzionino correttamente e che i test siano verdi:
```bash
python -m unittest discover -s . -p "test_*.py"
```

---

## Manuale Utente & Funzionalità

Il programma opera come un motore di validazione a politiche configurabili. Quando inserisci una password, il sistema esegue tre macro-attività:

1. **Validazione Regole (Approccio Polimorfico):** Verifica se la password rispetta i vincoli strutturali impostati (Lunghezza minima, Varietà di set di caratteri, assenza di Pattern banali come "123456" o "aaaa").
2. **Analisi Quantitativa (Entropia):** Calcola l'entropia di Shannon ($H = -\sum p_i \log_2 p_i$) e l'entropia di brute-force ($E = L \cdot \log_2(R)$) per misurare la complessità teorica dell'informazione.
3. **Controllo Compromissione Cloud (Estensione Avanzata):** Interroga in modo sicuro i server di *Have I Been Pwned*. La password viene convertita in hash SHA-1; al server vengono inviati solo i primi 5 caratteri dell'hash. Il client locale verifica se il suffisso rimanente è presente nella lista dei leak globali.

### Struttura del Risultato
Il terminale restituirà un report dettagliato indicante:
- Punteggio complessivo (Score da 0 a 100).
- Esito della validazione (Passato/Fallito con elenco delle regole violate).
- Livello di entropia in bit ed stima del tempo di cracking teorico.
- Warning di sicurezza critico nel caso in cui la password sia trapelata in data breach noti.

---

## Architettura del Software & Polimorfismo

Il cuore del progetto è strutturato seguendo il principio **Open/Closed** di SOLID. La gerarchia di ereditarietà è così definita:

- **Classe Base (`Regola`):** Classe astratta che definisce l'interfaccia comune per tutti i validatori tramite il metodo polimorfico `valida(self, password: str) -> Risultato`.
- **Sottoclassi Concrete:**
  - `RegolaLunghezza`: Verifica la soglia minima di caratteri.
  - `RegolaVarieta`: Controlla la presenza simultanea di maiuscole, minuscole, numeri e caratteri speciali.
  - `RegolaPattern`: Rileva sequenze ripetute o consecutività banali.
  - `RegolaPasswordCompromessa`: Integra il client HIBP per escludere password già violate.

Grazie al **polimorfismo**, l'oggetto `Valutatore` riceve una lista di oggetti di tipo `Regola` e le esegue ciclicamente in modo agnostico rispetto all'implementazione interna.
