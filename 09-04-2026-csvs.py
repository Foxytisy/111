import csv

# csv - komats
# tsv - tabultor

with open ("fails.csv", "r", encoding="UTF-8") as faila_mainigais:
    rindas = []
    #1
    for rinda in faila_mainigais:
        rindas.append(rinda.strip().split(","))
    print(rindas)
    
    faila_mainigais.seek(0)
    #2
    #atsauce uz failu, delimiter - atdalīšanas simbols, quotechar - citātu lietiņa idk
    csv_reader = csv.reader(faila_mainigais, delimiter=",", quotechar="\"")
    next(faila_mainigais) #izlaiž pirmo rindu, laikam
    for line in csv_reader:
        print(line)