"""Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron,
 jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan
 (kevät, kesä, syksy, talvi). Tallenna ohjelmassasi kuukausia
 vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
  Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten,
   että joulukuu on ensimmäinen talvikuukausi."""

my_tuple=("kevät", "kesä", "syksy", "talvi")
kuukausi= int(input('anna kuukausi numerona! '))

if kuukausi == 12 or kuukausi == 1 or kuukausi == 2:
    print(my_tuple[3])
elif kuukausi == 3 or kuukausi == 4 or kuukausi == 5:
    print(my_tuple[0])
elif kuukausi == 6 or kuukausi == 7 or kuukausi == 8:
    print(my_tuple[1])
elif kuukausi == 9 or kuukausi == 10 or kuukausi == 11:
    print(my_tuple[2])


