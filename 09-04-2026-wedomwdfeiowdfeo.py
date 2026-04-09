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