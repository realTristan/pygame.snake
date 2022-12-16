import pygame, random

# // Initalize constants
WINDOW = 500
TILE_SIZE = 25
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)

# // Lambda function to get a random position
get_random_position = lambda: (random.randrange(*RANGE), random.randrange(*RANGE))

# // Food object
class Food:
    def __init__(self):
        self.item = pygame.Rect((0, 0, TILE_SIZE - 2, TILE_SIZE - 2))
        self.item.center = get_random_position()
    
    # // Reset the food position
    def reset(self):
        self.item.center = get_random_position()
