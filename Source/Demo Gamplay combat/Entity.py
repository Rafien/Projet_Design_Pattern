
import pygame

class Entity:
    def __init__(self,section,win):
        self.section = section
        self.window = win
        self.sprite = pygame.image.load("../../img/perso_zst.png").convert_alpha()

    def section_swap(self,nsect):
        self.section.render(1)
        self.section = nsect
        self.render()
        
    
    def render(self):
        self.window.blit(self.sprite, self.section.pos)
        pygame.display.flip() 