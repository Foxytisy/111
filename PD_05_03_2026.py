# 2. Uzd

class LLMModelis():
    nosaukums: str
    izmers: float
    temperatura: float
    pieejamie_lidzekli: float
    cena_token: float
    
    def __init__(self, Nosaukums, Izmers, Temperatura, Pieejamie_Lidzekli, TokenaCena):
        self.nosaukums = Nosaukums
        self.izmers = Izmers
        self.temperatura = Temperatura
        self.pieejamie_lidzekli = Pieejamie_Lidzekli
        self.cena_token = TokenaCena
    
    def aprekinatIzmaksas(self, teksts):
        print(len(teksts)*self.cena_token)
    
    def izvaditTekstu(self, teksts):
        cena = len(teksts)*self.cena_token
        if cena < self.pieejamie_lidzekli:
            self.pieejamie_lidzekli -= cena
            print(teksts[::-1])
        else:
            print("Nepietiek līdzekļu šim! Maksā maksā")
            
    def __str__(self):
        return f"Modelis: {self.nosaukums}, Maksā: {self.cena_token}/token, Pieejamie līdzekļi: {self.pieejamie_lidzekli}"
            
    
CatGPT = LLMModelis("CatGPT 5", 9000, 35.6, 1000, 2.5)

CatGPT.aprekinatIzmaksas("Hallo pasaule!")

CatGPT.izvaditTekstu("Hallo pasaule!")

print(CatGPT)

print()
 
# 3. Uzd

class Genu_Tikls():
    Identifikators: str
    Nosaukums: str
    Geni: []
    Suga: str
    
    def __init__(self, identifikators, nosaukums, suga): #Šeit domāts, ka gēnus var pievienot vēlāk, pašlaik ir tukšs
        self.Identifikators = identifikators
        self.Nosaukums = nosaukums
        self.Suga = suga
        self.Geni = []
        
    def pievienotGenu(self, gens):
        self.Geni.append(gens)
        
    def __str__(self):
        for i in self.Geni:
            return f"{self.Identifikators}: {i}"

class Gens():
    Simbols: str
    Nosaukums: str
    Suga: str
    
    def __init__(self, simbols, nosaukums, suga):
        self.Simbols = simbols
        self.Nosaukums = nosaukums
        self.Suga = suga
        
    def __str__(self):
        pass
        
    
 #Gēniņi
g1 = Gens("ADRA1D", "adrenoceptor alpha 1D", "Homo sapiens")
g2 = Gens("RGS11", "regulator of G protein signaling 11", "Homo sapiens")
g3 = Gens("Wdr11", "WD repeat domain 11", "Mus musculus")
g4 = Gens("Ralgapa1", "Ral GTPase activating protein, alpha subunit 1", "Mus musculus")
 
p1 = Genu_Tikls("R-HSA-162582", "Signal Transduction", "Homo Sapiens")
p1.pievienotGenu(g1)
p1.pievienotGenu(g2)

p2 = Genu_Tikls("R-MMU-194315", "Signaling by Rho GTPases", "Mus musculus")
p2.pievienotGenu(g3)
p2.pievienotGenu(g4)

print(p1)
    