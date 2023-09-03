from tkinter import *

import View

class BindingSlider():

    def __init__(self,EnregistrerView : View.ParametrageView ,slider: View.Slider) -> None:

        self.EnregistrerView : View.ParametrageView = EnregistrerView
        self.slider : View.Slider = slider
        
    
    def OnAction(self,event: Event):


        try:
            valeur = int(event.widget.get())

            if valeur >= 1 and valeur <= 100:
                self.slider.setValeur(valeur)
                self.EnregistrerView.modifierImageAgrendissement(self.EnregistrerView.cheminVersImage.get(),valeur,valeur)
        except:
            pass

