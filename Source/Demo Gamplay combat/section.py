
import pygame,sys

from Entity import Entity

class Section:
    def __init__(self,x,y,wind,types,disp):
        self.pos = (x,y)
        self.type = int(types)
        self.window = wind
        if self.type == 0:
            self.font = pygame.image.load("../../img/dirt.png").convert_alpha()
        elif self.type == 1:
            self.font = pygame.image.load("../../img/lava.png").convert_alpha()
        elif self.type == 2:
            self.font = pygame.image.load("../../img/grass.png").convert_alpha()
        elif self.type == 4:
            self.font = pygame.image.load("../../img/deep_water.png").convert_alpha()
        elif self.type == 3:
            self.font = pygame.image.load("../../img/dirt.png").convert_alpha()
            
        else:
            print(self.type)
            self.font = pygame.image.load("../../img/Section.png").convert_alpha()
        self.front = pygame.image.load("../../img/Section.png").convert_alpha() 
        self.entity = ""
        self.render(disp)
    def render(self,disp):
        if self.pos[0] >= 180 or self.pos[1] >= 150:
            self.window.blit(self.font, self.pos)
            if self.entity != "":
                self.entity.render()
            if disp == 1:
                pygame.display.flip()
    def change(self):
        self.window.blit(self.front, self.pos)
        pygame.display.flip() 
    def swapEnt(self,nsect):
        self.entity.section_swap(nsect)
        nsect.entity = self.entity
        self.entity = ""
    def setEntity(self,ent):
        self.entity = ent