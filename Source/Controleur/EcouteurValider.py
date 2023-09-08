
import View
import Model
from Controleur import *

from PIL import Image

from tkinter import messagebox

class EcouteurValdier:

    def __init__(self,parametrageView : View.ParametrageView) -> None:
        self.parametrageView = parametrageView
        self.mainView  = parametrageView.master

    def OnAction(self,event):

        cheminImage = self.parametrageView.cheminVersImage.get()
        valeurAgrendissementX = self.parametrageView.sliderDimention.getValeur()
        valeurAgrendissementY = self.parametrageView.sliderDimention.getValeur()

        if cheminImage == "":
            messagebox.showerror(title="Erreur", message="Le chemin vers l'image n'est pas correcte")
            return

        image = Image.open(cheminImage)
        
        for numeroCaracter in range(len(cheminImage)):
            if cheminImage[numeroCaracter] in ("\\","/"):
                emplacementDernierSlach = numeroCaracter
            if cheminImage[numeroCaracter] == ".":
                emplacementDernierPoint = numeroCaracter

        
        nomFichier = cheminImage[emplacementDernierSlach+1:emplacementDernierPoint]
        extension = cheminImage[emplacementDernierPoint:]


        newView = View.EnregistrerView(self.mainView,image,nomFichier,extension,valeurAgrendissementX,valeurAgrendissementY) 

        newModel = Model.ModelEnregistrement(image,valeurAgrendissementX,valeurAgrendissementY)

        ecouteurModifier = EcouteurModifier(self.mainView)
        ecouteurEnregistrer = EcouteurEnregistrer(newView,newModel)
        ecouteurNouveau = EcouteurNouveau(self.mainView)
        ecouteurFermer = EcouteurFermer(self.mainView)

        newView.fixBoutons(ecouteurModifier.OnAction,ecouteurEnregistrer.OnAction,ecouteurNouveau.OnAction,ecouteurFermer.OnAction)
        
        self.mainView.goTo(newView)
