
from  View import MainView

class EcouteurFermer():

    def __init__(self,view: MainView ) -> None:
        
        self.view = view
    

    def OnAction(self, event):
        self.view.quit()