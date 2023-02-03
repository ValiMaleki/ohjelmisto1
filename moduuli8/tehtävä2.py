import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='2020',
         autocommit=True
         )

def hae_lentokentat_maasta(maa):
    """sql = "SELECT type, count(*) FROM airport WHERE iso_country = '" + maakoodi + "' GROUP BY type"""
   # sql = f"SELECT name FROM airport WHERE iso_country = '{maa}'"
    sql = "SELECT type,count(*) FROM airport WHERE iso_country = %s GROUP BY type ;"
    kursori = yhteys.cursor()
    kursori.execute(sql,(maa,))
    tulos = kursori.fetchall()

    return tulos
maa = input('anna maakoodit')
kentat =hae_lentokentat_maasta(maa)

for rivi in kentat:
    print(f"lentäkenttätyypiä {rivi[0]} {rivi[1]}  kappaletta" )
