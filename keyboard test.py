import keyboard, pygame, time

def stop():
    time.sleep(0.01)


pygame.init()

pygame.display.set_mode((1200, 675))

while True:

    keyboard.on_press_key('q', stop())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                print("Wow. I was right!!!")