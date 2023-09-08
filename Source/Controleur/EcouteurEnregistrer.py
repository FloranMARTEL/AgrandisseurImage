
import View
import Model

from tkinter.filedialog import askdirectory

from tkinter import messagebox


class EcouteurEnregistrer():

    def __init__(self,view: View.EnregistrerView,model : Model.ModelEnregistrement) -> None:
        
        self.view = view
        self.model = model
    

    def OnAction(self, event):

        destination = askdirectory()
        if destination != "":
            nomFichier = self.view.getNomFichier()

            if nomFichier == "":
                messagebox.showerror(title="Erreur", message="vous n'avez pas choisie de nom")
            else:
                self.model.sauvgarder(destination,nomFichier)
                messagebox.showinfo(title="Succès", message="l'image a bien été enregistrer")
