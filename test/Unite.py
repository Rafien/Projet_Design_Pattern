import math
import random


GAIN_XP_RECOLTE = 1
XP_NEEDED_EXPERT = 5
class Unite():
    def __init__(self, metiersid, metiers, outil, id_unite, x, y):
        self.id_unite = id_unite
        #Position
        self.pos_unit_x = x
        self.pos_unit_y = y
        
        #Metier
        self.metier_index = metiersid
        self.list_metier = metiers
        self.metier = metiers[metiersid]["name"]
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
        

    def augmenterXp(self, xp):
        self.xp += xp
        self.isExpert()
    
    def rammasserRessources(self, inventaire, carte, ressources):
        if self.isOnRessourcesRecuperables(carte, ressources):
            # Ajouter les ressources au stock (a modifier (mettre le bon nombre de ressources))
            inventaire.addressources(carte.type_ressource(self.pos_unit_x, self.pos_unit_y, ressources), 1 * self.outil.niveau)
            # Supprimer les ressources de la case
            print("Vous avez ramassé "+ carte.type_ressource(self.pos_unit_x, self.pos_unit_y, ressources) +"!")
            # for ress in inventaire.inventory:
            #     print("Vous avez "+ str(ress.quantity) + str(ress.nomenc))
            carte.supprimer_ressource(self.pos_unit_x, self.pos_unit_y, self)
            # Augmenter l'xp
            self.augmenterXp(GAIN_XP_RECOLTE)
            print("Vous avez maintenant "+ str(self.xp) +" xp!")
            return 0
    
    # Vérifier si la case contient des ressources récupérables
    def isOnRessourcesRecuperables(self, carte, ressources):
        # print("Vous êtes sur la case", self.pos_unit_x, self.pos_unit_y)
        if self.isOnRessources(carte, ressources) and self.isBonMetier(carte, ressources):
            return True
        
    # Vérifier si la case contient des ressources
    def isOnRessources(self, carte, ressources):
        if carte.case_avec_ressources(self.pos_unit_x, self.pos_unit_y, ressources) == True:
            # print("Vous avez trouvé "+ carte.type_ressource(self.pos_unit_x, self.pos_unit_y, ressources) +"!")
            return True
    
    # Vérifier si le métier du joueur correspond aux ressources
    def isBonMetier(self, carte, ressources):
        # print("metier :", self.metier_index)
        # print(carte.idMetier_ressource(self.pos_unit_x, self.pos_unit_y, ressources))
        if carte.idMetier_ressource(self.pos_unit_x, self.pos_unit_y, ressources) == str(self.metier_index):
            return True
        else:
            # print("Vous n'avez pas le bon métier pour récolter cette ressource!")
            return False
    
    # Placement sur un cheval
    def MettreSurCheval(self):
        self.surCheval = True

    # Vérifier si l'unite est expert
    def isExpert(self):
        if self.xp >= XP_NEEDED_EXPERT:
            self.Expert = True
            DecorateurExpert(self.metier_index, self.list_metier, self.outil, self.id_unite, self.pos_unit_x, self.pos_unit_y)
            # update list unite
            print("Cette unité est maintenant experte!")
    # Deplacement
    def seDeplacer(self, inventaire, carte, ressources):
        #Varialbes
        if self.surCheval:
            deplacement_restants = self.vitesse_base * 1.5
        else:
            deplacement_restants = self.vitesse_base
        #Tant qu'il reste des déplacements
        for _ in range(self.vitesse_base):
        # lire la direction dans la console
            carte.afficher_carte()
            print("Il vous reste "+ str(deplacement_restants) +" déplacements! et " + str(inventaire.inventory[3].quantity) + " nourriture")
            direction = input("Dans quelle direction voulez-vous aller? (haut : h, bas : b, gauche :g, droite : d, rien : r)")
            
        # si la direction est haut

            if direction == "h":
                if self.consommerNourriture(inventaire):
                    carte.supprimer_unite_carte(self, ressources)
                    self.deplacerHaut()
                    deplacement_restants -= 1
                else:
                    break
                

        # si la direction est bas
            elif direction == "b":
                if self.consommerNourriture(inventaire):
                    carte.supprimer_unite_carte(self, ressources)
                    self.deplacerBas(carte)
                    deplacement_restants -= 1
                else:
                    break

        # si la direction est gauche
            elif direction == "g":
                if self.consommerNourriture(inventaire):
                    carte.supprimer_unite_carte(self, ressources)
                    self.deplacerGauche()
                    deplacement_restants -= 1
                else:
                    break

        # si la direction est droite
            elif direction == "d":
                if self.consommerNourriture(inventaire):
                    carte.supprimer_unite_carte(self, ressources)
                    self.deplacerDroite(carte)
                    deplacement_restants -= 1
                else:
                    break
            
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

    def consommerNourriture(self, inventaire):
        if self.surCheval:
            conso = self.cout_nourriture_base + 3
        else:
            conso = self.cout_nourriture_base
        
        for ress in inventaire.inventory:
            # print("Il vous reste "+ str(ress.quantity) + str(ress.nomenc))
            if ress.nomenc == "N":
                if ress.quantity >= conso:
                    inventaire.suppressources("N", conso)
                    self.toursSansManger = 0
                    # print("Il vous reste "+ str(ress.quantity) +" nourriture!")
                    return True
                else:
                    print("Vous n'avez pas assez de nourriture pour vous deplacer!")
                    return False
        

