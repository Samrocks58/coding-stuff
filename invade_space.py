import pygame, time
from level import level_select


level=level_select()
empty_spot=[]
if level == 1:
    empty_spot=[3,4,5, 6]
elif level == 2:
    empty_spot=[5,6]
elif level == 3:
    empty_spot=[5]
elif level == 4:
    empty_spot=[1]
elif level == 5:
    empty_spot=[10]
max_height=600
max_width=800
screen = pygame.display.set_mode((max_width, max_height))
pygame.joystick.init()
black=(0, 0, 0)
full_heart=pygame.image.load(r"non-program bulcrapo\Full_heart.png")
full_heart=pygame.transform.scale(full_heart, (36, 32))
half_heart=pygame.image.load(r"non-program bulcrapo\Half_heart.png")
half_heart=pygame.transform.scale(half_heart, (36, 32))
heart_x=full_heart.get_width()
heart_y=full_heart.get_height()
space_ship=pygame.image.load(r"non-program bulcrapo\space.png")
space_ship=pygame.transform.scale(space_ship, (70, 84))
red_ship=pygame.image.load(r"non-program bulcrapo\image.png")
red_ship=pygame.transform.scale(red_ship, (70, 84))
red_ship_flipped=pygame.transform.flip(red_ship, False, True)
opponent_ship=pygame.transform.flip(space_ship, False, True)
rect_x=space_ship.get_width()
rect_y=space_ship.get_height()
pygame.font.init()
score="00000000"
zig=pygame.font.Font(r"non-program bulcrapo\\zig.ttf", 30)
zigtxt=zig.render(score, False, (255, 255, 255))
zigWidth=zigtxt.get_width()
zigHeight=zigtxt.get_height()


Left=80+93
Right=79+93
Up=82
Down=81
A=97
D=100

MoveX=max_width//2-rect_x//2
MoveY=max_height-rect_y

# def frame_avg(list):
#     sum=0
#     for i in list:
#         if i < 800:
#             sum += i
#     return sum // len(list)

# fps=1/time_delta_time
# fps_list.append(fps)
# # print(f"Average FPS: {frame_avg(fps_list)}")

