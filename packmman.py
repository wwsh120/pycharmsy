import pygame, sys, random
from pygame.locals import *


pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("PACKMAN")
screen = pygame.display.set_mode((1920, 1080))


block_image = pygame.image.load("C:\\Users\\KingGOD\\Desktop\\hangman\\ww.jpg").convert()
ghost_image = pygame.image.load("C:\\Users\\KingGOD\\Desktop\\hangman\\gho1.png").convert()
coin_image = pygame.image.load("C:\\Users\\KingGOD\\Desktop\\hangman\\cccc.png").convert()



class block:
    def __init__(self, x, y):
        self.x = x * 50
        self.y = y * 50
        self.sort = int(a[y][x])

    def draw(self):
        if self.sort == 0:
            screen.blit(coin_image, (self.x, self.y))
        elif self.sort == 1:
            screen.blit(block_image, (self.x, self.y))

class player:
    def __init__(self):
        self.x = random.randint(5 ,10) * 50
        self.y = random.randint(7 ,12) * 50
        self.point = 0


    def draw(self):
        screen.blit(ghost_image, (self.x, self.y))

    def move(self):
        if pressed_keys[K_RIGHT] and "right" in self.player_key_list:
            self.x += 2
        if pressed_keys[K_LEFT] and "left" in self.player_key_list:
            self.x -= 2
        if pressed_keys[K_UP] and "up" in self.player_key_list:
            self.y -= 2
        if pressed_keys[K_DOWN] and "down" in self.player_key_list:
            self.y += 2

    def positioning(self):
        self.player_key_list = ["up", "down", "left", "right"]

        if a[int(self.y / 50)][int(self.x / 50)] == 0:
            self.point += 1
        if a[int(self.y // 50)][int(round(self.x / 50))] == 1:
            self.player_key_list.remove("up")
        if a[int(self.y // 50) + 1][int(round(self.x / 50))] == 1:
            self.player_key_list.remove("down")
        if a[int(round(self.y / 50))][int(self.x // 50) + 1] == 1:
            self.player_key_list.remove("right")
        if a[int(round(self.y / 50))][int(self.x // 50)] == 1:
            self.player_key_list.remove("left")

class Ghost:
    def __init__(self):
        self.x = random.choice([5, 30]) * 50
        self.y = random.choice([7, 18]) * 50
        self.move_command = ["up", "down", "left", "right"]

    def draw(self):
        screen.blit(ghost_image, (self.x, self.y))

    def move(self):

        if a[int(self.y // 50)][int(round(self.x / 50))] == 1 and "up" in self.move_command:
            self.move_command.remove("up")
        if a[int(self.y // 50) + 1][int(round(self.x / 50))] == 1 and "down" in self.move_command:
            self.move_command.remove("down")
        if a[int(round(self.y / 50))][int(self.x // 50) + 1] == 1 and "right" in self.move_command:
            self.move_command.remove("right")
        if a[int(round(self.y / 50))][int(self.x // 50)] == 1 and "left" in self.move_command:
            self.move_command.remove("left")

        if (self.y - player.y < 0) and "down" in self.move_command and "up" in self.move_command:
            self.move_command.remove("up")
        if (self.y - player.y > 0) and "up" in self.move_command and "down" in self.move_command:
            self.move_command.remove("down")
        if (self.x - player.x < 0) and "right" in self.move_command and "left" in self.move_command:
            self.move_command.remove("left")
        if (self.x - player.x > 0) and "left" in self.move_command and "right" in self.move_command:
            self.move_command.remove("right")

        self.order = random.choice(self.move_command)

        self.move_command = ["up", "down", "left", "right"]

        if self.order == "up":
            self.y -= 1
            self.move_command.remove("down")
        elif self.order == "down":
            self.y += 1
            self.move_command.remove("up")
        elif self.order == "left":
            self.x -= 1
            self.move_command.remove("right")
        elif self.order == "right":
            self.x += 1
            self.move_command.remove("left")





a = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ,[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    ,[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    ,[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    ,[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    ,[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    ,[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    ,[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    ,[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    ,[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    ,[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    ,[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    ,[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    ,[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    ,[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    ,[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    ,[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    ,[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    ,[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    ,[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    ,[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
blocks = []
ghosts = []
player = player()

for y in range(21):
    for x in range(38):
        blocks.append(block(x, y))

for i in range(4):
    ghost = Ghost()
    if i >= 1:
        while (ghosts[i-1].x == ghost.x) and (ghosts[i-1].y == ghost.y):
            ghost = Ghost()
    ghosts.append(ghost)

while 1:
    clock.tick(144)

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    pressed_keys = pygame.key.get_pressed()
    screen.fill((0, 0, 0))

    for i in blocks:
        i.draw()

    player.draw()
    player.move()
    player.positioning()

    for i in ghosts:
        i.draw()
        i.move()

    pygame.display.update()