
from View import ParametrageView

from tkinter import *
from tkinter.filedialog import askopenfilename

from Model.model import agrendire

class EcouteurSelectionImage():

    def __init__(self,EnregistrerView : ParametrageView):

        self.EnregistrerView : ParametrageView = EnregistrerView
    
    def onAction(self, event):

        cheminFichier = askopenfilename()

        self.EnregistrerView.cheminVersImage.insert(0, cheminFichier)

        self.EnregistrerView.modifierImageSelectioner(cheminFichier)

        

        