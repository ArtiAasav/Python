# Arti Aasav
# 08.01.2025
# Ülesanne 21

import os
from PIL import Image, ImageOps


# Kontrolli, kas thumb kataloog on olemas, kui ei ole, siis loo see
thumb_dir = "img_thumb"
if not os.path.exists(thumb_dir):
    os.makedirs(thumb_dir)

kataloog = os.getcwd()+"\yl_pildid\yl_pildid"
for i in os.listdir(kataloog):
    if i.lower().endswith(".jpg"):
        img_path = os.path.join(kataloog, i)
        img = Image.open(kataloog+"/"+i)
        with img:
            # Pildi suuruse muutmine
            img = img.resize((350, 350))
            # Pildi pööramine
            img = img.rotate(90)
            # Värvisügavuse muutmine
            img = img.convert('1')

            thumb_path = os.path.join("img_thumb", i)  # Muuda tee, kus soovid pilti salvestada
            img.save(thumb_path, "JPEG")






