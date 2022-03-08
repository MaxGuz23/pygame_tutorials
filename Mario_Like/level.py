import pygame
from tiles import Tile
from settings import tile_size, SCREEN_W
from player import Player

class Level:
    
    def __init__(self,level_data,surface):
        # level setup
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self,layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for i, row in enumerate(layout):
            for j, cell in enumerate(row):
                x = j * tile_size
                y = i * tile_size

                if cell == 'X':
                    tile = Tile((x,y), tile_size)
                    self.tiles.add(tile)
                if cell == 'P':
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        # leftside and moving left
        if player_x < SCREEN_W/4 and direction_x < 0: 
            self.world_shift = 8
            player.speed = 0
        # rightside and moving right
        elif player_x > SCREEN_W*3/4 and direction_x > 0: 
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8


    def run(self):
        # level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        # player
        self.player.update()
        self.player.draw(self.display_surface)
        self.scroll_x()