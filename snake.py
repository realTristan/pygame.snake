import pygame, random, time

# // Initialize pygame
pygame.init()

# // Initalize constants
WINDOW = 500
TILE_SIZE = 25
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)

# // Lambda function to get a random position
get_random_position = lambda: (random.randrange(*RANGE), random.randrange(*RANGE))

# // Snake object
class Snake:
    def __init__(self):
        self.body = pygame.Rect((0, 0, TILE_SIZE - 2, TILE_SIZE - 2))
        self.reset()

    # // Update the snake's direction
    def update_direction(self, event_key):
        # // Check if the key is enabled
            if self.directions[event_key]["enabled"]:
                self.current_direction = self.directions[event_key]["dir"]

                # // Enable all the keys
                for key in self.directions.values():
                    key["enabled"] = True
                
                # // Disable the opposite key to prevent the snake 
                # // from going backwards and colliding with itself
                self.directions[self.directions[event_key]["opp"]]["enabled"] = False
    
    # // Move the snake
    def move(self):
        self.body.move_ip(self.current_direction)
        self.segments = (self.body.copy(), *self.segments[:self.size - 1])

        # // Update snake position based on fps
        self.body.move_ip(self.current_direction)
        self.segments = (self.segments[-self.size:], self.body.copy())
    
    # // Check if the snake is out of bounds
    def is_out_of_bounds(self):
        too_far_left = self.body.left < 0
        too_far_right = self.body.right > WINDOW
        too_far_top = self.body.top < 0
        too_far_bottom = self.body.bottom > WINDOW
        # self_eating = pygame.Rect.collidelist(self.body, self.segments) != -1
        return too_far_left or too_far_right or too_far_bottom or too_far_top # or self_eating
    
    # // Reset the snake
    def reset(self):
        self.body.center = get_random_position()
        self.segments = (self.body.copy())
        self.current_direction = (0, 0)
        self.size = 1
        self.directions = {
            pygame.K_w: {
                "enabled": True,
                "dir": (0, -TILE_SIZE),
                "opp": pygame.K_s
            }, 
            pygame.K_s: {
                "enabled": True,
                "dir": (0, TILE_SIZE),
                "opp": pygame.K_w
            }, 
            pygame.K_a: {
                "enabled": True,
                "dir": (-TILE_SIZE, 0),
                "opp": pygame.K_d
            }, 
            pygame.K_d: {
                "enabled": True,
                "dir": (TILE_SIZE, 0),
                "opp": pygame.K_a
            }
        }
