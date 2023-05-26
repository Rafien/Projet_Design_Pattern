from Carte import Carte
from Unite import Unite

carte = Carte()
unite = Unite()

def test_carte():
    carte.creer_carte()
    carte.afficher_carte()
    carte.ajouter_ressources()
    carte.afficher_carte()
    carte.case_avec_ressources(5,5)
    carte.type_ressource(5,5)

def test_unite():
    unite.isOnRessourcesRecuperables(carte)
    #unite.rammasserRessources()


test_carte()
test_unite()