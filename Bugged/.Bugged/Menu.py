import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
Width, Height = 800, 600
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Main Menu")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HOVER_COLOR = (100, 100, 100)
BUTTON_COLOR = (50, 50, 50)

# Fonts
pygame.font.init()
font = pygame.font.SysFont("Arial", 36)

# Background
background = pygame.image.load("Assets/Menu/Main_Menu.png")

# Button Class
class Button:
    def __init__(self, text, x, y, width, height, action=None):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = BUTTON_COLOR
        self.action = action

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.color = HOVER_COLOR
        else:
            self.color = BUTTON_COLOR

        pygame.draw.rect(screen, self.color, self.rect)
        text_surf = font.render(self.text, True, WHITE)
        screen.blit(text_surf, (self.rect.x + (self.rect.width - text_surf.get_width()) // 2,
                                 self.rect.y + (self.rect.height - text_surf.get_height()) // 2))

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            if self.action:
                return self.action()  # Return the result of the action function

# Game Functions
def start_game():
    return "game"  # Return the updated game state

def quit_game():
    pygame.quit()
    sys.exit()

# Function to render main menu
def main_menu(screen, game_state):
    # Create buttons
    start_button = Button("Start Game", Width // 2 - 100, Height // 2 - 50, 200, 50, start_game)
    quit_button = Button("Quit", Width // 2 - 100, Height // 2 + 50, 200, 50, quit_game)

    # Main menu loop
    menu_running = True
    while menu_running:
        screen.blit(background, (0, 0))  # Draw background
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Draw buttons
        start_button.draw(screen)
        quit_button.draw(screen)

        # Check button clicks
        new_game_state = start_button.check_click()
        quit_button.check_click()

        # Update the game state if start button is clicked
        if new_game_state == "game":
            menu_running = False  # Exit the menu loop

        # Update display
        pygame.display.update()
        clock.tick(60)

    return new_game_state  # Return the updated game state to Bugged.py