# Arti Aasav
# 08.01.2025
# Ülesanne 21

import os
from PIL import Image, ImageOps
Allow from all

img = Image.open("yl_pildid")
print(img)

# Kuvame pildi andmed
print("Pildi nimi:", img.filename)  # Näiteks 'turtle001.jpg'
print("Pildi formaat:", img.format)  # Näiteks JPEG, PNG
print("Pildi suurus (laius x kõrgus):", img.size)  # Näiteks (1920, 1080)
print("Värvirežiim:", img.mode)  # Näiteks 'RGB'

with img:
    # Pildi suuruse muutmine
    img = img.resize((350, 350))

    # Pildi pööramine
    img = img.rotate(90)  # Pööra pilti 90 kraadi vastupäeva

    # Värvisügavuse muutmine
    img = img.convert('1') # mustvalge pilt

    # Pildi salvestamine PNG formaadis
    output_path = 'yl_pildid'  # Muuda tee, kus soovid pilti salvestada
    img.save(output_path)

print("Pilt on edukalt töödeldud ja salvestatud!")
img.show()

with img:
    # Maksimaalne suurus, milleks pilti muuta
    max_suurus = (350, 350)  

     # Muuda pildi suurust, kui see on suurem kui max_size
    img.thumbnail(max_suurus)

    output_path = 'yl_pildid'
    img.save(output_path)


print("Pilt on edukalt töödeldud ja salvestatud!")
img.show()

with img:
    # Defineeritud suurus (1:1 suhe), näiteks 300x300 pikslit
    size = (300, 300)

    # Pildi kärpimine ja suuruse muutmine, keskendudes keskele
    ruut = ImageOps.fit(img, size, centering=(0.5, 0.5))

    # Töödeldud pildi salvestamine
    output_path = 'yl_pildid'
    ruut.save(output_path, format='JPEG')

print("Pilt on edukalt töödeldud ja salvestatud ruudu kujul!")
ruut.show()

def create_thumbnails(source_dir, thumb_dir, size=(300, 300)):
    # Kontrolli, kas thumb kataloog on olemas, kui ei ole, siis loo see
    if not os.path.exists(thumb_dir):
        os.makedirs(thumb_dir)

    # Kõikide JPG failide leidmine kataloogis
    for filename in os.listdir(source_dir):
        if filename.lower().endswith(".jpg"):
            img_path = os.path.join(source_dir, filename)
            img = Image.open(img_path)
           
            # Pisipildi loomine
            thumb_img = ImageOps.fit(img, size, centering=(0.5, 0.5))
            img.close()
           
            # Pisipildi salvestamine
            thumb_path = os.path.join(thumb_dir, filename)
            thumb_img.save(thumb_path, "JPEG")
           
            print(f"Pisipilt salvestatud: {thumb_path}")

# Kasuta funktsiooni
source_directory = 'img'
thumb_directory = 'img/thumb'
create_thumbnails(source_directory, thumb_directory)


