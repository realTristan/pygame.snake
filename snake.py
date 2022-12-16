import pygame, random

# // Initialize pygame
pygame.init()

# // Initalize constants
WINDOW = 1000
TILE_SIZE = 50
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)

# // Initialize global variables
time, time_step = 0, 110

# // Lambda function to get a random position
get_random_position = lambda: (random.randrange(*RANGE), random.randrange(*RANGE))

# // Snake object
class Snake:
    def __init__(self):
        self.body = pygame.rect.Rect((0, 0, TILE_SIZE - 2, TILE_SIZE - 2))
        self.body.center = get_random_position()
        self.segments = (self.body.copy())
        self.current_direction = (0, 0)
        self.size = 1
        self.directions = {
            pygame.K_w: {
                "enable": True,
                "dir": (0, -TILE_SIZE),
                "opp": pygame.K_s
            }, 
            pygame.K_s: {
                "enable": True,
                "dir": (0, TILE_SIZE),
                "opp": pygame.K_w
            }, 
            pygame.K_a: {
                "enable": True,
                "dir": (-TILE_SIZE, 0),
                "opp": pygame.K_d
            }, 
            pygame.K_d: {
                "enable": True,
                "dir": (TILE_SIZE, 0),
                "opp": pygame.K_a
            }
        }
    
    # // Move the snake
    def move(self):
        time_now = pygame.time.get_ticks()
        self.body.move_ip(self.current_direction)
        self.segments = (self.body.copy(), *self.segments[:self.size - 1])

        # // Update snake position based on fps
        if time_now - time > time_step:
            time = time_now
            self.body.move_ip(self.current_direction)
            snake_segments.append(self.body.copy())
            snake_segments = snake_segments[-self.size:]
    
    # // Check if the snake is out of bounds
    def is_out_of_bounds(self):
        self_eating = pygame.Rect.collidelist(self.body, self.segments) != -1
        return self.body.left < 0 or self.body.right > WINDOW or self.body.top < 0 or self.body.bottom > WINDOW or self_eating
    
    # // Reset the snake
    def reset(self):
        self.body.center = get_random_position()
        self.size, self.current_direction = 1, (0, 0)
        self.segments = (self.body.copy())
