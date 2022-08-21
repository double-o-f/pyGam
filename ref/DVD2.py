import random
import pygame

print('working...')

pygame.init()

rezH = 16
rezV = 9
rezMul = 120

fLength = rezH*rezMul
fHight = rezV*rezMul

siz = rezMul*2

posX = random.randint(1, fLength-siz) 
posY = random.randint(1, fHight-siz)

vel = rezMul/33

if random.randint(0,1) == 1:
    moveX = True
else:
    moveX = False

if random.randint(0,1) == 1:
    moveY = True
else:
    moveY = False


pos2X = posX
pos2Y = posY

move2X = moveX
move2Y = moveY

frames = 0

R = 255
G = 0
B = 0

colorS = 2

pygame.display.set_caption("sheesh")
screen = pygame.display.set_mode([fLength, fHight])


running = True
while running:
    frames += 1
    pygame.time.delay(16)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

#----2nd rect----
    if frames >= 1000:
        if move2X == True:
            if pos2X - vel >= 1:
                pos2X -= vel
            elif pos2X - vel < 1:
                pos2X = 1
                move2X = False

        if move2X == False:
            if pos2X + vel <= fLength-siz:
                pos2X += vel
            elif pos2X + vel > fLength-siz:
                pos2X = fLength-siz
                move2X = True

        if move2Y == True:
            if pos2Y - vel >= 1:
                pos2Y -= vel
            elif pos2Y - vel < 1:
                pos2Y = 1
                move2Y = False

        if move2Y == False:
            if pos2Y + vel <= fHight-siz:
                pos2Y += vel
            elif pos2Y + vel > fHight-siz:
                pos2Y = fHight-siz
                move2Y = True
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(pos2X, pos2Y, siz, siz))

#----1st redct----
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
    
    #pygame.draw.circle(screen, (R, G, B), (posX, posY), rezMul)
    pygame.draw.rect(screen, (R, G, B), pygame.Rect(posX, posY, siz, siz))
    pygame.display.flip()
    #screen.fill((0, 0, 0))

pygame.quit()