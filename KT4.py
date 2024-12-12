# Arti Aasav
# Iseseisev töö
# Ülesanne 4

# # 4.1

# mitu = int(input("Mitu korda: "))
# lause = input("Sinu reklaamlause: ")

# def banner(l):
#     print(l.upper())

# for i in range(mitu):
#     print(lause.upper())

# # 4.2

# def mahlapakkide_arv(ountekogus):
#     mahlapakkidearv = int(round(ountekogus * 0.4/3))
#     return mahlapakkidearv

# kg = float(input("Õunte kogus: "))
# print(mahlapakkide_arv(kg))

# # 4.3

# kylaliste_arv = int(input("Sisesta külaliste arv: "))
# def eelarve(kylaliste_arv):
#     kokku = kylaliste_arv * 10 + 55
#     return kokku
# print(f"Maksimum eelarve on {eelarve(kylaliste_arv)}")

# miin = int(input("Mitu inimest on tuleb: "))
# print(f"Miinimum eelarve on {eelarve(miin)}")

# # 4.4

# kylalised_arv = int(input("Palju külalisi: "))

# def tervitus(kylalised_arv):
#     for i in range(kylalised_arv):
#         print('Võõrustaja: "Tere!"')
#         print(f"Täna {i + 1}. kord tervitada, mõtiskleb võõrastaja")
#         print('Külaline: "Tere, suur tänu kutse eest!"')

# tervitus(kylalised_arv)

# 4.5


def pronksikarva_summa(nimi):
    pronksikarva_summa = 0
    fail = open(nimi, 'r+')
    read = fail.readlines()
    for i in read:
        if int(i) < 10:
            pronksikarva_summa += int(i)
    return pronksikarva_summa  
    
    
print(pronksikarva_summa("mündid.txt"))













