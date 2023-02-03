"""Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka,
kunnes käyttäjä syöttää tyhjän merkkijonon.Kunkin nimen syöttämisen jälkeen
ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan,
syötettiinkö nimi ensimmäistä kertaa. Lopuksi ohjelma
luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä.
Käytä joukkotietorakennetta nimien tallentamiseen."""
names =set()
while True:
    name = input('Anna nimi: ')
    if name =='':
        break
    if name in names:
        print("Aiemmin syötetty")
    else:
        print("Uusi nimi")
        names.add(name)

print('nimet listassa:')
for i in names:
    print(i)



