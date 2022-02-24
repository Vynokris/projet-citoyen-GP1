from enum import IntEnum
import sys, pygame

# -- UI FUNCTIONS -- #

def button(screen: pygame.Surface, caption: str, rectangle: pygame.Rect, color: tuple):
    """Draws a button on the given surface and returns True if it is pressed."""

    # Draw the button rectangle.
    pygame.draw.rect(screen, color, rectangle, 2)

    # Draw the button text.
    font = pygame.font.SysFont(None, 40)
    img = font.render(caption, True, color)
    screen.blit(img, (rectangle.left, rectangle.top))

    # Check if the button is pressed.
    if rectangle.contains((pygame.mouse.get_pos(), (1, 1))):
        if pygame.mouse.get_pressed()[0]:
            return True
    return False



# -- APP MENUS -- #

def notLoggedInMenu(screen: pygame.Surface, currentMenu: IntEnum):
    """Shows the menu for when the user isn't logged in."""

    # Draw a circle.
    pygame.draw.circle(screen, (0, 0, 0), (width // 2, -30), 700)
    pygame.draw.circle(screen, (255, 255, 255), (width // 2,  300), 150)

    # SignIn and LogIn buttons.
    if button(screen, "Login", pygame.Rect((width//2, 800), (100, 40)), (0, 0, 0)):
        currentMenu = Menus.LOG_IN
    if button(screen, "Sign In", pygame.Rect((width//2, 900), (100, 40)), (0, 0, 0)):
        currentMenu = Menus.SIGN_IN


def signInMenu(screen: pygame.Surface):
    """Shows the sign in menu."""
    
    font = pygame.font.SysFont(None, 15)
    img = font.render("Nom", True, (0, 0, 0))
    screen.blit(img, (300, 300))
    
    
def logInMenu(screen: pygame.Surface):
    """Shows the log in menu."""
    return 0


def mainMenu(screen: pygame.Surface):
    """Shows the main menu."""
    return 0
    
    

# -- APP SETUP -- #

class Menus(IntEnum):
    NOT_LOGGED_IN = 0
    LOG_IN = 1
    SIGN_IN = 2
    MAIN = 3

currentMenu = Menus.NOT_LOGGED_IN

width, height = 729, 1080
pygame.init()

display = pygame.display
display.set_caption("Appli Projet Citoyen")

screen = pygame.display.set_mode((width, height)) 


# -- APP MAIN LOOP -- #

while True:
    # Handle pygame events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    # Wipe the screen with white.
    screen.fill((255, 255, 255))

    if currentMenu == Menus.NOT_LOGGED_IN:
        notLoggedInMenu(screen, currentMenu)

    # Update the display.
    display.flip()
    