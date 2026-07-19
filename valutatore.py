from risultato import Risultato



class ValutatorePassword:


    def __init__(self, regole):

        self.regole = regole



    def valuta(self, password):

        punteggio = 0

        dettagli = []


        for regola in self.regole:

            punti = regola.verifica(
                password
            )

            punteggio += punti


            dettagli.append(
                regola.get_messaggio()
            )



        if punteggio >= 70:

            giudizio = "Password molto forte"


        elif punteggio >= 40:

            giudizio = "Password discreta"


        else:

            giudizio = "Password debole"



        return Risultato(
            punteggio,
            giudizio,
            dettagli
        )