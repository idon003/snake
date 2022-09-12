# I will implement by pygame
import pygame as pg
import time, random


pg.init()
# Cretaing display/ window
width = height = 600
wind = pg.display.set_mode((width, height))
pg.display.set_caption('Play me!')


clock = pg.time.Clock()

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
size, speed = 20, 10

f_style = pg.font.SysFont('Verdana', 20)
scores = pg.font.SysFont("Pokemon GB.ttf", 40)


def msg(msg, color):
    mesg = f_style.render(msg, True, color)
    wind.blit(mesg, [150, height/2])


def snake_print(size, snake_len):
    for i in snake_len:
        pg.draw.rect(wind, white, [i[0], i[1], size, size])


def score(score):
    val = scores.render('Score: ' + str(score), True, white)
    wind.blit(val, [0, 0])


def main():
    x0, y0 = width/2, height/2
    x1 = y1 = 0
    g_over = g_exit = False
    snake_len, snake_size = [], 1
    fruitx = round(random.randrange(0, width - size) / 20.0) * 20.0
    fruity = round(random.randrange(0, height - size) / 20.0) * 20.0

    while not g_over:

        while g_exit:
            wind.fill(black)
            msg('You lost! Play again: "C" Quit: "Q"', red)
            score(snake_size - 1)
            pg.display.update()
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_q:
                        g_over = True
                        g_exit = False
                    if event.key == pg.K_c:
                        main()
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                g_over = True
            elif ev.type == pg.KEYDOWN:
                if ev.key == ord('s'):
                    y1, x1 = size, 0
                elif ev.key == ord('w'):
                    y1, x1 = -size, 0
                elif ev.key == ord('a'):
                    x1, y1 = -size, 0
                elif ev.key == ord('d'):
                    x1, y1 = size, 0
        if (x0 >= width or x0 < 0) or (y0 >= height or y0 < 0):
            g_exit = True
        x0 += x1
        y0 += y1

        wind.fill(black)
        pg.draw.rect(wind, red, [fruitx, fruity, 15, 15])
        head = []
        head.append(x0)
        head.append(y0)
        snake_len.append(head)
        if len(snake_len) > snake_size:
            del snake_len[0]

        for i in snake_len[:-1]:
            if i == head:
                g_exit = True

        snake_print(size, snake_len)
        score(snake_size - 1)
        pg.display.update()

        if x0 == fruitx and y0 == fruity:
            fruitx = round(random.randrange(0, width - size) / 20.0) * 20.0
            fruity = round(random.randrange(0, height - size) / 20.0) * 20.0
            snake_size += 1

        clock.tick(speed)

    pg.quit()
    quit()


main()
