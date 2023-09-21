# Import necessary modules and classes
import pygame, math
from typing import Tuple
from vector import Vector2D

class Ray():
    def __init__(self, origin: Tuple[float, float], angle: float = 0):
        self.origin = Vector2D(*origin)
        self.direction = Vector2D(math.cos(angle), math.sin(angle))
        self.direction.normalize()
        self.thresh = 1e-6   
        
    def look_at(self, direction: Tuple[float, float]):
        target = Vector2D(*direction)
        self.direction = target - self.origin
        self.direction.normalize()
        
    def cast(self, segment: 'Segment') -> Vector2D:
        x1, y1 = segment.start.as_tuple()
        x2, y2 = segment.end.as_tuple()
        
        x3, y3 = self.origin.as_tuple()
        x4 = self.origin.x + self.direction.x
        y4 = self.origin.y + self.direction.y
        
        denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if denominator == 0 or abs(denominator) < self.thresh:
            return None
    
        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denominator

        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / denominator
        
        if t > 0 and t < 1 and u > 0:
            pt = Vector2D(x1 + t * (x2 - x1), y1 + t * (y2 - y1))
            return pt
        return None
    
    def update(self, mouse_pos: Tuple[int, int]):
        self.look_at(mouse_pos)
        
    def render(self, surface: pygame.Surface, color: Tuple[int, int, int], t: float = 10):
        # Calculate the endpoint of the ray based on the parameter t
        endpoint = self.origin + self.direction * t
        pygame.draw.line(surface, color, self.origin.as_tuple(), endpoint.as_tuple())
        
