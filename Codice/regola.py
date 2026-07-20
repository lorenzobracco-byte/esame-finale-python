from abc import ABC, abstractmethod


class Regola(ABC):
    """
    Classe base per tutte le regole di sicurezza.
    """

    def __init__(self, nome):
        self.nome = nome
        self.messaggio = ""

    @abstractmethod
    def verifica(self, password):
        """
        Metodo polimorfico.
        Ogni sottoclasse deve implementarlo.
        """
        pass

    def get_messaggio(self):
        return self.messaggio
