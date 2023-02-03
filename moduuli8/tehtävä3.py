from geopy import distance
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
    sql = f"SELECT latitude_deg,name,longitude_deg FROM  airport WHERE ident = '{icao}'"
    #sql = "SELECT ident,name FROM municipality airport WHERE ident = %s ;"
    #kursori = yhteys.cursor(dictionary=True)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

icao1 = input('Anna lentoasaman icai-koodi: ')
kentat1 =hae_lentokentat_maasta(icao1)

if kentat1:
    kentat1_name= kentat1[0][1]
    kentat1_coord =(kentat1[0][0],kentat1[0][2])
    print(f"lentoaseman nimi {kentat1_name} ja siainti {kentat1_coord}")

    icao2 = input('Anna lentoasaman icai-koodi: ')
    kentat2 =hae_lentokentat_maasta(icao2)

    if kentat2:
        kentat2_name = kentat2[0][1]
        kentat2_coord = (kentat2[0][0], kentat2[0][2])

        print(f'asema 1 koorinaatit on {kentat1_coord}')
        print(f'asema 2 koorinaatit on {kentat2_coord}')
        print(f'lentoasemien {kentat1_name} ja {kentat2_name} vällinen etäisyys on {distance.distance(kentat1_coord,kentat2_coord).kilometers:5.0f} kilometriä')

    else:
        print(f'lentoasema koodilla {icao2} ei löydyy ')
else:
    print(f'lentoasema koodilla {icao1} ei löydyy ')


yhteys.close()
