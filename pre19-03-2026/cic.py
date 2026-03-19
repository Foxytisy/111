import random
#for i in range(11):
#    if i != 4 and i != 6:
#        print(i)
#
#i=0
#while i!=11:
#    if i !=4 and i != 6:
#        print(i)
#    i+=1

#ievaditais_skaitlis=int(input("Ievadi skaitli, ko faktorializlwiezēt: "))
#faktorialis=1
#
#for i in range(ievaditais_skaitlis):
#    faktorialis *= i+1
#print(faktorialis)

#minamais_skaitlis=random.randint(1,100)
#
#while True:
#    minamais_skaitlis_ievade=int(input("Miniet skaitli no 1 līdz 100: "))
#    if minamais_skaitlis_ievade < minamais_skaitlis:
#        print("Par zemu")
#    elif minamais_skaitlis_ievade > minamais_skaitlis:
#        print("Par augstu")
#    else:
#        print("Uzminēts")
#        break
#

for i in range(1,100):
    if i%3==0 and i%5==0:
        print("AAABBB")
    elif i%3==0:
        print("AAA")
    elif i%5==0:
        print("BBB")
    else:
        print(i)