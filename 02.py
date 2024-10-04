from math import *

# Arti Aasav
# Harjutus 01
# 30.09.24

#Hüpotenuus **

a,b = 16,9
c = sqrt(a**2+b**2)
print("Hüpotenuus on:",c)
#Ajateisendus // %
aeg = int(input("Lisa aeg minutites: "))
h = aeg // 60
m = aeg % 60
print(h,":",m)

#Arvusüsteemid
arv = int(input("Lisa arv: "))
kahend = bin(arv)
kuust = hex(arv)
print("Sinu teisendused on: ",kahend,"ja",kuust)

#Kütusekulu arvutamine
l = int(input("Lisa tangitud liitrid: "))
km = int(input("Lisa läbitud kilomeetrid: "))
kytusekulu = l/(km/100)
print("Sinu kütusekulu on",kytusekulu)