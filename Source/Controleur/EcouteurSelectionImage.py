
from View import ParametrageView

from tkinter import *
from tkinter.filedialog import askopenfilename


class EcouteurSelectionImage():

    def __init__(self,EnregistrerView : ParametrageView):

        self.EnregistrerView : ParametrageView = EnregistrerView
    
    def onAction(self, event):

        cheminFichier = askopenfilename()

        self.EnregistrerView.cheminVersImage.delete(0,"end")
        self.EnregistrerView.cheminVersImage.insert(0, cheminFichier)

        self.EnregistrerView.modifierImageSelectioner(cheminFichier)

        valeurAgrendisement = self.EnregistrerView.sliderDimention.getValeur()
        self.EnregistrerView.modifierImageAgrendissement(cheminFichier,valeurAgrendisement,valeurAgrendisement)


        

        