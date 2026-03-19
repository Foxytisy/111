#vāvnīcas

vardnica = {
    "Lietotajsvards": "Jānis",
    "Parole": "parole1",
    "Vecums": 18,
    "Registrācijas datums": "2025-01-01 10:00:00TGMT -2"
}

for i in vardnica:
    print(i, " - ", vardnica[i])

vardn = {
    0: 10,
    2: 34,
    3: 56,
    5: 67
}

def reizinat(num: int, vardin: dict):
    for i in vardin:
        vardin[i] *= num
    return vardin

print(reizinat(2, vardn))



n = int(input("Ievadi n: "))
vardninnin = {}

for i in range(n):
    vardninnin[i] = i**2

print(vardninnin)