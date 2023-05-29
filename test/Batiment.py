from Unite import *
from Outils import *
class Batiment:
    def __init__(self,name,metierid,pos):
        self.name = name
        self.metierid = metierid
        self.pos = pos
        self.turn = 0
    def reseturn(self):
        self.turn = 0
    def CheckAction(self,unity):
        if self.turn == 3:
            self.action(unity)
            self.reseturn()
        else:
            self.turn +=1
    def action(self):
        print("Error bad creation")
class Ameliorateur(Batiment):
    def __init__(self,name,metierid,pos):
        super().__init__(name,metierid,pos)
    def action(self,unity):
        actual = unity[0]
        for ppl in unity:
            if ppl.outils.niveau < actual.outils.niveau:
                actual = ppl
        actual.outils.niveau += 1
class Createurs(Batiment):
    def __init__(self,name,metierid,pos):
        super().__init__(name,metierid,pos)

    def action(self,unity,taille, metiers):
        x,y = self.pos
        xt,yt = taille
        if x + 1 < xt:
            x += 1
        else:
            x -= 1
        unity.append(Unite(self.metierid, metiers,Outil(self.metierid),len(unity),x,y))
