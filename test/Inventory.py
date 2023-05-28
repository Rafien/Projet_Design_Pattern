from Ressources import Ressources
class inventory:
    def __init__(self,ressources):
        self.inventory = []
        self.ress = ressources
        self.creatres()

    def creatres(self):
        for unity in self.ress:
            self.inventory.append(Ressources(unity["name"],unity["nomenclature"],1))
    def addressources(self,nomenclature,quantity):
        for unity in self.inventory:
            if unity.nomenc == nomenclature:
                unity.addquantity(quantity)
    def suppressources(self,nomenclature,quantity):
        for unity in self.inventory:
            if unity.nomenc == nomenclature:
                unity.suppquantity(quantity)
