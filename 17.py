# Arti Aasav
# 28.11.2024
# Ülesanne 17

# Kirjuta Pythoni skript, mis loeb failist palgad.txt töötajate andmed ja arvutab eraldi
# meeste keskmised töötunnid, töötasu ning palk
# naiste keskmised töötunnid, töötasu ning palk

fail = open("palgad.txt")
read = fail.readlines()
print(read)
mpalgad = []
npalgad = []
palk = 500

for i in read:
    r = i.split(",")
    print(r[3])
    if r[3] == "Mees":
        mpalgad.append(float(r[6]))
    else:
        npalgad.append(float(r[6]))
print(mpalgad)








# Pangatehingud
# kogu tehingute arvu
# positiivsete tehingute arvu
# positiivsete tehingute kogusumma

fail = open("pangakonto.txt")
tekstiread = fail.readlines()
tehingute_arv = len(tekstiread)
pos_tehingud = 0
pos_tehingute_summa = 0

for i in tekstiread:
    if float(i.strip()) > 0:
        pos_tehingud+=1
        pos_tehingute_summa+=float(i)



print(f"Tehinguid kokku: {tehingute_arv}")
print(f"Pos tehinguid kokku: {pos_tehingud}")
print(f"Pos tehingute summa: {pos_tehingute_summa}")