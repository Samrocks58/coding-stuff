import pygame, random

pygame.init()

pygame.display.init()

width=int(1200)
height=int(675)

Orange=(255, 95, 0)
Red=(255, 0, 0)
Black=(0, 0, 0)

X=600
Y=int(675/2)

MoveX=100
MoveY=675-100

screen = pygame.display.set_mode((width, height))  #, depth=0, flags=pygame.FULLSCREEN)
screen.fill(Black)

Results={}
Actions=[]


class Object():
    def right():
        MoveX += 20
        Action.append("right")
    def left():
        MoveX -= 20
        Action.append("left")
    def up():
        MoveY += 20
        Action.append("up")
    def down():
        MoveY -= 20
        Action.append("down")
    def random():
        for i in range(37):
            vary = random.randint(0, 4)
            if vary == 0:
                Object.right()
            if vary == 1:
                Object.left()
            if vary == 2:
                Object.up()
            if vary == 3:
                Object.down()
            
a=0
fitness=0
while True:
    pygame.display.flip()

    fitness=abs(MoveX - X) + abs(MoveY - Y)

    screen.fill(Black)
    pygame.draw.circle(screen, Orange, (MoveX, MoveY), 15)
    pygame.draw.circle(screen, Red, (X, Y), 50)

    if a == 0:
        Object.random()
        a += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(fitness)
            pygame.quit()
            quit()