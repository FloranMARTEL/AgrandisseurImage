from tkinter import *
from View import *


class MainView(Tk):

    def __init__(self):
        super().__init__()

        self.title("Agrandisseur Image")
        self.iconbitmap('assets/icon_X10.ico')
        self.resizable(width=False, height=False)


        self.page : Frame = ParametrageView(self)

        self.historiquePage : list[Frame] = [self.page]
        self.page.pack()


    
    def new(self):
        self.goBack()

        self.page.restart()
        

    
    def goTo(self,page : Frame):
        self.historiquePage.append(self.page)
        self.page.pack_forget()
        self.page = page
        self.page.pack()

    def goBack(self):
        self.page.pack_forget()
        self.page = self.historiquePage[-1]
        self.page.pack()
        del self.historiquePage[-1]

    



