# Arti Aasav
# Iseseisev töö
# Ülesanne 4

# 4.1

mitu = int(input("Mitu korda: "))
lause = input("Sinu reklaamlause: ")

def banner(l):
    print(l.upper())

for i in range(mitu):
    print(lause.upper())

# 4.2

def mahlapakkide_arv(ountekogus):
    mahlapakkidearv = int(round(ountekogus * 0.4/3))
    return mahlapakkidearv

kg = float(input("Õunte kogus: "))
print(mahlapakkide_arv(kg))









