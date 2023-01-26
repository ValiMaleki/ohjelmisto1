import random
def noppa():
    return random.randint(1,6)

while True:
    x = noppa()
    print(x)
    if x == 6:
        break