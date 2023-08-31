
import View

from tkinter import *
from tkinter.filedialog import askopenfilename

from PIL import Image, ImageTk

class EcouteurSelectionImage():

    def __init__(self,EnregistrerView : View.ParametrageView):

        self.EnregistrerView : View.ParametrageView = EnregistrerView
    
    def onAction(self, event):

        cheminFichier = askopenfilename()

        self.EnregistrerView.cheminVersImage.insert(0, cheminFichier)

        image = Image.open(cheminFichier)
        resize_image = image.resize((100, 100))
        img = ImageTk.PhotoImage(resize_image)
 
        self.EnregistrerView.image.configure(image=img)
        self.EnregistrerView.image.image = img

        