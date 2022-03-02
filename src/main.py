from enum import IntEnum
import pygame
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

running = True
while running:
    # Handle pygame events.
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
    
    # Wipe the screen with white.
    screen.fill((255, 255, 255))

    # Update and draw the current menu.
    currentMenu = Menus.updateMenus(screen, currentMenu, events)

    # Update the display.
    display.flip()
    