import sys, pygame, random
from snake import Snake
from food import Food

# // Initialize pygame
pygame.init()

# // Initalize constants
WINDOW = 1000
TILE_SIZE = 50
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)

# // Initialize global variables
screen = pygame.display.set_mode((WINDOW, WINDOW))
clock = pygame.time.Clock()

# // Initialize the snake and food variables
snake = Snake()
food = Food()

# // Lambda function to get a random position
get_random_position = lambda: (random.randrange(*RANGE), random.randrange(*RANGE))

# // Main loop
while True:
    # // Get the pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        
        # // When the user presses a key
        if event.type == pygame.KEYDOWN:
            # // Snake moves up
            if snake.directions[event.key]["enable"]:
                snake.current_direction = snake.directions[event.key]["dir"]

                # // Enable all the keys
                for key in snake.directions.values():
                    key["enable"] = True
                
                # // Disable the opposite key to prevent the snake 
                # // from going backwards and colliding with itself
                snake.directions[snake.directions[event.key]["opp"]]["enable"] = False

    # // Screen background
    screen.fill("black")

    # // Check if the snake is out of bounds
    if snake.is_out_of_bounds():
        snake.reset()
        food.reset()

    # // Draw the food
    pygame.draw.rect(screen, "red", food)

    # // When the snake eats the food
    if snake.body.center == food.item.center:
        snake.size = snake.size + 1
        food.item.center = get_random_position()
    
    # // Draw the snake
    [pygame.draw.rect(screen, "green", segment) for segment in snake.segments]
    
    # // Move the snake
    snake.move()

    # // Update the display
    pygame.display.flip()
    clock.tick(60)
