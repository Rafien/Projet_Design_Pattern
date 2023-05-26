import random

metier = ["bucheron", "mineur", "paysan"]

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
            
    def isOnRessourcesRecuperables(self):
        # Vérifier si la case contient des ressources récupérables
        if self.isOnRessources() and self.isBonMetier():
            return True
        
    def isOnRessources(self, carte):
        # Vérifier si la case contient des ressources
        if carte.case_avec_ressources(self.pos_unit_x, self.pos_unit_y) == True:
            print("Vous avez trouvé "+ carte.type_ressource(self.pos_unit_x, self.pos_unit_y) +"!")
            return True
    
    def isBonMetier(self, carte):
        # Vérifier si le métier du joueur correspond aux ressources
        if carte.index_ressource(self.pos_unit_x, self.pos_unit_y) == self.metier_index:
            print("Vous avez le bon métier!")
        # Si oui, retourner True
            return True
    
    