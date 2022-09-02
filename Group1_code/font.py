import pygame
import sys, os
from sprites import *
import setting



class Font:
    def __init__(self):
        # 設定字型
        pygame.init()
        self.font = pygame.font.Font("txt/Silver.ttf", 35)
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

# short_intro txt
dad1 = Font().get_text('txt/short_intro/dad1.txt')
dad2 = Font().get_text('txt/short_intro/dad2.txt')
dad3 = Font().get_text('txt/short_intro/dad3.txt')
son1 = Font().get_text('txt/short_intro/son1.txt')
son2 = Font().get_text('txt/short_intro/son2.txt')
son3 = Font().get_text('txt/short_intro/son3.txt')
space = Font().get_text('txt/short_intro/space.txt')
week = Font().get_text('txt/short_intro/week.txt')