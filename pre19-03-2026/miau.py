#a = float(input("Ievadiet pirmo skaitli: "))
#b = float(input("Ievadiet otro skaitli: "))
#darb = input("Ievadiet darbību (+, -, *, /): ")
#
#if darb == "+":
#    print("(+) ", (a + b))
#elif darb == "-":
#    print("(-) ", (a - b))
#elif darb == "*":
#    print("(*) ", (a * b))
#elif darb == "/":
#    print("(/) ", (a / b))
#else:
#    print("Nepareizi ievadīta darbība..")
#

sarakst = [0, 2, 4, 5, 9]
reizsaraksts = []
lensarakst = len(sarakst)-2
#for i in sarakst:
#    reizsaraksts.append(i * 2)
#print(reizsaraksts)

while len(sarakst) > lensarakst:
    sarakst.pop(0)
print(sarakst[0])