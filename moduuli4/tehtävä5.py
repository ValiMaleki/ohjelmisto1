"""Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
 Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
  Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
   Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
   (Oikea käyttäjätunnus on python ja salasana rules)."""
kayttajatunnus = 'python'
paswd = 'rules'
i =1
while i <=5:
    nimi = input('anna käyttäjätunnus: ')
    if kayttajatunnus == nimi:
        salasana = input('anna salasana: ')
        if kayttajatunnus==nimi and salasana == paswd:

                print('Tervetuloa')
                break
        print('Pääsy evätty')

    i+=1

