import math
def gallonat_litroina(gallonat):
    litrat = gallonat * 3.785412
    return litrat


while True:
    gallonat = float(input("Syötä bensiinin määrä gallonina: "))
    if gallonat < 0:
        break
    print("Bensiinin määrä litroina: ", ("%.2f" % gallonat_litroina(gallonat)))