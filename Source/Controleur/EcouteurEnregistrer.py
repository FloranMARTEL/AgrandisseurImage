
import View
import Model

from tkinter.filedialog import askdirectory


class EcouteurEnregistrer():

    def __init__(self,view: View.EnregistrerView,model : Model.ModelEnregistrement) -> None:
        
        self.view = view
        self.model = model
    

    def OnAction(self, event):

        #        tkFileDialog.askdirectory(initialdir="/",title='Choisissez un repertoire')

        destination = askdirectory()
        nomFichier = self.view.getNomFichier()
        
        self.model.sauvgarder(destination,nomFichier)