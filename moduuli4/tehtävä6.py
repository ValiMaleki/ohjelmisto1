import random

n = int(input("Syötä arvottavien pisteiden määrä: "))

ympyran_sisalla = 0
for i in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        ympyran_sisalla += 1

pi = 4 * ympyran_sisalla / n
print("Piin likiarvo on:", pi)
