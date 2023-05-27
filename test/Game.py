from Carte import Carte
from Unite import Unite
import json
class Game:
    def __init__(self):
        self.carte = Carte(5,10)
        self.unite = Unite(self.carte)
        self.inventory = []
        self.ressources = self.getressource()
        ressource,pourcentage = self.getrespour()
        self.carte.ajouter_ressources(ressource,pourcentage)
        print(self.ressources)
    def draw(self):
        self.carte.afficher_unite(self.unite)
    def update(self):
        self.unite.seDeplacer(self.inventory, self.carte)
        return False
    def getressource(self):
        with open('data.json') as json_file:
            data = json.load(json_file)
        return data["Ressource"]
    def getrespour(self):
        pourc = []
        nomenclature = []
        for result in self.ressources:
            nomenclature.append(result["nomenclature"])
            pourc.append(result["pourcentage"])
        return nomenclature,pourc