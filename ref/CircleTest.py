import time
import pygame
#import os
#import socket

print('working')

pygame.init()

rezH = 16
rezV = 9
rezMul = 75

fLength = rezH*rezMul
fHight = rezV*rezMul

fpsLock = 60
fraimRate = 1/fpsLock

cirPosX = fLength/2
cirPosY = fHight/2

screen = pygame.display.set_mode([fLength, fHight])
screen.fill((255, 255, 255))

running = True
while running:
    time.sleep(fraimRate)

    pygame.draw.circle(screen, (0, 0, 255), (cirPosX, cirPosY), rezMul)
    pygame.display.flip()


pygame.quit()