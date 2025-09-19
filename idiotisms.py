
import time
i = 0
n = 50
ip = 0

while True:
    time.sleep(0.02)
    if i==n:
        bolb = True
    elif i == 0:
        bolb = False
    if i<n and bolb == False:
        i += 1
        print("."*i, end="")
        print("miau", end="")
        print("."*ip)
    elif i>0:
        i -= 1
        print("."*i, end="")
        print("miau", end="")
        print("."*ip)
    ip = n-i