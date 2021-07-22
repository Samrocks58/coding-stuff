import pygame

pygame.init()
pygame.display.init()

White = (255, 255, 255)
Red = (255, 0, 0)
bLAck= (0, 0, 0)
screen = pygame.display.set_mode((1200, 675))
cape_cod=pygame.image.load(r"C:\Users\spear\OneDrive\Desktop\Desktop Folder\CAPE COD MAP.jpg")
cape_cod = pygame.transform.scale(cape_cod, (300, 300))

Cursor_icon = pygame.image.load(r"C:\Users\spear\OneDrive\Desktop\Desktop Folder\cursor target.png")
Cursor_icon = pygame.transform.scale(Cursor_icon, (50, 50))

Fent = pygame.font.Font(r'C:\Users\spear\OneDrive\Desktop\Desktop Folder\gibster-font\Gibster-ow1XA.otf', 100)

screen.fill(White)
pygame.mouse.set_visible(False)
clicked=False

txt = Fent.render("Where do you think we are???", False, Red)
while True:

    pygame.display.flip()

    mouseX, mouseY = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not clicked:
                posx=mouseX
                posy=mouseY
                pygame.draw.circle(screen, Red, (posx, posy), 5)
                pygame.draw.polygon(screen, bLAck, [(posx, posy+20), (posx-20, posy+40), (posx+20, posy+40)])
                pygame.draw.polygon(screen, bLAck, [(posx-10, posy+40), (posx+10, posy+40), (posx+10, posy+80), (posx-10, posy+80)])
                clicked = True
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(White)
    screen.blit(txt, (75, 30))
    screen.blit(cape_cod, (450, 150))
    screen.blit(Cursor_icon, (mouseX-25, mouseY-25))
    if clicked:
        pygame.draw.polygon(screen, Red, [(posx, posy+20), (posx-40, posy+100), (posx+40, posy+100)])
        pygame.draw.polygon(screen, Red, [(posx-10, posy+60), (posx+10, posy+60), (posx+10, posy+160), (posx-10, posy+160)])
        pygame.draw.circle(screen, bLAck, (posx, posy), 5)
        screen.blit(Cursor_icon, (mouseX-25, mouseY-25))

