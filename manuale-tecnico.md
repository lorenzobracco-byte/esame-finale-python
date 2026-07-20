Manuale tecnico
Scritto per chi volesse estendere il programma (incluso il te di fra sei mesi). Spiega com'è fatto dentro: architettura, moduli, e soprattutto la gerarchia di classi.
Architettura generale
Il codice è organizzato per separare nettamente la visualizzazione e l'interazione con l'utente (CLI) dalla logica di dominio e dalle metriche di calcolo pure, garantendo disaccoppiamento.
src/password_evaluator/
├── __main__.py                         ← Punto di ingresso per l'avvio del programma come modulo (python -m password_evaluator).
    ├── regola.py                       ← Contiene la classe base astratta Regola per tutti i sistemi di controllo delle password.
    ├── valutatore.py                   ← Il motore centrale che orchestra ed esegue in modo polimorfico i vari controlli impostati.
    ├── risultato.py                    ← Struttura dati standardizzata per veicolare l'esito (successo/fallimento) di ciascun vincolo.
    ├── entropia.py                     ← Modulo matematico puro per il calcolo dell'entropia di Shannon e stima del tempo di brute-force.
    ├── hibp_client.py                  ← Client HTTP specifico per l'interazione anonimizzata con l'API Have I Been Pwned.
    ├── regola_lunghezza.py             ← Sottoclasse concreta: implementa il vincolo metrico sulla lunghezza minima della stringa.
    ├── regola_varieta.py               ← Sottoclasse concreta: valida la compresenza di set differenti (maiuscole, minuscole, numeri, simboli).
    ├── regola_pattern.py               ← Sottoclasse concreta: intercetta sequenze ripetitive o pattern sequenziali banali.
    └── regola_password_compromessa.py  ← Sottoclasse concreta: coordina il controllo cloud contro i breach sfruttando il client HIBP.


Chi dipende da chi: __main__.py dipendono direttamente da valutatore.py e entropia.py. valutatore.py dipende solo dalla classe astratta definita in regola.py, invertendo le dipendenze rispetto alle implementazioni reali.

La gerarchia di classi
Il cuore del sistema sfrutta il polimorfismo per consentire l'espansione indefinita dei criteri di controllo senza dover modificare il motore di orchestrazione (Open/Closed Principle).
Classe Base (Regola): Definita in regola.py, rappresenta la classe astratta di riferimento.
Sottoclassi Concrete: RegolaLunghezza, RegolaVarieta, RegolaPattern, RegolaPasswordCompromessa.
Metodo Polimorfico (valida(password: str) -> Risultato): Ogni sottoclasse implementa questo metodo in modo specifico per incapsulare la propria logica di verifica e restituire un oggetto uniforme Risultato.
+------------------------------------------+
|            <<abstract>>                  |
|               Regola                     |
+------------------------------------------+
| + valida(password: str) : Risultato      |
+------------------------------------------+
                     ^
                     | (Ereditarietà)
     +---------------+---------------+---------------+
     |                               |               |
+--------------------+      +--------------------+  +--------------------+
|   RegolaLunghezza  |      |    RegolaVarieta   |  |   RegolaPattern    |
+--------------------+      +--------------------+  +--------------------+
| + valida(password) |      | + valida(password) |  | + valida(password) |
+--------------------+      +--------------------+  +--------------------+



Come aggiungere una nuova sottoclasse
Per aggiungere un nuovo criterio di controllo (ad esempio, una verifica contro un dizionario di
parole note):
1. Crea una nuova classe all'interno di un nuovo modulo (es. regola_dizionario.py) che
erediti da Regola (definita in regola.py).
2. Ridefinisci il metodo polimorfico valida(self, password: str) -> Risultato implementando la
logica specifica.
3. Registra la nuova classe instanziandola all'interno della lista di regole passate al
costruttore di Valutatore nel punto di configurazione presente in main.py.

Dipendenze esterne
Il progetto persegue un approccio minimalista per massimizzare la portabilità e ridurre la superficie d'attacco delle dipendenze:
requests: Utilizzata unicamente nel modulo core/hibp_client.py per gestire le richieste HTTP verso l'API esterna di Have I Been Pwned in modo robusto.
hashlib (Standard Library): Utilizzata per l'hashing SHA-1 locale necessario a garantire il K-Anonimato.
math (Standard Library): Utilizzata per effettuare i calcoli logaritmici necessari all'analisi dell'entropia.
