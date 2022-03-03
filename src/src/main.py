import pygame
import Ui, Menus

# -- APP SETUP -- #

pygame.init()

currentMenu = Menus.Types.NOT_LOGGED_IN
displayWidth, displayHeight = pygame.display.Info().current_w, pygame.display.Info().current_h

width, height = 729, 1080
widthScale   = displayWidth  / width
heightScale  = displayHeight / height
widthOffset  = (displayWidth  - width ) // 2 if widthScale > heightScale else 0
heightOffset = (displayHeight - height) // 2 if widthScale < heightScale else 0
scale        =  widthScale                  if widthScale < heightScale else heightScale

display = pygame.display
display.set_caption("Appli Projet Citoyen")
screen = pygame.display.set_mode((displayWidth, displayHeight)) 
Menus.setScreenSize(width, height, scale, widthOffset, heightOffset)


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

    # Draw white rectangles in offset areas.
    """
    if (widthOffset):
        pygame.draw.rect(screen, (255, 255, 255), (0,                        0, widthOffset, displayHeight))
        pygame.draw.rect(screen, (255, 255, 255), (displayWidth-widthOffset, 0, widthOffset, displayHeight))
    elif (heightOffset):
        pygame.draw.rect(screen, (255, 255, 255), (0, 0,                          displayWidth, heightOffset))
        pygame.draw.rect(screen, (255, 255, 255), (0, displayHeight-heightOffset, displayWidth, heightOffset))
    """

    # Update the display.
    display.flip()
    