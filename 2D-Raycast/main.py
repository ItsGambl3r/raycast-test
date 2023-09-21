import pygame, math, random
from constants import *
from segment import Segment
from particle import Particle
SCREEN_WIDTH, SCREEN_HEIGHT = 1600, 600
WIDTH, HEIGHT = 800, 600
FPS = 60
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
walls = []

for i in range(5):
    x1 = random.randint(0, WIDTH)
    y1 = random.randint(0, HEIGHT)
    x2 = random.randint(0, WIDTH)
    y2 = random.randint(0, HEIGHT)
    walls.append(Segment((x1, y1), (x2, y2)))
    
walls.append(Segment((0, 0), (WIDTH, 0)))
walls.append(Segment((WIDTH, 0), (WIDTH, HEIGHT)))
walls.append(Segment((WIDTH, HEIGHT), (0, HEIGHT)))
walls.append(Segment((-1, HEIGHT), (0, 0)))
    
particle = Particle()

running = True
while running:
    clock.tick(FPS)
    screen.fill((BLACK))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    particle.update(pygame.mouse.get_pos())
    particle.render(screen, WHITE)
    for wall in walls:
        wall.render(screen, WHITE)
        particle.look_at(screen, walls)
        
    pygame.display.update()