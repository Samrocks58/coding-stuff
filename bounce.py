from cmath import rect
import pygame, time, os

def gameloop():
    global max_width, max_height, screen, startTime, skyBlue, brown, green, black, Right, Up, Left, Down, MoveX, MoveY, forceX, forceY, OnGround, onPlatform, topSpeed, jumped, screen2, screenNum, mouse1, mouse2, counter, walugi, waluigiLeft, Cheatnum, oldwally, rectdict, pause, rectColor, green2, blue
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
        if (mouse1 != (0, 0)) and (mouse2 != (0,0)):
            left = min(mouse1[0], mouse2[0])
            top = min(mouse1[1], mouse2[1])
            top = max(51, top)
            width = abs(mouse1[0]-mouse2[0])
            height = abs(mouse1[1]-mouse2[1])
            if screen2 == Cheatnum:
                rectlist.append(pygame.draw.rect(screen, (50, 50, 50), (left, top, width, height)))
        if screenNum > lastScreen:
            screenNum = lastScreen
            MoveY = max_height
            forceY = 0
        if not screen2:
            # r1 = pygame.draw.rect(screen, (255, 0, 0), (max_width-280, max_height-140, 80, 30))
            # r2 = pygame.draw.rect(screen, (255, 0, 0), (max_width-360, max_height-300, 80, 30))
            for k in list(rectdict.keys()):
                if rectdict[k] == 0:
                    colorNum = rectColor[list(rectdict.keys()).index(k)]
                    Rcolor = (50, 50, 50)
                    if colorNum == '0':
                        Rcolor = (50, 50, 50)
                    if colorNum == '1':
                        Rcolor = (255, 0, 0)
                    if colorNum == '2':
                        Rcolor = (0, 255, 0)
                    if colorNum == '3':
                        Rcolor = (255, 255, 0)
                    if colorNum == '4':
                            Rcolor = (0, 0, 255)
                    rectlist.append(pygame.draw.rect(screen, Rcolor, k))
            # rectlist.append(r1)
            # rectlist.append(r2)
        if screen2:
            if screenNum == 1:
                # r1 = pygame.draw.rect(screen, (255, 0, 255), (max_width-280, max_height-140, 80, 30))
                # r2 = pygame.draw.rect(screen, (255, 0, 255), (max_width-360, max_height-300, 80, 30))
                for k in list(rectdict.keys()):
                    if rectdict[k] == 1:
                        colorNum = rectColor[list(rectdict.keys()).index(k)]
                        Rcolor = (50, 50, 50)
                        if colorNum == '0':
                            Rcolor = (50, 50, 50)
                        if colorNum == '1':
                            Rcolor = (255, 0, 0)
                        if colorNum == '2':
                            Rcolor = (0, 255, 0)
                        if colorNum == '3':
                            Rcolor = (255, 255, 0)
                        if colorNum == '4':
                            Rcolor = (0, 0, 255)
                        rectlist.append(pygame.draw.rect(screen, Rcolor, k))
                # rectlist.append(r1)
                # rectlist.append(r2)
            elif screenNum == 2:
                # r1 = pygame.draw.rect(screen, (0, 0, 255), (max_width-280, max_height-140, 80, 30))
                # r2 = pygame.draw.rect(screen, (0, 0, 255), (max_width-360, max_height-300, 80, 30))
                for k in list(rectdict.keys()):
                    if rectdict[k] == 2:
                        colorNum = rectColor[list(rectdict.keys()).index(k)]
                        Rcolor = (50, 50, 50)
                        if colorNum == '0':
                            Rcolor = (50, 50, 50)
                        if colorNum == '1':
                            Rcolor = (255, 0, 0)
                        if colorNum == '2':
                            Rcolor = (0, 255, 0)
                        if colorNum == '3':
                            Rcolor = (255, 255, 0)
                        if colorNum == '4':
                            Rcolor = (0, 0, 255)
                        rectlist.append(pygame.draw.rect(screen, Rcolor, k))
                # rectlist.append(r1)
                # rectlist.append(r2)
        # if not topSpeed:
        #     player = pygame.draw.rect(screen, black, (MoveX, max_height-MoveY, 20, 50))
        # elif topSpeed:
        #     player = pygame.draw.rect(screen, (255, 255, 0), (MoveX, max_height-MoveY, 20, 50))

        keys = list(pygame.key.get_pressed())
        if not (green2 or blue):
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
        elif green2:
            if keys[Right]:
                if forceX > -15:
                    forceX -= 0.4
                if abs(forceX) >= 15:
                    topSpeed = True
                elif abs(forceX) < 15:
                    topSpeed = False
            if keys[Left]:
                if forceX < 15:
                    forceX += 0.4
                if abs(forceX) >= 15:
                    topSpeed = True
                elif abs(forceX) < 15:
                    topSpeed = False
        elif blue:
            if keys[Down]:
                if forceX > -15:
                    forceX -= 0.4
                if abs(forceX) >= 15:
                    topSpeed = True
                elif abs(forceX) < 15:
                    topSpeed = False
            if keys[Up]:
                if forceX < 15:
                    forceX += 0.4
                if abs(forceX) >= 15:
                    topSpeed = True
                elif abs(forceX) < 15:
                    topSpeed = False
            if keys[Left]:
                if jumped:
                    if OnGround or onPlatform:
                        if forceY < 10:
                            forceY += 1
        if not blue:
            if keys[Up]:
                if jumped:
                    if OnGround or onPlatform:
                        if forceY < 10:
                            forceY += 1

        # player = pygame.draw.rect(screen, skyBlue, (MoveX, max_height-MoveY, 20, 50))
        # if keys[Left]:
        #     screen.blit(walugi, (MoveX, max_height-MoveY))
        #     oldwally = walugi
        # elif keys[Right]:
        #     screen.blit(waluigiLeft, (MoveX, max_height-MoveY))
        #     oldwally = waluigiLeft
        # else:
        #     screen.blit(oldwally, (MoveX, max_height-MoveY))

        if topSpeed:
            player = pygame.draw.rect(screen, (255, 255, 0), (MoveX, max_height-MoveY, 20, 50))
        else:
            player = pygame.draw.rect(screen, (0, 0, 0), (MoveX, max_height-MoveY, 20, 50))

        if not pause:
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
        if not pause:
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
                if not (screen.get_at(r.center) == (255, 255, 0) and topSpeed):
                    if not onPlatform:
                        MoveX -= forceX
                    onPlatform = False
                    jumped = False
                    if (forceX > 0) and (MoveX < r.left) and (not onPlatform):
                        MoveX -= abs(player.right - r.left)
                        forceX=0
                        topSpeed=False
                    elif (forceX < 0) and (player.right > r.right) and (not onPlatform):
                        MoveX += abs(r.right - player.left)
                        forceX=0
                        topSpeed=False
                    elif (forceY > 0) and (r.bottom > player.top) and (r.bottom < player.bottom):
                        MoveY = min(MoveY, max_height-r.bottom)
                        forceY = 0
                    elif (player.y < r.y):
                        # os.system('clear')
                        # print("MoveY: {}".format(MoveY))
                        # print("Top: {}".format(r.top))
                        # print("Sum: {}".format(r.top+MoveY))
                        MoveY = max(max_height-(r.top-player.height), MoveY)
                        if forceY < 0:
                            if screen.get_at(r.center) == (255, 0, 0):
                                forceY *= -1
                            elif screen.get_at(r.center) == (0, 255, 0):
                                green2=True
                                forceY = 0
                                onPlatform=True
                            elif screen.get_at(r.center) == (0, 0, 255):
                                blue=True
                                forceY = 0
                                onPlatform=True
                            else:
                                forceY = 0
                                onPlatform=True
                    if onPlatform:
                        MoveY = max(max_height-(r.top-player.height), MoveY)
                        if forceY < 0:
                            forceY = 0
                        if screen.get_at(r.center) != (255, 0, 0):
                            onPlatform=True
                        if screen.get_at(r.center) == (0, 255, 0):
                            green2=True
                        else:
                            green2=False
                        if screen.get_at(r.center) == (0, 0, 255):
                            blue=True
                        else:
                            blue=False
            elif onPlatform:
                onPlatform = False
                green2=False
                blue=False
                if forceY <= 0:
                    for r in rectlist:
                        if r.collidepoint(player.left, player.bottom) or r.collidepoint(player.right, player.bottom) or r.collidepoint(player.centerx, player.bottom):
                            onPlatform = True
                            if screen.get_at(r.center) == (0, 255, 0):
                                green2=True
                            if screen.get_at(r.center) == (0, 0, 255):
                                blue=True
        # Debug:
        # counter+=1
        # if counter % 10 == 0:
        #     counter=0
            # print("Force X: {}".format(forceX))
            # print("Force Y: {}".format(forceY))
            # print("OnGround: {}".format(OnGround))
            # print("OnPlatform: {}".format(onPlatform))
            # print("MoveX: {}".format(MoveX))
            # print("MoveY: {}".format(MoveY))
            # print("Top: {}".format(r.top))
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse2 = (0, 0)
                mouse1 = pygame.mouse.get_pos()
                Cheatnum = screen2
                for r in rectlist:
                    if r.collidepoint(mouse1):
                        writelist=[]
                        for i in range(len(list(rectdict.keys()))):
                            if list(rectdict.keys())[i] == (r.left, r.top, r.width, r.height):
                                if int(rectColor[i]) < 4:
                                    rectColor[i] = str(eval(rectColor[i]+"+1"))
                                else:
                                    rectColor[i] = '0'
                            writelist.append(str(list(rectdict.keys())[i])+" - "+str(rectdict[list(rectdict.keys())[i]])+" - "+str(rectColor[i])+"\n")
                        with open(r'levels.txt', 'w') as l:
                            for w in writelist:
                                l.write(w)
            if event.type == pygame.MOUSEBUTTONUP:
                mouse2 = pygame.mouse.get_pos()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    quit()
                if event.key == pygame.K_r:
                    Restart()
                if event.key == pygame.K_s:
                    level_save()
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_c:
                    with open(r'levels.txt', 'w') as l:
                        l.write("")
                if event.key == pygame.K_UP:
                    if OnGround or onPlatform:
                        if not blue:
                            forceY += 15
                            jumped = True
                if event.key == pygame.K_LEFT:
                    if blue:
                        if OnGround or onPlatform:
                            forceY += 15
                            jumped = True
                if event.key == pygame.K_SPACE:
                    if (mouse1 != (0, 0)) and (mouse2 != (0,0)):
                        left = min(mouse1[0], mouse2[0])
                        top = min(mouse1[1], mouse2[1])
                        top = max(51, top)
                        width = abs(mouse1[0]-mouse2[0])
                        height = abs(mouse1[1]-mouse2[1])
                        with open(r'levels.txt', 'a') as l:
                            l.write(str((left, top, width, height))+" - "+str(int(Cheatnum))+" - "+'0'+"\n")
                        level_save()
                if event.key == pygame.K_z:
                    undo()
                    level_save()
