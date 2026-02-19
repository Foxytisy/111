class Prece:
    nosaukums: str
    skaits: int
    vertiba: float

    def __init__(self, nosaukums, skaits, vertiba):
        self.nosaukums = nosaukums
        self.skaits = skaits
        self.vertiba = vertiba

class Grozs:
    preces = []

    def pievienotPreci(self, Prece):
        self.preces.append(Prece)
        print("Pievienots!")

    def nomentPreci(self, Prece):
        self.preces.remove(Prece)
        print("Noņemts!")
    def vertiba(self):
        vertiba = 0
        for i in self.preces:
            vertiba += i
        print(self.vertiba)
            


grozins = Grozs()
rimiSaldejums = Prece("Rimi Saldejums", 2, 30.5)
rimiAboli = Prece("Rimi baigie aboli", 10, 5000.0)

grozins.pievienotPreci(rimiSaldejums)
grozins.pievienotPreci(rimiAboli)
grozins.nomentPreci(rimiAboli)
grozins.vertiba()


