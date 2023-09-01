from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

from View import *



class ParametrageView(Frame):

    def __init__(self,master):
        super().__init__(master)

        #FrameLeft
        frameLeft = Frame(self)

        image = Image.open("Source\\assets\imageAucunImage.png")

        img = ImageTk.PhotoImage(image)
 
        self.image = Label(frameLeft,image=img, width=350, height=350, borderwidth=2, relief="solid")
        self.image.image = img

        frameInputSelectionImage = Frame(frameLeft)

        self.BoutonSelectionImage = Button(frameInputSelectionImage,text="choisire une image")
        self.cheminVersImage = Entry(frameInputSelectionImage)
        self.boutonactualiserImage = Button(frameInputSelectionImage,text="🗘")

        #grid
        self.BoutonSelectionImage.grid(row=0,column=0)
        self.cheminVersImage.grid(row=0,column=1)
        self.boutonactualiserImage.grid(row=0,column=2)

        #grid
        self.image.grid(row=0,column=0)
        frameInputSelectionImage.grid(row=1,column=0)
        

        #FrameRight
        frameRight = Frame(self)

        frameSlider = Frame(frameRight,highlightbackground="Black", highlightthickness=2)
        
        
        self.sliderDimention = Slider(frameSlider,"mutliplicateur",100) #logaritmique
        self.BoutonPlusSlider = Button(frameSlider,text="Plus")

        #grid
        self.sliderDimention.grid(row=0,column=0)
        self.BoutonPlusSlider.grid(row=1,column=0,sticky=E)

        self.imageAgrendismenten = Canvas(frameRight,highlightbackground="Black", highlightthickness=2)

        self.BoutonValider = Button(frameRight,text="Valider")

        #grid
        frameSlider.grid(row=0,column=0,sticky=E)
        self.imageAgrendismenten.grid(row=1,column=0,sticky=E)
        self.BoutonValider.grid(row=2,column=0,sticky=E)

        #grid
        frameLeft.grid(row=0,column=0,sticky=S)
        frameRight.grid(row=0,column=1,sticky=S)


        
    
    def modifierImageSelectioner(self,cheminFichier):

        try:
            img = Image.open(cheminFichier)
        except:
            messagebox.showerror(title="Erreur", message="Le chemin vers l'image n'est pas correcte")
            return 
        
        

        imgl,imgh = img.size
        coterMax = imgl if imgl > imgh else imgh
        

        imageLongeurCoter = self.image.winfo_width()

        multiplicateur = (imageLongeurCoter-4)//coterMax

        resize_image = img.resize((imgl*multiplicateur, imgh*multiplicateur),Image.NEAREST)
        imgTK = ImageTk.PhotoImage(resize_image)
 
        self.image.configure(image=imgTK)
        self.image.image = imgTK


        

    
    def fixButton(self,fonctionSeletionnerImage,fonctionActualiserImage):
        self.BoutonSelectionImage.bind("<Button-1>",fonctionSeletionnerImage)
        self.boutonactualiserImage.bind("<Button-1>",fonctionActualiserImage)

    def fixSlider(self,fonctionSlidermutiplicateur):
        self.sliderDimention.fixSlider(fonctionSlidermutiplicateur)