class Ressources:
    def __init__(self,name,nomenclature,quantity):
            self.name = name
            self.nomenc = nomenclature
            self.quantity = quantity

    def addquantity(self,quant):
          self.quantity += quant
    def suppquantity(self,quant):
          self.quantity -= quant