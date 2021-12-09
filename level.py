import pygame

def level_select():
    black=(0, 0, 0)
    max_width=800
    max_height=600
    screen=pygame.display.set_mode((max_width, max_height))
    pygame.font.init()
    levelfont=pygame.font.Font(r"non-program bulcrapo\zig.ttf", 40)
    levelrects={}

    while True:
        screen.fill(black)


        textrender = levelfont.render("Level Select", False, (255, 0, 0))
        for i in range(5):
            leveltext = levelfont.render(str(i+1), False, (255, 255, 255))
            screen.blit(leveltext, (140+i*125-leveltext.get_width()//2, textrender.get_height()+30))
            levelrects[str(i+1)] = leveltext.get_rect(center=(140+i*125-3, textrender.get_height()+30+leveltext.get_width()//2))
            levelrects[str(i+1)].width += 5
            levelrects[str(i+1)].height += 5
        screen.blit(textrender, (max_width//2-textrender.get_width()//2, 5))
        for rect in levelrects.values():
            pygame.draw.rect(screen, (255, 255, 255), rect, width=1)
        pygame.draw.line(screen, (255, 255, 255), (0, textrender.get_height()+10), (max_width, textrender.get_height()+10))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousepos = pygame.mouse.get_pos()
                for i in range(len(levelrects)):
                    rect = list(levelrects.values())[i]
                    if rect.collidepoint(mousepos):
                        levelnum = i+1
                        return levelnum
        pygame.display.flip()