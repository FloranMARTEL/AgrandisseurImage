
from View.MainView import MainView

class EcouteurNouveau():

    def __init__(self,view : MainView) -> None:
        
        self.view = view
    

    def OnAction(self, event):
        self.view.quit()

        newvue = MainView()        
        newvue.mainloop()