from Carte import Carte
from Unite import Unite
from Unite import Mineur
from Unite import Bucheron
from Unite import Paysan
from Unite import GroupeUnite
from Outils import Outil
from Inventory import inventory
import json
class Game:
    def __init__(self):
        self.tourDeJeu = 1
        #carte
        self.carte = Carte(5,10)
        
        
        #lire json
        self.data = self.getdata()
        self.ressources = self.data["Ressource"]
        self.metiers = self.data["Metiers"]

        self.outils = self.data["Outils"]
        self.inventory = inventory(self.ressources)
        self.inventory.addressources("B",-5)
        for x in self.inventory.inventory:
            print(x.quantity)
        #ressources

        ressource,pourcentage = self.getrespour()
        self.carte.ajouter_ressources(ressource,pourcentage)

        #gestion unite
        self.liste_unite = []
        self.id_unite = 1
        # self.unite = Unite(self.carte, self.metiers, self.outils)
        # print("random : ", self.unite.metier)
        

        #tests
        self.unite_Bucheron = Bucheron(self.carte, self.metiers, Outil(0, self.outils), self.id_unite)
        self.id_unite += 1
        self.liste_unite.append(self.unite_Bucheron)
        self.unite_Mineur = Mineur(self.carte, self.metiers, Outil(1, self.outils), self.id_unite)
        self.liste_unite.append(self.unite_Mineur)
        self.id_unite += 1
        self.groupeUnite = GroupeUnite(0,0)
        self.groupeUnite.ajouterUnite(self.unite_Bucheron)
        self.groupeUnite.ajouterUnite(self.unite_Mineur)

        
    #Premier affichage
    def draw(self):
        for unite in self.liste_unite:
            self.carte.afficher_unite(unite)
        # self.carte.verifPresenceUnite(self.unite_Bucheron.pos_unit_x, self.unite_Bucheron.pos_unit_y,self.ressources)
        # self.carte.verifPresenceUnite(self.unite_Mineur.pos_unit_x, self.unite_Mineur.pos_unit_y,self.ressources)

    #Tour de jeu
    def update(self):
        print("Tour de jeu : ", self.tourDeJeu)
        for unite in self.liste_unite:
            print(" vous deplacez l'unite : ", unite.id_unite , " de type : ", unite.metier)
            unite.seDeplacer(self.inventory, self.carte, self.ressources)
        #self.unite_Mineur.seDeplacer(self.inventory, self.carte, self.ressources)

        self.tourDeJeu += 1
        
        return False
    
    # recuperer les ressources dans le json
    def getdata(self):
        with open('data.json') as json_file:
            data = json.load(json_file)
        return data
    
    # recuperer les ressources et les pourcentages
    def getrespour(self):
        pourc = []
        nomenclature = []
        for result in self.ressources:
            nomenclature.append(result["nomenclature"])
            pourc.append(result["pourcentage"])
        return nomenclature,pourc
    