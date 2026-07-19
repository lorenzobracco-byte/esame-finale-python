from regola_lunghezza import RegolaLunghezza
from regola_varieta import RegolaVarietaCaratteri
from regola_pattern import RegolaPattern
from regola_password_compromessa import RegolaPasswordCompromessa

from valutatore import ValutatorePassword
from entropia import Entropia



def main():


    password = input(
        "Inserisci una password: "
    )


    regole = [

        RegolaLunghezza(),

        RegolaVarietaCaratteri(),

        RegolaPattern(),

        RegolaPasswordCompromessa()

    ]



    valutatore = ValutatorePassword(
        regole
    )


    risultato = valutatore.valuta(
        password
    )


    risultato.stampa()



    print(
        "\nEntropia:",
        Entropia.calcola(password),
        "bit"
    )




if __name__ == "__main__":

    main()