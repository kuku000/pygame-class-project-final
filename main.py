import pygame


from tileMap import *
from sprite import *
from tileMap import*
from setting import *




# initialization
pygame.init()


class Game:
    tilemap_0 = [
        '........................................',
        '........................................',
        '........................................',
        '........................................',
        '........................................',
        '........................................',
        '........................................',
        '..........................//............',
        '..../.../.........ggggggg.......O.......',
        '......00..........ggggggg...............',
        '..................ggggggg...............',
        '.......O..........ggggggg../............',
        '.........000//.../gggggggggggggggggggggg',
        '..................gggggggggggggggggggggg',
        '..................gggggggggggggggggggggg',
        '.........../..OOOOggggggg...............',
        '..............O.O/ggggggg...../.........',
        '............./OO..ggggggg........OO/....',
        '..../.........O.OOggggggg......OO.......',
        '............./O./Oggggggg...../..../....',
        '............./OOOOggggggg...............',
        '....//ggggggggggggggggggg...............',
        '...OOOggggggggggggggggggg...............',
        '.0/OOOOOOOOOOO.....gggggg...............',
        '.0.................gggggg...............',
    ]

    def __init__(self):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption('My First Game')
        self.terrain_spritesheet = SpriteSheet('images/terrain.png')
        self.block_spritesheet = SpriteSheet('images/furniture.png')


    def update(self):
        self.all_sprites.update()

    def draw(self, surf):
        self.all_sprites.draw(surf)

    def new(self):
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.terrains = pygame.sprite.LayeredUpdates()
        self.NPCs= pygame.sprite.LayeredUpdates()
        self.map1 = TileMap(TileMap.map_type['village'])
        #self.map1.draw_map() #異常 正在DEBUG中

    def createmap(self):
        for i, row in enumerate(self.tilemap_0):
            for j, column in enumerate(row):
                TerrainA(self, j, i)
                if column == "/":
                    TerrainB(self, j, i)
                if column == "0":
                    TerrainC(self, j, i)
                if column == "g":
                    Road(self, j, i)

    def game_run(self):
        # game loop
        running = True
        clock = pygame.time.Clock()
        while running:
            clock.tick(FPS)
            self.draw(self.win)
            # 使用者能夠透過角落的打叉按鈕來關閉遊戲的功能
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            # 更新遊戲
            self.update()

            # 畫面顯示
            self.draw(self.win)

            pygame.display.update()
        pygame.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game = Game()
    game.new()
    game.createmap()
    game.game_run()