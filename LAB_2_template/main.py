import pygame
import time
import math
import sys
# import sys : force to turn off whole game properly or terminal will have error message(display Surface quit)
#  import math : use to display minute in order to unconditionally give up
WIN_WIDTH = 1024
WIN_HEIGHT = 600
# Frame Per Second
FPS = 60
# color (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE_1 = '#C4E1FF'
BLUE_2 = '#2894FF'

# initialization
pygame.init()

# load image
background_image = pygame.transform.scale(pygame.image.load("image/background.png"), (WIN_WIDTH, WIN_HEIGHT))
# ...(to be done)


# set the title
# ---第一題---
# My First Game
start_time = pygame.time.get_ticks() # game begining time use to count game time

pygame.mixer.init() #初始化混合器
# Only_in_sleep = pygame.mixer.music.load("A2_Only_in_Sleep.mp3") # 載入音樂
# South = pygame.mixer.music.load("south.mp3")
Only_in_sleep = pygame.mixer.Sound("A2_Only_in_Sleep.mp3")
Only_in_sleep.set_volume(0.2) 
South = pygame.mixer.Sound("south.mp3")
South.set_volume(0.2)

# pygame.mixer.music.set_volume(0.2)# 設置音量爲 0.2
# pygame.mixer.music.play() # 播放音樂

class Game:
    def __init__(self):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.title = pygame.display.set_caption("My First Game")
        self.font_size = 30
        self.font = pygame.font.Font("New-Super-Mario-Font-U-1.ttf", self.font_size)
        self.base_hp = 70
        self.base_max_hp = 100
        self.count_minute = 0
        self.x = 30
        self.y = 240

    def update(self):
        pass

    def draw_time(self, surf):
        # ---Bonus---
        # 請計算出遊戲經過的時間，並將他顯示出來
        end_time = pygame.time.get_ticks()
        count_time = (end_time - start_time) // 1000
        count_time_string =''
        if count_time > 59:
            count_time_string = str(count_time)
            self.count_minute = math.floor(count_time/60)
            count_time = count_time % 60

        if count_time < 10 :
            count_time_string = "0"+str(count_time)
        else :
            count_time_string = str(count_time)

        # 输出文字内容
        pygame.draw.rect(self.win, BLACK, [0, 550, 80, 60])
        text_surface = self.font.render(str(self.count_minute)+":"+count_time_string, True, WHITE)
        self.win.blit(text_surface, (15, 555))

    def draw_base_hp(self, surf):
        # ---第二題---
        # 請畫出主堡的血量條
        pygame.draw.rect(self.win,BLUE_1, [830, 30, 10, 20])
        pygame.draw.rect(self.win, BLUE_2, [830, 50, 10, 80])

    def draw(self, surf):
        # ---第一題---
        # 請把1.地圖背景 2.敵人(水)畫出來
        self.win.blit(background_image,(0,0))
        enemy_image1 = pygame.transform.scale(pygame.image.load("image/enemy/water-0.png"),(50,50))
        self.win.blit(enemy_image1,(self.x,self.y))
        self.draw_base_hp(surf)
        self.draw_time(surf)

    def game_run(self):
        # game loop
        running = True
        clock = pygame.time.Clock()
        # while pygame.sprite.spritecollide():

        while running:
            clock.tick(FPS)
            # 取得輸入
            # event loop
            for event in pygame.event.get(): #讓使用者能夠透過角落的打叉按鈕來關閉遊戲的功能
                key_pressed_is = pygame.key.get_pressed()
                # 判断用户是否点了"X"关闭按钮,并执行if代码段
                if event.type == pygame.QUIT:
                    # 卸载所有模块
                    pygame.quit()
                    sys.exit()
# 讓水可以上下左右移動
                velocity = 10
                #判斷有無走路
                if event.type == pygame.KEYDOWN:
                # 如果按下的按鈕是左箭頭鍵，則減小 x 坐標
                    if event.key == pygame.K_LEFT:
                        self.x -= velocity
                    # 如果按下的按鈕是右箭頭鍵，則增加 x 坐標
                    if event.key == pygame.K_RIGHT:
                        self.x += velocity
                    # 如果按下按鈕是向上箭頭鍵，則減小 y 坐標
                    if event.key == pygame.K_UP:
                        self.y -= velocity
                    # 如果按下按鈕是向下箭頭鍵，則增加 y 坐標
                    if event.key == pygame.K_DOWN:
                        self.y += velocity
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # button(1：左鍵；2：中間鍵；3：右鍵)
                    if event.button == 1: #表示點擊鼠標左鍵
                        pygame.mixer.init()
                        pygame.mixer.music.load("A2_Only_in_Sleep.mp3") # 讀音樂
                        if pygame.mixer.get_busy != 1: # 檢查是不是有音樂在放
                            pygame.mixer.music.play() # 放音樂
                    if event.button == 3: # 表示點擊鼠標右鍵
                        pygame.mixer.init()
                        pygame.mixer.music.load("south.mp3")
                        if pygame.mixer.get_busy != 1:
                            pygame.mixer.music.play()




            # 更新遊戲
            self.update()

            # 畫面顯示
            self.draw(self.win)
            if key_pressed_is[pygame.K_b]:
                self.win.fill(WHITE)
            
            pygame.display.update()
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.game_run()



