import pygame, time, random
import tkinter as tk
from tkinter import messagebox as mb, ttk, Tk

pygame.display.init()
pygame.font.init()

width=int(1200)
height=int(600)
Orange=(255, 95, 0)
white=(255, 255, 255)
Red=(255, 0, 0)
Black=(0, 0, 0)

screen = pygame.display.set_mode((width, height))#, depth=0, flags=pygame.FULLSCREEN)
screen.fill(white)
Font=pygame.font.Font(r'C:\Users\smprc\Downloads\gibster\GibsterRegular.ttf', 100)

total_width=48
total_height=24

stopgame=False

class snake:
    def __init__(self, direction, coord, id):
        self.direction=direction
        self.cord = coord
        self.id=id
        self.queue=[]
        global cord
        cord=self.cord
        if self.id == 1:
            global snake1_cord
            snake1_cord=self.cord
    #direction = [right if positive, down if positive]
    def move(self, cord):
        global snakes, stopgame
        snake1bool=False
        if self.id == 1:
            global snake1_cord
            snake1_cord = self.cord
            snake1bool=True
        else:
            snake1bool=False
        self.queue.append(self.direction)
        if self.direction == "right":
            if cord[0] >= total_width-1:
                if snake1bool:
                    for s in snakes:
                        if snakes[s].cord == [0, snake1_cord[1]]:
                            stopgame=True
                if not stopgame:
                    cord[0] = 0
            else:
                if snake1bool:
                    for s in snakes:
                        if [snake1_cord[0]+1, snake1_cord[1]] == snakes[s].cord:
                            stopgame=True
                if not stopgame:
                    cord[0] = cord[0]+1
        if self.direction == "left":
            if cord[0] <= 0:
                if snake1bool:
                    for s in snakes:
                        if [total_width-1, snake1_cord[1]] == snakes[s].cord:
                            stopgame=True
                if not stopgame:
                    cord[0] = total_width-1
            else:
                if snake1bool:
                    for s in snakes:
                        if [snake1_cord[0]-1, snake1_cord[1]] == snakes[s].cord:
                            stopgame=True
                if not stopgame:
                    cord[0] = cord[0]-1
        if self.direction == "up":
            if cord[1] <= 0:
                if snake1bool:
                    for s in snakes:
                        if [snake1_cord[0], total_height-1] == snakes[s].cord:
                            stopgame=True
                if not stopgame:                        
                    cord[1] = total_height-1
            else:
                if snake1bool:
                    for s in snakes:
                        if [snake1_cord[0], snake1_cord[1]-1] == snakes[s].cord:
                            stopgame=True
                if not stopgame:
                    cord[1] = cord[1]-1
        if self.direction == "down":
            if cord[1] >= total_height-1:
                if snake1bool:
                    for s in snakes:
                        if [snake1_cord[0], 0] == snakes[s].cord:
                            stopgame=True
                if not stopgame:
                    cord[1] = 0
            else:
                if snake1bool:
                    for s in snakes:
                        if [snake1_cord[0], snake1_cord[1]+1] == snakes[s].cord:
                            stopgame=True
                if not stopgame:
                    cord[1] = cord[1]+1


    def coordinate(self, ordered_pair):
        side_length=25
        return ordered_pair[0]*side_length, ordered_pair[1]*side_length


    def change_direction(self, orientation):
        global snakes
        keys=list(snakes.keys())
        if self.direction == "up" or self.direction == "down":
            if orientation == "right":
                self.direction="right"
            if orientation == "left":
                self.direction="left"
        if self.direction == "right" or self.direction == "left":
            if orientation == "up":
                self.direction="up"
            if orientation == "down":
                self.direction="down"
        if snakes[keys[-1]].id == self.id:
            return True
    #variableName = ['stuff', 'things', 'stuffs', 'thingmaybe', 'objects', 'nameLater', 'thinkOfBetterNameLater', 'pog','pogchamp', 'absloutePoggers']

    def follow(self, front_snake, snake_number):
        if len(front_snake.queue) > snake_number:
            new_direction=front_snake.queue[-1]
            del front_snake.queue[-1]
            # new_direction=front_snake.queue.get()
            if self.change_direction(new_direction):
                return True


    def create_snake(self):
        global snakes
        keys=list(snakes.keys())
        last_int=int(snakes[keys[-1]].id)+1
        name="snake"+str(last_int)
        if self.direction == "right":
            new_cord=[self.cord[0]-1, self.cord[1]]
        elif self.direction == "left":
            new_cord=[self.cord[0]+1, self.cord[1]]
        elif self.direction == "up":
            new_cord=[self.cord[0], self.cord[1]+1]
        elif self.direction == "down":
            new_cord=[self.cord[0], self.cord[1]-1]
        snakes[name] = snake(self.direction, new_cord, last_int)
        #self.cord


snakes={"snake1":snake("right", [24, 12], 1), "snake2":snake("right", [23, 12], 2), "snake3":snake("right", [22, 12], 3), "snake4":snake("right", [21, 12], 4), "snake5":snake("right", [20, 12], 5)}
snake1 = snake("right", [24, 12], 1)
snake2 = snake("right", [23, 12], 2)
snake3 = snake("right", [22, 12], 3)
snake4 = snake("right", [21, 12], 4)
snake5 = snake("right", [20, 12], 5)
blocklist=[snake1, snake2, snake3, snake4, snake5]
target_list=[]

class counterClass:
    def __init__(self):
        self.score=5
        self.font=Font
        self.txt=self.font.render(str(self.score), False, Orange)
    def render(self):
       self.txt=self.font.render(str(self.score), False, Orange)
counter=counterClass()

