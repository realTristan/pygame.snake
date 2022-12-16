import sys, pygame, random
from game.snake import Snake
from game.food import Food
from game.obstacle import Obstacle
from game.constants import WINDOW, RANGE

# // Initialize global variables
screen = pygame.display.set_mode((WINDOW, WINDOW))
clock = pygame.time.Clock()

# // Lambda function to get a random position
get_random_position = lambda: (random.randrange(*RANGE), random.randrange(*RANGE))

# // Create obstacles
obstacles = []
for _ in range(15):
    obstacles.append(Obstacle(obstacles))

# // Initialize the snake and food variables
snake = Snake(obstacles)
food = Food(obstacles)

# // Main Game Loop
def game_loop():
    # // Main loop
    while True:
        # // Fill the background with black
        screen.fill("black")

        # // Update the score, highscore, fps, etc.
        score_multiplier = lambda score: 0 if score == 1 else int(snake.high_score * 6.7194)
        pygame.display.set_caption(
            f"Tristan\'s Snake  |   Score: {score_multiplier(snake.size)}   |   Highscore: {score_multiplier(snake.high_score)}   |   FPS: {clock.get_fps():.2f}"
        )

        # // If the user has a higher score than
        # // their previous highscore...
        if snake.size > snake.high_score:
            snake.high_score = snake.size

        # // Get the pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            
            # // When the user presses a key
            elif event.type == pygame.KEYDOWN:
                snake.update_direction(event.key)

        # // Draw obcstacles
        [pygame.draw.rect(screen, "purple1", obstacle.item) for obstacle in obstacles]

        # // Draw the food
        pygame.draw.rect(screen, "red1", food.item)

        # // When the snake eats the food
        if snake.body.center == food.item.center:
            snake.size = snake.size + 1
            food.reset(obstacles)
        
        # // Draw the snake
        [pygame.draw.rect(screen, "green1", s) for s in snake.segments]
        
        # // Move the snake
        snake.move()

        # // Check if the snake is out of bounds
        if snake.had_collision(obstacles):
            snake.reset(obstacles)
            food.reset(obstacles)

        # // Update the display
        pygame.display.flip()
        clock.tick(60)
