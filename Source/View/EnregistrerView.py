from tkinter import *

from PIL import Image, ImageTk


class EnregistrerView(Frame):

    def __init__(self,master, image,nomfichier,nomExtension,AgrendisementX,AgrendisementY):
        super().__init__(master)

        #image
        coter = image.size
        if coter[0] > coter[1]:
            cotermax = coter[0]
        else:
            cotermax = coter[1]

        ratio = 350//cotermax
        image = image.resize((coter[0]*ratio, coter[1]*ratio),Image.NEAREST)
        imgtk = ImageTk.PhotoImage(image)
        image = Label(self,image=imgtk,width=350,height=350, borderwidth=2, relief="solid")
        image.image = imgtk
        

        #FrameNom
        frameNom = Frame(self)

        textnom = Label(frameNom,text="Nom :")

        self.valeur = StringVar()

        if AgrendisementY == AgrendisementX:
            textRadio1 :str = (nomfichier+"_X"+str(AgrendisementX)+nomExtension)
            self.radioTextmult = Radiobutton(frameNom,text=textRadio1, variable=self.valeur,value=textRadio1)


        textRadio2 :str = (nomfichier+"_"+str(AgrendisementX*coter[0])+"x"+str(AgrendisementY*coter[1])+nomExtension)
        self.radioTextdimention = Radiobutton(frameNom,text=textRadio2,variable=self.valeur ,value=textRadio2)

        #radio button Autre (quand choisie le text Autre devient un Entry)

        textnom.grid(row=0,column=0,columnspan=2,sticky=W)
        self.radioTextmult.grid(row=1,column=0)
        self.radioTextdimention.grid(row=1,column=1)

        #frameButon
        frameBouton = Frame(self)

        self.boutonModifier =       Button(frameBouton,text="Modifier")
        self.boutonEnregistrer =    Button(frameBouton,text="Enregistrer")
        self.boutonNouveau =        Button(frameBouton,text="Nouveau")
        self.boutonFermer =         Button(frameBouton,text="Fermer")

        self.boutonModifier.grid(row=0,column=0)
        self.boutonEnregistrer.grid(row=0,column=1)
        self.boutonNouveau.grid(row=0,column=2)
        self.boutonFermer.grid(row=0,column=3)

        image.grid(row=0,column=0)
        frameNom.grid(row=1,column=0)
        frameBouton.grid(row=2,column=0)


    def fixBoutons(self,fonctionModifier,fonctionEnregistrer,fonctionNouveau,fonctionFermer):
        self.boutonModifier.bind("<Button-1>",fonctionModifier)
        self.boutonEnregistrer.bind("<Button-1>",fonctionEnregistrer)
        self.boutonNouveau.bind("<Button-1>",fonctionNouveau)
        self.boutonFermer.bind("<Button-1>",fonctionFermer)
    

    def getNomFichier(self):
        return self.valeur.get()

    

#https://waytolearnx.com/2020/07/radiobutton-tkinter-python-3.html
        
        

