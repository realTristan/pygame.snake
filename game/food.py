from game.constants import RANGE, TILE_SIZE
import pygame, random

# // Lambda function to get a random position
get_random_position = lambda: (random.randrange(*RANGE), random.randrange(*RANGE))

# // Food object
class Food:
    def __init__(self, obstacles):
        self.item = pygame.Rect((0, 0, TILE_SIZE - 2, TILE_SIZE - 2))
        self.reset(obstacles)
    
    # // Reset the food position
    def reset(self, obstacles):
        self.item.center = get_random_position()
        while self.item.center in [obstacle.item.center for obstacle in obstacles]:
            self.item.center = get_random_position()
