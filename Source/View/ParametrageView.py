from tkinter import *
from PIL import Image, ImageTk



class ParametrageView(Frame):

    def __init__(self,master):
        super().__init__(master)

        #FrameLeft
        frameLeft = Frame(self)

        image = Image.open("Source\\assets\imageAucunImage.png")
        #resize_image = image.resize((300, 100))
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
        
        self.valeurSlider = IntVar()
        self.sliderDimention = Scale(frameSlider,variable=self.valeurSlider,  from_=1, to=100,length=146,orient = HORIZONTAL) #logaritmique
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


        self.image.update()
        print(self.image.winfo_height()," :: ",self.image.winfo_width())
        

    
    def fixButton(self,fonctionSeletionnerImage):
        self.BoutonSelectionImage.bind('<Button-1>',fonctionSeletionnerImage)