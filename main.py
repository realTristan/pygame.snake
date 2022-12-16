import sys, pygame, random
from snake import Snake
from food import Food

# // Initialize pygame
pygame.init()
pygame.font.init()

# // Initalize constants
WINDOW = 500
TILE_SIZE = 25
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
    pygame.display.set_caption(
        f"Tristan\'s Snake  |   Score: {snake.size}   |   Highscore: {snake.high_score}   |   FPS: {clock.get_fps():.2f}"
    )

    # // Get the pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        
        # // When the user presses a key
        if event.type == pygame.KEYDOWN:
            snake.update_direction(event.key)

    # // Screen background
    screen.fill("black")

    # // Draw the food
    pygame.draw.rect(screen, "red", food.item)

    # // When the snake eats the food
    if snake.body.center == food.item.center:
        snake.size = snake.size + 1

        # // Make sure the food doesn't spawn inside the snake
        while food.item.center in [s.center for s in snake.segments]:
            food.item.center = get_random_position()
    
    # // Draw the snake
    [pygame.draw.rect(screen, "green", s) for s in snake.segments]
    
    # // Move the snake
    snake.move()

    # // Check if the snake is out of bounds
    if snake.had_collision():
        snake.reset()
        food.reset()

    # // Update the display
    pygame.display.flip()
    clock.tick(60)