def Restart():
    global max_width, max_height, screen, startTime, skyBlue, brown, green, black, Right, Up, Left, Down, MoveX, MoveY, forceX, forceY, OnGround, onPlatform, topSpeed, jumped, screen2, screenNum, mouse1, mouse2, counter, walugi, waluigiLeft, Cheatnum, oldwally, rectdict, pause, rectColor, green2, blue
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
    mouse1 = (0, 0)
    mouse2 = (0, 0)
    Cheatnum=0
    OnGround = True
    onPlatform=False
    topSpeed = False
    jumped = False
    screen2=False
    pause=False
    screenNum = 0
    counter=0
    walugi = pygame.image.load(r"WAAA.png")
    walugi = pygame.transform.scale(walugi, (20, 50))
    waluigiLeft = pygame.transform.flip(walugi, True, False)
    oldwally = waluigiLeft
    rectdict={}
    rectColor=[]
    green2=False
    blue = False
    with open(r'levels.txt', 'r') as l:
        for line in l.readlines():
            if line != "":
                line = line.replace("\n", "")
                rectdict[eval(line.split(' - ')[0])] = int(line.split(' - ')[1])
                rectColor.append(line.split(' - ')[2])
    gameloop()
def level_save():
    global rectdict, mouse1, mouse2, rectColor
    rectdict={}
    rectColor=[]
    with open(r'levels.txt', 'r') as l:
        for line in l.readlines():
            if line != "":
                line = line.replace("\n", "")
                rectdict[eval(line.split(' - ')[0])] = int(line.split(' - ')[1])
                rectColor.append(line.split(' - ')[2])
    mouse1 = (0, 0)
    mouse2 = (0, 0)
def undo():
    with open(r'levels.txt', 'r') as r:
        data = r.readlines()
    with open(r'levels.txt', 'w') as l:
        l.writelines(data[:-1])
        
Restart()
