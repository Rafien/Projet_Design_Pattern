import random

metier = ["mineur", "bucheron", "paysan"]

class Unite():
    def __init__(self):
        self.pos_unit_x = 2
        self.pos_unit_y = 2
        
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
    
    