import pygame,sys
from Game import Game
res = (1920,1080)
clock = pygame.time.Clock()
frame = 0 
pygame.init()
pygame.font.init()  
window = pygame.display.set_mode(res)
game = Game(window,res)
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    game.event()