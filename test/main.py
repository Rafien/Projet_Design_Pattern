from Carte import Carte
from Unite import Unite

carte = Carte(5,10)
unite = Unite(carte)
inventaire = []

def test_carte():
    carte.ajouter_ressources()


test_carte()
carte.afficher_unite(unite)
# carte.afficher_carte()
unite.seDeplacer(inventaire, carte)
print(inventaire)