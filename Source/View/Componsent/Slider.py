from tkinter import *

#from Controleur import *

class Slider(Frame):

    def __init__(self,master,textTitre,length):
        super().__init__(master)

        titre = Label(self,text=textTitre)

        self.valeur = IntVar()

        self.slider = Scale(self,variable=self.valeur, from_=1, to=100,length=length,orient = HORIZONTAL)

        cmd = self.register(lambda s: not s or s.isdigit())
        self.entryValier = Entry(self,validate="key", vcmd=(cmd, "%P"), width=5)
        self.entryValier.insert(0,"1")

        titre.grid(row=0,column=0,columnspan=2)
        self.slider.grid(row=1,column=0,sticky=S)
        self.entryValier.grid(row=1,column=1,sticky=S)


    def getValeur(self):

        if self.valeur.get() == int(self.entryValier.get()):
            return self.valeur.get()
        else:
            print("c'est pas la même chose")
            return int(self.entryValier.get())
        

    def setValeur(self,valeur: int):

        self.valeur.set(value=valeur)
        self.entryValier.delete(0,"end")
        self.entryValier.insert(0,str(valeur))



    def fixSlider(self,fonction):
        self.slider.bind("<B1-Motion>",fonction)
        self.entryValier.bind("<FocusIn>",fonction)
        self.entryValier.bind("<Return>",fonction)

        