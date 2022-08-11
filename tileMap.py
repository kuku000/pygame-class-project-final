import pygame
from sprite import *
from setting import *

class TileMap:
    """
    """
    # object parameter
    map_type = {'village': 0, 'river': 1, 'store': 2}
    using_map = ''
    surface = None
    tilemap1 = [
        'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
        'B..CCC..S...A.....E.E.E.B..L.J.T..JA.J.B',
        'B...c...////....../.....B..............B',
        'B......./P./....../.....B..............B',
        'B......./../......//////B..............B',
        'B......./../............B..G.......F...B',
        'B.K//...................B..............B',
        'B.H/....................B..G.......F...B',
        'B.......................B..............B',
        'B.......................B..............B',
        'B..WWWW...WWWW...WWWW...B....I..I......B',
        'B.......................B..............B',
        'B.......................B....JA.A.J....B',
        'B.......................B..............B',
        'B.......................B..G.......F...B',
        'B......................................B',
        'B..R//....R//....R//...................B',
        'B......................................B',
        'BBBBBBBBBBBBBBBBBBBBBBBBB..............B',
        'MMMMMMMMMMMMMMMMMMMMMMMMB......JA.A.A.JB',
        'MMMMMMMMMMMMMMMMMMMMMMMMB..............B',
        'MMMMMMMMMMMMMMMMMMMMMMMMB......m!......B',
        'MMMMMMMMMMMMMMMMMMMMMMMMB..............B',
        'MMMMMMMMMMMMMMMMMMMMMMMMB..............B',
        'MMMMMMMMMMMMMMMMMMMMMMMMBBBBBBBBBBBB111B',
    ]
    tilemap0 = [
        '........................................',
        '........................................',
        '........................................',
        '........................................',
        '........................................',
        '........................................',
        '....//////.................////.........',
        '..../000//................/OOOO/........',
        '..../OOO/................./OOOO/........',
        '....//OO/................./OOOO/........',
        '..../OOO/................./OOOO/........',
        '..../OOO///////////////////OOOO////.....',
        '..../OOOOOOOOOOOOOOOOOOOOOOOOOOOOOO/....',
        '..../OOOOOOOOOOOOOOOOOOOOOOOOOOOOOO/....',
        '..../OOOOOOOOOOOOOOOOOOOOOOOOOOOOOO/....',
        '....//////////OOOO/////////////OOOO/....',
        '............./OOOO/.........../OOOO/....',
        '............./OOOO/.........../OOOO/....',
        '............./OOOO/.........../OOOO/....',
        '............./OOOO/.........../..../....',
        '............./OOOO/............////.....',
        '.000//////////OOOO/.....................',
        './0OOOOOOOOOOOOOOO/.....................',
        './OOOOOOOOOOOOOOOO/.....................',
        './////////////////......................',
    ]
    now_map=[]

    # method for initial instance
    def __init__(self, game,input_type=map_type['village']):
        print('init tilemap')
        self.game = game
        if input_type == self.map_type['village']:  # when construct with no extra parameter
            print('into_village')
            self.using_map = 'village'
            self.now_map = self.tilemap0
        elif input_type == self.map_type['river']:
            print('out of range random assign new number1')
            self.using_map = 'river'
            now_map = self.tilemap1
        elif input_type == self.map_type['store']:
            print('out of range random assign new number2')
            self.using_map = 'store'
            now_map = self.tilemap2
        # method for print(object)

    def __str__(self):
        return f'using: {self.using_map}'

        # method for object

    def __repr__(self):
        return self.now_map

    def draw_map(self):
        for i, row in enumerate(self.now_map):
            for j, column in enumerate(row):
                TerrainA(self.game, j, i)
                if column == "/":
                    TerrainB(self.game, j, i)
                if column == "0":
                    TerrainC(self.game, j, i)
                if column == "g":
                    Road(self.game, j, i)