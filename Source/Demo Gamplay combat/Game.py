
from select import select
import pygame,sys
from map import Map
from descripteur import Descripteur
    
class Game:
    def __init__(self,Wind,res):
        self.running = True
        self.window = Wind
        self.res = res
        self.width,self.heigh = res
        self.map = Map(res,Wind)
        self.mouse_pos = pygame.mouse.get_pos()
        self.act_sect = self.map.matrice[0][0]
        self.selected = self.act_sect
        self.select = False
        self.dc = False
        self.descrp = Descripteur(Wind)

    def event(self):
        left,mid,right = pygame.mouse.get_pressed()
        if right:
            if self.act_sect.entity != "" or self.selected.entity != "":
                if not self.select:
                    
                    self.selected = self.act_sect
                    if not self.dc:
                        self.select = True
                        print(self.select)
                    else:
                        self.dc = False
                        print(self.select)
                        self.selected = self.map.matrice[0][0]
                pygame.time.delay(70)
                if self.select and self.act_sect != self.selected and self.selected != self.map.matrice[0][0]:
                    self.select = False
                    self.dc = True
                    self.selected.swapEnt(self.act_sect)
                    self.selected.render(1)
                    self.selected = self.map.matrice[0][0]
                
        if self.mouse_pos != pygame.mouse.get_pos():
            x,y = self.mouse_pos
            cx = 0
            n = 0
            while x>n:
                cx += 1
                n += 30
            cy = 0
            n = 0
            while y>n:
                cy += 1
                n +=30
            x = cx -1
            y = cy -1
            print(cx,cy)
            if self.act_sect != self.map.matrice[y][x]:
                self.act_sect.render(1)
                
                self.map.matrice[y][x].change()
                self.act_sect = self.map.matrice[y][x]
                self.descrp.render(self.act_sect)
            self.mouse_pos = pygame.mouse.get_pos()
