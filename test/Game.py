from Carte import Carte
from Unite import Unite
from Unite import Mineur
from Unite import Bucheron
from Unite import Paysan
from Unite import GroupeUnite
import json
class Game:
    def __init__(self):
        self.carte = Carte(5,10)
        self.inventory = []
        self.ressources = self.getressource()
        ressource,pourcentage = self.getrespour()
        self.carte.ajouter_ressources(ressource,pourcentage)
        self.metiers = self.getMetiers()
        self.unite = Unite(self.carte, self.metiers)
        print("random : ", self.unite.metier)
        self.unite_Mineur = Mineur(self.carte, self.metiers)
        print( "mineur :" ,self.unite_Mineur.metier)
        self.groupeUnite = GroupeUnite(0,0)
        self.groupeUnite.ajouterUnite(self.unite)
        self.groupeUnite.ajouterUnite(self.unite_Mineur)
    def draw(self):
        self.carte.afficher_unite(self.unite)
    def update(self):
        self.unite.seDeplacer(self.inventory, self.carte, self.ressources)
        return False
    # recuperer les ressources dans le json
    def getressource(self):
        with open('data.json') as json_file:
            data = json.load(json_file)
        return data["Ressource"]
    # recuperer les ressources et les pourcentages
    def getrespour(self):
        pourc = []
        nomenclature = []
        for result in self.ressources:
            nomenclature.append(result["nomenclature"])
            pourc.append(result["pourcentage"])
        return nomenclature,pourc
    
    def getMetiers(self):
        with open('data.json') as json_file:
            data = json.load(json_file)
        return data["Metiers"]
        