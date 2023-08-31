from PIL import Image, ImageTk

from tqdm import tqdm


def agrendire(img ,multiplicateur : int):

    #img = Image.open("sdqsdqs")
    multiplicateur = int(multiplicateur)
    
    (longeur,hauter) = img.size
    modeimg = img.mode

    if multiplicateur == 1:
        return img
    
    nouvelleImage = Image.new(mode=modeimg, size=(longeur*multiplicateur, hauter*multiplicateur))
    for l in tqdm(range(longeur)):
        for h in range(hauter):
            couleurPixel = img.getpixel((l,h))
            for ml in range(multiplicateur):
                for mh in range(multiplicateur):
                    nouvelleImage.putpixel((l*multiplicateur+ml,h*multiplicateur+mh), couleurPixel)
    

    return nouvelleImage



                



