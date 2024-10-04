from math import *

# Arti Aasav
# Harjutus 01
# 30.09.24

# 3. Ümbermõõt
a,b,c = 5,8,3
P = a+b+c
print("Kolnurga ümbermõõt on:",P)

# 4. Toote hind
toode = 36.75
soodus = 0.4
Summa = (toode - (toode * soodus)) * 3
print("Kolme toote summa:",Summa)

# 5. Pitsa
sõbrad = 3
hind = 12.90
tipp = 0.1
maksmine = ((hind * tipp) + hind) / sõbrad
print("Iga sõber maksab:",maksmine)

# 6. Rulluisutajad 90km/h
kiirus = 29.9
aeg = 24/60
dist = kiirus * aeg
print("Rulluisutaja jõuabb:",dist,"km kaugusele")

# 7. Hüpotenuus **
a,b = 16,9
c = sqrt(a**2+b**2)
print("Hüpotenuus on:",c)

# 8. Ajateisendus // %
aeg = int(input("Lisa aeg minutites: "))
h = aeg // 60
m = aeg % 60
print(h,":",m)

# 9. Arvusüsteemid
arv = int(input("Lisa arv: "))
kahend = bin(arv)
kuust = hex(arv)
print("Sinu teisendused on: ",kahend,"ja",kuust)

# 10. Kütusekulu arvutamine
l = int(input("Lisa tangitud liitrid: "))
km = int(input("Lisa läbitud kilomeetrid: "))
kytusekulu = l/(km/100)
print("Sinu kütusekulu on",kytusekulu)