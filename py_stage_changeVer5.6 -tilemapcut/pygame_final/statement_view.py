import time
from setting import *
import pygame


class Statement_View:
    def __init__(self, game):
        # 飢餓程度
        self.game = game
        self.last_time = time.time()
        self.period = [20, 5, 1]

        self.dis_set = [192, 180]

        self.blood = 180
        pygame.draw.rect(self.game.screen, WHITE, [blood_x, blood_y, 180, 40])
        pygame.draw.rect(self.game.screen, RED, [blood_x, blood_y, self.blood, 40])

    def money_draw(self):
        pygame.draw.rect(self.game.screen, BLUE_1, [0, 680, 180, 40])
        display = "$ " + str(self.game.money)
        self.game.screen.blit(self.game.font.render(display, True, (0, 0, 0)), (10, 680))

    # 血量計算
    def blood_minus(self):
        now = time.time()
        if self.blood <= 0:
            self.blood = 0
        if now - self.last_time >= self.period[0]:
            self.last_time = now
            self.blood -= 10

    def blood_draw(self):
        # 血量小於零時，gameover
        self.blood_minus()
        if self.blood == 0:
            self.game.gameover()

        pygame.draw.rect(self.game.screen, WHITE, [blood_x, blood_y, 180, 40])
        pygame.draw.rect(self.game.screen, RED, [blood_x, blood_y, self.blood, 40])
        self.game.screen.blit(self.game.font.render("飢餓程度", True, (0, 0, 0)), (10, 640))

    def update(self):
        self.blood_draw()
        self.money_draw()
