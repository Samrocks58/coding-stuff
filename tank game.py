import pygame, math
from pygame.display import init as start

pygame.init()
start()

width=int(1200)
height=int(600)
Orange=(255, 95, 0)
white=(255, 255, 255)
Red=(255, 0, 0)
Black=(0, 0, 0)

screen = pygame.display.set_mode((width, height))#, depth=0, flags=pygame.FULLSCREEN)
screen.fill(white)

tank=pygame.image.load(r'non-program bulcrapo/cooler_tank.gif')
tank=pygame.transform.flip(tank, True, False)
rect_x=tank.get_width()
rect_y=tank.get_height()
playerY=height//2-rect_y//2
playerX=width//2-rect_x//2
opponent_tank=tank
opponentX=0
opponentY=0
current_degrees=0
opponent_tank=pygame.transform.rotate(opponent_tank, math.degrees(math.atan(abs(opponentX-playerX)/abs(opponentY-playerY)))-90)
current_degrees=math.degrees(math.atan(abs(opponentX-playerX)/abs(opponentY-playerY)))-90

while True:
    screen.fill(white)
    screen.blit(tank, (playerX, playerY))
    screen.blit(opponent_tank, (opponentX, opponentY))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                quit()
            if event.key == pygame.K_LEFT:
                opponent_tank=tank
                playerX -= 20
                new_angle=round(math.degrees(math.atan(abs(opponentX-playerX)/abs(opponentY-playerY)))-90)
                opponent_tank=pygame.transform.rotate(opponent_tank, new_angle)
            if event.key == pygame.K_RIGHT:
                opponent_tank=tank
                playerX += 20
                new_angle=round(math.degrees(math.atan(abs(opponentX-playerX)/abs(opponentY-playerY)))-90)
                opponent_tank=pygame.transform.rotate(opponent_tank, new_angle)
            if event.key == pygame.K_UP:
                opponent_tank=tank
                playerY -= 20
                new_angle=round(math.degrees(math.atan(abs(opponentX-playerX)/abs(opponentY-playerY)))-90)
                opponent_tank=pygame.transform.rotate(opponent_tank, new_angle)
            if event.key == pygame.K_DOWN:
                opponent_tank=tank
                playerY += 20
                new_angle=round(math.degrees(math.atan(abs(opponentX-playerX)/abs(opponentY-playerY)))-90)
                opponent_tank=pygame.transform.rotate(opponent_tank, new_angle)
    pygame.display.flip()