import re
from regola import Regola


class RegolaVarietaCaratteri(Regola):

    def __init__(self):
        super().__init__("Varieta caratteri")


    def verifica(self, password):

        punti = 0
        caratteristiche = []


        if re.search("[a-z]", password):
            punti += 5
            caratteristiche.append("minuscole")


        if re.search("[A-Z]", password):
            punti += 5
            caratteristiche.append("maiuscole")


        if re.search("[0-9]", password):
            punti += 5
            caratteristiche.append("numeri")


        if re.search("[^a-zA-Z0-9]", password):
            punti += 5
            caratteristiche.append("simboli")


        self.messaggio = (
            "Caratteristiche trovate: "
            + ", ".join(caratteristiche)
        )

        return punti
