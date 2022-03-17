from turtle import window_width
import pygame
import Ui
from enum import IntEnum



screenWidth, screenHeight, screenScale, widthOffset, heightOffset = 0, 0, 1, 0, 0
pygameEvents = 0


class Types(IntEnum):
    NOT_LOGGED_IN = 0
    LOG_IN  = 1
    SIGN_UP = 2
    MAIN_0  = 3
    MAIN_1  = 4
    MAIN_2  = 5
    MAIN_3  = 6


def setScreenSize(width: int, height: int, scale: int, offsetW: int, offsetH: int):
    """Sets the screen size to be used by the menus."""
    global screenWidth, screenHeight, screenScale, widthOffset, heightOffset
    screenWidth  = width
    screenHeight = height
    screenScale  = scale
    widthOffset  = offsetW
    heightOffset = offsetH
    Ui.setScreenScale(scale, offsetW, offsetH)


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
    
    # Main menu 0.
    elif currentMenu == Types.MAIN_0:
        currentMenu = main0(screen);
    
    # Main menu 1.
    elif currentMenu == Types.MAIN_1:
        currentMenu = main1(screen);
    
    # Main menu 2.
    elif currentMenu == Types.MAIN_2:
        currentMenu = main2(screen);
    
    # Main menu 3.
    elif currentMenu == Types.MAIN_3:
        currentMenu = main3(screen);
    
    return currentMenu


