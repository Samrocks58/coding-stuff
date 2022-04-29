from cmath import sqrt
import pygame, time, os

def gameloop():
    global max_width, max_height, screen, startTime, skyBlue, brown, green, black, Right, Up, Left, Down, MoveX, MoveY, forceX, forceY, OnGround, onPlatform, topSpeed, jumped, screen2, screenNum
    while True:
        endTime = time.perf_counter()
        if 1/60 - (endTime - startTime) > 0:
            time.sleep(1/60 - (endTime - startTime))
        startTime=time.perf_counter()

        pygame.display.flip()
        screen.fill(skyBlue)

        if not screen2:
            pygame.draw.rect(screen, brown, (0, max_height-35, max_width, 35))
            pygame.draw.rect(screen, green, (0, max_height-50, max_width, 15))
        rectlist = []
        lastScreen=2
        if screenNum > lastScreen:
            screenNum = lastScreen
            MoveY = max_height
            forceY = 0
        if not screen2:
            r1 = pygame.draw.rect(screen, (255, 0, 0), (max_width-280, max_height-140, 80, 30))
            r2 = pygame.draw.rect(screen, (255, 0, 0), (max_width-360, max_height-300, 80, 30))
            rectlist.append(r1)
            rectlist.append(r2)
        if screen2:
            if screenNum == 1:
                r1 = pygame.draw.rect(screen, (255, 0, 255), (max_width-280, max_height-140, 80, 30))
                r2 = pygame.draw.rect(screen, (255, 0, 255), (max_width-360, max_height-300, 80, 30))
                rectlist.append(r1)
                rectlist.append(r2)
            elif screenNum == 2:
                r1 = pygame.draw.rect(screen, (0, 0, 255), (max_width-280, max_height-140, 80, 30))
                r2 = pygame.draw.rect(screen, (0, 0, 255), (max_width-360, max_height-300, 80, 30))
                rectlist.append(r1)
                rectlist.append(r2)
        if not topSpeed:
            player = pygame.draw.rect(screen, black, (MoveX, max_height-MoveY, 20, 50))
        elif topSpeed:
            player = pygame.draw.rect(screen, (255, 255, 0), (MoveX, max_height-MoveY, 20, 50))


        keys = list(pygame.key.get_pressed())
        if keys[Right]:
            if forceX < 15:
                forceX += 0.4
            if abs(forceX) >= 15:
                topSpeed = True
            elif abs(forceX) < 15:
                topSpeed = False
        if keys[Left]:
            if forceX > -15:
                forceX -= 0.4
            if abs(forceX) >= 15:
                topSpeed = True
            elif abs(forceX) < 15:
                topSpeed = False
        if keys[Up]:
            if jumped:
                if OnGround or onPlatform:
                    if forceY < 10:
                        forceY += 1

        MoveX += forceX
        MoveY += forceY
        # for r in rectlist:
        #     if r.colliderect(player):
        #         if forceX != 0:
        #             MoveX -= forceX
        #             forceX = 0
        #             topSpeed = False
        #         if r.collidepoint((player.centerx, r.centery)) and not r.collidepoint(r.centerx, player.bottom-forceY) and (forceY < 0):
        #             onPlatform = True
        #         else:
        #             onPlatform = False
        #         if onPlatform:
        #             forceX = 0
        #         if forceY != 0 and onPlatform:
        #             MoveY -= forceY
        #             forceY = 0
        if (MoveX > max_width-20) or (MoveX < 0):
            forceX *= -1
        MoveX=min(max_width-20, max(0, MoveX))

        if MoveY > 100:
            OnGround=False
        if MoveY > max_height:
            screen2 = True
            MoveY = MoveY - max_height
            screenNum += 1
        if not OnGround:
            if not onPlatform:
                forceY -= 0.5
        if MoveY <= 100:
            if not screen2:
                OnGround = True
                MoveY = max(MoveY, 100)
                forceY = 0
                jumped = False
        if screen2 and MoveY < 0:
            screenNum -= 1
            MoveY = max_height
            if screenNum == 0:
                screen2 = False
        for r in rectlist:
            if r.colliderect(player):
                if not onPlatform:
                    MoveX -= forceX
                onPlatform = False
                jumped = False
                if (forceX > 0) and (MoveX < r.left) and (forceY >= 0) and (not onPlatform):
                    MoveX -= abs(player.right - r.left)
                    forceX=0
                    topSpeed=False
                elif (forceX < 0) and (player.right > r.right) and (forceY >= 0) and (not onPlatform):
                    MoveX += abs(r.right - player.left)
                    forceX=0
                    topSpeed=False
                elif (forceY > 0) and (r.bottom > player.top) and (r.bottom < player.bottom):
                    MoveY = min(MoveY, max_height-r.bottom)
                    forceY = 0
                elif (player.y < r.y):
                    MoveY = max(max_height-r.y+r.height-1, MoveY)
                    if forceY < 0:
                        forceY *= -1
                if onPlatform:
                    MoveY = max(max_height-r.y+r.height-1, MoveY)
                    if forceY < 0:
                        forceY -= forceY
                    onPlatform=True
        onPlatform = False
        for r in rectlist:
            if r.colliderect(player):
                onPlatform = True
        # Debug:
        # print("Force X: {}".format(forceX))
        # print("Force Y: {}".format(forceY))
        # print("OnGround: {}".format(OnGround))
        # print("OnPlatform: {}".format(onPlatform))
        # print("MoveX: {}".format(MoveX))
        # print("MoveY: {}".format(MoveY))
        # os.system('clear')

        if OnGround or onPlatform:
            if not topSpeed:
                # if abs(forceX) > 0:
                #     forceX *= abs(forceX)**63/64
                if forceX < 0:
                    forceX += 0.2
                elif forceX > 0:
                    forceX -= 0.2
                if abs(forceX) < 0.2:
                    forceX=0

        # OnGround = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    quit()
                if event.key == pygame.K_r:
                    Restart()
                if event.key == pygame.K_UP:
                    if OnGround:
                        forceY += 15
                        jumped = True
def Restart():
    global max_width, max_height, screen, startTime, skyBlue, brown, green, black, Right, Up, Left, Down, MoveX, MoveY, forceX, forceY, OnGround, onPlatform, topSpeed, jumped, screen2, screenNum
    pygame.init()
    pygame.display.init()
    max_width = 800
    max_height = 500
    screen = pygame.display.set_mode((max_width, max_height))
    startTime = time.perf_counter()
    skyBlue = (0, 200, 255)
    brown = (120, 60, 0)
    green = (0, 200, 0)
    black = (0, 0, 0)
    Right = 79
    Up = 82
    Left = 80
    Down = 81
    MoveX = 50
    MoveY = 100
    forceX = 0
    forceY = 0
    OnGround = True
    onPlatform=False
    topSpeed = False
    jumped = False
    screen2=False
    screenNum = 0
    gameloop()

Restart()
