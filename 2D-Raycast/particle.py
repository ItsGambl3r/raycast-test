import pygame
from typing import List, Tuple
from constants import *
from vector import Vector2D
from ray import Ray

class Particle(object):
    def __init__(self):
        self.position = Vector2D(WIDTH / 2, HEIGHT / 2)
        self.rays = [Ray(self.position.as_tuple(), angle) for angle in range(0, 360, 1)]
        
    def update(self, mouse_pos: Tuple[int, int]) -> None:
        self.position = Vector2D(*mouse_pos)
        for ray in self.rays:
            ray.origin = self.position
        
    def look_at(self, screen: pygame.Surface, walls: List['Segment']) -> None:
        for ray in self.rays:
            distances = {}  # Store distances to walls
            
            for wall in walls:
                pt = ray.cast(wall)
                if pt:
                    distance_to_wall = self.position.distance(pt)
                    distances[wall] = (distance_to_wall, pt)
            
            if distances:
                # Find the closest wall based on distance
                closest_wall = min(distances, key=lambda w: distances[w][0])
                
                # Draw a line from the ray's origin to the intersection point
                TRANSPARENT_WHITE = (255, 255, 255, 35)
                pygame.draw.line(screen, TRANSPARENT_WHITE, ray.origin.as_tuple(), distances[closest_wall][1].as_tuple())

        

            
    def render(self, surface: pygame.Surface, color: Tuple[int, int, int]) -> None:
        pygame.draw.circle(surface, color, self.position.as_tuple(), 2)
        for ray in self.rays:
            ray.render(surface, color)
        