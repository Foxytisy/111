n = float(input("Input number to squareroot"))
i=0

while True:
    if n > i*i:
        i += 0.000001
    else:
        break

print(i, "is the squareroot of it")

def sqrt(val: float):
    root = val / 2
    for _ in range(10):
        root = ((((root * root)-val)/(- (2 * root)))+root)

    return root

print(sqrt(n))