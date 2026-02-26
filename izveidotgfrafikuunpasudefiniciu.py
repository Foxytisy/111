class Prece:
    nosaukums: str
    skaits: int
    vertiba: float

    def __init__(self, nosaukums, skaits, vertiba):
        self.nosaukums = nosaukums
        self.skaits = skaits
        self.vertiba = vertiba

class Grozs:
    preces: list[Prece]

    def __init__(self):
        self.preces = []

    def pievienotPreci(self, Prece :Prece):
        self.preces.append(Prece)
        print("Pievienots!")

    def nomentPreci(self, Prece :Prece):
        self.preces.remove(Prece)
        print("Noņemts!")
    def vertiba(self):
        vertiba = 0
        for prece in self.preces:
            vertiba += prece.vertiba
        return(self.vertiba)
            


grozins = Grozs()
rimiSaldejums = Prece("Rimi Saldejums", 2, 30.5)
rimiAboli = Prece("Rimi baigie aboli", 10, 5000.0)

grozins.pievienotPreci(rimiSaldejums)
grozins.pievienotPreci(rimiAboli)
grozins.nomentPreci(rimiAboli)
print(grozins.vertiba())



class bankasKonts:
    nosaukums: str
    daudzums: float

    def __init__(self, nosaukums, sakumaDaudzums = 0):
        self.nosaukums = nosaukums
        self.daudzums = sakumaDaudzums

    def ieskaitit(self, summa):
        self.daudzums += summa
    def iznemt(self, summa):
        if self.daudzums > 50:
            self.daudzums -= summa
        else:
            print("nabags")

class krajkonts(bankasKonts):
    def __init__(self, nosaukums, sakumaDaudzums=0):
        super().__init__(nosaukums, sakumaDaudzums)
    def iznemt(self, summa):
        if self.daudzums > 50:
            self.daudzums -= summa + (summa*0.1)
            print(self.daudzums)
        else:
            print("nabags")
    

krajkontss = krajkonts("labaiis", 100)

krajkontss.iznemt(10)

class Akcija:
    nosaukums: str
    nominālvērtība: float
    def __init__(self, nosaukums, nominalvertiba):
        self.nosaukums = nosaukums
        self.nominālvērtība = nominalvertiba
        
        
class AkcijuKonts(bankasKonts):
    akcijas: list[Akcija]
    def __init__(self):
        super().__init__()
        self.akcijas = []
        
akc = AkcijuKonts()
akc.ieskaitit(200)
akc.pievienotAkc(Akcija("AAA", 100))
otrAkc = Akcija("AAA", 100)
akc.pievienotAkc(otrAkc)
print(akc)