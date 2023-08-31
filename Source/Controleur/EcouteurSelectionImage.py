
import View

from tkinter import *
from tkinter.filedialog import askopenfilename

from Model.model import agrendire

from PIL import Image, ImageTk

class EcouteurSelectionImage():

    def __init__(self,EnregistrerView : View.ParametrageView):

        self.EnregistrerView : View.ParametrageView = EnregistrerView
    
    def onAction(self, event):

        cheminFichier = askopenfilename()

        self.EnregistrerView.cheminVersImage.insert(0, cheminFichier)

        self.EnregistrerView.modifierImageSelectioner(cheminFichier)

        

        