import pygame,sys,csv
from section import Section
from Entity import Entity
class Map:
    def __init__(self,res,win):
        self.res = res
        self.win = win
        self.matrice = self.__gen_matr()
        
    def __gen_matr(self):
 
        row,col = self.res
        #calcul du nombre de section a faire
        nombreX = int(row/30)
        nombreY = int(col/30)
        #Recuperation de lq mqtrice csv
        mp_matrx = self.__matrx_csv(nombreX,nombreY)
        #creqtion d'une martrice de taille Nombre X et de largeur Nombre Y
        matrx = [[0 for i in range(nombreX)] for j in range(nombreY)]
        x = 0
        y = 0
        xm = 0
        ym = 0
        
        for nx in range(nombreX):
            for ny in range(nombreY):
                #Pour chaque case de la matrice, creation d'une section et attitrage de celle si
                type = mp_matrx[ny][nx]

                matrx[ny][nx] = Section(x,y,self.win,type,0)
                if int(type) == 3:                
                    entity = Entity(matrx[ny][nx],self.win)
                    matrx[ny][nx].setEntity(entity)
                    entity.render()
                y += 30
                ym +=1
            y = 0
            ym = 0
            x += 30
            xm +=1
        pygame.display.flip() 
        return matrx
    def __matrx_csv(self,nx,ny):
        #creation d'une matric de nx X ny
        map_matrx =[[0 for i in range(nx)] for j in range(ny)]
        with open("../../Data/maps/lv1.csv", "r") as file: #Ouverture du csv
            mfile = csv.reader(file)
            y = 0
            xu = 0
            for lines in mfile:
                for x in lines[0:nx]:
                    map_matrx[y][xu] = x #inscription des informations
                    xu +=1
                xu = 0
                y += 1
                if y>=ny:
                    break # finis
        return map_matrx