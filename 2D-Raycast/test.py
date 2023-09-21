import pygame 
from math import pi

pygame.init()

size = [600, 600] 
screen = pygame.display.set_mode(size)
while True:
    screen.fill((0, 0, 0))
    for i in range(0, 600, 20):
        vertical_line = pygame.Surface((1, 600), pygame.SRCALPHA)
        vertical_line.fill((0, 255, 0, 100)) # You can change the 100 depending on what transparency it is.
        screen.blit(vertical_line, (i - 1, 0))
        horizontal_line = pygame.Surface((600, 1), pygame.SRCALPHA)
        horizontal_line.fill((0, 255, 0, 100)) # You can change the 100 depending on what transparency it is.
        screen.blit(horizontal_line, (0, i - 1))

    pygame.display.flip()

pygame.quit()