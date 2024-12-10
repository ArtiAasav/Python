# Arti Aasav
# Iseseisev töö
# Ülesanne 3

# 3.1
# fail = open ("rebased.txt", encoding='UTF-8')

# vastuvoetud = []

# for rida in fail:
#     vastuvoetud.append(int(rida))
# print(vastuvoetud)
# fail.close()

# a = input("Palun sisetage, millise aasta andmeid vajate?: ")

# print(vastuvoetud[int(a[3])-1])

# # 3.3

# fail = open ("konto.txt", encoding='UTF-8')

# for rida in fail:
#     if float(rida) > 0:
#         print(rida,end="")

# # 3.4

# valik = (input("Sisesta faili nimi: "))
# fail = open(valik)
# read = fail.readlines()
# mitmes = 1
# for i in read:
#     print(mitmes, i, end="")
#     mitmes+=1

# lugu = int(input("Sisesta loo number: "))
# fail = open(valik)
# read = fail.readlines()
# print(str("Mängiv lugu:"),read[lugu-1])

# 3.5
from datetime import *

fail = open("nimekiri.txt")
read = fail.readlines()
print(read[datetime.now().day-1])











