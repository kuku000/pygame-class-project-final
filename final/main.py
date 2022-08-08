# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 22:21:39 2022
哭阿
@author: win10
"""
import pygame
import sys, os
from config import *
from sprites import *

class Game :
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # 設定視窗大小
        pygame.display.set_caption("keep in safe")
        self.clock = pygame.time.Clock()    # 設定時間
        self.running = True
        
        
    def update(self):
        pass
    
    def game_run(self):
        #self.title
        # game loop
        running = True
        timer = 0

        clock = pygame.time.Clock()
        while running:
            clock.tick(FPS)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
             # 更新遊戲        
            self.update()
             # 畫面顯示
            pygame.display.update()
        pygame.quit()
        



if __name__ == "__main__":
    game = Game()
    game.game_run()
