# Arti Aasav
# 28.11.2024
# Ülesanne 18

import csv

meeskonnad = {}
faili_nimi = 'EstonianBasketballGames.csv'
with open(faili_nimi, mode='r', encoding='utf-8') as fail:
    csv_lugeja = csv.DictReader(fail)
    for rida in csv_lugeja:
        mk = rida["Team 1"]
        mk2 = rida["Team 2"]
        #Tekitan nimekirja
        if mk not in meeskonnad:
            meeskonnad[mk] = 0
        if mk2 not in meeskonnad:
            meeskonnad[mk2] = 0
        #Lisan mitu korda mängis
        if mk in meeskonnad:
            meeskonnad[mk] += 1
        if mk2 in meeskonnad:
            meeskonnad[mk2] += 1
#Mitu meeskonda osales
print(f"Osales {len(meeskonnad)} meeskonda")

#Salvestan Excel CSVsse
faili_nimi = 'meeskonnad.csv'

with open(faili_nimi, 'w', encoding='utf-8') as csv_file:  
    writer = csv.writer(csv_file, delimiter=';', lineterminator='\n')
    for key, value in meeskonnad.items():
        writer.writerow([key, value])




