cypherStr = "..."
uncypherStr = ""
frequency = []

alphabet = ["a","ā", "b", "c", "č", "d", "e", "ē", "f", "g", "ģ", "h", "i", "ī", "j", "k", "ķ", "l", "ļ", "m", "n", "ņ", "o", "p", "r", "s", "š", "t", "u", "ū", "v", "z", "ž"]
alphabetOffset = []

#for a in alphabet:
#    cnt = 0
#    for i in cypherStr:
#        if str(a) == str(i):
#            cnt+=1
#    frequency.append([cnt, a])
#frequency.sort()
#for i in range(len(frequency)):
#    print(frequency[i])
#
#
#
#
#for i in range(33):
#    #i = -i #Ja ir šifrēts alfabēts no gala uz sākumu + ar atkāpi
#    print(i, ". pārbīde")
#    for c in range(len(alphabet)):
#        if c+i < len(alphabet):
#            alphabetOffset.append(alphabet[c+i])
#        else:
#            alphabetOffset.append(alphabet[c-33+i])
#    #print(alphabetOffset)
#
#    for ch in cypherStr:
#        if ch.isspace():
#            uncypherStr += chr(32)
#            continue
#        chVal = alphabet.index(ch)
#        uncypherStr += alphabetOffset[chVal]
#
#    print(uncypherStr)
#    check = input("Vai ir atšifrēts? ")
#    if check == 1:
#        print(uncypherStr)
#        break
#    else: 
#        uncypherStr = ""
#        alphabetOffset.clear()

replacedcypherStr = cypherStr

while True:
    known = input("Ievadi zināmo vārdu: ")
    knownCy = input("Ievadi zināmā vārda atbilstošo šifrēto vārdu: ")

    for i in range(len(known)):
        replacedcypherStr = replacedcypherStr.replace(knownCy[i], known[i])
    cypherStr = replacedcypherStr
    print(cypherStr)

    if int(input("Vai apstādināt? (1/0) ")) == 1:
        break