start_time=time.perf_counter()
fps_list=[]
shots=[]
opponent_shots=[]
parry_shots=[]
hit=False
playerHit=False
shield_out=False
hitpoints=6
full_heart_pos=[[0, 0], [heart_x, 0], [heart_x*2, 0]]
half_heart_pos=0
if hitpoints != 6:
    if hitpoints > 0:
        full_heart_pos=[]
        for i in range(hitpoints//2):
            full_heart_pos.append([i*heart_x, 0])
        if hitpoints % 2 == 1:
            if hitpoints // 2 > 0:
                half_heart_pos=[full_heart_pos[-1][0]+heart_x, 0]
            elif hitpoints > 0:
                half_heart_pos=[0, 0]
        elif hitpoints % 2 == 0:
            half_heart_pos=0
hitTime2=time.perf_counter()
opponentHitTime2=time.perf_counter()
opponentHitCounter=0

class Opponent():
    def __init__(self, pos, image):
        self.pos=self.get_pos(pos)
        self.x=self.pos[0]
        self.y=self.pos[1]
        self.image=image
        self.hit=False
        self.shots=[]
        self.dead=False
        self.rect=image.get_rect(center=(self.x+rect_x//2, self.y+rect_y//2))
        self.health=2
        self.parried=False
    def get_pos(self, ordered_pair):
        return [(ordered_pair[0]-1)*80, heart_y]

opponentShips={}
for i in range(1, 11):
    stringkey="op"+str(i)
    if not i in empty_spot:
        opponentShips[stringkey] = Opponent((i, heart_y), opponent_ship)

def lazer_shoot(x, y):
    shots.append([x+rect_x//2-3, y-25])

def opponent_shoot():
    opponent_shots.append([max_width//2-3, rect_y])

def game_over():
    return
    quit()

def add_score(num):
    global score
    added_score=str(int(score)+num)
    added_score="0"*(8-len(added_score))+added_score if len(added_score) < 8 else added_score
    score=added_score

def hitPointChange():
    global hitpoints, full_heart_pos, half_heart_pos
    hitpoints -= 1
    if hitpoints > 0:
        full_heart_pos=[]
        for i in range(hitpoints//2):
            full_heart_pos.append([i*heart_x, 0])
        if hitpoints % 2 == 1:
            if hitpoints // 2 > 0:
                half_heart_pos=[full_heart_pos[-1][0]+heart_x, 0]
            elif hitpoints > 0:
                half_heart_pos=[0, 0]
        elif hitpoints % 2 == 0:
            half_heart_pos=0
    else:
        half_heart_pos=0
        game_over()
    
pygame.mouse.set_visible(False)
while True:
    end_time=time.perf_counter()
    if 1/(end_time-start_time) < 2000:
        time_delta_time=end_time-start_time
    else:
        time_delta_time=1/500
    start_time=time.perf_counter()
    screen.fill(black)
    if opponentHitCounter >= 1:
        add_score(10)
        opponentHitCounter -= 1
    zigtxt=zig.render(score, False, (255, 255, 255))
    screen.blit(zigtxt, (max_width//2-zigWidth//2, 0))
    for i in full_heart_pos:
        screen.blit(full_heart, i)
    if half_heart_pos != 0:
        screen.blit(half_heart, half_heart_pos)
    for op in opponentShips:
        if not opponentShips[op].hit:
            if not opponentShips[op].dead:
                screen.blit(opponentShips[op].image, opponentShips[op].pos)
        elif opponentShips[op].hit:
            if not opponentShips[op].dead:
                    screen.blit(red_ship_flipped, opponentShips[op].pos)
            opponentHitTime=time.perf_counter()
            if opponentHitTime-opponentHitTime2 > 0.05:
                opponentShips[op].health -= 1
                if not opponentShips[op].dead:
                    if opponentShips[op].parried:
                        opponentHitCounter += 10
                    if not opponentShips[op].parried:
                        opponentHitCounter += 5
                if opponentShips[op].health <= 0:
                    opponentShips[op].dead = True
            opponentHitTime2=time.perf_counter()
            opponentShips[op].hit=False
    if not playerHit:
        screen.blit(space_ship, (MoveX, MoveY))
    elif playerHit:
        screen.blit(red_ship, (MoveX, MoveY))
        hitTime=time.perf_counter()
        if hitTime-hitTime2 > 0.1:
            hitPointChange()
        hitTime2=time.perf_counter()
        playerHit=False
    pygame.draw.line(screen, (255, 255, 255), (0, heart_y), (max_width, heart_y))

    # vvvvvvvvvvv Looping Code vvvvvvvvvvvvvv
    # if MoveX > max_width-rect_x:
    #     overRight=True
    #     out_of_frame=MoveX-(max_width-rect_x)
    #     screen.blit(space_ship, (0-rect_x+out_of_frame, MoveY))
    # if MoveX <   0:
    #     overLeft=True
    #     overhang=0-MoveX
    #     screen.blit(space_ship, (max_width-overhang, MoveY))
    # if MoveX >= max_width:
    #     MoveX=0
    # if MoveX <= 0-rect_x:
    #     MoveX=max_width-rect_x-1
    # if MoveX > 0 and MoveX < 800:
    #     overLeft=False
    #     overRight=False
    joysticks = []
    num_joystick=pygame.joystick.get_count()
    for i in range(num_joystick):
        joysticks += pygame.joystick.Joystick(i)
    if len(joysticks) >= 1:
        controller = joysticks[0]
        axes=[]
        for i in controller.get_numaxes():
            axes += controller.get_axis(i)
        print(len(joysticks))

    for op in opponentShips:
        if len(opponentShips[op].shots) < 1:
            if not opponentShips[op].parried:
                if not opponentShips[op].dead:
                    opponentShips[op].shots.append([opponentShips[op].rect.centerx-3, rect_y])
    if len(shots) > 0:
        for op in opponentShips:
            for position in shots:
                if not opponentShips[op].rect.collidepoint(position):
                    pygame.draw.rect(screen, (255, 0, 0), (position[0], position[1], 7, 25))
                elif opponentShips[op].rect.collidepoint(position):
                    opponentShips[op].hit=True
    if len(parry_shots) > 0:
        for op in opponentShips:
            for position in parry_shots:
                if not opponentShips[op].rect.collidepoint(position):
                    pygame.draw.rect(screen, (255, 0, 255), (position[0], position[1], 7, 25))
                elif opponentShips[op].rect.collidepoint(position):
                    opponentShips[op].hit=True
    for op in opponentShips:
        if len(opponentShips[op].shots) > 0:
            playerRect = space_ship.get_rect(center=(MoveX+rect_x//2, MoveY+rect_y//2))
            for oppPos in opponentShips[op].shots:
                if not playerRect.collidepoint(oppPos):
                    if shield_out:
                        if not oppPos[1] >= MoveY-10-25:
                            pygame.draw.rect(screen, (255, 0, 0), (oppPos[0], oppPos[1], 7, 25))
                        if not (oppPos[0] >= MoveX-10 and oppPos[0] <= MoveX-10+rect_x+20):
                            pygame.draw.rect(screen, (255, 0, 0), (oppPos[0], oppPos[1], 7, 25))
                    if not shield_out:
                        pygame.draw.rect(screen, (255, 0, 0), (oppPos[0], oppPos[1], 7, 25))
                elif oppPos[1] >= MoveY-10-25-5:
                    if shield_out:
                        parryTime2=time.perf_counter()
                        if parryTime2-parryTime <= 10*time_delta_time: # Old time : 0.2 seconds
                            parry_shots.append(oppPos)
                            opponentShips[op].parried=True
                            del opponentShips[op].shots[opponentShips[op].shots.index(oppPos)]
                    elif not shield_out:
                        playerHit=True
                elif not shield_out:
                    playerHit=True


    keys=pygame.key.get_pressed()
    # for i in range(len(keys)):
    #     if keys[i] == 1:
    #         print(i)
    # for i in keys:
    #     if i == 1:
    #         print(keys.index(i))
    if keys[Left]:
        MoveX -= 3 * time_delta_time * 200
    if keys[Right]:
        MoveX += 3 * time_delta_time * 200
    if keys[A] == 1:
        MoveX -= 3 * time_delta_time * 200
    if keys[D] == 1:
        MoveX += 3 * time_delta_time * 200
    if keys[115]:
        shield = pygame.draw.rect(screen, (0, 0, 255), (MoveX-10, MoveY-12, rect_x+20, 10))
        shield_out=True
    if not keys[115]:
        shield_out=False
    
    pygame.display.flip()
    #  vvvvvvvvvvv Bordering Code vvvvvvvvvv
    MoveX=max(0, min(MoveX, max_width-rect_x))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                quit()
            if event.key == pygame.K_s:
                parryTime=time.perf_counter()
            if event.key == pygame.K_y:
                hitPointChange()
            if event.key == pygame.K_SPACE:
                if len(shots) <= 1:
                    # play.play(r"retro_sound_effect.wav")
                    if not shield_out:
                        lazer_shoot(MoveX, MoveY)
                    # if overRight:
                    #     lazer_shoot(0-rect_x+out_of_frame, MoveY)
                    # if overLeft:
                    #     lazer_shoot(max_width-overhang, MoveY)
    if len(shots) > 0:
        for i in shots:
            i[1] -= 5 * time_delta_time * 200
            if i[1] < heart_y:
                del shots[shots.index(i)]
    for op in opponentShips:
        if len(opponentShips[op].shots) > 0:
            for i in opponentShips[op].shots:
                i[1] += 5 * time_delta_time * 200
                if i[1] > max_height:
                    del opponentShips[op].shots[opponentShips[op].shots.index(i)]
    if len(parry_shots) > 0:
        for i in parry_shots:
            i[1] -= 5 * time_delta_time * 200
            if i[1] < heart_y:
                del parry_shots[parry_shots.index(i)]
                for op in opponentShips:
                    opponentShips[op].parried=False