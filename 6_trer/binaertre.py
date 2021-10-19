class Binaertre:
    def __init__(self, dataobjekt):
        self.data = dataobjekt
        self.forelder = None
        self.venstre_barn = None
        self.hoyre_barn = None

    @property
    def venstre_barn(self):
        return self.__venstre_barn

    @venstre_barn.setter
    def venstre_barn(self, node):
        self.__venstre_barn = node
        if node is not None:
            node.forelder = self

    @property
    def hoyre_barn(self):
        return self.__hoyre_barn

    @hoyre_barn.setter
    def hoyre_barn(self, node):
        self.__hoyre_barn = node
        if node is not None:
            node.forelder = self

    def er_bladnode(self):
        if self.venstre_barn is None and self.hoyre_barn is None:
            return True
        return False

    def rekursiv_preorder_utskrift(self, nivaa=0):
        for i in range(nivaa):
            print("\t", end="")
        print(self.data)
        if self.venstre_barn is not None:
            self.venstre_barn.rekursiv_preorder_utskrift(nivaa+1)
        if self.hoyre_barn is not None:
            self.hoyre_barn.rekursiv_preorder_utskrift(nivaa+1)

    def rekursiv_postorder_utregning(self):
        if self.er_bladnode():
            return float(self.data)
        venstre_verdi = self.venstre_barn.rekursiv_postorder_utregning()
        hoyre_verdi = self.hoyre_barn.rekursiv_postorder_utregning()
        if self.data == "+":
            return venstre_verdi + hoyre_verdi
        if self.data == "*":
            return venstre_verdi * hoyre_verdi
        if self.data == "**":
            return venstre_verdi ** hoyre_verdi
        if self.data == "-":
            return venstre_verdi + hoyre_verdi
        if self.data == "/":
            return venstre_verdi / hoyre_verdi
        raise ValueError(f"Ukjent operator: {self.data}")

    def rekursiv_inorder_formelutskrift(self):
        if self.er_bladnode():
            print(self.data, end="")
        else:
            print("(", end="")
            self.venstre_barn.rekursiv_inorder_formelutskrift()
            print(f" {self.data} ", end="")
            self.hoyre_barn.rekursiv_inorder_formelutskrift()
            print(")", end="")

    def __iter__(self):
        return BinaertrePostorderIterator(self)

class BinaertrePostorderIterator:
    def __init__(self, treet):
        self.treet = treet
        self.stabel = []
        self.stabel.append((treet, 0))

    def __next__(self):
        while len(self.stabel) > 0:
            element = self.stabel.pop()
            if element[0].er_bladnode():
                return element[0].data
            if element[1] == 0:
                self.stabel.append((element[0], 1))
                if element[0].venstre_barn is not None:
                    self.stabel.append((element[0].venstre_barn, 0))
            if element[1] == 1:
                self.stabel.append((element[0], 2))
                if element[0].hoyre_barn is not None:
                    self.stabel.append((element[0].hoyre_barn, 0))
            if element[1] == 2:
                return element[0].data
        raise StopIteration

    def __iter__(self):
        return self

if __name__ == "__main__":
    rot = Binaertre("+")
    v_barn_1 = Binaertre("**")
    rot.venstre_barn = v_barn_1
    v_v_barn = Binaertre("5")
    v_h_barn = Binaertre("2")
    v_barn_1.venstre_barn = v_v_barn
    v_barn_1.hoyre_barn = v_h_barn
    h_barn_1 = Binaertre("+")
    rot.hoyre_barn = h_barn_1
    h_v_barn = Binaertre("*")
    h_v_barn.venstre_barn = Binaertre("2")
    h_v_barn.hoyre_barn = Binaertre("3")
    h_barn_1.venstre_barn = h_v_barn
    h_h_barn = Binaertre("*")
    h_barn_1.hoyre_barn = h_h_barn
    h_h_barn.venstre_barn = Binaertre("7")
    h_h_h_barn = Binaertre("+")
    h_h_barn.hoyre_barn = h_h_h_barn
    h_h_h_barn.venstre_barn = Binaertre("9")
    h_h_h_barn.hoyre_barn = Binaertre("5")
    rot.rekursiv_preorder_utskrift()
    print(rot.rekursiv_postorder_utregning())
    rot.rekursiv_inorder_formelutskrift()
    print()
    print("\n Iterativ iteratortest")
    for element in rot:
        print(element)
