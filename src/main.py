from enum import IntEnum
import pygame
import Ui, Menus

# -- APP SETUP -- #

pygame.init()

currentMenu = Menus.Types.NOT_LOGGED_IN
displayWidth, displayHeight = pygame.display.Info().current_w, pygame.display.Info().current_h

width, height = 729, 1080
scale = displayHeight / height

display = pygame.display
display.set_caption("Appli Projet Citoyen")
screen = pygame.display.set_mode((width * scale, height * scale)) 
Menus.setScreenSize(width, height, scale)


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
    