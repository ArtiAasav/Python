# Arti Aasav
# Iseseisev töö
# Ülesanne 3

fail = open ("rebased.txt", encoding='UTF-8')

vastuvoetud = []

for rida in fail:
    vastuvoetud.append(int(rida))
print(vastuvoetud)
fail.close()

a = input("Palun sisetage, millise aasta andmeid vajate?: ")

print(vastuvoetud[int(a[3])-1])












