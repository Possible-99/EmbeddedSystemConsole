import pygame
import sys

# Initialize PyGame
pygame.init()

# Define the color palette
colors = {
    "background": (46, 52, 64),   # Dark background for depth effect
    "list_bg": (59, 66, 82),      # Slightly lighter background for the list container
    "list_element_bg": (76, 86, 106),  # Background for list elements
    "list_element_hover_bg": (94, 129, 172),  # Hover background color for list elements
    "text": (236, 239, 244),      # Text color for readability
    "instruction_text": (136, 192, 208)  # Color for the instructional text
}

# Set up the screen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game List")

# Set up fonts
font = pygame.font.SysFont('Arial', 16)
large_font = pygame.font.SysFont('Arial', 24)

# Sample game list
games = ["Game 1", "Game 2", "Game 3", "Game 4", "Game 5", "Game 6", "Game 7"]

# Function to draw text
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Main loop
running = True
while running:
    screen.fill(colors["background"])

    # Draw the list background
    list_bg_rect = pygame.Rect(80, 60, 640, 480)
    pygame.draw.rect(screen, colors["list_bg"], list_bg_rect)

    # Draw the instruction text
    draw_text("Please select a game:", large_font, colors["instruction_text"], screen, 100, 70)

    # Draw the list elements
    element_height = 40
    for i, game in enumerate(games):
        element_rect = pygame.Rect(100, 120 + i * (element_height + 10), 600, element_height)
        
        # Check for hover
        if element_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, colors["list_element_hover_bg"], element_rect)
        else:
            pygame.draw.rect(screen, colors["list_element_bg"], element_rect)
        
        draw_text(game, font, colors["text"], screen, element_rect.x + 10, element_rect.y + 10)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
sys.exit()

