import math
import random

print("1.Uzd")

vertejums = int(input("Ievadi vērtējumu no 1% līdz 100%: "))

if vertejums < 60 and vertejums >= 0:
    print("F")
elif vertejums >= 60 and vertejums <= 62:
    print("D-")
elif vertejums >= 63 and vertejums <= 65:
    print("D")
elif vertejums >= 66 and vertejums <= 69:
    print("D+")
elif vertejums >= 70 and vertejums <= 72:
    print("C-")
elif vertejums >= 73 and vertejums <= 75:
    print("C")
elif vertejums >= 76 and vertejums <= 79:
    print("C+")
elif vertejums >= 80 and vertejums <= 82:
    print("B-")
elif vertejums >= 83 and vertejums <= 85:
    print("B")
elif vertejums >= 86 and vertejums <= 89:
    print("B+")
elif vertejums >= 90 and vertejums <= 93:
    print("A-")
elif vertejums >= 94 and vertejums <= 100:
    print("A")

print()
print("2.uzd")
print()

ievade = []
kvievade = []

for i in range(5):
    ievadesk = float(input("Ievadi skaitli: "))
    ievade.append(ievadesk)
    kvievade.append(math.sqrt(ievadesk))

print("Izvade: ", ievade)
print("Kvadrātsaknes: ", kvievade)

print()
print("3.uzd")
print()

teksts = input("Ievadi tekstu: ")
print(teksts)

for i in teksts:
    if i.isdigit():
        print(i, end="")

print()
print("4. uzd")
print()

temp = float(input("Ievadi doto temperatūru: "))
mervieniba = input("Ievadi doto temperatūras mērvienību (C/F): ")

if mervieniba.upper() == "C":
    jaunatemp = (temp * (9/5)) + 32
    print(jaunatemp, "°F")
elif mervieniba.upper() == "F":
    jaunatemp = (temp - 32) * (5/9)
    print(jaunatemp, "°C")
else:
    print("Nepareizi ievadīta mērvienība..")

print()
print("5. uzd")
print()

n = int(input("Cik n nejaušu skaitļu? "))
nejausieSkaitli = []
paraSk = 0
neparaSk = 0

for i in range(n):
    x = random.randint(1,100)
    nejausieSkaitli.append(x)
    if x % 2 == 0:
        paraSk += 1
    else:
        neparaSk += 1

        
print(nejausieSkaitli)
print("Pāra skaitļi: ", paraSk)
print("Nepāra skaitļi: ", neparaSk) 