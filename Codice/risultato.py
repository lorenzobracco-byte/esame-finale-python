class Risultato:

    def __init__(self, punteggio, giudizio, dettagli):

        self.punteggio = punteggio
        self.giudizio = giudizio
        self.dettagli = dettagli


    def stampa(self):

        print("\n--- RISULTATO ---")

        print(
            f"Punteggio: {self.punteggio}/100"
        )

        print(
            f"Giudizio: {self.giudizio}"
        )


        print("\nDettagli:")

        for dettaglio in self.dettagli:
            print("-", dettaglio)
