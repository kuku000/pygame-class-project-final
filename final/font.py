# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 22:20:12 2022

@author: win10
"""
import pygame
import sys, os
from config import *
from sprites import *
#from main import*
from plot import *
class Font:
    def __init__(self):
        # 設定字型
        pygame.init()
        self.font = pygame.font.Font("txt/NotoSerifCJKtc-Regular.otf", 20)
        pygame.font.init()

    def get_text(self, text_file):
        # 讀取文字檔
        file = open(text_file, "r", encoding="utf-8")
        text = (file.read())
        return text

    def get_image(self, text):
        # 取得圖片
        image = self.font.render(text, True, (0, 0, 0), (255, 255, 255))
        return image
