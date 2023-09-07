
from View.MainView import MainView
from Controleur import *

class EcouteurNouveau():

    def __init__(self,view : MainView) -> None:
        
        self.view = view
    

    def OnAction(self, event):
        f1, f2, f3,bi = self.view.historiquePage[0].getFonction()

        self.view.new()

        self.view.page.fixButton(f1, f2, f3)
        self.view.page.fixSlider(bi)

        