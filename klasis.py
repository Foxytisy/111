class Austinas:
    brends: str
    modelis: str

    ieslegts: bool
    savienots: bool
    skalums: float
    atskano: bool
    dziesma: str

    def __init__(self, brends, modelis):
        self.brends = brends
        self.modelis = modelis

        self.ieslegts = False
        self.savienots = False
        self.atskano = False
    
    def elektriba(self):
        if self.ieslegts == False:
            self.ieslegts = True
            print("yo bluetotz devaic is redi to pear")
        else:
            self.ieslegts = False
            print("bai baiii!")

    def savienot(self):
        if self.savienots == False:
            self.savienots = True
            print("Blueetooth devaic is redayy")
        else:
            self.savienots = False
            self.atskano = False
            print("yo blutoz devaic has deskonekted uh sukesfuley")

    def skalums(self, cik):
        if self.ieslegts == True:
            self.skalums =+ cik
            print("yo hedphoner is ", self.skalums, "dB lautness")
        else:
            print("Austinas ir izslegtas!")

    def atskanot(self, dziesma):
        if self.ieslegts == True:
            self.atskano = True
            self.dziesma = dziesma
            print("Now playeing ", self.dziesma, " on saundklaud")
        else:
            print("Austinas ir izslegtas!")

    def __str__(self):
        print(self.brends, self.modelis, self.ieslegts, self.savienots, self.skalums, self.atskano, self.dziesma)


labasAusis = Austinas("volkswagen", "HB-495BT 392000 5000xTX pT BT")

labasAusis.elektriba()
labasAusis.savienot()
labasAusis.skalums(50)
labasAusis.atskanot("Genoveva - Kanjiks Austrums")

labasAusis.__str__()