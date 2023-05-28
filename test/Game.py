from Carte import Carte
from Unite import Unite
from Unite import Mineur
from Unite import Bucheron
from Unite import Paysan
from Unite import GroupeUnite
from Outils import Outil
import json
class Game:
    def __init__(self):
        self.carte = Carte(5,10)
        self.inventory = []
        self.ressources = self.getressource()
        ressource,pourcentage = self.getrespour()
        self.carte.ajouter_ressources(ressource,pourcentage)
        self.metiers = self.getMetiers()
        self.outils = self.getOutil()
        # self.unite = Unite(self.carte, self.metiers, self.outils)
        # print("random : ", self.unite.metier)
        self.unite_Bucheron = Bucheron(self.carte, self.metiers, Outil(0, self.outils))
        self.unite_Mineur = Mineur(self.carte, self.metiers, Outil(1, self.outils))
        self.groupeUnite = GroupeUnite(0,0)
        self.groupeUnite.ajouterUnite(self.unite_Bucheron)
        self.groupeUnite.ajouterUnite(self.unite_Mineur)
    def draw(self):
        pass
        self.carte.afficher_unite(self.unite_Mineur)
    def update(self):
        self.unite_Mineur.seDeplacer(self.inventory, self.carte, self.ressources)
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
        
    def getOutil(self):
        with open('data.json') as json_file:
            data = json.load(json_file)
        return data["Outils"]