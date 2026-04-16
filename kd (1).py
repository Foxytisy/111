#1.uzd
class Fails:
    nosaukums: str
    formāts: str
    izmers_kb: float
    atrasanas_vieta: str
    ir_atverts: bool

    def __init__(self, nosaukums, formats, izmers_kb, atrasanas_vieta):
        self.nosaukums = nosaukums
        self.formats = formats
        self.izmers_kb = izmers_kb
        self.atrasanas_vieta = atrasanas_vieta
        self.ir_atverts = False

    def atvert(self):
        self.ir_atverts = True

    def aizvert(self):
        self.ir_atverts = False

    def parvietot(self, jauna_vieta):
        self.atrasanas_vieta = jauna_vieta

    def __str__(self):
        return f"{self.nosaukums}.{self.formats} ({self.izmers_kb} KB) - {self.atrasanas_vieta}"


fails1 = Fails("dokuments", "txt", 12.5, "C:/Users/Skola/Documents")
fails1.atvert()
fails1.parvietot("D:/Darbi")
print(fails1)
#2.uzd
class Pieraksts:
    specialists: str
    datums: str
    cena: float
    atlikusi_summa: float
    apmaksats: bool
    pierakstits: bool

    def __init__(self, specialists, datums, cena):
        self.specialists = specialists
        self.datums = datums
        self.cena = cena
        self.atlikusi_summa = cena
        self.apmaksats = False
        self.pierakstits = True

    def maksat(self, summa):
        self.atlikusi_summa -= summa
        if self.atlikusi_summa < 0:
            self.atlikusi_summa = 0
        if self.atlikusi_summa == 0:
            self.apmaksats = True

    def __str__(self):
        return f"[{self.pierakstits}] pieraksts pie {self.specialists} {self.datums}. Apmaksats {self.apmaksats}, atlikusi summa: {self.atlikusi_summa} no {self.cena}."


pier1 = Pieraksts("frizieris", "2026-04-20 15:30", 25.0)
pier1.maksat(25.0)
print(pier1)
#3.uzd
class Prece:
    id: int
    nosaukums: str
    vertiba: float

    def __init__(self, id, nosaukums, vertiba):
        self.id = id
        self.nosaukums = nosaukums
        self.vertiba = vertiba

    def __str__(self):
        return f"[{self.id}] {self.nosaukums} - {self.vertiba} EUR"


class Noliktava:
    adrese: str
    max_ietilpiba: int
    preces: list[Prece]

    def __init__(self, adrese, max_ietilpiba):
        self.adrese = adrese
        self.max_ietilpiba = max_ietilpiba
        self.preces = []

    def pievienot(self, prece: Prece):
        if len(self.preces) < self.max_ietilpiba:
            self.preces.append(prece)
        else:
            print("Kluda: Noliktava ir pilna")

    def iznemt(self, prece: Prece):
        self.preces.remove(prece)

    def atjaunotVertibu(self, id, jauna_vertiba):
        for prece in self.preces:
            if prece.id == id:
                prece.vertiba = jauna_vertiba

    def izvaditPreces(self):
        for prece in self.preces:
            print(prece)

    def kopejaVertiba(self):
        summa = 0.0
        for prece in self.preces:
            summa += prece.vertiba
        return summa


pr1 = Prece(1, "Televizors", 350.00)
pr2 = Prece(2, "Ledusskapis", 500.00)
pr3 = Prece(3, "Tosteris", 45.00)

nol = Noliktava("Avg", 2)

nol.pievienot(pr1)
nol.pievienot(pr2)
nol.pievienot(pr3)

nol.izvaditPreces()
print(nol.kopejaVertiba())

nol.atjaunotVertibu(1, 400.00)
print("Pec atjaunosanas:")
nol.izvaditPreces()

nol.iznemt(pr2)
print("Pec iznemsanas:")
nol.izvaditPreces()
#4.uzd
import math

class Punkts2D:
    x: float
    y: float

    def __init__(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y

    def uzstaditX(self, x):
        self.x = x

    def uzstaditY(self, y):
        self.y = y

    def izvaditX(self):
        return self.x

    def izvaditY(self):
        return self.y

    def __str__(self):
        return f"({self.x}, {self.y})"


class Punkts3D(Punkts2D):
    z: float

    def __init__(self, x = 0.0, y = 0.0, z = 0.0):
        super().__init__(x, y)
        self.z = z

    def uzstaditZ(self, z):
        self.z = z

    def izvaditZ(self):
        return self.z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"


p1 = Punkts2D(2, 3)
p2 = Punkts2D(7, 11)

attalums = math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)
print(p1)
print(p2)
print(attalums)

p3 = Punkts3D(4, 5, 6)
print(p3)
