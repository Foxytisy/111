#def reeziinaajums(*skaitli :tuple[int]):
#    sk=1
#    for i in skaitli:
#        sk=i*sk
#    return sk
#
#print(reeziinaajums(90, 10, 20, 4))

input = int(input("Ievadi skaitli: "))

def fakt(n :int):
    faktor = 1
    for i in range(n):
        faktor=(i+1)*faktor
    return faktor

print(fakt(input))

