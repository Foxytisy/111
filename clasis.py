import webbrowser

# Mašīna
# Ieslēgts? Bool
# Ātrums? float

#Paatrinat()
#Bremzet()
#Ieslegt()

class Auto():
    ieslegts :bool
    atrums :float
    rusa :int

    def __init__(self):
        self.ieslegts = False
        self.atrums = 0.0
        self.rusa = 50

    def ieslegtizslegt(self):
        if self.ieslegts == False:
            self.ieslegts = True
            print("brummbrbrbbrbrbrb (Ieslēgts)")
        else:
            self.ieslegts = False
            print("bbrbrbrbrtrrrk... kachuk kachuk kachuk.. kachuk (Izslēgts)")

    def paatrinat(self, cikDaudz):
        if self.ieslegts == True:
            self.atrums += cikDaudz
            print("Tagadējais ātrums: ", self.atrums, "km/h!")
        else:
            print("Ieslēdz verķi!")

    def bremzet(self, cikDaudz):
        self.atrums -= cikDaudz
        print("Tagadējais ātrums: ", self.atrums, "km/h!")

    def tauret(self):
        print("BEEEEEEEP BEEEEEEEEEEEEEEP")

    def saruset(self):
        self.rusa += 1
        print("Rūsas līmenis tagad ir: ", self.rusa, "%")

    def ieslegtradio(self): #lol nevar izlegt
        webbrowser.open('https://youtu.be/7uuhh2uIJlE?si=15eaEy9oWStxGzWt')
    
    def stavoklis(self):
        print(self.atrums, "km/h")
        
        
beha = Auto()

while True:
    a = input("Ko Jus darisiet? (paatrinat/bremzet/ieslegtradio/saruset/tauret/ieslegtizslegt) ")

    if a == "paatrinat":
        b = float(input("Cik daudz? "))
        beha.paatrinat(b)
    elif a == "bremzet":
        b = float(input("Cik daudz? "))
        beha.bremzet(b)
    elif a == "ieslegtradio":
        beha.ieslegtradio()
    elif a == "ieslegtizslegt":
        beha.ieslegtizslegt()
    elif a == "tauret":
        beha.tauret()
    else:
        print("Nav tāda funkcija!")

