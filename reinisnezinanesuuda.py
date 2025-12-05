import random

vardnica = {}
for iii in range (0,20):
    vardnica[iii] = random.randint(1, 1000)
    
for i in range(len(vardnica)):
    if i%2!=0:
        vardnica.pop(i)
print(vardnica)   
     
     
     
vardnica2 = {}
for iii in range (0,20):
    vardnica2[iii] = random.randint(1, 1000)   
  
for keyifesnuwfesonuwfesonuwfeoni, valueefnuifenuiwfeuiwfeui in list(vardnica2.items()):
    if valueefnuifenuiwfeuiwfeui % 2 == 0:
        vardnica2.pop(keyifesnuwfesonuwfesonuwfeoni)
#mim
print(vardnica2)