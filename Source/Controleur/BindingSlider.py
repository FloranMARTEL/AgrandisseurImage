from tkinter import *

import View

class BindingSlider():

    def __init__(self,slider: View.Slider) -> None:

        self.slider : View.Slider = slider
        
    
    def OnAction(self,event: Event):


        try:
            valeur = int(event.widget.get())

            if valeur >= 1 and valeur <= 100:
                self.slider.setValeur(valeur)
        except:
            pass

