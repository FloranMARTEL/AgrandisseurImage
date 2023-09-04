
from View import MainView

class EcouteurModifier():

    def __init__(self,view : MainView) -> None:        
        self.view = view
    

    def OnAction(self, event):
        self.view.goBack()