class object:
    def __init__(self):
        self.cord=self.random_pos()# Center: [24, 12]
        self.image=pygame.image.load(r"C:\Users\smprc\AppData\Local\Programs\Microsoft VS Code\coding files\my programs\non-program bulcrapo\coin.png")
        self.scaled_image=pygame.transform.scale(self.image, (25, 25))
        global object_cord
        object_cord = self.cord
    def random_pos(self):
        global snakes, snake1_cord
        pos_done=False
        while not pos_done:
            rand_pos=[random.randint(1, 47), random.randint(1, 23)]
            for snake_string in snakes:
                if snakes[snake_string].cord != rand_pos:
                    keys=list(snakes.keys())
                    if snakes[keys[0]].direction == "right" or snakes[keys[0]].direction == "left":
                        if abs((snake1_cord[1]-rand_pos[1])) > 3:
                            if not rand_pos[0] in [1, 2, 3] and not rand_pos[1] in [1, 2, 3]:
                                pos_done=True
                                return rand_pos
                    if snakes[keys[0]].direction == "up" or snakes[keys[0]].direction == "down":
                        if abs((snake1_cord[0] - rand_pos[0])) > 3:
                            if not rand_pos[0] in [1, 2, 3] and not rand_pos[1] in [1, 2, 3]:
                                pos_done=True
                                return rand_pos
    def create_target(self):
        global target_list
        while len(target_list) < 1:
            pos=self.cord
            target_list.append(pos)
    def coordinate(self, ordered_pair):
        side_length=25
        return ordered_pair[0]*side_length, ordered_pair[1]*side_length
    def destroy_target(self):
        global target_list
        for i in target_list:
            target_list.remove(i)
        target_list.clear()

restartbool=False
def restart():
    global snakes, snake1, snake2, snake3, snake4, snake5, counter, target_list, blocklist, restartbool, screen, rectlist, stopgame
    restartbool=True
    stopgame=False
    snakes={"snake1":snake("right", [24, 12], 1), "snake2":snake("right", [23, 12], 2), "snake3":snake("right", [22, 12], 3), "snake4":snake("right", [21, 12], 4), "snake5":snake("right", [20, 12], 5)}
    snake1 = snake("right", [24, 12], 1)
    snake2 = snake("right", [23, 12], 2)
    snake3 = snake("right", [22, 12], 3)
    snake4 = snake("right", [21, 12], 4)
    snake5 = snake("right", [20, 12], 5)
    blocklist=[snake1, snake2, snake3, snake4, snake5]
    target_list=[]
    del counter
    counter=counterClass()
    rectlist=[]
    gameloop()
def die():
    root=Tk()
    root.wm_withdraw()
    # root.mainloop()
    MsgBox=mb.askyesno("You Died!!!", "Do you want to play again?")
    if MsgBox:
        root.destroy()
        restart()
    elif not MsgBox:
        root.destroy()
        quit()

key_pressed=False
def check_inputs():
    global key_pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            # if snake.direction == "right" or snake.direction == "left":
            if not key_pressed:
                if event.key == pygame.K_UP:
                    snakes["snake1"].change_direction("up")
                    key_pressed=True
                elif event.key == pygame.K_DOWN:
                    snakes["snake1"].change_direction("down")
                    key_pressed=True
                # if snake.direction == "up" or snake.direction == "down":
                elif event.key == pygame.K_RIGHT:
                    snakes["snake1"].change_direction("right")
                    key_pressed=True
                elif event.key == pygame.K_LEFT:
                    snakes["snake1"].change_direction("left")
                    key_pressed=True
                elif event.key == pygame.K_w:
                    snakes["snake1"].change_direction("up")
                    key_pressed=True
                elif event.key == pygame.K_s:
                    snakes["snake1"].change_direction("down")
                    key_pressed=True
                elif event.key == pygame.K_a:
                    snakes["snake1"].change_direction("left")
                    key_pressed=True
                elif event.key == pygame.K_d:
                    snakes["snake1"].change_direction("right")
                    key_pressed=True
            if event.key == pygame.K_q:
                quit()
            if event.key == pygame.K_r:
                restart()
rectlist=[]
def gameloop():
    global key_pressed, target_list, snake1_cord, object_cord, snakes, counter, restartbool, screen
    restartbool=False
    pygame.display.init()
    while not restartbool:
        pygame.display.flip()
        screen.fill(white)
        for i in snakes:
            rectlist.append([snakes[i].coordinate(snakes[i].cord), (25, 25)])
        pygame.draw.rect(screen, Red, rectlist[0])
        for a in range(1, len(rectlist)):
            pygame.draw.rect(screen, Black, rectlist[a])
        rectlist.clear()
        screen.blit(counter.txt, [0, 0])
        if len(target_list) == 0:
            target_object=object()
            target_object.create_target()
        if len(target_list) == 1:
            screen.blit(target_object.scaled_image, target_object.coordinate(target_object.cord))
        if stopgame:
            die()
        key_pressed=False
        check_inputs()
        time.sleep(1/16)
        for snake in snakes:
            if snake != "snake1":
                keys=list(snakes.keys())
                values=list(snakes.values())
                done = snakes[snake].follow(values[keys.index(snake)-1], keys.index(snake)+1)
        if len(target_list) == 1:
            if snake1_cord == object_cord:
                target_list.clear()
                del target_object
                keys=list(snakes.keys())
                if done:
                    snakes[keys[-1]].create_snake()
                else:
                    while not done:
                        if done:
                            snakes[keys[-1]].create_snake()
                counter.score += 1
                counter.render()
        for i in snakes:
            snakes[i].move(snakes[i].cord)
        # for snake in snakes:
        #     if snake != "snake1":
        #         if snakes[snake].cord == snake1_cord:
        #             break
# t1=threading.Thread(target=check_inputs)
# t2=threading.Thread(target=gameloop)

# t1.start()
# t2.start()
gameloop()