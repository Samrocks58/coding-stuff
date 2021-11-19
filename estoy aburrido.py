import pygame, time

pygame.init()

pygame.display.init()

width=int(1200)
height=int(675)

green=(0, 255, 0)
Red=(255, 0, 0)
White=(255, 255, 255)
Black=(0, 0, 0)

Fent = pygame.font.Font(r'C:\Users\smprc\Downloads\gibster\GibsterRegular.ttf', 200)

Font2 = pygame.font.Font(r'C:\Users\smprc\Downloads\gibster\GibsterRegular.ttf', 200)
Font2.set_underline(True)
Font2.set_bold(False)


screen = pygame.display.set_mode((width, height))

screen.fill(White)
pygame.draw.polygon(screen, Red, [(270, 461), (358, 490), (266, 539)])
pygame.draw.polygon(screen, Red, [(296, 523), (329, 581), (363, 567), (328, 505)])
buddy = pygame.draw.circle(screen, green, (int(width/2), int(height/2)), 100)

mouseX, mouseY = pygame.mouse.get_pos()

mousedown=False

clicks=False


while True:
    mouseX, mouseY = pygame.mouse.get_pos()
    pygame.display.flip()
    text2 = Font2.render("BPM COUNTER", False, Red)
    screen.blit(text2, (150, 25))

    for event in pygame.event.get():
        if not mousedown:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if buddy.collidepoint(mouseX, mouseY) == 1:
                    if clicks:
                        end_time=time.perf_counter()
                        text = Fent.render(str(round(60 / (end_time-start_time))), False, Black)
                        screen.fill(White)
                        pygame.draw.polygon(screen, Red, [(270, 461), (358, 490), (266, 539)])
                        pygame.draw.polygon(screen, Red, [(296, 523), (329, 581), (363, 567), (328, 505)])
                        buddy = pygame.draw.circle(screen, green, (int(width/2), int(height/2)), 100)
                        screen.blit(text2, (150, 25))
                        screen.blit(text, (100, (int(height/2))-75))
                        #print(round(60 / (end_time-start_time)))
                    start_time=time.perf_counter()
                    mousedown=True
                    clicks=True
        if mousedown:
            if event.type == pygame.MOUSEBUTTONUP:
                mousedown=False
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()