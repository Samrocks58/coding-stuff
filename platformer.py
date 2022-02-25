import pygame, time

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
    time.sleep(1/60 - (endTime - startTime))
    startTime=time.perf_counter()

    pygame.display.flip()
    screen.fill(skyBlue)

    pygame.draw.rect(screen, brown, (0, max_height-35, max_width, 35))
    pygame.draw.rect(screen, green, (0, max_height-50, max_width, 15))
    pygame.draw.rect(screen, black, (MoveX, max_height-MoveY, 20, 50))

    keys = list(pygame.key.get_pressed())
    if keys[Right]:
        if forceX < 10:
            forceX += 1
        if abs(forceX) == 10:
            topSpeed = True
        elif abs(forceX) < 10:
            topSpeed = False
    if keys[Left]:
        if forceX > -10:
            forceX -= 1
        if abs(forceX) == 10:
            topSpeed = True
        elif abs(forceX) < 10:
            topSpeed = False
    # if keys[Up]:
    #     # if OnGround:
    #         if forceY < 10:
    #             forceY += 1
    #     # OnGround = False

    MoveX += forceX
    MoveY += forceY

    if MoveY > 100:
        forceY -= 0.5
        OnGround=False
    elif MoveY == 100:
        OnGround = True
        forceY=0

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