class Bucheron(Unite):
    def __init__(self, metiersid, metiers, outil, id_unite, x, y):
        super().__init__(metiersid, metiers, outil, id_unite, x, y)
        self.metier_index = 0
        self.metier = "Bucheron"
        self.outil = outil
        
        # print("metier : ", self.metier)
        # print("outil : ", self.outil.name)

class Mineur(Unite):
    def __init__(self, metiersid, metiers, outil, id_unite, x, y):
        super().__init__(metiersid, metiers, outil, id_unite, x, y)
        self.metier_index = 1
        self.metier = "Mineur"
        self.outil = outil

        # print("metier : ", self.metier)
        # print("outil : ", self.outil.name)


class Paysan(Unite):
    def __init__(self, metiersid, metiers, outil, id_unite, x, y):
        super().__init__(metiersid, metiers, outil, id_unite, x, y)
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


class DecorateurMonture(Unite):
    def __init__(self, metierid, metiers, outil, id_unite, x, y):
        super().__init__(metierid, metiers, outil, id_unite, x, y)
        self.metier = metiers[metierid]["name"]
    def seDeplacer(self, inventaire, carte, ressources):
        #Varialbes
        deplacement_restants = math.floor(self.vitesse_base * 1.5)
        #Tant qu'il reste des déplacements
        for _ in range(self.vitesse_base):
        # lire la direction dans la console
            carte.afficher_carte()
            print("Il vous reste "+ str(deplacement_restants) +" déplacements! et " + str(inventaire.inventory[3].quantity) + " nourriture")
            direction = input("Dans quelle direction voulez-vous aller? (haut : h, bas : b, gauche :g, droite : d, rien : r)")
            
        # si la direction est haut

            if direction == "h":
                if self.consommerNourriture(inventaire):
                    carte.supprimer_unite_carte(self, ressources)
                    self.deplacerHaut()
                    deplacement_restants -= 1
                else:
                    break
                

        # si la direction est bas
            elif direction == "b":
                if self.consommerNourriture(inventaire):
                    carte.supprimer_unite_carte(self, ressources)
                    self.deplacerBas(carte)
                    deplacement_restants -= 1
                else:
                    break

        # si la direction est gauche
            elif direction == "g":
                if self.consommerNourriture(inventaire):
                    carte.supprimer_unite_carte(self, ressources)
                    self.deplacerGauche()
                    deplacement_restants -= 1
                else:
                    break

        # si la direction est droite
            elif direction == "d":
                if self.consommerNourriture(inventaire):
                    carte.supprimer_unite_carte(self, ressources)
                    self.deplacerDroite(carte)
                    deplacement_restants -= 1
                else:
                    break
            
        # si la direction est rien
            elif direction == "r":
                deplacement_restants = 0
                break
            carte.afficher_unite(self)
            self.rammasserRessources(inventaire, carte, ressources)


    def consommerNourriture(self, inventaire):
        for ress in inventaire.inventory:
            # print("Il vous reste "+ str(ress.quantity) + str(ress.nomenc))
            if ress.nomenc == "N":
                if ress.quantity >= self.cout_nourriture_base + 3:
                    inventaire.suppressources("N", self.cout_nourriture_base + 3)
                    self.toursSansManger = 0
                    # print("Il vous reste "+ str(ress.quantity) +" nourriture!")
                    return True
                else:
                    print("Vous n'avez pas assez de nourriture pour vous deplacer!")
                    return False
                
class DecorateurExpert(Unite):
    def __init__(self, metierid, metiers, outil, id_unite, x, y):
        super().__init__(metierid, metiers, outil, id_unite, x, y)      
    def rammasserRessources(self, inventaire, carte, ressources):
        if self.isOnRessourcesRecuperables(carte, ressources):
            # Ajouter les ressources au stock (a modifier (mettre le bon nombre de ressources))
            inventaire.addressources(carte.type_ressource(self.pos_unit_x, self.pos_unit_y, ressources), (1 * self.outil.niveau) + 1)
            # Supprimer les ressources de la case
            print("Vous avez ramassé "+ carte.type_ressource(self.pos_unit_x, self.pos_unit_y, ressources) +"!")
            # for ress in inventaire.inventory:
            #     print("Vous avez "+ str(ress.quantity) + str(ress.nomenc))
            carte.supprimer_ressource(self.pos_unit_x, self.pos_unit_y, self)
            # Augmenter l'xp
            self.augmenterXp(GAIN_XP_RECOLTE)
            print("Vous avez maintenant "+ str(self.xp) +" xp!")
            return 0
    
    def PerteExpert(self):
        if self.toursSansManger > 5:
            self.Expert = False
            self.xp = 0
            #supprimer le decorateur
            pass