def notLoggedIn(screen: pygame.Surface):
    """Shows the menu for when the user isn't logged in."""
    
    # Check if the mouse was clicked.
    mouseClicked = False
    for event in pygameEvents:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
            mouseClicked = True

    # Draw circles.
    pygame.draw.rect  (screen, (216, 247, 188), (widthOffset, heightOffset, screenScale*screenWidth, screenScale*screenHeight))
    pygame.draw.circle(screen, (255, 255, 255), (screenScale*screenWidth//2+widthOffset, screenScale*-30+heightOffset), screenScale*700)
    pygame.draw.circle(screen, (166, 239,  68), (screenScale*screenWidth//2+widthOffset, screenScale*-30+heightOffset), screenScale*700, 10)
    pygame.draw.circle(screen, (176, 133, 114), (screenScale*screenWidth//2+widthOffset, screenScale*300+heightOffset), screenScale*243)
    pygame.draw.circle(screen, ( 95,  67,  39), (screenScale*screenWidth//2+widthOffset, screenScale*300+heightOffset), screenScale*243, 10)

    # Draw logo.
    img = pygame.image.load("Resources/logo.png")
    img = pygame.transform.scale(img, (screenScale * 300, screenScale * 300))
    screen.blit(img, (screenWidth//2 - img.get_width()/5 + widthOffset, screenScale*300 - img.get_height()/2 + heightOffset))

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
    pygame.draw.rect  (screen, (216, 247, 188), (widthOffset, heightOffset, screenScale*screenWidth, screenScale*screenHeight))
    pygame.draw.circle(screen, (0, 0, 0), (screenScale*screenWidth//2+widthOffset, screenScale*(-1125)              +heightOffset), screenScale*1300, 2)
    pygame.draw.circle(screen, (0, 0, 0), (screenScale*screenWidth//2+widthOffset, screenScale*(screenHeight + 1125)+heightOffset), screenScale*1300, 2)

    # Draw text.
    Ui.text(screen, "Inscription", screenWidth//2, 60, 100)

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
    pygame.draw.rect  (screen, (216, 247, 188), (widthOffset, heightOffset, screenScale*screenWidth, screenScale*screenHeight))
    pygame.draw.circle(screen, (255, 255, 255), (screenScale*screenWidth//2+widthOffset, screenScale*-30+heightOffset), screenScale*700)
    pygame.draw.circle(screen, (166, 239,  68), (screenScale*screenWidth//2+widthOffset, screenScale*-30+heightOffset), screenScale*700, 10)
    pygame.draw.circle(screen, (176, 133, 114), (screenScale*screenWidth//2+widthOffset, screenScale*300+heightOffset), screenScale*243)
    pygame.draw.circle(screen, ( 95,  67,  39), (screenScale*screenWidth//2+widthOffset, screenScale*300+heightOffset), screenScale*243, 10)

    # Draw logo.
    img = pygame.image.load("Resources/logo.png")
    img = pygame.transform.scale(img, (screenScale * 300, screenScale * 300))
    screen.blit(img, (screenWidth//2 - img.get_width()/5 + widthOffset, screenScale*300 - img.get_height()/2 + heightOffset))

    # Draw the back button.
    if (Ui.button(screen, "<", 37, 50, 100, mouseClicked)):
        return Types.NOT_LOGGED_IN

    # Define the input boxes text and positions.
    inputBoxes = [ ["E-mail",       screenWidth//2, 735, screenWidth - 50], 
                   ["Mot de passe", screenWidth//2, 835, screenWidth - 50] ]
    
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
    if Ui.button(screen, "Montrer" if logIn.hidePass else "Cacher", screenWidth - 80, 695, 40, mouseClicked):
        logIn.hidePass = not logIn.hidePass
    
    # Draw the "forgotten password" button.
    Ui.button(screen, "Mot de passe oublié ?", screenWidth - 168, 775, 40, mouseClicked)

    # Draw the login button.
    # TODO: maybe check if the input boxes are filled in.
    if (Ui.button(screen, "Se connecter", screenWidth//2 + 120, 970, 100, mouseClicked)):
        return Types.MAIN_0

    # Login with facebook button.
    img = pygame.image.load("Resources/Facebook.png")
    img = pygame.transform.scale(img, (screenScale * 60, screenScale * 60))
    if (Ui.buttonImage(screen, img, 58, 930, mouseClicked)):
        return Types.MAIN_0

    # Login with google button.
    img = pygame.image.load("Resources/Google.png")
    img = pygame.transform.scale(img, (screenScale * 70, screenScale * 70))
    if (Ui.buttonImage(screen, img, 58, 1030, mouseClicked)):
        return Types.MAIN_0

    return Types.LOG_IN

# Define login static variables.
logIn.selectedInput = -1
logIn.inputs        = [""]*2
logIn.hidePass      = True


def main0(screen: pygame.Surface):
    """Shows the leftmost main menu."""

    mouseClicked = False
    for event in pygameEvents:
        # Check if the mouse was clicked.
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
            mouseClicked = True
        # Go to the next input if enter is pressed.
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and 0 <= logIn.selectedInput <= 2:
            logIn.selectedInput += 1
            pygameEvents.remove(event)

    # Draw the bottom line.
    pygame.draw.line(screen, (0, 0, 0), (widthOffset,                             screenScale * screenHeight + heightOffset - 50 * screenScale), 
                                        (widthOffset + screenScale * screenWidth, screenScale * screenHeight + heightOffset - 50 * screenScale), 1)

    # Show the bottom navigation buttons.
    pygame.draw.circle(screen, (100, 100, 100), (widthOffset + 150 * screenScale, screenScale * screenHeight + heightOffset - 80 * screenScale), 60 * screenScale)
    if (Ui.buttonCircle(screen, 300, screenHeight - 60, 40, mouseClicked)):
        return Types.MAIN_1
    if (Ui.buttonCircle(screen, 450, screenHeight - 60, 40, mouseClicked)):
        return Types.MAIN_2
    if (Ui.buttonCircle(screen, 600, screenHeight - 60, 40, mouseClicked)):
        return Types.MAIN_3

    return Types.MAIN_0


def main1(screen: pygame.Surface):
    """Shows the leftmost main menu."""

    mouseClicked = False
    for event in pygameEvents:
        # Check if the mouse was clicked.
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
            mouseClicked = True
        # Go to the next input if enter is pressed.
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and 0 <= logIn.selectedInput <= 2:
            logIn.selectedInput += 1
            pygameEvents.remove(event)

    # Draw the bottom line.
    pygame.draw.line(screen, (0, 0, 0), (widthOffset,                             screenScale * screenHeight + heightOffset - 50 * screenScale), 
                                        (widthOffset + screenScale * screenWidth, screenScale * screenHeight + heightOffset - 50 * screenScale), 1)

    # Show the bottom navigation buttons.
    if (Ui.buttonCircle(screen, 150, screenHeight - 60, 40, mouseClicked)):
        return Types.MAIN_0
    pygame.draw.circle(screen, (100, 100, 100), (widthOffset + 300 * screenScale, screenScale * screenHeight + heightOffset - 80 * screenScale), 60 * screenScale)
    if (Ui.buttonCircle(screen, 450, screenHeight - 60, 40, mouseClicked)):
        return Types.MAIN_2
    if (Ui.buttonCircle(screen, 600, screenHeight - 60, 40, mouseClicked)):
        return Types.MAIN_3

    Ui.text(screen, "\"Better to cum in the sink", screenWidth // 2, screenHeight // 2, 60)
    Ui.text(screen, "than to sink in the cum\"", screenWidth // 2, screenHeight // 2 + 100, 60)
    Ui.text(screen, "~Martin Luther King Junior", screenWidth // 2, screenHeight // 2 + 200, 40)

    return Types.MAIN_1


def main2(screen: pygame.Surface):
    """Shows the leftmost main menu."""

    mouseClicked = False
    for event in pygameEvents:
        # Check if the mouse was clicked.
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
            mouseClicked = True
        # Go to the next input if enter is pressed.
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and 0 <= logIn.selectedInput <= 2:
            logIn.selectedInput += 1
            pygameEvents.remove(event)

    # Draw the bottom line.
    pygame.draw.line(screen, (0, 0, 0), (widthOffset,                             screenScale * screenHeight + heightOffset - 50 * screenScale), 
                                        (widthOffset + screenScale * screenWidth, screenScale * screenHeight + heightOffset - 50 * screenScale), 1)

    # Show the bottom navigation buttons.
    if (Ui.buttonCircle(screen, 150, screenHeight - 60, 40, mouseClicked)):
        return Types.MAIN_0
    if (Ui.buttonCircle(screen, 300, screenHeight - 60, 40, mouseClicked)):
        return Types.MAIN_1
    pygame.draw.circle(screen, (100, 100, 100), (widthOffset + 450 * screenScale, screenScale * screenHeight + heightOffset - 80 * screenScale), 60 * screenScale)
    if (Ui.buttonCircle(screen, 600, screenHeight - 60, 40, mouseClicked)):
        return Types.MAIN_3

    # 

    return Types.MAIN_2


def main3(screen: pygame.Surface):
    """Shows the leftmost main menu."""

    mouseClicked = False
    for event in pygameEvents:
        # Check if the mouse was clicked.
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
            mouseClicked = True
        # Go to the next input if enter is pressed.
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and 0 <= logIn.selectedInput <= 2:
            logIn.selectedInput += 1
            pygameEvents.remove(event)

    # Draw the bottom line.
    pygame.draw.line(screen, (0, 0, 0), (widthOffset,                             screenScale * screenHeight + heightOffset - 50 * screenScale), 
                                        (widthOffset + screenScale * screenWidth, screenScale * screenHeight + heightOffset - 50 * screenScale), 1)

    # Show the bottom navigation buttons.
    if (Ui.buttonCircle(screen, 150, screenHeight - 60, 40, mouseClicked)):
        return Types.MAIN_0
    if (Ui.buttonCircle(screen, 300, screenHeight - 60, 40, mouseClicked)):
        return Types.MAIN_1
    if (Ui.buttonCircle(screen, 450, screenHeight - 60, 40, mouseClicked)):
        return Types.MAIN_2
    pygame.draw.circle(screen, (100, 100, 100), (widthOffset + 600 * screenScale, screenScale * screenHeight + heightOffset - 80 * screenScale), 60 * screenScale)

    return Types.MAIN_3