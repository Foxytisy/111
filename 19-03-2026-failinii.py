import os

print(os.getcwd())
print(os.path.isfile(".\.\.\."))


print(os.path.isdir("\\ri.riga.lv\avg\Audzekni\mTreimanis3\My Documents\ProgMT\111\bhop-monke.gif"))

#os.path.exists() #pārbauda vai eksistē ceļš ig

pasreizejais_fails = __file__
print(pasreizejais_fails)

faila_mape = os.path.dirname(pasreizejais_fails)
print(faila_mape)

os.chdir(os.path.dirname(__file__))


import sys
print()
print(sys.argv[0]) #šis ne vienmēr dabūn pilno ceļu**
print(sys.argv[1]) #returns lietas, kas ir pēc palaišanas tie variables, piemēram, file.py --gato, iedos atpakaļ "--gato"