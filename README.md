# pygame.snake
pygame.snake is a snake game built with python using the pygame library. Upon pygame.snake's first launch, a menu displaying the game title, a play button, and a quit button is drawn to the window. If the player decides to click the "Quit" button, the game is quickly shut down. Although, if the player decides to click the "Play" button, a maze of cubes is drawn to the screen. The green cube, the snake, is interactable through the keys: ```W: Move Up``` ```A: Move Left``` ```S: Move Down``` and ```D: Move Right```

Seen within the images exhibited below are fifteen purple blocks, each distributed across the screen. These purple blocks act as obstacles that the player must maneuver. If the player (the snake) hits one of these obstacles, the snake's position is reset, along with the player's current score. If the player's current score is greater than zero, a ```Highscore``` will be saved into a variable whose value can be seen located on the window title. To see your current score, also located on the window title, is the ```Score``` header.

To increase your current score, you need to hit the red blocks located on your screen. These red blocks act as food for the snake. When the snake hits one of these red blocks, his body size is increased, with the increment being displayed at the snake's tail. (A block is added to the end of the snake)

Apart from hitting the random purple blocks (obstacles) displayed on the screen, hitting the outer bounds of the window (500x500) will also cause the snake and its components to reset.

![pygame summ 1](https://user-images.githubusercontent.com/75189508/208195364-41b2f3bb-4baf-41b8-a74f-000fa014532d.png)
![pygame summ 3](https://user-images.githubusercontent.com/75189508/208195361-8cabf1fa-0585-4658-99f6-f363f06dc5c8.png)
