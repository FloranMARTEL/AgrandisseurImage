from tkinter import *
from View import *


class MainView(Tk):

    def __init__(self):
        super().__init__()

        self.title("Agrendisseur Image")
        self.iconbitmap('Source\\assets\\icon_X10.ico')
        self.resizable(width=False, height=False)


        self.page : Frame = ParametrageView(self)

        self.historiquePage : list[Frame] = [self.page]
        self.page.pack()

        #self.update()
        #print(self.winfo_width(),self.winfo_height())

    
    def new(self):
        self.goBack()
        for w in self.page.winfo_children():
            w.destroy()
        
        self.page.make()
        
        #self.page.pack()

    
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

    



