import time
from setting import *
import pygame
from sprites import SpriteSheet


class Statement_View:
    def __init__(self, game):
        # 飢餓程度
        self.game = game
        self.last_time = time.time()
        self.period = [20, 5, 1]

        self.dis_set = [192, 180]

        pygame.draw.rect(self.game.screen, WHITE, [blood_x, blood_y, 180, 40])
        pygame.draw.rect(self.game.screen, RED, [blood_x, blood_y, self.game.blood, 40])

        self.count_down = False
        self.count_time = 0
        self.remain = TIME_LIMIT

        self.font = pygame.font.Font("txt/Silver.ttf", 35)

    def money_draw(self):
        pygame.draw.rect(self.game.screen, BLUE_1, [0, 680, 180, 40])
        display = "$ " + str(self.game.money)
        self.game.screen.blit(self.font.render(display, True, (0, 0, 0)), (10, 680))

    # 血量計算
    def blood_minus(self):
        now = time.time()
        if self.game.blood <= 0:
            self.game.blood = 0
        if now - self.last_time >= self.period[0]:
            self.last_time = now
            self.game.blood -= 10

    def blood_draw(self):
        # 血量小於零時，gameover
        self.blood_minus()
        if self.game.blood == 0:
            self.game.playing = False

        pygame.draw.rect(self.game.screen, WHITE, [blood_x, blood_y, 180, 40])
        pygame.draw.rect(self.game.screen, RED, [blood_x, blood_y, self.game.blood, 40])
        self.game.screen.blit(self.font.render("體力", True, (0, 0, 0)), (10, 640))

    def button_draw(self):
        pygame.draw.rect(self.game.screen, BLUE_2, pygame.Rect(180, 640, 336, 160))
        pygame.draw.rect(self.game.screen, PERPLE1, pygame.Rect(180, 640, 336, 160))
        self.game.screen.blit(self.game.button_spritesheet.get_sprite(0, 0, 336, 153), (180, 640))
        self.game.screen.blit(self.font.render(str(self.game.item_bag[0]), True, (0, 0, 0)), (265, 690))
        self.game.screen.blit(self.font.render(str(self.game.item_bag[1]), True, (0, 0, 0)), (375, 690))
        self.game.screen.blit(self.font.render(str(self.game.item_bag[2]), True, (0, 0, 0)), (490, 690))
        self.game.screen.blit(self.font.render(str(self.game.item_bag[3]), True, (0, 0, 0)), (265, 770))
        self.game.screen.blit(self.font.render(str(self.game.item_bag[4]), True, (0, 0, 0)), (375, 770))

    def dialog_frame_draw(self):
        pygame.draw.rect(self.game.screen, PERPLE1, pygame.Rect(516, 640, 764, 160), 2)

    def draw_time(self):

        game_time = int(pygame.time.get_ticks() - self.count_time)
        self.remain = (TIME_LIMIT - game_time // 1000)
        pygame.draw.rect(self.game.screen, BLACK, pygame.Rect(0, WIN_HEIGHT - 80, 180, 80))
        self.game.screen.blit(self.font.render('颱風倒數:'+str(self.remain), True, WHITE), (20, WIN_HEIGHT - 50))
        if self.game.check_win():
            self.game.win = True
            self.game.playing = False
        elif self.remain == 0:
            self.game.playing = False

    def time_start(self):
        self.count_time = pygame.time.get_ticks()
        self.count_down = True

    def update(self):
        self.blood_draw()
        self.money_draw()
        self.button_draw()
        self.dialog_frame_draw()
        if self.count_down:
            self.draw_time()
