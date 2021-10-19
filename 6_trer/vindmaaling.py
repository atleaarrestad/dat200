import datetime

class Vindmaaling:
    neste_id = 1

    def __init__(self, tidspunkt, vindstyrke):
        self.__tidspunkt = tidspunkt
        self.__vindstyrke = vindstyrke
        self.__id = Vindmaaling.neste_id
        Vindmaaling.neste_id += 1

    def get_tidspunkt(self):
        return self.__tidspunkt

    def get_vindstyrke(self):
        return self.__vindstyrke

    def get_id(self):
        return self.__id

    def __str__(self):
        return f"Vindmåling {self.__id}. Tidspunkt: {self.__tidspunkt}. Vindstyrke: {self.__vindstyrke}"

    def __lt__(self, other):
        return self.__tidspunkt < other.get_tidspunkt()


def les_vindmaalinger(filnavn):
    vindmaalinger = []
    with open(filnavn, "r") as fila:
        for linje in fila:
            linje.strip()
            komponenter = linje.split("\t")
            tidspunkt = datetime.datetime.fromisoformat(komponenter[1])
            vindstyrke = float(komponenter[3])
            ny_maaling = Vindmaaling(tidspunkt, vindstyrke)
            vindmaalinger.append(ny_maaling)
    return vindmaalinger


if __name__ == "__main__":
    vindmaalinger = les_vindmaalinger("vindmaalinger_redusert_mer.txt")
    print(len(vindmaalinger))
    print(vindmaalinger[0])
    print(vindmaalinger[1000])
    print(vindmaalinger[-1])
