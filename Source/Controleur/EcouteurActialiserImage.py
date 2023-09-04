
import View

from tkinter import *
from tkinter.filedialog import askopenfilename


from PIL import Image, ImageTk

class EcouteurActialiserImage():

    def __init__(self,EnregistrerView : View.ParametrageView):

        self.EnregistrerView : View.ParametrageView = EnregistrerView
    
    def onAction(self, event):

        cheminFichier = self.EnregistrerView.cheminVersImage.get()

        self.EnregistrerView.modifierImageSelectioner(cheminFichier)

        valeurAgrendisement = self.EnregistrerView.sliderDimention.getValeur()
        self.EnregistrerView.modifierImageAgrendissement(cheminFichier,valeurAgrendisement,valeurAgrendisement)

    

        

        