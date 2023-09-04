import View

from Controleur import *

vue = View.MainView()

ecouteurBoutonSeletionerImage = EcouteurSelectionImage(vue.page)
ecouteurBoutonActualiserImage = EcouteurActialiserImage(vue.page)
ecouteurBoutonValider = EcouteurValdier(vue.page)
bindingSlidermult = BindingSlider(vue.page,vue.page.sliderDimention)

vue.page.fixButton(ecouteurBoutonSeletionerImage.onAction,ecouteurBoutonActualiserImage.onAction,ecouteurBoutonValider.OnAction)
vue.page.fixSlider(bindingSlidermult.OnAction)

vue.mainloop()