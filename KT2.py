# Arti Aasav
# Iseseisev töö
# Ülesanne 2

# 2.1

äratus_arv = int(input("Mitu korda äratus heliseb: "))

for i in range(äratus_arv):
    print("Tõuse ja sära!")

# 2.2

porgandid = 0
ringi_number = 1

ringide_arv = int(input("Mitu ringi: "))
while ringi_number <= ringide_arv:
    if ringi_number % 2 == 0:
        porgandid += ringi_number
    ringi_number += 1

print(f"Porgandite koguarv on {porgandid}")





