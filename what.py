n = int(input("Input number to squareroot"))
i=0

while True:
    if n != round(i*i):
        i += 0.000001
    else:
        break

print(i, "is the squareroot of it")
