import pygame, time, os

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
topSpeed = False

while True:
    endTime = time.perf_counter()
    if 1/60 - (endTime - startTime) > 0:
        time.sleep(1/60 - (endTime - startTime))
    startTime=time.perf_counter()

    pygame.display.flip()
    screen.fill(skyBlue)

    pygame.draw.rect(screen, brown, (0, max_height-35, max_width, 35))
    pygame.draw.rect(screen, green, (0, max_height-50, max_width, 15))
    bouncey = pygame.draw.rect(screen, (255, 0, 0), (max_width-240, max_height-65, 40, 65))
    if not topSpeed:
        player = pygame.draw.rect(screen, black, (MoveX, max_height-MoveY, 20, 50))
    elif topSpeed:
        player = pygame.draw.rect(screen, (255, 255, 0), (MoveX, max_height-MoveY, 20, 50))


    keys = list(pygame.key.get_pressed())
    if keys[Right]:
        if forceX < 15:
            forceX += 0.5
        if abs(forceX) >= 15:
            topSpeed = True
        elif abs(forceX) < 15:
            topSpeed = False
    if keys[Left]:
        if forceX > -15:
            forceX -= 0.5
        if abs(forceX) >= 15:
            topSpeed = True
        elif abs(forceX) < 15:
            topSpeed = False
    if keys[Up]:
        if OnGround:
            if forceY < 10:
                forceY += 1
    if keys[Down]:
        if not OnGround:
            if forceY > 0:
                forceY -= 1

    MoveX += forceX
    MoveY += forceY

    if MoveY > 100:
        forceY -= 0.5
        OnGround=False
    elif MoveY <= 100:
        OnGround = True
        forceY = 0
    if (MoveX > max_width-20) or (MoveX < 0):
        forceX *= -1
    if player.colliderect(bouncey):
        if OnGround:
            if (player.left < bouncey.left) and (MoveX < bouncey.centerx):
                MoveX -= abs(player.right - bouncey.left)
                forceX=0
            if (player.right > bouncey.right) and (player.right > bouncey.centerx):
                MoveX += abs(bouncey.right - player.left)
                forceX=0
        else:
            if (player.bottom > bouncey.top):
                MoveY = max(115, MoveY)
                forceY=0
        
    # Debug:
    # print("Force X: {}".format(forceX))
    # print("Force Y: {}".format(forceY))
    # print("OnGround: {}".format(OnGround))
    # print("MoveX: {}".format(MoveX))
    # print("MoveY: {}".format(MoveY))
    # os.system('cls')

    if OnGround:
        if not topSpeed:
            if forceX < 0:
                forceX += 0.2
            elif forceX > 0:
                forceX -= 0.2
    
    MoveX=min(max_width-20, max(0, MoveX))
    MoveY=min(max_height, max(100, MoveY))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                quit()
            if event.key == pygame.K_UP:
                if OnGround:
                    forceY += 15
