import pygame

pygame.init()
pygame.display.init()

width=int(1200)
height=int(600)
Orange=(255, 95, 0)
white=(255, 255, 255)
Red=(255, 0, 0)
Black=(0, 0, 0)

screen = pygame.display.set_mode((width, height))#, depth=0, flags=pygame.FULLSCREEN)
screen.fill(white)

while True:
    screen.fill(white)
    pygame.display.init()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                quit()