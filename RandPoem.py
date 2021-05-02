import random, pygame, sys

#randomly arranging the word order of the poem
def randpoem(poem):
    pList = []
    nList = ''
    for i in poem:
        pList.append(i)
    for i in range (len(pList)):
        n = random.randint(0,len(pList))
        nList += (pList[n-1])
        pList.pop(n-1)
    return(nList)

# draw the matrix on the screen
def drawmatrix(scr, n, lw, fw, clr):
    for y in range(n + 1):
        pygame.draw.rect(scr,clr, (0, 155 * y, 470, 5), 0)
        pygame.draw.rect(scr,clr, (155 * y, 0, 5, 470), 0)

# draw the poem on the screen
def drawpoem(scr, rdpoem, n, lw, fw):
    for y in range(3):
        for x in range(3):
            p = y * n + x
            xf, yf = x * (lw + fw) + 5, y * (lw + fw) + 5
            # creating shades by drawing two layers
            imgWord = myfont.render(rdpoem[p], True,(100, 100, 100))
            scr.blit(imgWord, (xf, yf))
            imgWord = myfont.render(rdpoem[p], True,(255, 255, 255))
            scr.blit(imgWord, (xf - 5, yf - 5))

#------------------主程序----------------
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((470, 470), 0, 32)
clock = pygame.time.Clock()
# change the font by changing the font's directory below
myfont = pygame.font.Font('Deng.ttf', 150)
# add poems to the txt file named below
myfile =  open('poem.txt', 'r')
strList = myfile.readlines()
myfile.close()
wID = 0
# change the background image by changing the directory below
bgPic = pygame.image.load('miku.jpg')
matrix_clr = (57, 197, 187)
rdpoem = randpoem(strList[wID].strip('\n'))

while True:
    screen.blit(bgPic, (0, 0))
    drawmatrix(screen, 3, 5, 150, matrix_clr)
    drawpoem(screen, rdpoem, 3, 5, 150)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # press SPACE to skip to the next poem
            if event.key == pygame.K_SPACE:
                wID += 1
                wID = wID % len(strList)
            # press any key to rearrange the words
            rdpoem = randpoem(strList[wID].strip('\n'))
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(50)
