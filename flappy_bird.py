import pygame, sys

WIDTH = 576
HEIGHT = 1024
FPS = 120
SPRITES_PATH = "assets/sprites/"

def draw_floor():
    screen.blit(floor_surface,(floor_x_pos,900))
    screen.blit(floor_surface,(floor_x_pos+WIDTH,900))


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

bg_surface = pygame.image.load(SPRITES_PATH+'background-day.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load(SPRITES_PATH+'base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg_surface,(0,0))
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -1*WIDTH:
        floor_x_pos = 0
    
    pygame.display.update()
    clock.tick(FPS)