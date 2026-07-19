import hashlib
import requests


class HibpClient:
    """
    Client per interrogare Have I Been Pwned
    usando il metodo k-anonymity.
    """

    API_URL = "https://api.pwnedpasswords.com/range/"


    def __init__(self):
        pass


    def calcola_hash(self, password):

        sha1 = hashlib.sha1()

        sha1.update(
            password.encode("utf-8")
        )

        return sha1.hexdigest().upper()



    def password_compromessa(self, password):

        hash_password = self.calcola_hash(password)


        # Primo blocco inviato al server
        prefisso = hash_password[:5]

        # Parte che rimane privata
        suffisso = hash_password[5:]


        risposta = requests.get(
            self.API_URL + prefisso
        )


        if risposta.status_code != 200:
            raise Exception(
                "Errore nella richiesta HIBP"
            )


        risultati = risposta.text.splitlines()


        for risultato in risultati:

            hash_parziale, conteggio = risultato.split(":")


            if hash_parziale == suffisso:

                return int(conteggio)


        return 0