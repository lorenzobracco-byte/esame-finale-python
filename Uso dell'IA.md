# Uso dell'IA

## Sintesi

L'IA è stata utilizzata come co-pilota per velocizzare la scrittura di espressioni regolari complesse, algoritmi di hashing standard e boilerplate per i test, mantenendo il controllo completo sull'architettura e sul design dei componenti.

## Dettaglio per parte

| parte del progetto | cosa avete chiesto | cosa avete accettato / modificato / rifiutato | perché |
| :---- | :---- | :---- | :---- |
| regola\_pattern.py | Regex per individuare sequenze ripetute (es. "12345") o pattern da tastiera ("qwerty"). | Accettata la logica delle espressioni regolari; modificato il binding per integrarlo con l'oggetto Risultato custom. | Risparmio di tempo sulla sintassi complessa delle regex. |
| hibp\_client.py | Esempio di implementazione del protocollo K-Anonymity (invio primi 5 caratteri dell'hash SHA-1 a HIBP). | Accettata la logica di derivazione dell'hash; rifiutata la gestione nativa degli errori, riscritta da zero per non bloccare l'applicazione. | Sicurezza nell'implementazione dell'algoritmo di anonimizzazione richiesto dalle API. |
| Unit Test | Generazione di casi limite (edge cases) per testare le regole di lunghezza e varietà. | Accettati i vettori di test (es. stringhe vuote, caratteri speciali); modificata la struttura per usare le fixture del framework di testing. | Copertura più rapida ed efficace dei casi critici. |

## Cosa NON abbiamo delegato all'IA

L'IA non ha preso alcuna decisione architetturale. La scelta di adottare una gerarchia di classi polimorfica basata su Regola, il design del flusso dei dati gestito dal Valutatore, la stesura della documentazione (incluso questo documento e il DevLog) e l'analisi dei compromessi implementativi sono farina del nostro sacco.  
