# Arti Aasav
# 18.12.2024
# Ülesanne 3,4,9,11,17

import itertools

# 3. Positiivsed ja negatiivsed
# tee kaks loendit positiivsete ja negatiivsete arvude hoidmiseks
# kasutaja sisestab 5 arvu ja programm tuvastab, kumba loendisse selle lisab
# nulli lisamisel ei tehta midagi
# väljasta mõlemad loendit

pos = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
neg = [-1, -1, -2, -3, -5, -8, -13, -21, -34, -55, -89]
a = int(input("Sisesta loendites olev arv: "))
if (a) > 0:
    pos.append(a)
    print(pos)
# lisab positiivse arvu pos loendisse
elif (a) < 0:
    neg.append(a)
    print(neg)
# lisab negatiivse arvu neg loendisse
elif (a) == 0:
    pass
# ei tee midagi

# 4. List Less Than Ten
# Take a list and write a program that prints out all the elements of the list that are less than 5.
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
# Write this in one line of Python.
# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]; b = [i for i in a if i < 5]; print(b)
# a on list, b on uus list, kuhu tulevad kõik numbrid mis on väiksemad kui 5


# 11. Salakeel
# sinu programm kÃ¼sib kasutajalt, kas ta soovib salakeelt luua vÃµi tÃµlkida - 1p
# kasutaja sisestab tavalise sÃµna, mis muudetakse salakeeleks - 1p
# kasutaja sisestab salakeeles sÃµna, mis teisendatakse jÃ¤lle normaalseks - 1p
# kood kommenteeritud - 1p

# küsib kasutajalt kas ta tahab salakeelt luua või tõlkida
salakeel_tegemine = (input("1 = salakeele loomine, 2 = salakeele tõlkimine: "))

# Kui 1 siis loob salakeele
if salakeel_tegemine == "1":
    # sisesta mis sõna tahad
    Salakeel = input("Sisesta sõna: ").lower()
    # vahetab ära tähed
    print(Salakeel.replace("a", "^").replace("o", "0").replace("i", "1").replace("e", "3").replace("u", "v"))

    # Kui 2 siis tõlgib salakeele
elif salakeel_tegemine == "2":
    # sisesta mis sõna tahad
    Salakeel = (input("Sisesta sõna: ")).lower()
    # vahetab ära tähed
    print(Salakeel.replace("^", "a").replace("0", "o").replace("1", "i").replace("3", "e").replace("v", "u"))

    #kui kasutaja valib midagi muud siis prindib et valik on vale
else:
    print("Vale valik!")

# 9. Emaili kontroll
# kasutaja lisab emaili kujul enimi.pnimi@server.com - 1p
# programm kontrollib kas email on sisestatud Ãµigesti - vÃ¤hemalt @-mÃ¤rgi kontroll - 1p
# programm tÃ¼keldab selle ja vÃ¤ljastab lause: â€˜Tere enimi, sinu email on server serveris ja domeeniks on sul comâ€™ - 1p
# kasutajalt kÃ¼situd kÃ¼simused on selgelt Ã¼heselt mÃµistetavad - 1p
# kood kommenteeritud - 1p

email = input("Sisesta email kujul enimi.pnimi@server.com: ")
if "@" in email:
    print("Tere, " + str(email.split("@")[0].split(".")[0].capitalize()) +","+" sinu email on server serveris ja domeeniks on sul com")





