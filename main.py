import pygame, sys
from game.loop import game_loop
from ui.button import Button
from game.constants import WINDOW

# // Initialize pygame
pygame.init()
SCREEN = pygame.display.set_mode((WINDOW, WINDOW))
pygame.display.set_caption("Tristan's Snake Summative")

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def main_menu():
    while True:
        SCREEN.fill("black")
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(70).render("SNAKE", True, "#00FF00")
        MENU_RECT = MENU_TEXT.get_rect(center=(250, 100))
        PLAY_BUTTON = Button(
            pos = (250, 215),
            text_input = "PLAY",
            font = get_font(50),
            base_color = "#FF0000",
            hovering_color = "White"
        )
        QUIT_BUTTON = Button(
            pos = (250, 325),
            text_input = "QUIT",
            font = get_font(50),
            base_color = "#FF0000",
            hovering_color = "White"
        )
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        # // Change button color when the user hovers over it
        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        # // Event listener
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # // Listen for mouse clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                # // Start playing the game
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    game_loop()
                
                # // Quit the game
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit(); sys.exit()
        pygame.display.update()

# // Run the program
if __name__ == "__main__":
    main_menu()