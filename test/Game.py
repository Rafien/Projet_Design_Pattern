from Carte import Carte
from Unite import *
from Outils import Outil
from Inventory import inventory
from Batiment import *
import json

TAILLE_MIN_MAP = 5
TAILLE_MAX_MAP = 10
NOURRITURE_AT_SPAWN = 10

class Game:
    def __init__(self):
        self.tourDeJeu = 1
        #carte
        self.carte = Carte(TAILLE_MIN_MAP,TAILLE_MAX_MAP)
        self.taille = (self.carte.axe_x,self.carte.axe_y)
        
        #lire json
        self.data = self.getdata()
        self.ressources = self.data["Ressource"]
        self.metiers = self.data["Metiers"]

        self.outils = self.data["Outils"]
        self.inventory = inventory(self.ressources)
        self.inventory.addressources("N",NOURRITURE_AT_SPAWN)
        
        #ressources

        ressource,pourcentage = self.getrespour()
        self.carte.ajouter_ressources(ressource,pourcentage)

        #gestion unite
        self.liste_unite = []
        self.id_unite = len(self.liste_unite)
        #self.unite = Unite(1, self.metiers, Outil(1), self.id_unite, random.randint(0,self.carte.axe_y-1), random.randint(0,self.carte.axe_x-1))
        #self.liste_unite.append(self.unite)
        #self.id_unite = len(self.liste_unite)
        

        #tests
        #unite
        self.unite_Paysan = Paysan(self.metiers[2]["metierid"], self.metiers, Outil(2), self.id_unite, 0 , 0)
        self.liste_unite.append(self.unite_Paysan)
        self.id_unite = len(self.liste_unite)

        self.unite_Bucheron = Bucheron(self.metiers[0]["metierid"], self.metiers, Outil(0), self.id_unite, 0, 1)
        self.liste_unite.append(self.unite_Bucheron)
        self.id_unite = len(self.liste_unite)


        self.unite_Mineur = Mineur(self.metiers[1]["metierid"], self.metiers, Outil(1), self.id_unite, 1, 0)
        self.liste_unite.append(self.unite_Mineur)
        self.id_unite = len(self.liste_unite)

        #monture
        self.testMonture = DecorateurMonture(self.unite_Mineur.metier_index, self.metiers, Outil(1), self.unite_Mineur.id_unite, 1, 0)
        self.liste_unite[self.testMonture.id_unite] = self.testMonture
        # self.testMonture.seDeplacer(self.inventory, self.carte, self.ressources)

        #expert
        self.testExpert = DecorateurExpert(self.unite_Bucheron.metier_index, self.metiers, Outil(0), self.unite_Bucheron.id_unite, 0, 1)
        self.liste_unite[self.testExpert.id_unite] = self.testExpert
        #batiment
        
        self.BatimentCreaMineur = Createurs("CreaMineur", 1, (2,2))
        # print("BatimentCreaMineur : ", self.BatimentCreaMineur)
        # print(self.liste_unite)
        self.BatimentCreaMineur.action(self.liste_unite, self.taille, self.metiers)
        # print(self.liste_unite)
        self.carte.afficherBatiment(self.BatimentCreaMineur)

        self.BatimentAmelioPaysan = Ameliorateur("AmelioPaysan", 2, (5,5))
        self.BatimentAmelioPaysan.action(self.liste_unite)
        self.carte.afficherBatiment(self.BatimentAmelioPaysan)

        # print(self.liste_unite[3].metier)
        #groupe unite
        self.groupeUnite = GroupeUnite(0,0)
        self.groupeUnite.ajouterUnite(self.unite_Bucheron)
        self.groupeUnite.ajouterUnite(self.unite_Mineur)
        # print(self.groupeUnite)
        # print(self.liste_unite)

        
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
            self.afficherInventaire()
            self.carte.afficher_carte()
            # affichage type metier bug sur decorateurs
            print(" vous deplacez l'unite : ", unite.id_unite , " de type : ", unite.metier)
            unite.seDeplacer(self.inventory, self.carte, self.ressources)
        #self.unite_Mineur.seDeplacer(self.inventory, self.carte, self.ressources)

        self.tourDeJeu += 1
        
        return False
    
    def afficherInventaire(self):
        print("Inventory :")
        for x in self.inventory.inventory:
            print(x.name, ":", x.quantity)
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
    