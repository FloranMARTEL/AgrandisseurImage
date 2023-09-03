
import View

class EcouteurValdier:

    def __init__(self,parametrageView : View.ParametrageView) -> None:
        self.mainView  = parametrageView.master

    def OnAction(self,event):
        print("valider")
