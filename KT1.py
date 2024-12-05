# Arti Aasav
# Iseseisev töö
# Ülesanne 1

# 1.1
# print("Tere, maailm!")

# # 1.2

# aasta = 2020
# liblikas = "teelehe-mosaiikliblikas"
# lause_keskosa = "aasta liblikas on"
# lause = str(aasta) + " " + str(lause_keskosa) + " " + str(liblikas)
# print(lause)

# # 1.3

# pilv = float(input("Mis on pilvede aluse kõrgus (km): "))
# if pilv > 6.0:
#     print("Need on ülemised pilved")
# else:
#     print("Need ei ole ülemised pilved")

# 1.4

inimesed = int(input("Transporditavate inimeste arv: "))
bussi_kohad = int(input("Mis on bussi kohtade arv: "))

busside_arv = inimesed // bussi_kohad
viimane_buss = inimesed % bussi_kohad
if viimane_buss > 0:
    busside_arv +=1
else:
    viimane_buss = bussi_kohad
print(f"Vaja läheb {busside_arv} bussi, viimases bussis {viimane_buss}.")





