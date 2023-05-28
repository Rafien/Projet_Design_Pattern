import random
#Ressources foutre en enum pour pouvoir avoir plusieurs ressources par metiers
unite_aff = "U"
class Carte:
    def __init__(self,TAILLE_MIN,TAILLE_MAX,):
        #taille de la carte
        self.axe_x = random.randint(TAILLE_MIN,TAILLE_MAX)
        self.axe_y = random.randint(TAILLE_MIN,TAILLE_MAX)
        self.carte = self.__creer_carte()
        

#Cree une carte sous forme de liste de liste
    def __creer_carte(self):
        matrx = [[" " for i in range(self.axe_x)] for j in range(self.axe_y)]
        return matrx
#affiche la carte
    def afficher_carte(self):
        for ligne in self.carte:
            print(ligne)
        print("\n")

#ajoute des ressources sur la carte en fonction du pourcentage donné
    def ajouter_ressources(self,ressources,pourcentages):
        hauteur = len(self.carte)
        largeur = len(self.carte[0])
        total_cases = hauteur * largeur
        #calcul du nombre de cases à remplir
        for ressource, pourcentage in zip(ressources, pourcentages):
            nb_cases = int(total_cases * pourcentage)
        
            for _ in range(nb_cases):
                x = random.randint(0, hauteur - 1)
                y = random.randint(0, largeur - 1)
                #verif si la case est vide
                if self.carte[x][y] == " ":
                    #ajout de la ressource
                    self.carte[x][y] = ressource
                    
#return true si la case a des ressources 
    def case_avec_ressources(self, x , y, ressources):
        temp = self.recuperer_ressource_de_string(x, y)
        for i in range(len(ressources)):
            if temp == ressources[i]["nomenclature"]:
                #print("Vous avez trouvé "+ ressources[i] +"!")
                return True
        return False    
#return le type de ressource sur la case             
    def type_ressource(self, x , y, ressources):
        temp = self.recuperer_ressource_de_string(x, y)
        for i in range(len(ressources)):
            if temp == ressources[i]["nomenclature"]:
                return ressources[i]["nomenclature"]

    def idMetier_ressource(self, x , y, ressources):
        temp = self.recuperer_ressource_de_string(x, y)
        for i in range(len(ressources)):
            if temp == ressources[i]["nomenclature"]:
                return ressources[i]["metierid"]
    

    def recuperer_ressource_de_string(self, x, y):
        return self.carte[x][y][len(self.carte[x][y])-1]


    def recuperer_2nd_de_string(self, x, y):
        return self.carte[x][y][1]
    
    def recuperer_3em_de_string(self, x, y):
        return self.carte[x][y][2]
        

    
    def supprimer_ressource(self, x , y, unite):
        temp = ""
        # si j'ai une unité je laisse l'unite
        if self.carte[x][y] == str(unite.id_unite):
            self.carte[x][y] = str(unite.id_unite)
        # si j'ai une unite et une ressource je laisse l'unite
        elif len(self.carte[x][y]) >= 2:
            for i in range(len(self.carte[x][y])-1):
                temp += (self.carte[x][y][i])
            print(temp)
            self.carte[x][y] = temp
        # sinon je laisse vide
        else:
            self.carte[x][y] = " "
        


    #affiche une unité sur la carte a sa position 
    def afficher_unite(self, unite):
        print(unite.pos_unit_x,unite.pos_unit_y)
        #si la case est vide
        if self.carte[unite.pos_unit_x][unite.pos_unit_y] == " ":
            # placer l'unite
            self.carte[unite.pos_unit_x][unite.pos_unit_y] = str(unite.id_unite)
        else:
            #placer l'unite sur la case avec les elements deja presents
            self.carte[unite.pos_unit_x][unite.pos_unit_y] = str(unite.id_unite) + self.carte[unite.pos_unit_x][unite.pos_unit_y]
        self.afficher_carte()

    def supprimer_unite_carte(self, unite, ressources):
        if self.carte[unite.pos_unit_x][unite.pos_unit_y] != str(unite.id_unite):
            #lire case et recuperer ressource
            elementADelete = str(unite.id_unite)
            self.carte[unite.pos_unit_x][unite.pos_unit_y] = self.carte[unite.pos_unit_x][unite.pos_unit_y].replace(elementADelete, "")
        else:
            self.carte[unite.pos_unit_x][unite.pos_unit_y] = " "

    # def verifPresenceUnite(self, x, y, ressources):
    #     if self.carte[x][y] != " " and self.carte[x][y] != self.type_ressource(x, y, ressources):
    #         print("il y a une unite")
    #         return True