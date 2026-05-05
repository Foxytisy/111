class Filma:
    nosaukums: str
    zanrs: str
    
class Kinoteatris:
    nosaukums: str
    filma: Filma
    
    def __init__(self):
        
        pass
    

class Spuldze:
    modelis: str
    elektriba: bool = False
    gaisums: int = 0
    
    def __init__(self, modelis):
        self.modelis = modelis
    
    
class Lampa:
    modelis: str
    ieslegta: bool = False
    spuldzite: Spuldze
    
    def __init__(self, modelislampa, modelisspuldze = "nav"):
        self.spuldzite = Spuldze(modelisspuldze)
        self.modelis = modelislampa
        
    def stavoklis(self):
        if self.ieslegta == False:
            self.spuldzite.elektriba = True
            self.ieslegta = True #Vnk on/off
            print("Spuldzite ieslegta!")
        else:
            self.spuldzite.elektriba = False
            self.ieslegta = False
            print("Spuldzite izslegta!")
            
    def info(self):
        print("Spuldzites stāvoklis: ", self.spuldzite.elektriba)
        print("Lampas stāvoklis: ", self.ieslegta)
        print("Spuldzites modelis: ", self.spuldzite.modelis)
        print("Lampas modelis: ", self.modelis)
      
      
spuldz = Spuldze("Phillips huh 3000") #šis arī nestrādā lol
labalampa = Lampa("ddd", spuldz)

labalampa.stavoklis()
labalampa.info()

class Transportlidzeklis:
    razotajs: str
    modelis: str
    ritenu_skaits: int
    parvadajamo_skaits: int
    
    def __init__(self, razotajs, modelis):
        self.razotajs = razotajs
        self.modelis = modelis
        self.ritenu_skaits = 0
        self.parvadajamo_skaits = 0

class Automatisna(Transportlidzeklis):
    def __init__(self, razotajs, modelis, parvadajamoSkaits):
        super().__init__(self, modelis)
        self.modelis = modelis
        self.razotajs = razotajs
        self.ritenu_skaits = 4
        self.parvadajamo_skaits = parvadajamoSkaits
    def braukt(self):
        print("wroom wroom")
        
brumbrum = Automatisna("skoda", "ātrais žigulis", 5) #nestrādā lol

class Dzivnieks:
    vards: str
    kaju_skaits: int

    def __init__(self, vards):
        self.vards = vards
        self.kaju_skaits = 0

    def skana(self):
        print("no")
        
class Suns(Dzivnieks):
    def __init__(self, vards, kajuskaits):
        super().__init__(self)
        self.vards = vards
        self.kaju_skaits = kajuskaits
    def skana(self):
        print("woof woofing, rej rejing")
        
class Kakis(Dzivnieks):
    def __init__(self, vards, kajuskaits):
        super().__init__(self)
        self.vards = vards
        self.kaju_skaits = kajuskaits
    def skana(self):
        print("maaaaaaaaaaaaaaaaaaaaaauuu maaaaaaaaauuu")
        
labsSuns = Suns("reksis", 4)
labsSuns.skana()
    
kakitis = Kakis("Bocmanis", 4)
kakitis.skana()