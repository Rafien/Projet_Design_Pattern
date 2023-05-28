import random

outils = ["pioche", "hache", "houe"]

class Unite():
    def __init__(self, carte, metiers, outil, id_unite):
        self.id_unite = id_unite
        #Position
        self.pos_unit_x = random.randint(0,carte.axe_y-1)
        self.pos_unit_y = random.randint(0,carte.axe_x-1)
        
        #Metier
        self.metier_index = random.randint(0,len(metiers)-1)
        self.metier = metiers[self.metier_index]["name"]
        #Outil
        self.outil = outil
        self.niveau_outil = outil.niveau
        #Stats
        self.vitesse_base = 5
        self.cout_nourriture_base = 1
        self.xp = 0
        self.toursSansManger = 0
        #decorateur
        self.surCheval = False
        self.Expert = False
        

        
    
    def rammasserRessources(self, inventaire, carte, ressources):
        if self.isOnRessourcesRecuperables(carte, ressources):
            # Ajouter les ressources au stock (a modifier)
            inventaire.append(carte.type_ressource(self.pos_unit_x, self.pos_unit_y, ressources))
            # Supprimer les ressources de la case
            print("Vous avez ramassé "+ carte.type_ressource(self.pos_unit_x, self.pos_unit_y, ressources) +"!")
            carte.supprimer_ressource(self.pos_unit_x, self.pos_unit_y, self)
            # Augmenter l'xp
            self.xp += 1
            print("Vous avez maintenant "+ str(self.xp) +" xp!")
            return 0
    
    # Vérifier si la case contient des ressources récupérables
    def isOnRessourcesRecuperables(self, carte, ressources):
        print("Vous êtes sur la case", self.pos_unit_x, self.pos_unit_y)
        if self.isOnRessources(carte, ressources) and self.isBonMetier(carte, ressources):
            return True
        
    # Vérifier si la case contient des ressources
    def isOnRessources(self, carte, ressources):
        if carte.case_avec_ressources(self.pos_unit_x, self.pos_unit_y, ressources) == True:
            print("Vous avez trouvé "+ carte.type_ressource(self.pos_unit_x, self.pos_unit_y, ressources) +"!")
            return True
    
    # Vérifier si le métier du joueur correspond aux ressources
    def isBonMetier(self, carte, ressources):
        print("metier :", self.metier_index)
        print(carte.idMetier_ressource(self.pos_unit_x, self.pos_unit_y, ressources))
        if carte.idMetier_ressource(self.pos_unit_x, self.pos_unit_y, ressources) == str(self.metier_index):
            return True
        else:
            print("Vous n'avez pas le bon métier pour récolter cette ressource!")
            return False
    
    # Placement sur un cheval
    def MettreSurCheval(self):
        self.surCheval = True

    # Vérifier si l'unite est expert
    def isExpert(self):
        if self.xp >= 5:
            self.Expert = True

    # Deplacement
    def seDeplacer(self, inventaire, carte, ressources):
        #Varialbes
        deplacement_restants = self.vitesse_base
        #Tant qu'il reste des déplacements
        for _ in range(self.vitesse_base):
        # lire la direction dans la console
            print("Il vous reste "+ str(deplacement_restants) +" déplacements!")
            direction = input("Dans quelle direction voulez-vous aller? (haut : h, bas : b, gauche :g, droite : d, rien : r)")
            carte.supprimer_unite_carte(self, ressources)
        # si la direction est haut

            if direction == "h":
                self.deplacerHaut()
                deplacement_restants -= 1

        # si la direction est bas
            elif direction == "b":
                self.deplacerBas(carte)
                deplacement_restants -= 1

        # si la direction est gauche
            elif direction == "g":
                self.deplacerGauche()
                deplacement_restants -= 1

        # si la direction est droite
            elif direction == "d":
                self.deplacerDroite(carte)
                deplacement_restants -= 1
            
        # si la direction est rien
            elif direction == "r":
                deplacement_restants = 0
                break
            carte.afficher_unite(self)
            self.rammasserRessources(inventaire, carte, ressources)


    def deplacerHaut(self):
        #verifier out of range
        if self.pos_unit_x == 0:
            print("Vous ne pouvez pas aller plus haut!")
        else:
            self.pos_unit_x -= 1
    
    def deplacerBas(self, carte):
        #verifier out of range
        if self.pos_unit_x == carte.axe_y-1:
            print("Vous ne pouvez pas aller plus bas!")
        else:
            self.pos_unit_x += 1
    
    def deplacerGauche(self):
        #verifier out of range
        if self.pos_unit_y == 0:
            print("Vous ne pouvez pas aller plus à gauche!")
        else:
            self.pos_unit_y -= 1

    def deplacerDroite(self, carte):
        #verifier out of range
        if self.pos_unit_y == carte.axe_x-1:
            print("Vous ne pouvez pas aller plus à droite!")
        else:
            self.pos_unit_y += 1


class Bucheron(Unite):
    def __init__(self, carte, metiers, outil, id_unite):
        super().__init__(carte, metiers, outil, id_unite)
        self.metier_index = 0
        self.metier = "Bucheron"
        self.outil = outil
        
        # print("metier : ", self.metier)
        # print("outil : ", self.outil.name)

class Mineur(Unite):
    def __init__(self, carte, metiers, outil, id_unite):
        super().__init__(carte, metiers, outil, id_unite)
        self.metier_index = 1
        self.metier = "Mineur"
        self.outil = outil

        # print("metier : ", self.metier)
        # print("outil : ", self.outil.name)


class Paysan(Unite):
    def __init__(self, carte, metiers, outil, id_unite):
        super().__init__(carte, metiers, outil, id_unite)
        self.metier_index = 2
        self.metier = "Paysan"
        self.outil = outil

        # print("metier : ", self.metier)
        # print("outil : ", self.outil.name)

class GroupeUnite():
    def __init__(self, pos_x, pos_y):
        self.listeUnite = []
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vitesse = self.calculerVitesse()
        self.cout_nourriture = self.calculerCoutNourriture()

    def ajouterUnite(self, unite):
        self.listeUnite.append(unite)
        self.calculerVitesse()
        self.calculerCoutNourriture()
        

    def supprimerUnite(self, unite):
        self.listeUnite.remove(unite)
        self.calculerVitesse()
        self.calculerCoutNourriture()
    
    # calculer la vitesse du groupe
    def calculerVitesse(self):
        self.vitesse = 0
        for unite in self.listeUnite:
            self.vitesse += unite.vitesse_base
        return self.vitesse
        # print("vitesse groupe : ", self.vitesse)
    
    # calculer le cout en nourriture du groupe
    def calculerCoutNourriture(self):
        self.cout_nourriture = 0
        for unite in self.listeUnite:
            self.cout_nourriture += unite.cout_nourriture_base
        return self.cout_nourriture
        # print("cout_nourriture groupe : ", self.cout_nourriture)
