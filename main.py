import pygame
from copy import deepcopy
import matplotlib.pyplot as plt

RES = WIDTH, HEIGHT = 1000, 1000
TILE = 10
W, H = (WIDTH)//TILE, HEIGHT//TILE
FPS = 10

pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

next_field = [[0 for i in range(W)] for j in range(H)]
statistic = []

with open('z3.txt', 'r') as f:
    current_field = []
    h = list(f.read().split())
    for i in range(len(h)):
        print(current_field.append(list(h[i])))
    m = 0
    for i in current_field:
        m += i.count('1')
    statistic.append(m)

def check_cell(current_field, x, y):
    count = 0
    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if current_field[j][i] == '1':
                count += 1
    if current_field[y][x] == '1':
        count -= 1
        return '1' if count == 2 or count == 3 else '0'
    else:
        return '1' if count == 3 else '0'



while True:
    surface.fill(pygame.Color('black'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            plt.plot(statistic)
            plt.suptitle("Анализ клеток")
            plt.ylabel('Количесво живых клеток')
            plt.xlabel('Количесво итераций')
            plt.show()
            exit()

    [pygame.draw.line(surface, pygame.Color('dimgray'), (x, 0), (x, HEIGHT))
    for x in range(0, WIDTH, TILE)]
    [pygame.draw.line(surface, pygame.Color('dimgray'), (0, y), (WIDTH, y))
    for y in range(0, HEIGHT, TILE)]

    for x in range(1, W - 1):
        for y in range(1, H - 1):
            if current_field[y][x] == '1':
                pygame.draw.rect(surface, pygame.Color('green'),(x * TILE + 2, y * TILE + 2, TILE - 2, TILE - 2))
            next_field[y][x] = check_cell(current_field, x, y)

    current_field = deepcopy(next_field)
    m = 0
    for i in current_field:
        m += i.count('1')
    statistic.append(m)

    with open('z3.txt', 'w') as fw:
        for i in current_field:
            k = ''
            for j in i:
                k += str(j)
            fw.write(k + '\n')

    pygame.display.flip()
    clock.tick(FPS)
