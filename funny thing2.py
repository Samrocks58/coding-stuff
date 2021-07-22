import os, time, pygame

white=(255, 255, 255)
black=(0, 0, 0)
pygame.init()
Font=pygame.font.Font(r'C:\Users\spear\OneDrive\Desktop\Desktop Folder\gibster-font\Gibster-ow1XA.otf', 100)
weird=r"non-program bulcrapo/abnormal.txt"
screen=pygame.display.set_mode((1200, 675))
screen.fill(white)

# Get .txt files
with open(weird, 'r') as f:
    data = f.readlines()
    for i in data:
        data[data.index(i)] = i.split(" \n")[0]
    data[0] = data[0].split("ï»¿")[1]
    for i in data:
        if data.count(i) > 1:
            for x in range(data.count(i)-1):
                data.remove(i)
    for i in range(len(data)):
        text = (f"It's a little {data[i]}.")
        txt = Font.render(text, False, black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(data)
                quit()
        time.sleep(1)
        screen.fill(white)
        screen.blit(txt, (300, int(675/2)))
        pygame.display.flip()

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        quit()