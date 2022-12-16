from game.constants import WINDOW, RANGE, TILE_SIZE
import pygame, random

# // Initialize pygame
pygame.init()

# // Lambda function to get a random position
get_random_position = lambda: (random.randrange(*RANGE), random.randrange(*RANGE))

# // Snake object
class Snake:
    def __init__(self, obstacles):
        self.body = pygame.Rect((0, 0, TILE_SIZE - 2, TILE_SIZE - 2))
        self.high_score = 1
        self.time = 0
        self.time_step = 110
        self.reset(obstacles)

    # // Update the snake's direction
    def update_direction(self, event_key):
        # // If the event key exists in the directions map
        if event_key not in self.directions:
            return

        # // Check if the key is enabled
        elif self.directions[event_key]["enabled"]:
            self.current_direction = self.directions[event_key]["dir"]

            # // Enable all the keys
            for key in self.directions.values():
                key["enabled"] = True
            
            # // Disable the opposite key to prevent the snake 
            # // from going backwards and colliding with itself
            self.directions[self.directions[event_key]["opp"]]["enabled"] = False
    
    # // Move the snake
    def move(self):
        time_now = pygame.time.get_ticks()
        if time_now - self.time > self.time_step:
            self.time = time_now
            self.body.move_ip(self.current_direction)
            self.segments.append(self.body.copy())
            self.segments = self.segments[-self.size:]
    
    # // Check if the snake is out of bounds / collided with itself
    def had_collision(self, obstacles):
        # // Define the out of bounds variables
        too_far_left = self.body.left < 0
        too_far_right = self.body.right > WINDOW
        too_far_top = self.body.top < 0
        too_far_bottom = self.body.bottom > WINDOW

        # // Check if the snake collided with an obstacle
        for o in obstacles:
            if self.body.colliderect(o.item):
                return True
        
        # // Check if the snake collided with itself
        for s in self.segments[:-1]:
            if self.body.colliderect(s):
                return True
        
        # // Return whether the snake was out of bounds
        return too_far_left or too_far_right or too_far_top or too_far_bottom
    
    # // Reset the snake
    def reset(self, obstacles):
        # // Reset the snake's position (make sure it doesn't overlap with an obstacle)
        self.body.center = get_random_position()
        while self.body.center in [obstacle.item.center for obstacle in obstacles]:
            self.body.center = get_random_position()

        # // Reset the rest of the snake's components
        self.segments = [self.body.copy()]
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
