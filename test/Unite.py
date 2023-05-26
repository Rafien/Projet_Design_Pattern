import random

metier = ["mineur", "bucheron", "paysan"]

class Unite():
    def __init__(self, carte):
        #Position
        self.pos_unit_x = random.randint(0,carte.axe_x-1)
        self.pos_unit_y = random.randint(0,carte.axe_y-1)
        #Metier
        self.metier_index = random.randint(0,2)
        self.metier = metier[self.metier_index]

        
    
    def rammasserRessources(self):
        if self.isOnRessourcesRecuperables():
            # Récupérer les ressources
            # Ajouter les ressources au stock
            # Supprimer les ressources de la case
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
    
    