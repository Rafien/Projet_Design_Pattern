import random

#Taille carte
TAILLE_MIN = 5
TAILLE_MAX = 10
#Ressources
ressources = ["P", "B", "N"]
pourcentages = [0.1, 0.15, 0.25]
unite_aff = "U"
class Carte:
    def __init__(self):
        #taille de la carte
        self.axe_x = random.randint(TAILLE_MIN,TAILLE_MAX)
        self.axe_y = random.randint(TAILLE_MIN,TAILLE_MAX)
        self.carte = []
        

#Cree une carte sous forme de liste de liste
    def creer_carte(self):
        for i in range(self.axe_y):
            #creation d'une ligne de la carte
            ligne = [" "] * self.axe_x
            #ajout de la ligne à la carte
            self.carte.append(ligne)
            i+=1

#affiche la carte
    def afficher_carte(self):
        for ligne in self.carte:
            print(ligne)
        print("\n")

#ajoute des ressources sur la carte en fonction du pourcentage donné
    def ajouter_ressources(self):
        hauteur = len(self.carte)
        largeur = len(self.carte[0])

        total_cases = hauteur * largeur
        #calcul du nombre de cases à remplir
        for ressource, pourcentage in zip(ressources, pourcentages):
            nb_cases = int(total_cases * pourcentage)
        
            for _ in range(nb_cases):
                while True:
                    x = random.randint(0, hauteur - 1)
                    y = random.randint(0, largeur - 1)
                    #verif si la case est vide
                    if self.carte[x][y] == " ":
                        #ajout de la ressource
                        self.carte[x][y] = ressource
                        break

#return true si la case a des ressources 
    def case_avec_ressources(self, x , y):
        #print("Vous êtes sur la case", x-1, y-1)
        #print("Cette case contient", self.carte[y-1][x-1])
        for i in range(len(ressources)):
            if self.carte[x-1][y-1] == ressources[i]:
                #print("Vous avez trouvé "+ ressources[i] +"!")
                return True
        return False    
#return le type de ressource sur la case             
    def type_ressource(self, x , y):
        for i in range(len(ressources)):
            if self.carte[x-1][y-1] == ressources[i]:
                return ressources[i]

    def index_ressource(self, x , y):        
        for i in range(len(ressources)):
            if self.carte[x-1][y-1] == ressources[i]:
                return i
    
    def supprimer_ressource(self, x , y):
        # si j'ai une unité je laisse l'unite
        if self.carte[x-1][y-1] == unite_aff:
            self.carte[x-1][y-1] = unite_aff
        # si j'ai une unite et une ressource je laisse l'unite
        elif self.carte[x-1][y-1] != " ":
            self.carte[x-1][y-1] = unite_aff
        # sinon je laisse vide
        else:
            self.carte[x-1][y-1] = " "
        


    #affiche une unité sur la carte a sa position 
    def afficher_unite(self, unite):
        if self.carte[unite.pos_unit_x][unite.pos_unit_y] == " ":
            self.carte[unite.pos_unit_x][unite.pos_unit_y] = unite_aff
        else:
            self.carte[unite.pos_unit_x][unite.pos_unit_y] = unite_aff + self.carte[unite.pos_unit_x-1][unite.pos_unit_y-1]

