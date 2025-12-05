import random

vardnica = {}
for iii in range (0,20):
    vardnica[iii] = random.randint(1, 1000)
    
for i in range(len(vardnica)):
    if i%2!=0:
        vardnica.pop(i)
print(vardnica)   
     
     
     
vardnica2 = {}
for iii in range (0,20):
    vardnica2[iii] = random.randint(1, 1000)   
  
for keyifesnuwfesonuwfesonuwfeoni, valueefnuifenuiwfeuiwfeui in list(vardnica2.items()):
    if valueefnuifenuiwfeuiwfeui % 2 == 0:
        vardnica2.pop(keyifesnuwfesonuwfesonuwfeoni)

print(vardnica2)

#i/ni darbs

vardn = {
    "V": 0,
    "VI": 0,
    "VII": 0,
    "VIII": 0,
    "X": 0,
    "XI": 0,
    "XII": 0
}

for key, sk in list(vardn.items()):
    for i in key:
        if i == "I":
            vardn[key] += 1
        elif i == "V":
            vardn[key] += 5
        elif i == "X":
            vardn[key] += 10
        else:
            print("Neatpazists romiešu whatever")
    
print(vardn)