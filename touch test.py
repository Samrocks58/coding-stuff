import sdl2, pygame, sdl2.ext, sdl2.dll
from pygame import event

sdl2.ext.init()

pygame.init()
pygame.display.init()
screen = pygame.display.set_mode((1200, 600))
#black = (0, 0, 0)

#sdl2.ext.fill(black, screen)

while True:
    screen = sdl2.ext.Window("GAME", (1200, 675), None)
    sdl2.ext.Window.refresh(screen)
    #for i in pygame.sdl2.touch.get_num_devices():
    #    thing=pygame.sdl2.touch.get_device(i)
    #    print(pygame.sdl2.touch.get_num_fingers(thing))


    #event=sdl2.SDL_PollEvent(SDL_FINGERDOWN)
    #if event == SDL_FINGERDOWN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    for event in sdl2.ext.get_events():
        if event.type == SDL_FINGERDOWN:
            print("\nHurray!!")
        if event.type == SDL_QUIT:
            quit()