import time
import pygame
import os
import socket

print('working')

pygame.init()

rezH = 16
rezV = 9
rezMul = 100
fpsLock = 60
fraimRate = 1/fpsLock

screen = pygame.display.set_mode([rezH*rezMul, rezV*rezMul])

running = True
while running:

    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (0, 0, 255), ((rezH/2)*rezMul, (rezV/2)*rezMul), rezMul)
    pygame.display.flip()
    time.sleep(fraimRate)

    pygame.draw.circle(screen, (255, 0, 0), ((rezH/2)*rezMul, (rezV/2)*rezMul), rezMul)
    pygame.display.flip()
    time.sleep(fraimRate)

pygame.quit()