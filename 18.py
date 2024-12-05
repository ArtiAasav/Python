# Arti Aasav
# 28.11.2024
# Ülesanne 18

import csv

meeskonnad = []
faili_nimi = 'EstonianBasketballGames.csv'
with open(faili_nimi, mode='r', encoding='utf-8') as fail:
    csv_lugeja = csv.reader(fail)
    for rida in csv_lugeja:
        #print(rida[1], rida[2]):
        if rida[1] not in meeskonnad and rida[1] != 'Team 1':
            meeskonnad.append(rida[1])

print(f"Meeskondade arv: {len(meeskonnad)}")
for i in meeskonnad:
    print(i)
    




