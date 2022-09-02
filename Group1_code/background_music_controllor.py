
import pygame
from setting import *

class Background_music:

    def __init__(self,game):
        self.game = game
        #self.counter = 0



    def music_choose(self):
        if self.game.map_number == 0:
            pygame.mixer.music.load(self.game.entry_music)
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play(-1)

        elif self.game.map_number == 1:
            pygame.mixer.music.load(self.game.house_music)
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play(-1)

        elif self.game.map_number == 2:
            self.game.river2.set_volume(0.15)
            self.game.river2.play(-1)
            pygame.mixer.music.load(self.game.river)
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play(-1)

    #def change_Sound(self):
    #    pygame.mixer.music.load(self.game.final_countdown)
    #    pygame.mixer.music.set_volume(0.2)
    #    pygame.mixer.music.play(-1)


    #def update(self):
    #    self.music_choose()
