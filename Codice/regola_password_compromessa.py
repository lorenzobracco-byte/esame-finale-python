from regola import Regola
from hibp_client import HibpClient



class RegolaPasswordCompromessa(Regola):


    def __init__(self):

        super().__init__(
            "Controllo password compromessa"
        )

        self.client = HibpClient()



    def verifica(self, password):

        try:

            numero = self.client.password_compromessa(
                password
            )


            if numero > 0:

                self.messaggio = (
                    "Password trovata in "
                    f"{numero} leak"
                )

                return 0


            else:

                self.messaggio = (
                    "Password non presente nei leak conosciuti"
                )

                return 25



        except Exception as errore:

            self.messaggio = (
                "Errore controllo HIBP: "
                + str(errore)
            )

            return 0
