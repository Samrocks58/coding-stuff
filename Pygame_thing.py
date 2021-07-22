import pygame, time, random

boolean=True

pygame.display.init()
pygame.joystick.init()

width=int(1200)
height=int(675)

MoveX=int(width/2)
MoveY=int(height/2)+3

Orange=(255, 95, 0)
white=(255, 255, 255)
Black=(0, 0, 0)

Center_Point=(MoveX, MoveY)
Radius = 40

Target = pygame.image.load(r"C:\Users\spear\OneDrive\Desktop\Desktop Folder\new target.png")
Target = pygame.transform.scale(Target, (100, 100))

Cusor_width=50
Cursor_height=50

Cursor_icon = pygame.image.load(r"C:\Users\spear\OneDrive\Desktop\Desktop Folder\cursor target.png")
Cursor_icon = pygame.transform.scale(Cursor_icon, (Cusor_width, Cursor_height))

screen = pygame.display.set_mode((width, height))#, depth=0, flags=pygame.FULLSCREEN)
screen.fill(white)

Object = pygame.draw.circle(screen, Orange, Center_Point, Radius)

speed=7.5

target_lst=[]
I_dont_care_anymore=[]
RectList=[]
num_rect=5
while True:
    def create_target():
        full=(len(I_dont_care_anymore) == num_rect)
        if len(I_dont_care_anymore) <= num_rect:
            randit=([random.randint(50, 1150), random.randint(50, 625)])
            if not full:
                time.sleep(0.001*random.randrange(1, 10))
            target_lst.append([randit[0], randit[1]])
            I_dont_care_anymore.append([randit[0]-50, randit[1]-50])
        try:
            global Rect1, Rect2, Rect3, Rect4, Rect5, RectList
            Rect1 = pygame.draw.rect(screen, Orange, [(target_lst[0][0]-50), (target_lst[0][1]-50), 100, 100])
            Rect2 = pygame.draw.rect(screen, Orange, [(target_lst[1][0]-50), (target_lst[1][1]-50), 100, 100])
            Rect3 = pygame.draw.rect(screen, Orange, [(target_lst[2][0]-50), (target_lst[2][1]-50), 100, 100])
            Rect4 = pygame.draw.rect(screen, Orange, [(target_lst[3][0]-50), (target_lst[3][1]-50), 100, 100])
            Rect5 = pygame.draw.rect(screen, Orange, [(target_lst[4][0]-50), (target_lst[4][1]-50), 100, 100])
            RectList=[Rect1, Rect2, Rect3, Rect4, Rect5]
        except IndexError:
            pass
        global rect_x
        global rect_y
        rect_x=[]
        rect_y=[]
        for box in target_lst:
            rect_x.append(box[0])
            rect_y.append(box[1])
        for coordinate in target_lst:
            for a in range(len(target_lst)):
                try:
                    if coordinate == target_lst[a]:
                        pass
                    else:
                        for r in RectList:
                            if r.collidepoint(coordinate):
                                I_dont_care_anymore.remove(I_dont_care_anymore[target_lst.index(coordinate)])
                                target_lst.remove(coordinate)
                except Exception:
                    pass
    def remove_target(X, Y):
        global RectList, I_dont_care_anymore, target_lst, rect_x, rect_y
        for rect in RectList:
            if rect.collidepoint(X, Y):
                print("yay")
                print(f"target list: {target_lst}")
                print(f"rect_x: {rect_x}")
                print(f"rect_y: {rect_y}")
                print(f"i don't care anymore: {I_dont_care_anymore}")
                print(f"rect coordinate: {rect.centerx, rect.centery}")
                print(f"rect index: {(RectList.index(rect))}")
                print(f"moveX, moveY: {MoveX, MoveY}")
                target_lst.remove((rect.centerx, rect.centery))
                I_dont_care_anymore.remove((rect.centerx, rect.centery))
                time.sleep(5)
                #(112, 378)
                        # elif abs((coordinate[1])-(target_lst[a][1])) <= 30:
                        #     I_dont_care_anymore.remove(I_dont_care_anymore[target_lst.index(coordinate)])
                        #     target_lst.remove(coordinate)
                

                                
    #start_time=time.clock()
    pygame.display.flip()
    pygame.joystick.init()
    for i in range(pygame.joystick.get_count()):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        hats=joystick.get_numhats()
        for i in range(hats):
            hat = joystick.get_hat(i)   
        hatx, haty = hat
        x = round(joystick.get_axis(0), 1) * speed
        y = round(joystick.get_axis(1), 1) * speed
        trigger = round(joystick.get_axis(2), 1)
        x2 = round(joystick.get_axis(4), 1) * speed
        y2 = round(joystick.get_axis(3), 1) * speed
        buttonA = joystick.get_button(0)
        buttonX = joystick.get_button(2)
        buttonY = joystick.get_button(3)
        buttonB = joystick.get_button(1)
        Left_Bumper=joystick.get_button(4)
        Right_Bumper=joystick.get_button(5)
    
        if abs(x) > 0:
            if buttonA:
                MoveX += int(x*5)
                MoveX=min(1160, max(40, MoveX))
            else:
                MoveX += int(x)
                MoveX=min(1160, max(40, MoveX))
        if abs(y) > 0:
            if buttonA:
                MoveY += int(y*5)
                MoveY=min(635, max(40, MoveY))
            else:
                MoveY += int(y)
                MoveY=min(635, max(40, MoveY))
        Center_Point=(MoveX, MoveY)
    if pygame.joystick.get_count() == 0:
        pygame.mouse.set_visible(False)
        if boolean:
            MoveX, MoveY = pygame.mouse.get_pos()
            Center_Point=MoveX, MoveY
            #MoveY=min(635, max(40, MoveY))
            #MoveX=min(1160, max(40, MoveX))
    create_target()
    create_target()
    create_target()
    create_target()
    create_target()
        #if not boolean:
            #for i in pygame._sdl2.touch.get_num_devices():
            #    thing=pygame._sdl2.touch.get_device(i)
            #    print(pygame._sdl2.touch.get_num_fingers(thing))


    MoveY=min(635, max(40, MoveY))
    MoveX=min(1160, max(40, MoveX))

    #pygame.draw.circle(screen, white, (int(width/2), int(height/2)), 1)
    screen.fill(white)
    for i in I_dont_care_anymore:
        screen.blit(Target, i)
    screen.blit(Cursor_icon, ((MoveX - int(Cusor_width/2)), (MoveY - int(Cursor_height/2))))
    pygame.draw.circle(screen, Black, (MoveX, MoveY), 5)
    create_target()
   # pygame.draw.circle(screen, Orange, Center_Point, Radius)
    Center_Point=(MoveX, MoveY)
    #axis_list={"x" : x, "y" : y, "x2" : x2, "y2" : y2, "trigger": trigger} 
    #print(axis_list)
    #axis_list.clear()
    #button_list={"A":buttonA, "X":buttonX, "Y":buttonY, "B":buttonB, "Right Bumper": Right_Bumper, "Left Bumper": Left_Bumper, "D-Pad":hat}
    #print(button_list)
    #button_list.clear()
    #time.sleep(0.01)

    Left = 276
    Right = 275
    Up=273
    Down=274
    keys=pygame.key.get_pressed()
    if keys[Left]:
        MoveX -= 5
        #print("boooyah")
    if keys[Right]:
        MoveX += 5
       # print("hell yeah")
    if keys[Up]:
        MoveY -= 5
        #print("fuck yeah")
    if keys[Down]:
        MoveY += 5
        #print("thank god")
    if not boolean:
        pygame.mouse.set_pos([MoveX, MoveY])
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                quit()
            if event.key == pygame.K_a:
                num_rect -= 1
            if event.key == pygame.K_s:
                num_rect += 1
            if event.key == pygame.K_SPACE:
                boolean = not boolean
        if event.type == pygame.MOUSEBUTTONDOWN:
            remove_target(MoveX, MoveY)    
            #for i in target_lst:
            #    if MoveX in eval(i[0]):
            #        if MoveY in eval(i[0]):
            #            print("boooyah")
            #            #destroy_target(i)

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    #end_time=time.clock()
    #fps = 1.0 / (end_time - start_time)
    #high_list=[]
    #high_list.append(fps)
    #high=high_list[0]
    #for i in high_list:
    #    if i > high:
    #        high=i
    #print(round(high))
   # speed = 7.5 * (end_time - start_time) * 200