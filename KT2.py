# Arti Aasav
# Iseseisev töö
# Ülesanne 2

import random

# # 2.1

# äratus_arv = int(input("Mitu korda äratus heliseb: "))

# for i in range(äratus_arv):
#     print("Tõuse ja sära!")

# # 2.2

# porgandid = 0
# ringi_number = 1

# ringide_arv = int(input("Mitu ringi: "))
# while ringi_number <= ringide_arv:
#     if ringi_number % 2 == 0:
#         porgandid += ringi_number
#     ringi_number += 1

# print(f"Porgandite koguarv on {porgandid}")

# # 2.3

# taringute_arv = int(input("Mitu täringut: "))

# for i in range(taringute_arv):
#     taringud = random.randint(1,6)
#     print(taringud)

# 2.4

nisutera = 0
taisarv = int(input("Sisesta Täisarv: "))
if taisarv > 64:
    print("Nii palju ruute ei ole")

korda = taisarv
if korda >= 1:
    nisutera += 1
    korda -= 1

while korda >= 1:
    korda -= 1
    nisutera *= 2

print(f"Leiduri palutud arv {taisarv}. Ruudu eest: {nisutera}")

# 2.5

ounade_arv = 14
poialpoisse = 3
for i in range(poialpoisse):
    ounade_arv -= (random.randint(1,2))

print(f"lumivalgekesele jääb alles {ounade_arv} õuna.")



