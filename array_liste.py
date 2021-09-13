import numpy as np
import math


class ArrayListe:
    def __init__(self, startkapasitet = 20):
        self.array = np.zeros(startkapasitet, dtype=object)
        self.lengde = 0
        self.start_index = math.floor(startkapasitet/2)

    #gir resultatet av len funksjonen
    def __len__(self):
        return self.lengde

    # Kjøretid Theta(n)
    def utvid(self, ny_storrelse=None):
        if ny_storrelse is None:
            ny_storrelse = len(self.array)*2
        ny_array = np.zeros(ny_storrelse, dtype=object)
        for index in range(self.lengde):
            ny_array[self.start_index + index] = self.array[self.start_index + index]
        self.array = ny_array


    def utvid_left(self, ny_storrelse=None):
        if ny_storrelse is None:
            ny_storrelse = len(self.array)*2
        ny_array = np.zeros(ny_storrelse, dtype=object)
        ny_start_index = int(ny_storrelse/2)
        for index in range(self.lengde):
            ny_array[ny_start_index + index] = self.array[self.start_index + index]
        self.array = ny_array
        self.start_index = ny_start_index



    # Legger til element på slutten av lista
    # Kjøretid: Worst case Theta(n) hvis jeg må lage en ny array
    #           Ellers Theta(1)
    # Kjøretid O(1) amortized, O(n) worst case
    def append(self, element):
        if self.lengde >= len(self.array) - self.start_index:
            self.utvid()
        self.array[self.start_index + self.lengde] = element
        self.lengde += 1

    # O(1) hvis ledig buffer, ellers O(n) når utvidet array lages.
    def append_left(self, element):
        if self.start_index == 0:
            self.utvid_left()
            self.start_index = math.floor(len(self.array)/2)
        self.array[self.start_index - 1] = element
        self.lengde += 1
        self.start_index -= 1


    # Legger inn det oppgitte elementet på oppgitt indeks, og forskyver alle elementer som ligger
    # etterpå ett hakk bak
    # Best case på slutten O(1)
    # Worst case starten O(n)
    # Gjennomsnitt: Forventningsverdi n/2, O(n)
    def insert(self, indeks, element):
        if self.lengde >= len(self.array) - self.start_index:
            self.utvid()
        for index in range(self.lengde-1, indeks-1, -1):
            self.array[self.start_index + index+1] = self.array[self.start_index + index]
        self.array[self.start_index + indeks] = element
        self.lengde += 1

    # Overskriver det som ligger på oppgitt indeks med det oppgitte elementet.
    # Tilsvarer Python liste[indeks] = element
    # Kjøretid Theta(1)
    def put(self, indeks, element):
        self.array[indeks] = element

    # Fjerner første forekomst av oppgitt element
    # Kjøretid Theta(n)
    def remove(self, element):
        index = self.search(element)
        self.delete(index)

    # O(1), sletter kun siste element, trenger ikke flytte noe i .delete(index)
    def pop(self):
        if self.lengde > 0:
            index = self.start_index + self.lengde - 1
            element = self.array[index]
            self.delete(index)
            return element
        else:
            return None

    # O(n), flytter n elementer mot venstre.
    def popleft(self):
        if self.lengde > 0:
            element = self.array[self.start_index]
            self.delete(0)
            return element
        else:
            return None

    # Fjerner elementet på oppgitt indeks
    # Tilsvarer Python del liste[indeks]
    # Kjøretid er antall elementer som må flyttes
    # Best case siste element O(1)
    # Worst case første element O(n)
    # Gjennomsnitt O(n)
    def delete(self, indeks):
        for i in range(indeks, self.lengde):
            self.array[self.start_index + i] = self.array[self.start_index + i + 1]
        self.array[self.lengde] = 0
        self.lengde -= 1

    # Legger alle elementete i oppgitt samling til i lista
    # Kjøretid O(m) best case
    # Kjøretid O(n + m) worst case
    def append_all(self, samling):
        for element in samling:
            self.append(element)

    # Setter inn den oppgitte samlingen på oppgitt indeks, og forskyver alt som ligger bak
    # Kjøretid som en flytting + lengden til den nye lista
    def insert_all(self, indeks, samling):
        if self.lengde + len(samling) >= len(self.array) - self.start_index + 1:
            self.utvid((self.lengde + len(samling))*2)
        for i in range(self.lengde-1, indeks-1, -1):
            self.array[self.start_index + i + len(samling)] = self.array[self.start_index + i]
        for i in range(len(samling)):
            self.array[self.start_index + indeks + i] = samling[i]
        self.lengde += len(samling)


    # Returnerer elementet på oppgitt indeks.
    # Tilsvarer Python variabel = liste[indeks]
    # Kjøretid Theta(1)
    def get(self, indeks):
        return self.array[indeks + self.start_index]

    # Finner første indeks hvor dette elementet forekommer
    # Kjøretid som sekvensielt søk
    def search(self, element):
        for index in range(self.lengde):  # Kjører maks n ganger
            if element == self.array[index]:  # Kjører maks n ganger
                return index  # Kjører maks 1 gang
        return -1  # Kjører maks 1 gang

    # Gå gjennom lista, element for element
    def __iter__(self):
        return ArrayListIterator(self)

    # Python spesialmetoder slik at array-lista kan brukes som en Python liste. Ikke forelest siden
    # det ikke er en sentral del av faget DAT200.
    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __contains__(self, item):
        if self.search(item) != -1:
            return True
        return False

    def __delitem__(self, key):
        self.delete(key)

    # Implementerer "+" operatoren, og viser hva den gjør for lister.
    def __add__(self, liste):
        self.append_all(liste)


class ArrayListIterator:
    def __init__(self, lista):
        self.lista = lista
        self.nv_element = 0

    def __next__(self):
        if self.nv_element >= len(self.lista):
            raise StopIteration
        resultat = self.lista.get(self.nv_element)
        self.nv_element += 1
        return resultat


if __name__ == "__main__":
    liste = ArrayListe(4)
    liste.append(4)
    liste.append_left(1)
    liste.insert_all(1, [2, 3])
    liste.pop()
    liste.popleft()
    liste.pop()
    liste.popleft()










    print(f"start_index: {liste.start_index},  array_lenght: {liste.lengde}")
    print(liste.array)
    for element in liste:
        print(element)
