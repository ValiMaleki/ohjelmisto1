def poista_parittomat_funktio(numbers):
    return [x for x in numbers if x % 2 == 0]
numerot = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Alkuperäinen lista: ", numerot)
print("Karsittu lista: ",poista_parittomat_funktio(numerot))