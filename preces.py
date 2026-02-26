class Akcija:
    nosaukums: str
    nominālvērtība: float
    def __init__(self, nosaukums, nominalvertiba):
        self.nosaukums = nosaukums
        self.nominālvērtība = nominalvertiba
        
        
class AkcijuKonts(BankasKonts):
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