import os
os.chdir(os.path.dirname(__file__))

#fails = open() #nevajadzetu lietot, jo blokeeeeee
#fails.close()

#open funkcijas parametri:
# 1. Faila nosaukums
# 2. Faila atvēršanas režīms
# (r - read; w - write (pilnībā pārraksta); a - append faila beigās; read+append - r+ (pārraksta failu); write+append - w+ (nepārraksta failu))
# (b - bināri (wb - write binary un welcome back :-))
# 3. Faila kodējums (encoding) UTF-8
saturs = ""

#with open("fails.ignored", "r", encoding="UTF-8") as nosaukums:
#    fails.write("vkvkv\n")
#    fails.writelines(["aassada\n", "wowie\n"])
#    for ii in saraksts:
#        fails.write(ii+"\n")
#        
#    for line in fails:
#        print(line.strip())
#        saturs += line
#    print(saturs)
#    print(nosaukums.read(3)) #iet kā iet 
#    nosaukums.seek(0, 0) #faila sākums
#    print("Fails atvērts")
#print("Fails aizvērts")


#uzd
with open("wow.txt", "w", encoding="UTF-8") as fails:
    ievade = input("Ievadīt: ")
    fails.write(ievade)
