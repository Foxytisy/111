import datetime

date=""

with open("wow.txt", "a", encoding="UTF-8") as tagad:
    date=str(datetime.datetime.now())
    tagad.write(f"{date}\n")
    print(datetime.datetime.now())


isa=""

#with open("AAABBBB.txt", "r", encoding="UTF-8") as fails:
#    with open("kopija.txt", "w", encoding="UTF-8") as failsk: 
#        for line in fails: zsfgd for u in my assys
#            failsk.write(line)


vardnica = {
    "messageHtml": "<div>Laiks programmēt!</div>",
    "atslēga": "vērtība"
}

import json

print(json.dumps(vardnica, ensure_ascii=False))

lietotajs = {
    "lietotājvārds": "",
    "parole": ""
}

lietotajs["lietotājvārds"] = input("Lietotajvards: ")