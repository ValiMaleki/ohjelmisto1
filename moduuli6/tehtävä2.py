import random
nopanTahkot = int(input("Syötä nopan tahkojen määrä: "))
def noppa():
    return random.randint(1, nopanTahkot)
while True:
    x = noppa()
    print(x)
    if x == nopanTahkot:
        break