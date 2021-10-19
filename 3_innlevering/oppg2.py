class Hanoi:
    
    def __init__(self, plates: int):
        self.plates = plates
        self.a = [str(index) for index in range(1, plates + 1)]
        self.b, self.c = [], []
        self.print()

    def solve(self, n, source, destination, auxiliary):
        if n==1:
            destination.insert(0, source[0])
            del source[0]
            self.print()
            return

        self.solve(n-1, source, auxiliary, destination)
        destination.insert(0, source[0])
        del source[0]
        self.print()
        self.solve(n-1, auxiliary, destination, source)
    
    def print(self):
        s = ""
        length = max(len(self.a), len(self.b), len(self.c))
        for i in range(length):
            if i < len(self.a):
                s += f"|{self.a[i]}|\t"
            else:
                s+= "| |\t"
            if i < len(self.b):
                s += f"|{self.b[i]}|\t"
            else:
                s+= "| |\t"
            if i < len(self.c):
                s += f"|{self.c[i]}|"
            else:
                s+= "| |"
            print(s)
            s = ""
        print("\n")  


hanoi = Hanoi(7)
hanoi.solve(hanoi.plates, hanoi.a, hanoi.c, hanoi.b)

  


