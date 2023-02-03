import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='2020',
         autocommit=True
         )

def hae_lentokentat_maasta(icao):

    sql = f"SELECT ident,name,municipality FROM  airport WHERE ident = '{icao}'"

    #sql = "SELECT ident,name FROM municipality airport WHERE ident = %s ;"
    #kursori = yhteys.cursor(dictionary=True)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()

    return tulos
icao = input('Anna lentoasaman icai-koodi: ')
kentat =hae_lentokentat_maasta(icao)

if kentat:
    print(kentat)
else:
    print(f'lentoasema koodilla {icao} ei löydyy ')

yhteys.close()

"""for rivi in kentat:
    print(rivi['name'])"""

