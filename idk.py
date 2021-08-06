import pygame, random

pygame.init()

pygame.display.init()

width=int(1200)
height=int(600)

Orange=(255, 95, 0)
Red=(255, 0, 0)
Black=(0, 0, 0)

X=600
Y=int(600/2)

# MoveX=100
# MoveY=700

screen = pygame.display.set_mode((width, height))  #, depth=0, flags=pygame.FULLSCREEN)
screen.fill(Black)

Results={}
# Actions=[]


class Object():
    def __init__(self):
        self.MoveX = 100
        self.MoveY = 500
        self.Action = []
        self.Done = False
    def right(self):
        self.MoveX += 20
        self.Action.append("right")
    def left(self):
        self.MoveX -= 20
        self.Action.append("left")
    def up(self):
        self.MoveY += 20
        self.Action.append("up")
    def down(self):
        self.MoveY -= 20
        self.Action.append("down")
    def random(self):
        last_move=""
        possible_moves=["right", "left", "up", "down"]
        for i in range(60):
            if last_move == "right":
                possible_moves=["left", "up", "down"]
            elif last_move == "left":
                possible_moves=["right", "up", "down"]
            elif last_move == "up":
                possible_moves=["right", "left", "down"]
            elif last_move == "down":
                possible_moves=["right", "left", "up"]
            vary = random.randint(0, len(possible_moves)-1)
            if possible_moves[vary] == "right":
                self.right()
                last_move="right"
            if possible_moves[vary] == "left":
                self.left()
                last_move="left"
            if possible_moves[vary] == "up":
                self.up()
                last_move="up"
            if possible_moves[vary] == "down":
                self.down()
                last_move="down"
dots = {}
for i in range(100):
    dots[f"dot{i}"] = Object()

generationDone=False
fitness=0
radius=10
while True:
    pygame.display.flip()
    screen.fill(Black)

    keys=list(dots.keys())
    for dotname in keys:
        dots[dotname].MoveX = min(1200-radius, max(radius, dots[dotname].MoveX))
        dots[dotname].MoveY = min(600-radius, max(radius, dots[dotname].MoveY))
        # fitness=abs(dots[dotname].MoveX - X) + abs(dots[dotname].MoveY - Y)
        pygame.draw.circle(screen, Orange, (dots[dotname].MoveX, dots[dotname].MoveY), radius)
        if not dots[dotname].Done:
            dots[dotname].random()
            dots[dotname].Done = True

    pygame.draw.circle(screen, Red, (X, Y), 50)
    pygame.draw.circle(screen, Red, (100, 500), 4)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                print(fitness)
                pygame.quit()
                quit()
        if event.type == pygame.QUIT:
            print(fitness)
            pygame.quit()
            quit()