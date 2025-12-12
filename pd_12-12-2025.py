import random

# 1 Uzd
"""
def random_dict():
  dict1 = {}
  for iii in range(0,100):
    dict1.update({iii: random.randint(0, 1000)})
  return dict1

vardnica = random_dict()
#print(vardnica)

rezultats = 0

for a, b in vardnica.items():
    rezultats += a + b

rezultats/=len(vardnica)*2
print("Videjais aritmetiskais: ", rezultats)

# 2 Uzd

# Brends: Pieprasa telefona brenda tipu (String)
# Gads: Telefona pirkšanas gads (int)
# spelites: Vai telefonam ir spēlītes (bool)
# cena: Telefona cena (float)

telefoni = []

cik = int(input("Cik telefonus ievadisiet? "))

def jaunsTelefons(brends: str, gads: int, spelites: bool, cena: float):
    telefons = {
        "Brends": brends,
        "Gads": gads,
        "Spelites": spelites,
        "Cena": cena
    }
    return telefons

for i in range(cik):
    print(i+1, ". telefona dati:")
    brends = input("Ievadiet telefona brendu: ")
    gads = input("Ievadiet telefona pirkšanas gadu: ")
    spelites = bool(input("Norādiet vai telefonā ir spēlītes: (true/false)"))
    cena = float(input("Ievadiet telefona cenu: "))
    telefons = jaunsTelefons(brends, gads, spelites, cena)
    telefoni.append(telefons)

print(telefoni)

# IZDZĒST PĒC TAM
telefoni = [{"brends": "lol", "cena": 3}, {"brends": "lol2", "cena": 9}]

#3 Uzd



def pieejamieTal():
    for i in range(len(telefoni)):
        telefons = telefoni[i]
        print(i, ". telefons: ", end="")
        for vertiba in telefons.values():
            info = vertiba
            print(info, end=" ")
        print()
    
        
def dabutTelefon(a):
    return telefoni[a]

def izdzestTelefon(b):
    telefoni.pop(b)

def lietotajs():
    imp = int(input("Ko jus velaties darit? (1 - Izvadit pieejamos, 2 - Izvadit specifisku telefonu, 3 - Izdzest specifisku telefonu, 0 - Beigt darbu): "))
    if imp == 1:
        pieejamieTal()
        lietotajs()
    elif imp == 2:
        i = int(input("Kuru telefonu? "))
        print(dabutTelefon(i))
        lietotajs()
    elif imp == 3:
        i = int(input("Kuru telefonu? "))
        izdzestTelefon(i)
        lietotajs()

lietotajs()

#4 Uzd


def random_dict(): 
  dict1 = {}
  for iii in range(0,100):
    dict1.update({iii: random.randint(0, 1000)})
  return dict1
vardnica = random_dict()

cik = random.randint(0, len(vardnica))

for i in range(cik):
  key = random.choice(list(vardnica.keys()))
  vardnica.pop(key)

print(vardnica)
"""
# 5 Uzd

def compareText(text1: str, text2: str) -> str:
    if len(text1) != len(text2):
        return "nebūs :( errorr)"
    
    result = ""
    for i in range(len(text1)):
        if text1[i] != text2[i]:
            result += text2[i]
    
    return result

print(compareText("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"))
print(compareText("MĀJA", "KĀJA"))
print(compareText("ĪSS", "GARĀKS"))