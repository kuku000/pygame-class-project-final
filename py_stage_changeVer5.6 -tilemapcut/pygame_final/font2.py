#4.0
import pygame
import sys, os
from sprites import *
import setting



class Font:
    def __init__(self):
        # 設定字型
        pygame.init()
        self.font = pygame.font.Font("txt/Silver.ttf", 20)
        pygame.font.init()

    def get_text(self, input):
        # 讀取文字檔
        f = open(input, 'r', encoding="utf-8")
        temp = f.read()
        paragraphs = temp.split('#')
        return paragraphs

    def get_image(self, text):
        # 取得圖片
        image = self.font.render(text, True, (0, 0, 0), (255, 255, 255))
        return image

class Plot(pygame.sprite.Sprite):
    def __init__(self,txt_list):

        self._layer = 90
        pygame.sprite.Sprite.__init__(self)
        self.txt_list = txt_list
        self.x = 250
        self.y = 580
        self.image = pygame.Surface((1000, 200)) # 出現位置
        self.rect = self.image.get_rect(center = (640,650))     
    
    def textSurf1(self,text,color):
        self.textSurf = self.font.render(text, 1, color)
        return self.textSurf
          
    def play_story(self,arr): # 用來 製作 對話
        self.image.fill(pygame.Color('green'))
        if arr[1].find('\n'):
            lines = arr[1].split('\n')
            for line in lines:
                self.y += 25
                ttt = Text(line,self.game, self.x,self.y )
        else:
            ttt = Text(line,self.game, self.x,self.y )

class Text(pygame.sprite.Sprite):
    """ display a text"""

    def __init__(self,game, msg,x,y):
        self.game = game
        self.groups = self.game.all_sprites , self.game.textgroup
        self._layer = TEXT_LAYER
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.newmsg(msg,x,y)

    def write(self, msg="pygame is cool"):
        """write text into pygame surfaces"""
        myfont = pygame.font.SysFont('Arial', 25)
        mytext = myfont.render(msg, True, WHITE)
        mytext = mytext.convert_alpha()
        return mytext

    def update(self):
        pass

    def newmsg(self,msg="i have nothing to say", x = 0, y = 0):
        self.image = self.write(msg)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

class PlotBoxGroups:
    def __init__(self, game):
        self.game = game
        self.plotBoxes_list = []

    def generate_plotBox(self, name, text):
        new_box = None
        if name is None:
            return
        if name == 'box':
            new_box = PlotBox(self.game, text)
        if name == 'text box':
            new_box = PlotBox.text_box(self.game, text)
        if name == 'hint box':
            new_box = PlotBox.hint_box(self.game, text)
        self.plotBoxes_list.append(new_box)

    def generate_plots(self, text):
        self.generate_plotBox('box', text)
        self.generate_plotBox('text box', text)
        self.generate_plotBox('hint box', HINT)

    def draw(self, screen):
        for plotBox in self.plotBoxes_list:
            screen.blit(plotBox.image, plotBox.rect)

    def update(self):
        pass

class PlotBox():
    def __init__(self):
        self.plot_1 = False
        self.playing_plot = False
        self.plot_counter = 0
    def play_plot_1(self):
        self.playing_plot = True
        self.plot = Plot(PLOT_1_1)
# short_intro txt
dad1_1 = Font().get_text('txt/short_intro/dad1.txt')
dad2_1 = Font().get_text('txt/short_intro/dad2.txt')
dad3_1 = Font().get_text('txt/short_intro/dad3.txt')
son1_1 = Font().get_text('txt/short_intro/son1.txt')
son2_1 = Font().get_text('txt/short_intro/son2.txt')
son3_1 = Font().get_text('txt/short_intro/son3.txt')
space_1 = Font().get_text('txt/short_intro/space.txt')
week_1 = Font().get_text('txt/short_intro/week.txt')
dad1 = dad1_1[0]
dad2 = dad2_1[0]
dad3 = dad3_1[0]
son1 = son1_1[0]
son2 = son2_1[0]
son3 = son3_1[0]
space = space_1[0]
week =week_1[0]
#PLOT_1_1 = Font().get_text('txt/input.txt')

# plot ******要加在設定的東西！*************

PLOT_LAYER = 10 # 對話框底圖
TEXT_LAYER = 99 # 對話文字
# 設定對話框大小及位置
PLOT_BOX_X = 240
PLOT_BOX_Y = 540
PLOT_BOX_WIDTH = 800
PLOT_BOX_HEIGHT = 200
# 設定對話點大小及位置
DIALOGUE_BOX_X = 240
DIALOGUE_BOX_Y = 540
DIALOGUE_BOX_WIDTH = 800
DIALOGUE_BOX_HEIGHT = 200
# 設定文字大小及位置
TEXT_BOX_X = 290
TEXT_BOX_Y = 620
TEXT_BOX_WIDTH = 600
TEXT_BOX_HEIGHT = 120
# 設定
HINT_BOX_X = 340
HINT_BOX_Y = 680
HINT_BOX_WIDTH = 600
HINT_BOX_HEIGHT = 20
# 設定標題大小及位置
TITLE_BOX_X = 290
TITLE_BOX_Y = 560
TITLE_BOX_WIDTH = 600
TITLE_BOX_HEIGHT = 25
# 設定選項指示初始位置
ARROW_X = 290
ARROW_Y = 601
# 設定選項指示大小及位置
ARROW_CHOOSE_ONE_Y = 601
ARROW_CHOOSE_TWO_Y = 631
ARROW_CHOOSE_THREE_Y = 661
ARROW_CHOOSE_FOUR_Y = 691
ARROW_WIDTH = 10
ARROW_HEIGHT = 10
# 設定選項1指示大小及位置
CHOICE_ONE_BOX_X = 340
CHOICE_ONE_BOX_Y = 590
CHOICE_ONE_BOX_WIDTH = 600
CHOICE_ONE_BOX_HEIGHT = 20
# 設定選項2指示大小及位置
CHOICE_TWO_BOX_X = 340
CHOICE_TWO_BOX_Y = 620
CHOICE_TWO_BOX_WIDTH = 600
CHOICE_TWO_BOX_HEIGHT = 20
# 設定選項3指示大小及位置
CHOICE_THREE_BOX_X = 340
CHOICE_THREE_BOX_Y = 650
CHOICE_THREE_BOX_WIDTH = 600
CHOICE_THREE_BOX_HEIGHT = 20
# 設定選項4指示大小及位置
CHOICE_FOUR_BOX_X = 340
CHOICE_FOUR_BOX_Y = 680
CHOICE_FOUR_BOX_WIDTH = 600
CHOICE_FOUR_BOX_HEIGHT = 20
# 設定選項指示大小
CHOOSING_ARROW_WIDTH = 20
CHOOSING_ARROW_HEIGHT = 20