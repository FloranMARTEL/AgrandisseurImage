from tkinter import *
from View import *

from Controleur import *

class MainView(Tk):

    def __init__(self):
        super().__init__()

        self.title("Agrendisseur Image")

        self.page : Frame = ParametrageView(self)

        ecouteurBoutonSeletionerImage = EcouteurSelectionImage(self.page)

        self.page.fixButton(ecouteurBoutonSeletionerImage.onAction)

        self.historiquePage : list[Frame] = [self.page]
        self.page.pack()

    
    def gotTo(self,page : Frame):
        self.historiquePage.append(self.page)
        self.page.pack_forget()
        self.page = page
        self.page.pack()

    def goBack(self):
        self.page.pack_forget()
        self.page = self.historiquePage[-1]
        self.page.pack()
        del self.historiquePage[-1]

    



