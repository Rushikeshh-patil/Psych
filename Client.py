import pygame
import sys
pygame.init()

size = width, height = 800 , 800

black = 50,150,100

screen1 = pygame.display.set_mode(size, flags = pygame.RESIZABLE)
pygame.display.set_caption('Rushikesh Psych')
#Creating the screen.
pygame.mouse.set_cursor(*pygame.cursors.broken_x)

Question_box = pygame.draw.rect(screen1,(255,255,255),(200,200,400,100))
Answer_box = pygame.draw.rect(screen1,(255,255,255),(200,400,400,100))
 
while 1: 

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
        pygame.display.update()
        #pygame.display.flip()  
        #screen1.fill(black)
        #pygame.display.flip()  