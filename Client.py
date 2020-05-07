import pygame
import sys
pygame.init()

size = width, height = 800, 800
speed = [1,1]
black = 50,150,100

screen = pygame.display.set_mode(size, flags = pygame.NOFRAME)
#Creating the screen.
pygame.mouse.set_cursor(*pygame.cursors.broken_x)

ball = pygame.image.load("download.jpeg")
#ball object, that will just load the image
ballrect = ball.get_rect()
#ball rectangle, a handy object in python that can be manipulated. Add ball image loaded 
# to this rectangle
 
while 1: 

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    #screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()  