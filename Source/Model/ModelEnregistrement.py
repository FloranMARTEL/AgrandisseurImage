from PIL import Image

class ModelEnregistrement():

    def __init__(self,image:Image.Image,AgrendissementX,AgrendissementY) -> None:

        dimentionImage = image.size
        self.image = image.resize((dimentionImage[0]*AgrendissementX, dimentionImage[1]*AgrendissementY),Image.NEAREST)
        print(type(self.image))

    
    def sauvgarder(self,cheminDossier,NomFichier):
        
        destination = cheminDossier+"/"+NomFichier
        print(destination)
        self.image.save(destination)

    


        