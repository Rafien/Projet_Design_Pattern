from Carte import Carte
from Unite import Unite

carte = Carte()
unite = Unite(carte)
inventaire = []

def test_carte():
    carte.creer_carte()
    carte.ajouter_ressources()
    carte.case_avec_ressources(5,5)
    carte.type_ressource(5,5)

def test_unite():
    unite.rammasserRessources(inventaire, carte)


test_carte()
carte.afficher_unite(unite)
carte.afficher_carte()
test_unite()
carte.afficher_carte()