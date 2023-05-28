

class Outil():
    def __init__(self, id, outils):
        self.id = id
        self.name = outils[id]["name"]
        self.niveau = 1

    def ameliorer(self):
        self.niveau += 1

    def calcEfficacite():
        pass
    
