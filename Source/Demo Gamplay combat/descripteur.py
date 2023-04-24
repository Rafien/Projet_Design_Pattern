import pygame,sys

class Descripteur:
    def __init__(self,win):
        self.windows = win
        self.font = pygame.image.load("../../img/descr.png").convert_alpha()
        self.police = pygame.font.SysFont("monospace" ,15)
    def render(self,section):
        txt = ""
        txt2 = ""
        if section.type == 0 or section.type == 3:
            txt += "Dirt "
        if section.type == 1:
            txt += "Lava "
        if section.type == 2:
            txt += "Grass "
        if section.type == 4:
            txt += "Water "
        if section.entity != "":
            txt2 += "Entity "
        
        image_texte = self.police.render ( txt, 1 , (255,0,0) )
        image_texte2 = self.police.render ( txt2, 1 , (255,0,0) )
        self.windows.blit(self.font,(0,0))
        self.windows.blit(image_texte, (30,30))
        self.windows.blit(image_texte2, (30,40))
        pygame.display.flip()
