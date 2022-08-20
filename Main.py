import time
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
        if posX - vel >= rezMul:
            posX -= vel
        elif posX - vel < rezMul:
            posX = rezMul

    if keys[pygame.K_RIGHT]:
        if posX + vel <= fLength-rezMul:
            posX += vel
        elif posX + vel > fLength-rezMul:
            posX = fLength-rezMul

    if keys[pygame.K_UP]:
        if posY - vel >= rezMul:
            posY -= vel
        elif posY - vel < rezMul:
            posY = rezMul

    if keys[pygame.K_DOWN]:
        if posY + vel <= fHight-rezMul:
            posY += vel
        elif posY + vel > fHight-rezMul:
            posY = fHight-rezMul


    pygame.draw.circle(screen, (0, 0, 255), (posX, posY), rezMul)
    pygame.display.flip()
    screen.fill((255, 255, 255))


pygame.quit()