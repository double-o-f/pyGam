import pygame
#import os
#import socket

print('working')

pygame.init()

rezH = 16
rezV = 9
rezMul = 100

fLength = rezH*rezMul
fHight = rezV*rezMul

posX = fLength/2
posY = fHight/2

vel = 10

pygame.display.set_caption("sheesh")
screen = pygame.display.set_mode([fLength, fHight])
screen.fill((255, 255, 255))


running = True
while running:
    pygame.time.delay(17)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    

    if keys[pygame.K_LEFT]:
        if posX - vel >= rezMul/2:
            posX -= vel
        elif posX - vel < rezMul/2:
            posX = rezMul/2

    if keys[pygame.K_RIGHT]:
        if posX + vel <= fLength-rezMul/2:
            posX += vel
        elif posX + vel > fLength-rezMul/2:
            posX = fLength-rezMul/2

    if keys[pygame.K_UP]:
        if posY - vel >= rezMul/2:
            posY -= vel
        elif posY - vel < rezMul/2:
            posY = rezMul/2

    if keys[pygame.K_DOWN]:
        if posY + vel <= fHight-rezMul/2:
            posY += vel
        elif posY + vel > fHight-rezMul/2:
            posY = fHight-rezMul/2


    pygame.draw.circle(screen, (0, 0, 255), (posX, posY), rezMul/2)
    pygame.display.flip()
    screen.fill((255, 255, 255))


pygame.quit()