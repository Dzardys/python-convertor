from PIL import Image
import os
import os.path

def start():
    loadpath = input('Zadejte cestu k souboru: ')
    isFile = os.path.isfile(loadpath)
    if isFile == True:
        if loadpath.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp')):
            savepath = input("Zadejte cestu k uložení souboru bez formátu: ")
            suffix = input("Zadejte formát (jpg, png, jpeg, tiff, bmp): ")
            suffix = suffix.replace(" ", "")
            if suffix == "jpg" or suffix == "png" or suffix == "jpeg" or suffix == "tiff" or suffix == "bmp":
                im1 = Image.open(loadpath)
                rgb_im = im1.convert('RGB')
                save = savepath + "." + suffix
                rgb_im.save(save)
                print('Soubor úspěšně uložen jako ' + save + '.')
                quit()
            else:
                print('Nepodporovaný formát, zkuste to znovu.')
                quit()
    else:
        print('Zadali jste složku nebo neexistující soubor, zkuste to znovu.')
        quit()
start()
