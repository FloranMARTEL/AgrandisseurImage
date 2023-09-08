from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

from View import *



class ParametrageView(Frame):

    def __init__(self,master):
        super().__init__(master)
        self.make()

    def make(self):
        #FrameLeft
        frameLeft = Frame(self)

        image = Image.open("./assets/imageAucunImage.png")
        
        img = ImageTk.PhotoImage(image)

        longeurcoterImage = 400
        self.image = Label(frameLeft,image=img, width=longeurcoterImage, height=longeurcoterImage, borderwidth=2, relief="solid")
        self.image.image = img

        frameInputSelectionImage = Frame(frameLeft)

        self.BoutonSelectionImage = Button(frameInputSelectionImage,text="choisire une image")
        self.cheminVersImage = Entry(frameInputSelectionImage,width=40)
        self.boutonactualiserImage = Button(frameInputSelectionImage,text="🗘")

        #grid
        self.BoutonSelectionImage.grid(row=0,column=0)
        self.cheminVersImage.grid(row=0,column=1)
        self.boutonactualiserImage.grid(row=0,column=2)

        #grid
        self.image.grid(row=0,column=0,sticky=N)
        frameInputSelectionImage.grid(row=1,column=0,sticky=S)
        

        #FrameRight
        frameRight = Frame(self)

        frameSlider = Frame(frameRight,highlightbackground="Black", highlightthickness=2)
        
        
        self.sliderDimention = Slider(frameSlider,"mutliplicateur",300)
        self.BoutonPlusSlider = Button(frameSlider,text="Plus")

        #grid
        self.sliderDimention.grid(row=0,column=0)
        self.BoutonPlusSlider.grid(row=1,column=0,sticky=E)

        self.imageAgrendissement = Canvas(frameRight,height=300,width=300,highlightbackground="Black", highlightthickness=2)
        

        #grid
        frameSlider.grid(row=0,column=0,sticky=E,pady=(0,5))
        self.imageAgrendissement.grid(row=1,column=0,sticky=E)

        #Bouton Valider
        self.BoutonValider = Button(self,text="Valider",width=60)

        #grid
        frameLeft.grid(row=0,column=0,sticky=N,padx=5,pady=10)
        frameRight.grid(row=0,column=1,sticky=N,padx=5,pady=10)
        self.BoutonValider.grid(row=1,column=0,columnspan=2)


        
    
    def modifierImageSelectioner(self,cheminFichier):

        try:
            img = Image.open(cheminFichier)
        except:
            messagebox.showerror(title="Erreur", message="Le chemin vers l'image n'est pas correcte")
            return 
        
        

        imgl,imgh = img.size
        coterMax = imgl if imgl > imgh else imgh
        

        imageLongeurCoter = self.image.winfo_width()

        multiplicateur = (imageLongeurCoter-4)/coterMax

        resize_image = img.resize((int(imgl*multiplicateur), int(imgh*multiplicateur)),Image.NEAREST)
        imgTK = ImageTk.PhotoImage(resize_image)
 
        self.image.configure(image=imgTK)
        self.image.image = imgTK

    def modifierImageAgrendissement(self,cheminFichier,AgrendiementX,AgrendiementY):

        try:
            img = Image.open(cheminFichier)
        except:
            return
        
        dimentionImage = img.size
        dimentionImageAgrendi = (dimentionImage[0]*AgrendiementX,dimentionImage[1]*AgrendiementY)
        
        longeurCoterImageAgrensiement = (self.imageAgrendissement.winfo_width()-10)

        if dimentionImageAgrendi[0] > dimentionImageAgrendi[1]:
            dimentionImageMax = dimentionImageAgrendi[0]
        else:
            dimentionImageMax = dimentionImageAgrendi[1]
        
        rasio = longeurCoterImageAgrensiement/dimentionImageMax

        dimentionImageRectangleL = dimentionImage[0] * rasio
        dimentionImageRectangleH = dimentionImage[1] * rasio

        dimentionImageRectangleAL = dimentionImageAgrendi[0] * rasio
        dimentionImageRectangleAH = dimentionImageAgrendi[1] * rasio

        decalagex = (self.imageAgrendissement.winfo_width() - dimentionImageRectangleL) // 2
        decalagey = (self.imageAgrendissement.winfo_width() - dimentionImageRectangleH) // 2

        decalageAx = (self.imageAgrendissement.winfo_width() - dimentionImageRectangleAL) // 2
        decalageAy = (self.imageAgrendissement.winfo_width() - dimentionImageRectangleAH) // 2

        self.imageAgrendissement.delete("all")
        self.imageAgrendissement.create_rectangle((decalageAx,decalageAy),(decalageAx+dimentionImageRectangleAL,decalageAy+dimentionImageRectangleAH),outline="black")
        self.imageAgrendissement.create_rectangle((decalagex,decalagey),(decalagex+dimentionImageRectangleL,decalagey+dimentionImageRectangleH),outline="red")



    def fixButton(self,fonctionSeletionnerImage,fonctionActualiserImage,fonctionValider):
        self.BoutonSelectionImage.bind("<Button-1>",fonctionSeletionnerImage)
        self.boutonactualiserImage.bind("<Button-1>",fonctionActualiserImage)
        self.BoutonValider.bind("<Button-1>",fonctionValider)
        
        self.fonctionSeletionnerImage = fonctionSeletionnerImage
        self.fonctionActualiserImage = fonctionActualiserImage
        self.fonctionValider = fonctionValider
    

    def fixSlider(self,fonctionSlidermutiplicateur):
        self.sliderDimention.fixSlider(fonctionSlidermutiplicateur)
        self.fonctionSlidermutiplicateur = fonctionSlidermutiplicateur

    
    def getFonction(self):
        return self.fonctionSeletionnerImage,self.fonctionActualiserImage,self.fonctionValider,self.fonctionSlidermutiplicateur
    
    def restart(self):

        image = Image.open("./assets/imageAucunImage.png")
        
        img = ImageTk.PhotoImage(image)
        self.image.configure(image=img)
        self.image.image = img
        self.cheminVersImage.delete(0,"end")
        
        self.sliderDimention.setValeur(1)
        self.imageAgrendissement.delete("all")
