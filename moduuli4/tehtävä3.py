
lista = []
while True:
    luku = input("Syötä luku: ")
    if luku == "":
        break
    lista.append(float(luku))
    print(luku)
print("Pienin luku: " + str(min(lista)))
print("Suurin luku: " + str(max(lista)))
