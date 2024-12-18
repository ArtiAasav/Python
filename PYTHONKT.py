# Arti Aasav
# 18.12.2024
# Ülesanne 3,4,9,11,17

import itertools

# 3. Positiivsed ja negatiivsed
# tee kaks loendit positiivsete ja negatiivsete arvude hoidmiseks
# kasutaja sisestab 5 arvu ja programm tuvastab, kumba loendisse selle lisab
# nulli lisamisel ei tehta midagi
# väljasta mõlemad loendit

# pos = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# neg = [-1, -1, -2, -3, -5, -8, -13, -21, -34, -55, -89]
# a = int(input("Sisesta loendites olev arv: "))
# if (a) > 0:
#     pos.append(a)
#     print(pos)
# # lisab positiivse arvu pos loendisse
# elif (a) < 0:
#     neg.append(a)
#     print(neg)
# # lisab negatiivse arvu neg loendisse
# elif (a) == 0:
#     pass
# # ei tee midagi

# 4. List Less Than Ten
# Take a list and write a program that prints out all the elements of the list that are less than 5.
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
# Write this in one line of Python.
# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], b = [i for i in a if i < 5]
b = []
for i in (a):
    if i < 5: 
        b.append(a[i])
print(b)








