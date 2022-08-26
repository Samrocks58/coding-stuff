from math import sqrt
from statistics import median
import pygame, random

pygame.init()

pygame.display.init()

width=int(1200)
height=int(600)

Orange=(255, 95, 0)
Red=(255, 0, 0)
Black=(0, 0, 0)

X=800
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
        self.fitness = 0
        self.moves=0
        self.possible_moves=["right", "left", "up", "down"]
    def right(self):
        oldFitness = self.calcFitness()
        self.MoveX += 20
        self.Action.append("right")
        self.calcFitness()
        if self.fitness < oldFitness:
            self.possible_moves=["right", "up", "down"]
        elif self.fitness > oldFitness:
            self.possible_moves=["left", "up", "down"]
        self.moves += 1
    def left(self):
        oldFitness = self.calcFitness()
        self.MoveX -= 20
        self.Action.append("left")
        self.calcFitness()
        if self.fitness < oldFitness:
            self.possible_moves=["left", "up", "down"]
        elif self.fitness > oldFitness:
            self.possible_moves=["right", "up", "down"]
        self.moves += 1
    def up(self):
        oldFitness = self.calcFitness()
        self.MoveY += 20
        self.Action.append("up")
        self.calcFitness()
        if self.fitness < oldFitness:
            self.possible_moves=["right", "left", "up"]
        elif self.fitness > oldFitness:
            self.possible_moves=["right", "left", "down"]
        self.moves += 1
    def down(self):
        oldFitness = self.calcFitness()
        self.MoveY -= 20
        self.Action.append("down")
        self.calcFitness()
        if self.fitness < oldFitness:
            self.possible_moves=["right", "left", "down"]
        elif self.fitness > oldFitness:
            self.possible_moves=["right", "left", "up"]
        self.moves += 1
    def random(self):
        for i in range(60):
            vary = random.randint(0, len(self.possible_moves)-1)
            if self.moves < 60:
                if self.possible_moves[vary] == "right":
                    self.right()
                if self.possible_moves[vary] == "left":
                    self.left()
                if self.possible_moves[vary] == "up":
                    self.up()
                if self.possible_moves[vary] == "down":
                    self.down()
    def calcFitness(self):
        self.fitness = abs(sqrt((dots[dotname].MoveX - X)**2 + (dots[dotname].MoveY - Y)**2))
        return abs(sqrt((dots[dotname].MoveX - X)**2 + (dots[dotname].MoveY - Y)**2))
    def copy(self, copyObject):
        for i in copyObject.Action:
            if i == "up":
                self.MoveY += 20
                self.Action.append("up")
            elif i == "down":
                self.MoveY -= 20
                self.Action.append("down")
            elif i == "right":
                self.MoveX += 20
                self.Action.append("right")
            elif i == "left":
                self.MoveX -= 20
                self.Action.append("left")
        self.calcFitness()

dots = {}
for i in range(100):
    dots["dot"+str(i)] = Object()

generationDone=False
generationCounter=0
highestFitness=0
fitnessLst = []
radius=10
oldmousepos = (X, Y)
while True:

    pygame.display.flip()
    screen.fill(Black)
    mousepos = pygame.mouse.get_pos()

    keys=list(dots.keys())
    for dotname in keys:
        if dotname == "dot1":
            if not dots[dotname].Done:
                highestFitness = dots[dotname].calcFitness()
        dots[dotname].MoveX = min(1200-radius, max(radius, dots[dotname].MoveX))
        dots[dotname].MoveY = min(600-radius, max(radius, dots[dotname].MoveY))
        # fitness=abs(dots[dotname].MoveX - X) + abs(dots[dotname].MoveY - Y)
        pygame.draw.circle(screen, Orange, (dots[dotname].MoveX, dots[dotname].MoveY), radius)
        if not dots[dotname].Done:
            dots[dotname].random()
            dots[dotname].Done = True
            generationDone=True
            generationCounter += 1
            dots[dotname].calcFitness()
            fitnessLst.append(dots[dotname].fitness)
            if dots[dotname].fitness < highestFitness:
                highestFitness = dots[dotname].calcFitness()
    fitnessLst.sort()
    fitnessMedian = median(fitnessLst)
    if generationDone:
        for d in keys:
            generationDone=False
            if dots[d].fitness > fitnessMedian:
                if len(dots) > 3:
                    del dots[d]
                for dotname in keys:
                    if dotname in list(dots.keys()):
                        if dots[dotname].fitness == highestFitness:
                            newdot = Object()
                            dots["dot" + str(list(dots.keys())[-1][-3])] = newdot.copy(dots[dotname])
            if generationCounter <= 20:
                if d in list(dots.keys()):
                    dots[d].Done=False
            

    pygame.draw.circle(screen, Red, (mousepos), 50)
    pygame.draw.circle(screen, Red, (100, 500), 4)

    if abs(mousepos[0]-X) >= 50:
        generationDone=True
        generationCounter=0
        oldmousepos=mousepos
    elif abs(mousepos[1]-Y) >= 50:
        generationDone=True
        generationCounter=0
        oldmousepos=mousepos

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                print(highestFitness)
                pygame.quit()
                quit()
        if event.type == pygame.QUIT:
            print(highestFitness)
            pygame.quit()
            quit()