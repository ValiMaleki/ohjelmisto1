import math
import random

while True:

    luku = random.randint(1,10)
   # print(f'kone {luku}')
    luku1 = int(input("Arvaa luku: "))
    if luku1 == luku:
        print("Luku on oikein")
        break
    elif luku1 < luku:
        print("Liian pieni arvaus ")
    else:
        print("Liian suuri arvaus ")