import pygame as pg
import random as rn
import sys
from time import sleep
pg.font.init()
pg.mixer.init()
RES = WIDTH, HEIGHT = 455, 455
FPS = 60
SPEED = 20
MUSIC = True

def iszmeya(x, y):
    for i in range(100):
        if Snake[i][0] == x and Snake[i][1] == y:
            return True
    return False

def spawnfood():
    while True:
        food_x = rn.randint(0, 9)
        food_y = rn.randint(0, 9)
        if not iszmeya(food_x, food_y):
            break
    return food_x, food_y

def moving():
    movingnow = ''
    eated = False
    Kostil1 = Snake[0][0]
    Kostil2 = Snake[0][1]
    if key == 'left':
        if not iszmeya((Snake[0][0] - 1) % 10, Snake[0][1]):
            Snake[0][0] = (Snake[0][0] - 1) % 10
            movingnow = 'left'
        else:
            return True, False, movingnow
    if key == 'right':
        if not iszmeya((Snake[0][0] + 1) % 10, Snake[0][1]):
            Snake[0][0] = (Snake[0][0] + 1) % 10
            movingnow = 'right'
        else:
            return True, False, movingnow
    if key == 'up':
        if not iszmeya(Snake[0][0], (Snake[0][1] - 1) % 10):
            Snake[0][1] = (Snake[0][1] - 1) % 10
            movingnow = 'up'
        else:
            return True, False, movingnow
    if key == 'down':
        if not iszmeya(Snake[0][0], (Snake[0][1] + 1) % 10):
            Snake[0][1] = (Snake[0][1] + 1) % 10
            movingnow = 'down'
        else:
            return True, False, movingnow
    if iszmeya(food_x, food_y):
        eated = True
    for i in range(98, -1, -1):
        if Snake[i + 1][0] != -1 or eated:
            Snake[i + 1][0] = Snake[i][0]
            Snake[i + 1][1] = Snake[i][1]
    Snake[1][0] = Kostil1
    Snake[1][1] = Kostil2
    return False, eated, movingnow

f1 = pg.font.Font(None, 36)
text1 = f1.render('Easy', True,
                  (255, 199, 199))
f2 = pg.font.Font(None, 36)
text2 = f2.render('Normal', True,
                  (255, 199, 199))
f3 = pg.font.Font(None, 36)
text3 = f3.render('Hard', True,
                  (255, 199, 199))


screen = pg.display.set_mode(RES)
pg.display.set_caption("Snake")
clock = pg.time.Clock()
size = 40
margin = 5
gray = (127, 118, 121)
gray2 = (102, 94, 97)
black = (48, 45, 46)
greenday = (60, 179, 113)
lime = (66, 255, 73)
pink = (145, 30, 66)
uplayer = (255, 164, 116)
uplayer2 = (238, 147, 116)
downlayer = (255, 119, 51)

while True:

    Snake = [[-1 for i in range(2)] for j in range(100)]

    Snake[0][0] = Snake[1][0] = Snake[2][0] = 4
    Snake[0][1] = 4
    Snake[1][1] = 5
    Snake[2][1] = 6

    food_x, food_y = spawnfood()

    key = 'up'
    movingnow = 'up'
    eated = False
    ToggleColor = 0
    go = False
    LOSE = False
    while True:
        screen.fill(black)
        pg.draw.rect(screen, downlayer, (88,57,279,86))
        pg.draw.rect(screen, downlayer, (88,197,279,86))
        pg.draw.rect(screen, downlayer, (88,337,279,86))
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit(0)
            elif event.type == pg.MOUSEMOTION:
                if event.pos[0] >= 91 and event.pos[0] <= 91+273 and event.pos[1] >= 60 and event.pos[1] <= 140:
                    ToggleColor = 1
                elif event.pos[0] >= 91 and event.pos[0] <= 91+273 and event.pos[1] >= 200 and event.pos[1] <= 280:
                    ToggleColor = 2
                elif event.pos[0] >= 91 and event.pos[0] <= 91+273 and event.pos[1] >= 340 and event.pos[1] <= 420:
                    ToggleColor = 3
                else:
                    ToggleColor = 0
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if event.pos[0] >= 91 and event.pos[0] <= 91+273 and event.pos[1] >= 60 and event.pos[1] <= 140:
                        SPEED = 30
                        go = True
                    elif event.pos[0] >= 91 and event.pos[0] <= 91+273 and event.pos[1] >= 200 and event.pos[1] <= 280:
                        SPEED = 20
                        go = True
                    elif event.pos[0] >= 91 and event.pos[0] <= 91+273 and event.pos[1] >= 340 and event.pos[1] <= 420:
                        SPEED = 10
                        go = True
                    
        if ToggleColor == 1:
            pg.draw.rect(screen, uplayer2, (91,60,273,80))
            pg.draw.rect(screen, uplayer, (91,200,273,80))
            pg.draw.rect(screen, uplayer, (91,340,273,80))
        elif ToggleColor == 2:
            pg.draw.rect(screen, uplayer2, (91,200,273,80))
            pg.draw.rect(screen, uplayer, (91,60,273,80))
            pg.draw.rect(screen, uplayer, (91,340,273,80))
        elif ToggleColor == 3:
            pg.draw.rect(screen, uplayer2, (91,340,273,80))
            pg.draw.rect(screen, uplayer, (91,60,273,80))
            pg.draw.rect(screen, uplayer, (91,200,273,80))
        else:
            pg.draw.rect(screen, uplayer, (91,60,273,80))
            pg.draw.rect(screen, uplayer, (91,200,273,80))
            pg.draw.rect(screen, uplayer, (91,340,273,80))

        screen.blit(text1, (200, 90))
        screen.blit(text2, (185, 230))
        screen.blit(text3, (200, 370))
        if go:
            break
        
        pg.display.update()
    sleep(1)
    if MUSIC:
        pg.mixer.music.load("track.mp3")
        pg.mixer.music.set_volume(0.05)
        pg.mixer.music.play(9)
        MUSIC = False
    time_to_move = SPEED

    while True:
        screen.fill(black)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit(0)
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT and movingnow != 'right':
                    key = 'left'
                elif event.key == pg.K_RIGHT and movingnow != 'left':
                    key = 'right'
                elif event.key == pg.K_UP and movingnow != 'down':
                    key = 'up'
                elif event.key == pg.K_DOWN and movingnow != 'up':
                    key = 'down'
        time_to_move -= 1
        if time_to_move == 0 and not LOSE:
            LOSE, eated, movingnow = moving()
            if eated:
                food_x, food_y = spawnfood()
            time_to_move = SPEED
        
        for col in range(10):
            for row in range(10):
                x = col * size + (col+1) * margin
                y = row * size + (row+1) * margin
                if (col + row)%2 == 0:
                    pg.draw.rect(screen, gray, (x,y,size,size))
                else:
                    pg.draw.rect(screen, gray2, (x,y,size,size))

        x = food_x * size + (food_x+1) * margin
        y = food_y * size + (food_y+1) * margin
        pg.draw.rect(screen, pink, (x,y,size,size))        
        
        for i in range(100):
            col = Snake[i][0]
            row = Snake[i][1]
            x = col * size + (col+1) * margin
            y = row * size + (row+1) * margin
            if i == 0:
                pg.draw.rect(screen, greenday, (x,y,size,size))
            elif Snake[i][0] != -1:
                pg.draw.rect(screen, lime, (x,y,size,size))
        if LOSE:
            break
        
        pg.display.update()
        clock.tick(FPS)
    del Snake
