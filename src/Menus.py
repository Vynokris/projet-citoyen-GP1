from turtle import update
import pygame
import Ui
from enum import IntEnum



screenWidth, screenHeight, screenScale = 0, 0, 1
pygameEvents = 0


class Types(IntEnum):
    NOT_LOGGED_IN = 0
    LOG_IN = 1
    SIGN_UP = 2
    MAIN = 3


def setScreenSize(width: int, height: int, scale: int):
    """Sets the screen size to be used by the menus."""
    global screenWidth, screenHeight, screenScale
    screenWidth  = width
    screenHeight = height
    screenScale  = scale
    Ui.setScreenScale(scale)


def updateMenus(screen: pygame.Surface, currentMenu: Types, events: pygame.event):
    """Updates and draws the current menu."""

    # Update the global events.
    global pygameEvents
    pygameEvents = events

    # Not logged in menu.
    if currentMenu == Types.NOT_LOGGED_IN:
        currentMenu = notLoggedIn(screen)

    # Sign in menu.
    elif currentMenu == Types.SIGN_UP:
        currentMenu = signUp(screen)

    # Log in menu.
    elif currentMenu == Types.LOG_IN:
        currentMenu = logIn(screen)
    
    return currentMenu


def notLoggedIn(screen: pygame.Surface):
    """Shows the menu for when the user isn't logged in."""
    
    # Check if the mouse was clicked.
    mouseClicked = False
    for event in pygameEvents:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
            mouseClicked = True

    # Draw circles.
    pygame.draw.circle(screen, (0,   0,   0  ), (screenScale*screenWidth // 2, screenScale*-30), screenScale*700, 2)
    pygame.draw.circle(screen, (0,   0,   0  ), (screenScale*screenWidth // 2, screenScale*300), screenScale*243)
    pygame.draw.circle(screen, (255, 255, 255), (screenScale*screenWidth // 2, screenScale*300), screenScale*225, 2)
    pygame.draw.circle(screen, (255, 255, 255), (screenScale*screenWidth // 2, screenScale*300), screenScale*235, 2)

    # Sign up and Login buttons.
    if Ui.button(screen, "Inscription", screenWidth//2, 800, 100, mouseClicked):
        return Types.SIGN_UP
    if Ui.button(screen, "Connexion", screenWidth//2, 950, 60, mouseClicked):
        return Types.LOG_IN
    return Types.NOT_LOGGED_IN


def signUp(screen: pygame.Surface):
    """Shows the sign up menu."""
    
    mouseClicked = False
    for event in pygameEvents:
        # Check if the mouse was clicked.
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
            mouseClicked = True
        # Go to the next input if enter is pressed.
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and 0 <= signUp.selectedInput <= 6:
            signUp.selectedInput += 1
            pygameEvents.remove(event)

    # Draw circles.
    pygame.draw.circle(screen, (0, 0, 0), (screenScale*screenWidth // 2, screenScale*(-1125)),               screenScale*1300, 2)
    pygame.draw.circle(screen, (0, 0, 0), (screenScale*screenWidth // 2, screenScale*(screenHeight + 1125)), screenScale*1300, 2)

    # Draw text.
    font = pygame.font.SysFont(None, int(100 * screenScale))
    img = font.render("Inscription", True, (0, 0, 0))
    screen.blit(img, (screenScale*screenWidth//2 - img.get_width()//2, screenScale*60))

    # Draw the back button.
    if (Ui.button(screen, "<", 37, 50, 100, mouseClicked)):
        return Types.NOT_LOGGED_IN

    # Define the input boxes text and positions.
    inputBoxes = [ ["Nom",          screenWidth//2, 250, screenWidth    - 50], 
                   ["Prénom",       screenWidth//2, 350, screenWidth    - 50], 
                   ["E-mail",       screenWidth//2, 450, screenWidth    - 50], 
                   ["Mot de passe", screenWidth//2, 550, screenWidth    - 50], 
                   ["Adresse",      screenWidth//2, 650, screenWidth    - 50], 
                   ["Ville",        screenWidth//2, 750, screenWidth    - 50], 
                   ["Code postal",  187,            850, screenWidth//2 - 50] ]
    
    # Draw the input boxes.
    inputSelected = False
    for i in range(len(inputBoxes)):
        selected, signUp.inputs[i] = Ui.inputStr(screen, inputBoxes[i][0], signUp.selectedInput == i, signUp.inputs[i], inputBoxes[i][1], inputBoxes[i][2], inputBoxes[i][3], 
                                                 40, pygameEvents, mouseClicked, maxChars=int(i==6)*5, onlyNumbers=i==6, hideInput=(signUp.hidePass if i==3 else False))
        if selected: 
            signUp.selectedInput = i
            inputSelected = True
    
    if not inputSelected:
        signUp.selectedInput = -1

    # Draw the show password button.
    if Ui.button(screen, "Montrer" if signUp.hidePass else "Cacher", screenWidth - 80, 510, 40, mouseClicked):
        signUp.hidePass = not signUp.hidePass

    # Draw the newsletter checkbox.
    signUp.newsletter = Ui.checkbox(screen, "S'abonner à la newsletter", signUp.newsletter, 540, 852, 30, mouseClicked)

    # Draw the sign up button.
    Ui.button(screen, "S'inscrire", screenWidth//2, 1000, 100, mouseClicked)

    return Types.SIGN_UP

# Define sign up static variables.
signUp.selectedInput = -1
signUp.inputs        = [""]*7
signUp.newsletter    = True
signUp.hidePass      = True
    
    
def logIn(screen: pygame.Surface):
    """Shows the log in menu."""

    mouseClicked = False
    for event in pygameEvents:
        # Check if the mouse was clicked.
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
            mouseClicked = True
        # Go to the next input if enter is pressed.
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and 0 <= logIn.selectedInput <= 2:
            logIn.selectedInput += 1
            pygameEvents.remove(event)

    # Draw circles.
    pygame.draw.circle(screen, (0, 0, 0), (screenScale*screenWidth // 2, screenScale*(-1100)),              screenScale*1300, 2)
    pygame.draw.circle(screen, (0, 0, 0), (screenScale*screenWidth // 2, screenScale*(screenHeight + 800)), screenScale*1300, 2)

    # Draw text.
    font = pygame.font.SysFont(None, int(100 * screenScale))
    img = font.render("Connexion", True, (0, 0, 0))
    screen.blit(img, (screenScale*screenWidth//2 - img.get_width()//2, screenScale*60))

    # Draw the back button.
    if (Ui.button(screen, "<", 37, 50, 100, mouseClicked)):
        return Types.NOT_LOGGED_IN

    # Define the input boxes text and positions.
    inputBoxes = [ ["E-mail",       screenWidth//2, 350, screenWidth - 50], 
                   ["Mot de passe", screenWidth//2, 450, screenWidth - 50] ]
    
    # Draw the input boxes.
    inputSelected = False
    for i in range(len(inputBoxes)):
        selected, logIn.inputs[i] = Ui.inputStr(screen, inputBoxes[i][0], logIn.selectedInput == i, logIn.inputs[i], inputBoxes[i][1], inputBoxes[i][2], inputBoxes[i][3], 
                                                40, pygameEvents, mouseClicked, hideInput=(logIn.hidePass if i==1 else False))
        if selected: 
            logIn.selectedInput = i
            inputSelected = True
    
    if not inputSelected:
        logIn.selectedInput = -1

    # Draw the show password button.
    if Ui.button(screen, "Montrer" if logIn.hidePass else "Cacher", screenWidth - 80, 410, 40, mouseClicked):
        logIn.hidePass = not logIn.hidePass
    
    # Draw the "forgotten password" button.
    Ui.button(screen, "Mot de passe oublié ?", screenWidth - 171, 492, 40, mouseClicked)

    # Draw the login button.
    Ui.button(screen, "Se connecter", screenWidth//2, 735, 100, mouseClicked)

    # Draw text.
    font = pygame.font.SysFont(None, int(30*screenScale))
    img = font.render("OU", True, (0, 0, 0))
    screen.blit(img, (screenScale*screenWidth//2 - img.get_width()//2, screenScale*820))

    # Draw the google login button.
    Ui.button(screen, " G    Continuer avec Google   ", screenWidth//2, 920, 60, mouseClicked)

    # Draw the facebook login button.
    Ui.button(screen, " F  Continuer avec Facebook ", screenWidth//2, 1000, 60, mouseClicked)

    return Types.LOG_IN

# Define login static variables.
logIn.selectedInput = -1
logIn.inputs        = [""]*2
logIn.hidePass      = True


def main(screen: pygame.Surface):
    """Shows the main menu."""
    return Types.MAIN