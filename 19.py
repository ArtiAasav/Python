# Arti Aasav
# 07.01.2025
# Ülesanne 19

import json
# Faili avamine ja JSON-i laadimine
with open('haridustulemused.json', 'r', encoding='utf-8') as file:
    haridus_tulemused = json.load(file)

# Iga raamatu andmete väljastamine
klass10 = 0
klass11 = 0
klass12 = 0
for tulemused in haridus_tulemused:
    nimi = tulemused['nimi']
    klass = tulemused['klass']
    trennid = tulemused['tegevused']
    hinded = tulemused['hinded']
    if klass == "12":
        klass12 += 1
        # hinneteleht
        for k, v in hinded.items():
            print(k, v)
        #12. klassi õpilaste trennid
        trenn = ""
        for i in trennid:
            trenn += i
            trenn += ", "
        # Prindib õpilaste nimed ja trennid, kes õpivad 12. klassis
        print(f"{nimi}: {trenn}, {hinded}")

    if klass == "11":
        klass11 += 1
    if klass == "10":
        klass10 += 1

print(f"12. klassis õpib {klass12} õpilast, 11. klassis õpib {klass11} õpilast, 10. klassis õpib {klass10} õpilast.")