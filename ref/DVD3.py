import random
import pygame
import threading

print('working...')

pygame.init()

rezH = 16
rezV = 9
rezMul = 120

fLength = rezH*rezMul
fHight = rezV*rezMul

siz = rezMul*2

vel = rezMul/33

R = 255
G = 0
B = 0

colorS = 2

pygame.display.set_caption("sheesh")
screen = pygame.display.set_mode([fLength, fHight])

run = True

posX = 0
posY = 0

moveX = 0
moveY = 0

def clearer():
    pygame.time.delay(6000)
    
    posX = random.randint(1, fLength-siz) 
    posY = random.randint(1, fHight-siz)

    if random.randint(0,1) == 1:
        moveX = True
    else:
        moveX = False

    if random.randint(0,1) == 1:
        moveY = True
    else:
        moveY = False
    
    screen.fill((0, 0, 0))

def updater():
    pygame.time.delay(6)
    pygame.draw.rect(screen, (R, G, B), pygame.Rect(posX, posY, siz, siz))
    pygame.display.flip()


def runner():
    pygame.time.delay(6)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if moveX == True:
        if posX - vel >= 1:
            posX -= vel
        elif posX - vel < 1:
            posX = 1
            moveX = False

    if moveX == False:
        if posX + vel <= fLength-siz:
            posX += vel
        elif posX + vel > fLength-siz:
            posX = fLength-siz
            moveX = True

    if moveY == True:
        if posY - vel >= 1:
            posY -= vel
        elif posY - vel < 1:
            posY = 1
            moveY = False

    if moveY == False:
        if posY + vel <= fHight-siz:
            posY += vel
        elif posY + vel > fHight-siz:
            posY = fHight-siz
            moveY = True

    if R == 255 and G < 255 and B == 0:
        G += 1
    elif G == 255 and R > 0 and B == 0:
        R -= 1
    elif G == 255 and B < 255 and R == 0:
        B += 1
    elif B == 255 and G > 0 and R == 0:
        G -= 1
    elif B == 255 and R < 255 and G == 0:
        R += 1
    elif R == 255 and B > 0 and G == 0:
        B -= 1  

pygame.quit()