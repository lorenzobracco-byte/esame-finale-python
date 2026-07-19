import math
import string



class Entropia:


    @staticmethod
    def calcola(password):

        spazio = 0


        if any(c in string.ascii_lowercase for c in password):
            spazio += 26


        if any(c in string.ascii_uppercase for c in password):
            spazio += 26


        if any(c in string.digits for c in password):
            spazio += 10


        if any(c in string.punctuation for c in password):
            spazio += len(string.punctuation)



        if spazio == 0:
            return 0


        return round(
            len(password)
            *
            math.log2(spazio),
            2
        )