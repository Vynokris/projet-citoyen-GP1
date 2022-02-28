from enum import IntEnum
import sys, pygame
import Ui, Menus

# -- APP SETUP -- #

width, height = 729, 1080
currentMenu = Menus.Types.NOT_LOGGED_IN
pygame.init()

display = pygame.display
display.set_caption("Appli Projet Citoyen")
screen = pygame.display.set_mode((width, height)) 
Menus.setScreenSize(width, height)


# -- APP MAIN LOOP -- #

while True:
    # Handle pygame events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    # Wipe the screen with white.
    screen.fill((255, 255, 255))

    # Not logged in menu.
    if currentMenu == Menus.Types.NOT_LOGGED_IN:
        currentMenu = Menus.notLoggedIn(screen)

    # Sign in menu.
    elif currentMenu == Menus.Types.SIGN_UP:
        currentMenu = Menus.signUp(screen)

    # Log in menu.
    elif currentMenu == Menus.Types.LOG_IN:
        currentMenu = Menus.logIn(screen)

    # Update the display.
    display.flip()
    