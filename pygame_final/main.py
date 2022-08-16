# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pygame
import time
import sys, os
from setting import *
from sprites import *
from font import*

class Game :

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.font = pygame.font.Font("txt/Silver.ttf", 20)
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # 設定視窗大小
        pygame.display.set_caption("keep in safe")
        self.clock = pygame.time.Clock()    # 設定時間
        self.running = True
        self.restart = True
        self.fade_in = True
        self.fade_out = False
        self.fade_in_counter = 255
        self.fade_in_from_black = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
        self.fade_in_from_black.fill((0, 0, 0))

        self.character_spritesheet = SpriteSheet('img/character.png')
        self.terrain_spritesheet = SpriteSheet('img/terrain.png')
        self.buliding_spritesheet = SpriteSheet('img/building2.png')

        self.entry = pygame.transform.scale(pygame.image.load("img/intro/00.png"), (WIN_WIDTH, WIN_HEIGHT))
        self.test = pygame.transform.scale(pygame.image.load("img/intro/tortus.jpg"), (WIN_WIDTH, WIN_HEIGHT))
        self.black = pygame.transform.scale(pygame.image.load("img/black.png"), (WIN_WIDTH, WIN_HEIGHT))

        self.entry_music = r'music/begining.mp3'  # 音樂測試
        self.walk_effect = r'music/walking_on_a_floor.mp3'






        self.map_using = tilemap_0

    def draw(self):
        self.all_sprites.draw(self.screen)
        self.blocks.draw(self.screen)
        self.player.draw(self.screen)
        self.NPCS.draw(self.screen)



    def update(self):
        #self.terrains.update()
        self.all_sprites.update()
        self.blocks.update()
        self.player.update()

    def events(self):
        self.clock.tick(FPS)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.playing = False
                    # self.running = False

        pygame.display.update()

    def new(self):

        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.player =pygame.sprite.LayeredUpdates()
        self.NPCS = pygame.sprite.LayeredUpdates()

        game.createmap()
        self.walk_sound = pygame.mixer.Sound(self.walk_effect)
        self.walk_sound.set_volume(0.1)

    def entry_screen(self):
        self.restart = False
        in_entry_screen = True
        self.font = pygame.font.Font("txt/Silver.ttf", 40)
        intro_text = Font().get_text('txt/start.txt')
        intro_text_image = self.font.render(intro_text, True, (255, 255, 255))
        counter = 0
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

        # tilemap set

    def createmap(self):

        for i, row in enumerate(self.map_using):
            for j, column in enumerate(row):
                Ground.terrainC(self,j,i)
                if column == "/":
                    Ground.terrainA(self,j,i)

                if column == "O":
                    Ground.modA(self, j, i)

                if column == "1":
                    Ground.rockB(self, j, i)

                if column == "g":
                    Ground.road(self, j, i)

                if column == 'H':
                    Block.house(self, j, i)

                if column == 'R':
                    Block.river(self, j, i)

                if column == 'S':
                    Block.shop(self, j, i)
                if column == 'P':
                    Player(self, j, i)

    def short_intro(self):
        in_short_intro = True

        part_counter = 0
        pygame.mixer.music.load(self.entry_music)
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)
        self.font = pygame.font.Font("txt/Silver.ttf", 30)
        self.screen.blit(self.black, (0, 0))

        counter = 0


        # short_intro_text1 = Font().get_text('txt/start.txt')
        # short_intro_text1_image = self.font.render(short_intro_text1,True,(255, 255, 255))

        while in_short_intro:
            space_image = self.font.render(space, True, (255, 255, 255))
            space_image.set_alpha(counter)
            self.screen.blit(space_image, (600, 750))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.playing = False
                    in_short_intro = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.playing = False
                        self.running = False
                        in_short_intro = False

                    if event.key == pygame.K_SPACE:

                        if part_counter == 7:
                            in_short_intro = False
                            pygame.mixer.music.stop()
                        else:
                            if part_counter == 0:
                                self.screen.blit(self.black, (0, 0))

                                self.screen.blit(self.font.render(dad1, True, (255, 255, 255)), (400, 100))
                            if part_counter == 1:
                                self.screen.blit(self.black, (0, 0))

                                self.screen.blit(self.font.render(dad1, True, (255, 255, 255)), (400, 100))
                                self.screen.blit(self.font.render(son1, True, (255, 255, 255)), (680, 200))
                            if part_counter == 2:
                                self.screen.blit(self.black, (0, 0))

                                self.screen.blit(self.font.render(dad1, True, (255, 255, 255)), (400, 100))
                                self.screen.blit(self.font.render(son1, True, (255, 255, 255)), (680, 200))
                                self.screen.blit(self.font.render(dad2, True, (255, 255, 255)), (400, 300))
                            if part_counter == 3:
                                self.screen.blit(self.black, (0, 0))
                                self.screen.blit(self.font.render(dad1, True, (255, 255, 255)), (400, 100))
                                self.screen.blit(self.font.render(son1, True, (255, 255, 255)), (680, 200))
                                self.screen.blit(self.font.render(dad2, True, (255, 255, 255)), (400, 300))
                                self.screen.blit(self.font.render(son2, True, (255, 255, 255)), (680, 400))
                            if part_counter == 4:
                                self.screen.blit(self.black, (0, 0))
                                self.screen.blit(self.font.render(dad1, True, (255, 255, 255)), (400, 100))
                                self.screen.blit(self.font.render(son1, True, (255, 255, 255)), (680, 200))
                                self.screen.blit(self.font.render(dad2, True, (255, 255, 255)), (400, 300))
                                self.screen.blit(self.font.render(son2, True, (255, 255, 255)), (680, 400))
                                self.screen.blit(self.font.render(son3, True, (255, 255, 255)), (680, 500))
                            if part_counter == 4:
                                self.screen.blit(self.black, (0, 0))
                                self.screen.blit(self.font.render(dad1, True, (255, 255, 255)), (400, 100))
                                self.screen.blit(self.font.render(son1, True, (255, 255, 255)), (680, 200))
                                self.screen.blit(self.font.render(dad2, True, (255, 255, 255)), (400, 300))
                                self.screen.blit(self.font.render(son2, True, (255, 255, 255)), (680, 400))
                                self.screen.blit(self.font.render(son3, True, (255, 255, 255)), (680, 500))

                            if part_counter == 5:
                                self.screen.blit(self.black, (0, 0))
                                self.screen.blit(self.font.render(dad1, True, (255, 255, 255)), (400, 100))
                                self.screen.blit(self.font.render(son1, True, (255, 255, 255)), (680, 200))
                                self.screen.blit(self.font.render(dad2, True, (255, 255, 255)), (400, 300))
                                self.screen.blit(self.font.render(son2, True, (255, 255, 255)), (680, 400))
                                self.screen.blit(self.font.render(son3, True, (255, 255, 255)), (680, 500))
                                self.screen.blit(self.font.render(dad3, True, (255, 255, 255)), (400, 600))
                            if part_counter == 6:
                                self.screen.blit(self.black, (0, 0))
                                self.screen.blit(self.font.render(week, True, (255, 255, 255)), (500, 400))
                            part_counter += 1

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

    def main(self):
        # loop
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False

game = Game()
while game.restart:
    game = Game()
    game.entry_screen()
    game.short_intro()
    game.new()

    game.createmap()

    while game.running:
        game.main()
pygame.quit()
sys.exit()


