import random

TAILLE_MIN = 5
TAILLE_MAX = 10
ressources = ["P", "B", "N"]
pourcentages = [0.2, 0.3, 0.5]

class Carte:
    def __init__(self):
        self.axe_x = random.randint(TAILLE_MIN,TAILLE_MAX)
        self.axe_y = random.randint(TAILLE_MIN,TAILLE_MAX)
        self.carte = []
        

#Cree une carte sous forme de liste de liste
    def creer_carte(self):
        for i in range(self.axe_x):
            ligne = ["X"] * self.axe_y
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

        for ressource, pourcentage in zip(ressources, pourcentages):
            nb_cases = int(total_cases * pourcentage)
        
            for _ in range(nb_cases):
                while True:
                    x = random.randint(0, largeur - 1)
                    y = random.randint(0, hauteur - 1)
                    if self.carte[y][x] == "X":
                        self.carte[y][x] = ressource
                        break