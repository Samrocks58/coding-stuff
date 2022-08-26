from random import randint
import pygame, time
from tkinter import Tk, messagebox

def rand_pos():
    return [randint(1, max_width), randint(1, max_height)]

def cord_find(x, y): return (x*25, y*25)

def restart():
    global screen, Red, Black, White, max_width, max_height, MoveX, MoveY, old_pos, direction, length, painted_snakes, coin, coinPos, keyPressed
    screen = pygame.display.set_mode((625, 500))
    Red = (255, 0, 0)
    Black = (0, 0, 0)
    White = (255, 255, 255)
    max_width = 25
    max_height = 20
    MoveX=14
    MoveY=10
    old_pos=(14, 10)
    direction=1 #1: right 2: up 3: left 4: down
    length = 5
    painted_snakes = [(10, 10), (11, 10), (12, 10), (13, 10)]
    coin = pygame.image.load(r'non-program bulcrapo/coin.png')
    coin = pygame.transform.scale(coin, (25, 25))
    coinPos = rand_pos()
    keyPressed=False
    gameloop()

def game_over():
    global length
    print(f"Score: {length}")
    root=Tk()
    root.wm_withdraw()
    MsgBox=messagebox.askyesno("You Died!!!", "Do you want to play again?")
    if MsgBox:
        root.destroy()
        restart()
    elif not MsgBox:
        root.destroy()
        quit()

def gameloop():
    global screen, Red, Black, White, max_width, max_height, MoveX, MoveY, old_pos, direction, length, painted_snakes, coin, coinPos, keyPressed
    while True:
        screen.fill(White)

        cord = cord_find(MoveX-1, MoveY-1)
        leadSnake = pygame.draw.rect(screen, Red, (cord[0], cord[1], 25, 25))
        screen.blit(coin, cord_find(coinPos[0]-1, coinPos[1]-1))
        for snake in painted_snakes:
            cord = cord_find(snake[0]-1, snake[1]-1)
            pygame.draw.rect(screen, Black, (cord[0], cord[1], 25, 25))
        
        keyPressed=False
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    quit()
                if not keyPressed:
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        if direction % 2 == 1:
                            direction=4
                            keyPressed=True
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        if direction % 2 == 1:
                            direction=2
                            keyPressed=True
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        if direction % 2 == 0:
                            direction=3
                            keyPressed=True
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_s:
                        if direction % 2 == 0:
                            direction=1
                            keyPressed=True
            if event.type == pygame.QUIT:
                quit()

        if (MoveX, MoveY) in painted_snakes:
            game_over()
        
        time.sleep(1/16)
        if direction == 1:
            MoveX += 1
        elif direction == 2:
            MoveY -= 1
        elif direction == 3:
            MoveX -= 1
        elif direction == 4:
            MoveY += 1

        if MoveX > max_width:
            MoveX=1
        if MoveX < 1:
            MoveX = max_width
        if MoveY > max_height:
            MoveY = 1
        if MoveY < 1:
            MoveY = max_height

        if [MoveX, MoveY] == coinPos:
            length += 1
            coinPos = rand_pos()

        painted_snakes.append(old_pos)
        old_pos=(MoveX, MoveY)
        if len(painted_snakes) > length:
            del painted_snakes[0]
        pygame.display.flip()
restart()