# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 22:21:39 2022

@author: win10
"""
import pygame
import time
import sys, os
from config import *
from sprites import *
from font import*
from plot import *


class Game :
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.font = pygame.font.Font("txt/Pixel.ttf", 20)
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # 設定視窗大小
        pygame.display.set_caption("keep in safe")
        self.clock = pygame.time.Clock()    # 設定時間
        self.running = True
        self.restart = True
        self.playing = True
        self.fade_in = True
        self.fade_out = False
        #self.fade_in_counter = 255
        #self.fade_in_from_black = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
        #self.fade_in_from_black.fill((0, 0, 0))
        self.entry = pygame.transform.scale(pygame.image.load("img/intro/00.png"), (WIN_WIDTH, WIN_HEIGHT))
        self.test = pygame.transform.scale(pygame.image.load("img/intro/tortus.jpg"), (WIN_WIDTH, WIN_HEIGHT))

        self.entry_music = r'music/street.mp3'#音樂測試

    #def do_fade_in(self):
    #    self.clock.tick(FPS)
    #    self.fade_in_from_black.set_alpha(self.fade_in_counter)
    #    self.screen.blit(self.fade_in_from_black, (0, 0))
    #    self.fade_in_counter -= 4



    def draw(self):
        pass

    def update(self):
        self.clock.tick(FPS)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False

    def events(self):
        pass

    def new_game(self):
        self.screen.blit(self.test, (0, 0))
        text_gan = '靠北'
        text_gan2 = ''

        self.font = pygame.font.Font("txt/Silver.ttf", 200)
        text_image_gan = self.font.render(text_gan, True, (255, 255, 255))
        self.screen.blit(text_image_gan, (500, 300))
        text_image_gan2 = self.font.render(text_gan2, True, (255, 255, 255))
        self.screen.blit(text_image_gan2, (500, 400))

    def main(self):
        #loop
        while self.playing:
            self.update()
            self.events()
            self.draw()
        self.running =False

    def entry_screen_and_game_run(self):
        self.restart = False
        in_entry_screen = True
        intro_text = Font().get_text('txt/start.txt')
        intro_text_image = self.font.render(intro_text,True,(255, 255, 255))
        counter = 0
        #fade_in = True
        #fade_out = False
        pygame.mixer.music.load(self.entry_music)
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)


        while in_entry_screen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.playing = False
                    in_entry_screen = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.playing = False
                        self.running = False
                        in_entry_screen = False
                    if event.key == pygame.K_SPACE:
                        pygame.mixer.music.stop()
                        in_entry_screen = False
            intro_text_image.set_alpha(counter)
            self.screen.blit(self.entry, (0, 0))
            self.screen.blit(intro_text_image, (500, 700))
            self.clock.tick(FPS)
            pygame.display.update()
            if self.fade_in:
                counter += 2
            if self.fade_out:
                counter -= 2
            if counter >= 255:
                self.fade_out = True
                self.fade_in = False
            if counter == 0:
                self.fade_in = True
                self.fade_out = False







game = Game()
while game.restart:
    game = Game()
    game.entry_screen_and_game_run()
    game.new_game()
    while game.running:
        game.main()
pygame.quit()
sys.exit()




