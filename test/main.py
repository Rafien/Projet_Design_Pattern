from Carte import Carte


def test_carte():
    carte = Carte()
    carte.creer_carte()
    carte.afficher_carte()
    carte.ajouter_ressources()
    carte.afficher_carte()
    carte.lire_case(5,5)


test_carte()