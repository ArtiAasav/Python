# Arti Aasav
# 15.01.2025
# Ülesanne 22

import locale
from datetime import datetime
import dateparser

# #22.1
# sp = datetime(2008, 7, 18)
# now = datetime.now()
# print(now)
# print(now.strftime("%d.%m %Y %H:%M:%S"))

# date2 = datetime(2024, 2, 15)

# # Arvuta nende kahe kuupäeva vahe
# vahe = now - sp

# print("Kuupäevade vahe päevades:", vahe.days)
# print("Kuupäevade vahe aastates:", int(vahe.days/365))
# if int(vahe.days/365)%5==0:
#     print("Juubel")
# else:
#     print("Ei ole juubel")


#22.2
import csv
now = datetime.now()
faili_nimi = 'rentals.csv'
kokku = 0
kliendid = []
vanused = []
mvordsed= 0
rendiajad = []
#Faili avamine ja lugemine

with open(faili_nimi, mode='r', encoding='utf-8') as fail:
    rentals = csv.reader(fail)
    pais = next(rentals)
    for rent in rentals:
        kokku+=1
        #vanused
        kp = rent[8].split("/")
        synna = datetime(int(kp[2]), int(kp[0]), int(kp[1]))
        vanus = int((now - synna).days/365)
        vanused.append(int(vanus))
        #unikaalsed ID
        if rent[7] not in  kliendid:
            kliendid.append(rent[7])
        #tagastamine
        if rent[2]!=rent[3]:
            mvordsed+=1
        #keskmine rentimise aeg
        ajavahe = datetime.strptime(rent[1],"%d/%m/%Y")-datetime.strptime(rent[0],"%d/%m/%Y")
        rendiajad.append(ajavahe.days)





print(f"Rentimisi kokku: {kokku}")
print(f"Kliente kokku: {len(kliendid)}")
print(f"Keskmine vanus: {sum(vanused)/len(vanused):0.1f}")
print(f"Risti-kontorite rentimise osakaal: {mvordsed/kokku*100}%")
print(f"Keskmine rendiaeg: {sum(rendiajad)/len(rendiajad):0.1f}")


