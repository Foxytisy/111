vardnica = {
    0:"viens",
    2:"divi",
    "atslēga": "vērtība"
}

#piekļūšana
print(vardnica["atslēga"])
print(vardnica.keys())
print(vardnica.values())
print(vardnica.items())
#for key in value in vardnica

#items():
#   print(key, value)


#pievienošana / atjaunināšana
vardnica.update({"jauna atsl":"jauna vērt"})
vardnica["neeksistējoša atslēga"] = "???"
print(vardnica)

#dzēšana no vārdnīcas - izdzēš vērtību ar atbilstošo atslēgu
vardnica.pop("neeksistējoša atslēga")
vardnica.pop("jauna atsl1")
del vardnica["jauna atsl2"]
print(vardnica)


#I UZD
import random
vardnica = {}
for iii in range(0, 20):
    vardnica[iii] = random.randint(1, 1000)

#DZĒŠ NEPĀRA

for iii in list(vardnica.keys()):
    if iii % 2 != 0:
        vardnica.pop(iii)
print(vardnica)

#DZĒŠ PĀRA

for iii in list(vardnica.keys()):
    if iii % 2 == 0:
        vardnica.pop(iii)
print(vardnica)


#II UZD         Jālabo, jāieliek atb vārdnīca
import random
dict1 = {}
for i in range(0, 20):
    dict1[i] = random.randint(0, 1000)
print(dict1)

#DZĒŠ <500 
for i in list(dict1.keys()):
    if dict1[i] < 501 :
        dict1.pop(i)
print(dict1)


#III %UZD
atbilde ={}
vardn = {
    "V":0,
    "VI":0,
    "VII":0,
    "VIII":0,
    "X":0,
    "XI":0,
    "XII":0,
}

for i in list(vardn.keys()):
    vērt=0
    for burti in i :
        if burti == "V":
            vērt+=5
        elif burti == "I":
            vērt+=1
        elif burti == "X":
            vērt+=10
    atbilde.update({i:vērt})
print(atbilde)