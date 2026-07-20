Manuale utente
Scritto per chi usa il programma, non per chi lo ha scritto. Niente dettagli interni: solo come si
installa, come si lancia, cosa fa ogni comando, con esempi.
Installazione
git clone <https://github.com/lorenzobracco-byte/esame-finale-python>
cd password-evaluator
pip install -r requirements.txt
Richiede Python 3.11+.

Uso
python main.py [opzioni]

Comandi e opzioni
comando / opzione cosa fa esempio
--help, -h Mostra la guida all'uso
dell'interfaccia e l'elenco dei
parametri disponibili.

python main.py --help

Modalità Interattiva (default) Avvia il motore in ascolto
continuo, consentendo
all'utente di digitare e valutare
password in tempo reale una
dopo l'altra.

python main.py

Esempi pratici
Di seguito vengono illustrati tre scenari reali di esecuzione con i relativi output attesi generati dal
sistema.
Caso 1: Password estremamente debole (Pattern banale)
$ python main.py
Inserisci la password da analizzare: 123456
=== REPORT DI SICUREZZA ===
Punteggio: 0/100 (INSUFFICIENTE)

Esito Validazione: FALLITO
Regole violate:
- [RegolaPattern]: La password contiene sequenze numeriche o
caratteri ripetuti elementari.
Analisi Entropia:
- Entropia di Shannon: 0.00 bit (Complessità nulla)
- Tempo stimato di cracking: Immediato (Attacco Brute-force diretto)
Sicurezza Cloud (HIBP):
- CRITICO: Questa password è compromessa! Risulta presente in oltre
23.000.000 di data breach noti.

Caso 2: Password robusta dal punto di vista locale ma compromessa nel Cloud
$ python main.py
Inserisci la password da analizzare: Password123!
=== REPORT DI SICUREZZA ===
Punteggio: 40/100 (VULNERABILE)
Esito Validazione: FALLITO
Regole violate:
- [RegolaPasswordCompromessa]: Password strutturalmente corretta ma
non sicura.
Analisi Entropia:
- Entropia stimata: 44.2 bit
- Tempo stimato di cracking: Poche ore
Sicurezza Cloud (HIBP):
- PERICOLO: Nonostante superi i criteri di lunghezza e varietà,
questa stringa è presente nei database dei leak pubblici. Non
utilizzarla.

Caso 3: Password eccellente e sicura
$ python main.py
Inserisci la password da analizzare: K9!mQ$zP27_xLw
=== REPORT DI SICUREZZA ===
Punteggio: 100/100 (ECCELLENTE)
Esito Validazione: SUPERATO
Regole violate: Nessuna
Analisi Entropia:
- Entropia stimata: 92.4 bit
- Tempo stimato di cracking: Secoli (Resistente ad attacchi
standard)
Sicurezza Cloud (HIBP):
- SICURA: La password non compare in nessun data breach censito.

Errori comuni e cosa fare
● La rete non risponde / Timeout HIBP: Se il computer non è connesso a Internet o i
server di *Have I Been Pwned* non sono raggiungibili, il modulo hibp_client.py intercetta
l'eccezione di connessione. Il programma non va in crash: mostra un avviso a schermo
escludendo temporaneamente il controllo cloud e basando la valutazione unicamente sui
criteri metrici locali ed entropici.
● Modulo 'requests' non trovato (ModuleNotFoundError): Si verifica se si avvia il
programma senza aver installato le dipendenze. Risoluzione: Esegui nuovamente pip
install -r requirements.txt all'interno dell'ambiente virtuale attivo.
● Input vuoto: Se l'utente preme invio senza digitare caratteri, il sistema notifica l'errore
invitando a inserire una stringa valida, bloccando l'analisi a punteggio zero senza
interrompere l'esecuzione del terminale.
