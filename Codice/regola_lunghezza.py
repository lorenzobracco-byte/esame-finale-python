from regola import Regola


class RegolaLunghezza(Regola):

    def __init__(self):
        super().__init__("Controllo lunghezza")


    def verifica(self, password):

        lunghezza = len(password)

        if lunghezza >= 12:
            self.messaggio = "Password lunga almeno 12 caratteri"
            return 25

        elif lunghezza >= 8:
            self.messaggio = "Password sufficiente ma migliorabile"
            return 15

        else:
            self.messaggio = "Password troppo corta"
            return 0
