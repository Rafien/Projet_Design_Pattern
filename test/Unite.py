import random

metier = ["mineur", "bucheron", "paysan"]
outils = ["pioche", "hache", "houe"]

class Unite():
    def __init__(self, carte):
        #Position
        
        self.pos_unit_x = random.randint(0,carte.axe_y-1)
        self.pos_unit_y = random.randint(0,carte.axe_x-1)
        
        #Metier
        self.metier_index = random.randint(0,2)
        self.metier = metier[self.metier_index]
        self.outil = outils[self.metier_index]
        #Stats
        self.vitesse_base = 5
        self.cout_nourriture_base = 1
        self.xp = 0
        #decorateur
        self.surCheval = False
        self.Expert = False
        

        
    
    def rammasserRessources(self, inventaire, carte):
        if self.isOnRessourcesRecuperables(carte):
            # Ajouter les ressources au stock (a modifier)
            inventaire.append(carte.type_ressource(self.pos_unit_x, self.pos_unit_y))
            # Supprimer les ressources de la case
            print("Vous avez ramassé "+ carte.type_ressource(self.pos_unit_x, self.pos_unit_y) +"!")
            carte.supprimer_ressource(self.pos_unit_x, self.pos_unit_y)
            # Augmenter l'xp
            self.xp += 1
            print("Vous avez maintenant "+ str(self.xp) +" xp!")
            return 0
    
    # Vérifier si la case contient des ressources récupérables
    def isOnRessourcesRecuperables(self, carte):
        print("Vous êtes sur la case", self.pos_unit_x, self.pos_unit_y)
        if self.isOnRessources(carte) and self.isBonMetier(carte):
            return True
        
    # Vérifier si la case contient des ressources
    def isOnRessources(self, carte):
        if carte.case_avec_ressources(self.pos_unit_x, self.pos_unit_y) == True:
            print("Vous avez trouvé "+ carte.type_ressource(self.pos_unit_x, self.pos_unit_y) +"!")
            return True
    
    # Vérifier si le métier du joueur correspond aux ressources
    def isBonMetier(self, carte):
        
        print("Votre métier est "+ self.metier)
        if carte.index_ressource(self.pos_unit_x, self.pos_unit_y) == self.metier_index:
            print("Vous avez le bon métier!")
        # Si oui, retourner True
            return True
    
    def isSurCheval(self):
        self.surCheval = True

    def isExpert(self):
        if self.xp >= 5:
            self.Expert = True

    def seDeplacer(self, inventaire, carte):
        for _ in range(self.vitesse_base):
        # lire la direction dans la console
            direction = input("Dans quelle direction voulez-vous aller? (h, b, g, d)")
            carte.supprimer_unite_carte(self)
        # si la direction est h
            if direction == "h":
                self.deplacerHaut()
        # si la direction est b
            elif direction == "b":
                self.deplacerBas(carte)
        # si la direction est g
            elif direction == "g":
                self.deplacerGauche()

        # si la direction est d
            elif direction == "d":
                self.deplacerDroite(carte)
            carte.afficher_unite(self)
            self.rammasserRessources(inventaire, carte)


    def deplacerHaut(self):
        #verifier out of range
        if self.pos_unit_x == 0:
            print("Vous ne pouvez pas aller plus haut!")
        else:
            self.pos_unit_x -= 1
    
    def deplacerBas(self, carte):
        #verifier out of range
        if self.pos_unit_x == carte.axe_x-1:
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
        if self.pos_unit_y == carte.axe_y-1:
            print("Vous ne pouvez pas aller plus à droite!")
        else:
            self.pos_unit_y += 1