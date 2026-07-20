from regola import Regola


class RegolaPattern(Regola):

    def __init__(self):
        super().__init__("Pattern comuni")


    def verifica(self, password):

        password_lower = password.lower()


        pattern_vietati = [
            "password",
            "123456",
            "qwerty",
            "admin",
            "letmein"
        ]


        for pattern in pattern_vietati:

            if pattern in password_lower:

                self.messaggio = (
                    f"Pattern pericoloso trovato: {pattern}"
                )

                return 0


        self.messaggio = "Nessun pattern comune trovato"

        return 15
