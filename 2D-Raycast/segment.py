# Import necessary modules and classes
import pygame
from typing import List, Tuple
from vector import Vector2D

class Segment():
    def __init__(self, start: Tuple[float, float], end: Tuple[float, float]):
        self.start = Vector2D(*start)
        self.end = Vector2D(*end)
        self.thresh = 1e-6
        
    def render(self, surface: pygame.Surface, color: Tuple[int, int, int]):
        pygame.draw.line(surface, color, self.start.as_tuple(), self.end.as_tuple())
        