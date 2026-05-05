import os

with open ("loremipsum.txt", "r", encoding="UTF-8") as loremipsumtext:
    print("Teksta garums ir ", len(loremipsumtext.readline()))
    
    
A=0
B=0
C1=0
C2=0
C3=0
    
with open ("ini.txt", "r", encoding="ASCII") as darbibas:
    for line in darbibas:
        linija = line.strip()
        if linija[0] == "A":
            A=int(linija[3::])
        elif linija[0] == "B":
            B=int(linija[3::])
        elif linija[0] == "C":
            funk = linija[6:7:]
            if funk == "-":
                C1 = A-B
            elif funk == "/":
                C2 = A/B
            elif funk == "*":
                C3 = A*B
                
print(C1, C2, C3)

#print(os.path.isdir(".\\ignored")) pārbauda vai eksistē
#if not os.path.isdir(".\\ignored"):
#   os.mkdir("ignored")
#   os.makedirs("ignored/ignore232/igigg") izveido vairākas mapes
#else
#   print("mau") 

#for file in os.listdir("ignored"):
#    print(f"Dzēšam {file}")
#    os.remove("ignored\\"+file) #Faila dzēšana
    
#os.rmdir("ignored") # izdzēš mapi

import shutil
#shutil.rmtree("ignored")

if not os.path.exists("mape"):
    os.mkdir("mape")
for iii in range(1,101):
    with open(f"mape\\{iii}", "w", encoding="UTF-8"):
        pass
    
faili = os.listdir("mape")
for iii in range(0, len(faili), 3):
    os.remove(f"mape\\{faili(iii)}")
    
import random
faili = os.listdir("mape")
fails = random.choice(faili)
b = random.randint(0, 100)
with open(f"mape\\{fails}", "w", encoding="UTF-8") as failins:
    fails.write(str(b))
ievad = input(f"Ievadiet skaitli no faila {fails}")
if ievad == b:
    print("ok!!!")