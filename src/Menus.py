import pygame
import Ui
from enum import IntEnum



screenWidth, screenHeight, screenScale, widthOffset, heightOffset = 0, 0, 1, 0, 0
pygameEvents = 0


class Types(IntEnum):
    NOT_LOGGED_IN = 0
    LOG_IN      = 1
    SIGN_UP     = 2
    MAIN_0      = 3
    MAIN_1      = 4
    MAIN_2      = 5
    MAIN_3      = 6
    RECIPE_0    = 7
    RECIPE_1    = 8
    RECIPE_2    = 9
    CHALLENGE_0 = 10
    CHALLENGE_1 = 11
    CHALLENGE_2 = 12
    CO2_COUNTER = 13


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

    topRectColor = (255, 255, 255)
    botRectColor = (255, 255, 255)

    # Not logged in menu.
    if currentMenu == Types.NOT_LOGGED_IN:
        currentMenu = notLoggedIn(screen)
        botRectColor = (216, 247, 188)

    # Sign up menu.
    elif currentMenu == Types.SIGN_UP:
        currentMenu = signUp(screen)
        topRectColor = (216, 247, 188)
        botRectColor = (216, 247, 188)

    # Log in menu.
    elif currentMenu == Types.LOG_IN:
        currentMenu = logIn(screen)
        botRectColor = (216, 247, 188)
    
    # Main menu 0.
    elif currentMenu == Types.MAIN_0:
        currentMenu = main0(screen)
        botRectColor = (217, 233, 188)
    
    # Main menu 1.
    elif currentMenu == Types.MAIN_1:
        currentMenu = main1(screen)
        botRectColor = (217, 233, 188)
    
    # Main menu 2.
    elif currentMenu == Types.MAIN_2:
        currentMenu = main2(screen)
        botRectColor = (217, 233, 188)
    
    # Main menu 3.
    elif currentMenu == Types.MAIN_3:
        currentMenu = main3(screen)
        botRectColor = (217, 233, 188)

    # Recipe page 0.
    elif currentMenu == Types.RECIPE_0:
        currentMenu = recipe0(screen)

    # Recipe page 1.
    elif currentMenu == Types.RECIPE_1:
        currentMenu = recipe1(screen)

    # Recipe page 2.
    elif currentMenu == Types.RECIPE_2:
        currentMenu = recipe2(screen)

    # Challenge page 0.
    elif currentMenu == Types.CHALLENGE_0:
        currentMenu = challenge0(screen)

    # Challenge page 1.
    elif currentMenu == Types.CHALLENGE_1:
        currentMenu = challenge1(screen)

    # Challenge page 2.
    elif currentMenu == Types.CHALLENGE_2:
        currentMenu = challenge2(screen)

    # Co2 counter.
    elif currentMenu == Types.CO2_COUNTER:
        currentMenu = co2menu(screen)

    # Draw the two side white rectangles.
    if widthOffset > 0:
        pygame.draw.rect(screen, (255, 255, 255), (0, 0, widthOffset, screenHeight * screenScale))
        pygame.draw.rect(screen, (255, 255, 255), (widthOffset + screenWidth * screenScale, 0, widthOffset, screenHeight * screenScale))
    else:
        pygame.draw.rect(screen, topRectColor,    (0, 0, screenWidth * screenScale, heightOffset))
        pygame.draw.rect(screen, botRectColor,    (0, heightOffset + screenHeight * screenScale, screenWidth * screenScale, heightOffset))
    
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
    pygame.draw.circle(screen, (255, 255, 255), (int(screenScale*screenWidth//2+widthOffset), int(screenScale*-30+heightOffset)), int(screenScale*700))
    pygame.draw.circle(screen, (166, 239,  68), (int(screenScale*screenWidth//2+widthOffset), int(screenScale*-30+heightOffset)), int(screenScale*700), 10)
    pygame.draw.circle(screen, (176, 133, 114), (int(screenScale*screenWidth//2+widthOffset), int(screenScale*300+heightOffset)), int(screenScale*243))
    pygame.draw.circle(screen, ( 95,  67,  39), (int(screenScale*screenWidth//2+widthOffset), int(screenScale*300+heightOffset)), int(screenScale*243), 10)

    # Draw logo.
    img = pygame.image.load("Resources/logo.png")
    img = pygame.transform.scale(img, (int(screenScale * 300), int(screenScale * 300)))
    Ui.image(screen, img, screenWidth//2, 300)

    # Sign up and Login buttons.
    if Ui.button(screen, "Inscription", screenWidth//2, 800, 100, mouseClicked):
        return Types.SIGN_UP
    if Ui.button(screen, "Connexion", screenWidth//2, 980, 60, mouseClicked):
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
    Ui.text(screen, "Inscription", screenWidth//2, 60, 60)

    # Draw the back button.
    if Ui.button(screen, "<", 37, 50, 55, mouseClicked):
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
                                                 25, pygameEvents, mouseClicked, maxChars=int(i==6)*5, onlyNumbers=i==6, hideInput=(signUp.hidePass if i==3 else False))
        if selected: 
            signUp.selectedInput = i
            inputSelected = True
    
    if not inputSelected:
        signUp.selectedInput = -1

    # Draw the show password button.
    if Ui.button(screen, "Montrer" if signUp.hidePass else "Cacher", screenWidth - 69, 510, 25, mouseClicked):
        signUp.hidePass = not signUp.hidePass

    # Draw the newsletter checkbox.
    signUp.newsletter = Ui.checkbox(screen, "S'abonner à la newsletter", signUp.newsletter, 590, 852, 20, mouseClicked)

    # Draw the sign up button.
    if Ui.button(screen, "S'inscrire", screenWidth//2, 1000, 60, mouseClicked):
        return Types.MAIN_0

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
    img = pygame.transform.scale(img, (int(screenScale * 300), int(screenScale * 300)))
    Ui.image(screen, img, screenWidth//2, 300)

    # Draw the back button.
    if Ui.button(screen, "<", 37, 50, 55, mouseClicked):
        return Types.NOT_LOGGED_IN

    # Define the input boxes text and positions.
    inputBoxes = [ ["E-mail",       screenWidth//2, 735, screenWidth - 50], 
                   ["Mot de passe", screenWidth//2, 835, screenWidth - 50] ]
    
    # Draw the input boxes.
    inputSelected = False
    for i in range(len(inputBoxes)):
        selected, logIn.inputs[i] = Ui.inputStr(screen, inputBoxes[i][0], logIn.selectedInput == i, logIn.inputs[i], inputBoxes[i][1], inputBoxes[i][2], inputBoxes[i][3], 
                                                25, pygameEvents, mouseClicked, hideInput=(logIn.hidePass if i==1 else False))
        if selected: 
            logIn.selectedInput = i
            inputSelected = True
    
    if not inputSelected:
        logIn.selectedInput = -1

    # Draw the show password button.
    if Ui.button(screen, "Montrer" if logIn.hidePass else "Cacher", screenWidth - 69, 695, 25, mouseClicked):
        logIn.hidePass = not logIn.hidePass
    
    # Draw the "forgotten password" button.
    Ui.button(screen, "Mot de passe oublié ?", screenWidth - 149, 775, 25, mouseClicked)

    # Draw the login button.
    # TODO: maybe check if the input boxes are filled in.
    if Ui.button(screen, "Se connecter", screenWidth - 190, 970, 55, mouseClicked):
        return Types.MAIN_0

    # Login with facebook button.
    img = pygame.image.load("Resources/Facebook.png")
    img = pygame.transform.scale(img, (int(screenScale * 60), int(screenScale * 60)))
    if Ui.buttonImage(screen, img, 58, 930, mouseClicked):
        return Types.MAIN_0

    # Login with google button.
    img = pygame.image.load("Resources/Google.png")
    img = pygame.transform.scale(img, (int(screenScale * 70), int(screenScale * 70)))
    if Ui.buttonImage(screen, img, 58, 1030, mouseClicked):
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

    # Show the whole page.
    img = pygame.image.load("Resources/News.png")
    img = pygame.transform.scale(img, (int(screenScale * img.get_width() * 0.85), int(screenScale * img.get_height() * 0.85)))
    Ui.image(screen, img, screenWidth//2, screenHeight//2)

    # Draw the bottom color.
    pygame.draw.rect(screen, (217, 233, 188), (widthOffset, screenScale * screenHeight + heightOffset - 50 * screenScale, screenScale * screenWidth, 50 * screenScale))

    # Draw the bottom line.
    pygame.draw.line(screen, (167, 204, 64), (widthOffset,                             screenScale * screenHeight + heightOffset - 50 * screenScale),
                                             (widthOffset + screenScale * screenWidth, screenScale * screenHeight + heightOffset - 50 * screenScale), 3)

    # Show the bottom navigation buttons.
    pygame.draw.circle(screen, (217, 233, 188), (widthOffset + 150 * screenScale, screenScale * screenHeight + heightOffset - 80 * screenScale), 60 * screenScale)
    pygame.draw.circle(screen, (167, 204,  64), (widthOffset + 150 * screenScale, screenScale * screenHeight + heightOffset - 80 * screenScale), 60 * screenScale, 4)
    if Ui.buttonCircle(screen, 300, screenHeight - 60, 40, mouseClicked, 3, (167, 204, 64), True, (255, 255, 255)):
        return Types.MAIN_1
    if Ui.buttonCircle(screen, 450, screenHeight - 60, 40, mouseClicked, 3, (167, 204, 64), True, (255, 255, 255)):
        return Types.MAIN_2
    if Ui.buttonCircle(screen, 600, screenHeight - 60, 40, mouseClicked, 3, (167, 204, 64), True, (255, 255, 255)):
        return Types.MAIN_3

    return Types.MAIN_0


def main1(screen: pygame.Surface):
    """Shows the center-left main menu."""

    mouseClicked = False
    for event in pygameEvents:
        # Check if the mouse was clicked.
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
            mouseClicked = True
        # Go to the next input if enter is pressed.
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and 0 <= logIn.selectedInput <= 2:
            logIn.selectedInput += 1
            pygameEvents.remove(event)

    # Show the header.
    img = pygame.image.load("Resources/Recipes of the day/Recettes Du Jour.png")
    img = pygame.transform.scale(img, (int(screenScale * img.get_width()), int(screenScale * img.get_height())))
    Ui.image(screen, img, screenWidth//2, 100)

    # Show the first recipe.
    img = pygame.image.load("Resources/Recipes of the day/Cocottofu au curry.png")
    img = pygame.transform.scale(img, (int(screenScale * img.get_width()), int(screenScale * img.get_height())))
    if Ui.buttonImage(screen, img, screenWidth//2, 310, mouseClicked):
        return Types.RECIPE_0

    # Show the second recipe.
    img = pygame.image.load("Resources/Recipes of the day/Couscous Express.png")
    img = pygame.transform.scale(img, (int(screenScale * img.get_width()), int(screenScale * img.get_height())))
    if Ui.buttonImage(screen, img, screenWidth//2, 560, mouseClicked):
        return Types.RECIPE_1

    # Show the third recipe.
    img = pygame.image.load("Resources/Recipes of the day/Chili Medio Carne.png")
    img = pygame.transform.scale(img, (int(screenScale * img.get_width()), int(screenScale * img.get_height())))
    if Ui.buttonImage(screen, img, screenWidth//2, 810, mouseClicked):
        return Types.RECIPE_2

    # Draw the bottom color.
    pygame.draw.rect(screen, (217,233,188), (widthOffset, screenScale * screenHeight + heightOffset - 50 * screenScale, screenScale * screenWidth, 50 * screenScale))

    # Draw the bottom line.
    pygame.draw.line(screen, (167,204,64), (widthOffset,                             screenScale * screenHeight + heightOffset - 50 * screenScale),
                                           (widthOffset + screenScale * screenWidth, screenScale * screenHeight + heightOffset - 50 * screenScale), 2)

    # Show the bottom navigation buttons.
    if Ui.buttonCircle(screen, 150, screenHeight - 60, 40, mouseClicked, 3, (167, 204, 64), True, (255, 255, 255)):
        return Types.MAIN_0
    pygame.draw.circle(screen, (217, 233, 188), (widthOffset + 300 * screenScale, screenScale * screenHeight + heightOffset - 80 * screenScale), 60 * screenScale)
    pygame.draw.circle(screen, (167, 204,  64), (widthOffset + 300 * screenScale, screenScale * screenHeight + heightOffset - 80 * screenScale), 60 * screenScale, 4)
    if Ui.buttonCircle(screen, 450, screenHeight - 60, 40, mouseClicked, 3, (167, 204, 64), True, (255, 255, 255)):
        return Types.MAIN_2
    if Ui.buttonCircle(screen, 600, screenHeight - 60, 40, mouseClicked, 3, (167, 204, 64), True, (255, 255, 255)):
        return Types.MAIN_3

    return Types.MAIN_1


def main2(screen: pygame.Surface):
    """Shows the center-right main menu."""

    mouseClicked = False
    for event in pygameEvents:
        # Check if the mouse was clicked.
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
            mouseClicked = True
        # Go to the next input if enter is pressed.
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and 0 <= logIn.selectedInput <= 2:
            logIn.selectedInput += 1
            pygameEvents.remove(event)

    # Draw the map image.
    img = pygame.image.load("Resources/Map.png")
    img = pygame.transform.scale(img, (int(screenScale * img.get_width() * 1.1), int(screenScale * img.get_height() * 1.1)))
    Ui.image(screen, img, screenWidth//2, screenHeight//2 - 33)

    # Draw the bottom color.
    pygame.draw.rect(screen, (217,233,188), (widthOffset, screenScale * screenHeight + heightOffset - 50 * screenScale, screenScale * screenWidth, 50 * screenScale))

    # Draw the bottom line.
    pygame.draw.line(screen, (167,204,64), (widthOffset,                             screenScale * screenHeight + heightOffset - 50 * screenScale),
                                           (widthOffset + screenScale * screenWidth, screenScale * screenHeight + heightOffset - 50 * screenScale), 2)

    # Show the bottom navigation buttons.
    if Ui.buttonCircle(screen, 150, screenHeight - 60, 40, mouseClicked, 3, (167, 204, 64), True, (255, 255, 255)):
        return Types.MAIN_0
    if Ui.buttonCircle(screen, 300, screenHeight - 60, 40, mouseClicked, 3, (167, 204, 64), True, (255, 255, 255)):
        return Types.MAIN_1
    pygame.draw.circle(screen, (217, 233, 188), (widthOffset + 450 * screenScale, screenScale * screenHeight + heightOffset - 80 * screenScale), 60 * screenScale)
    pygame.draw.circle(screen, (167, 204,  64), (widthOffset + 450 * screenScale, screenScale * screenHeight + heightOffset - 80 * screenScale), 60 * screenScale, 4)
    if Ui.buttonCircle(screen, 600, screenHeight - 60, 40, mouseClicked, 3, (167, 204, 64), True, (255, 255, 255)):
        return Types.MAIN_3

    return Types.MAIN_2


def main3(screen: pygame.Surface):
    """Shows the rightmost main menu."""

    mouseClicked = False
    for event in pygameEvents:
        # Check if the mouse was clicked.
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
            mouseClicked = True
        # Go to the next input if enter is pressed.
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and 0 <= logIn.selectedInput <= 2:
            logIn.selectedInput += 1
            pygameEvents.remove(event)

    # Show the whole page.
    img = pygame.image.load("Resources/AccountPage.png")
    img = pygame.transform.scale(img, (int(screenScale * img.get_width() * 0.87), int(screenScale * img.get_height() * 0.87)))
    Ui.image(screen, img, screenWidth//2, screenHeight//2 - 20)

    # Draw the bottom color.
    pygame.draw.rect(screen, (217,233,188), (widthOffset, screenScale * screenHeight + heightOffset - 50 * screenScale, screenScale * screenWidth, 50 * screenScale))

    # Draw the bottom line.
    pygame.draw.line(screen, (167,204,64), (widthOffset,                             screenScale * screenHeight + heightOffset - 50 * screenScale),
                                           (widthOffset + screenScale * screenWidth, screenScale * screenHeight + heightOffset - 50 * screenScale), 2)

    # Show the bottom navigation buttons.
    if Ui.buttonCircle(screen, 150, screenHeight - 60, 40, mouseClicked, 3, (167, 204, 64), True, (255, 255, 255)):
        return Types.MAIN_0
    if Ui.buttonCircle(screen, 300, screenHeight - 60, 40, mouseClicked, 3, (167, 204, 64), True, (255, 255, 255)):
        return Types.MAIN_1
    if Ui.buttonCircle(screen, 450, screenHeight - 60, 40, mouseClicked, 3, (167, 204, 64), True, (255, 255, 255)):
        return Types.MAIN_2
    pygame.draw.circle(screen, (217, 233, 188), (widthOffset + 600 * screenScale, screenScale * screenHeight + heightOffset - 80 * screenScale), 60 * screenScale)
    pygame.draw.circle(screen, (167, 204,  64), (widthOffset + 600 * screenScale, screenScale * screenHeight + heightOffset - 80 * screenScale), 60 * screenScale, 4)

    return Types.MAIN_3


def recipe0(screen: pygame.Surface):
    """Draws the recipe page for the cocottofu."""

    mouseClicked = False
    for event in pygameEvents:
        # Check if the mouse was clicked.
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
            mouseClicked = True
        # Go to the next input if enter is pressed.
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and 0 <= logIn.selectedInput <= 2:
            logIn.selectedInput += 1
            pygameEvents.remove(event)

    # Show the whole page.
    img = pygame.image.load("Resources/Recipe Pages/Cocottofu au curry.png")
    img = pygame.transform.scale(img, (int(screenScale * img.get_width() * 0.87), int(screenScale * img.get_height() * 0.87)))
    Ui.image(screen, img, screenWidth//2, screenHeight//2 - 20)

    # Draw the back button.
    if Ui.button(screen, "<", 95, 50, 55, mouseClicked, (167, 204, 64)):
        return Types.MAIN_1

    # Draw the Co2 button.
    img = pygame.image.load("Resources/Recipe Pages/Co2Button.png")
    img = pygame.transform.scale(img, (int(screenScale * img.get_width() * 0.87), int(screenScale * img.get_height() * 0.87)))
    if Ui.buttonImage(screen, img, screenWidth - 80, 210, mouseClicked):
        co2menu.lastMenu = Types.RECIPE_0
        return Types.CO2_COUNTER

    # Draw the challenge button.
    img = pygame.image.load("Resources/Recipe Pages/ChallengeButton.png")
    img = pygame.transform.scale(img, (int(screenScale * img.get_width() * 0.87), int(screenScale * img.get_height() * 0.87)))
    if Ui.buttonImage(screen, img, screenWidth//2, screenHeight - img.get_height()//2, mouseClicked):
        return Types.CHALLENGE_0

    return Types.RECIPE_0


def recipe1(screen: pygame.Surface):
    """Draws the recipe page for the couscous."""

    mouseClicked = False
    for event in pygameEvents:
        # Check if the mouse was clicked.
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
            mouseClicked = True
        # Go to the next input if enter is pressed.
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and 0 <= logIn.selectedInput <= 2:
            logIn.selectedInput += 1
            pygameEvents.remove(event)

    # Show the whole page.
    img = pygame.image.load("Resources/Recipe Pages/Couscous Express.png")
    img = pygame.transform.scale(img, (int(screenScale * img.get_width() * 0.87), int(screenScale * img.get_height() * 0.87)))
    Ui.image(screen, img, screenWidth//2, screenHeight//2 - 20)

    # Draw the back button.
    if Ui.button(screen, "<", 95, 50, 55, mouseClicked, (167, 204, 64)):
        return Types.MAIN_1

    # Draw the Co2 button.
    img = pygame.image.load("Resources/Recipe Pages/Co2Button.png")
    img = pygame.transform.scale(img, (int(screenScale * img.get_width() * 0.87), int(screenScale * img.get_height() * 0.87)))
    if Ui.buttonImage(screen, img, screenWidth - 80, 210, mouseClicked):
        co2menu.lastMenu = Types.RECIPE_1
        return Types.CO2_COUNTER

    # Draw the challenge button.
    img = pygame.image.load("Resources/Recipe Pages/ChallengeButton.png")
    img = pygame.transform.scale(img, (int(screenScale * img.get_width() * 0.87), int(screenScale * img.get_height() * 0.87)))
    if Ui.buttonImage(screen, img, screenWidth//2, screenHeight - img.get_height()//2, mouseClicked):
        return Types.CHALLENGE_1

    return Types.RECIPE_1


def recipe2(screen: pygame.Surface):
    """Draws the recipe page for the chili."""

    mouseClicked = False
    for event in pygameEvents:
        # Check if the mouse was clicked.
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
            mouseClicked = True
        # Go to the next input if enter is pressed.
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and 0 <= logIn.selectedInput <= 2:
            logIn.selectedInput += 1
            pygameEvents.remove(event)

    # Show the whole page.
    img = pygame.image.load("Resources/Recipe Pages/Chili Medio Carne.png")
    img = pygame.transform.scale(img, (int(screenScale * img.get_width() * 0.87), int(screenScale * img.get_height() * 0.87)))
    Ui.image(screen, img, screenWidth//2, screenHeight//2 - 20)

    # Draw the back button.
    if Ui.button(screen, "<", 95, 50, 55, mouseClicked, (167, 204, 64)):
        return Types.MAIN_1

    # Draw the Co2 button.
    img = pygame.image.load("Resources/Recipe Pages/Co2Button.png")
    img = pygame.transform.scale(img, (int(screenScale * img.get_width() * 0.87), int(screenScale * img.get_height() * 0.87)))
    if Ui.buttonImage(screen, img, screenWidth - 80, 210, mouseClicked):
        co2menu.lastMenu = Types.RECIPE_2
        return Types.CO2_COUNTER

    # Draw the challenge button.
    img = pygame.image.load("Resources/Recipe Pages/ChallengeButton.png")
    img = pygame.transform.scale(img, (int(screenScale * img.get_width() * 0.87), int(screenScale * img.get_height() * 0.87)))
    if Ui.buttonImage(screen, img, screenWidth//2, screenHeight - img.get_height()//2, mouseClicked):
        return Types.CHALLENGE_2

    return Types.RECIPE_2


def challenge0(screen: pygame.Surface):
    """Draws the challenge page for the cocottofu."""

    mouseClicked = False
    for event in pygameEvents:
        # Check if the mouse was clicked.
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
            mouseClicked = True
        # Go to the next input if enter is pressed.
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and 0 <= logIn.selectedInput <= 2:
            logIn.selectedInput += 1
            pygameEvents.remove(event)

    # Show the whole page.
    img = pygame.image.load("Resources/Challenges/Cocottofu au curry.png")
    img = pygame.transform.scale(img, (int(screenScale * img.get_width() * 0.95), int(screenScale * img.get_height() * 0.95)))
    Ui.image(screen, img, screenWidth//2, screenHeight//2 + 5)

    # Show the pass button.
    img = pygame.image.load("Resources/Challenges/PassButton.png")
    img = pygame.transform.scale(img, (int(screenScale * img.get_width() * 0.95), int(screenScale * img.get_height() * 0.95)))
    if Ui.buttonImage(screen, img, screenWidth//2, screenHeight - 130, mouseClicked):
        return Types.RECIPE_0

    return Types.CHALLENGE_0


def challenge1(screen: pygame.Surface):
    """Draws the challenge page for the couscous."""

    mouseClicked = False
    for event in pygameEvents:
        # Check if the mouse was clicked.
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
            mouseClicked = True
        # Go to the next input if enter is pressed.
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and 0 <= logIn.selectedInput <= 2:
            logIn.selectedInput += 1
            pygameEvents.remove(event)

    # Show the whole page.
    img = pygame.image.load("Resources/Challenges/Couscous Express.png")
    img = pygame.transform.scale(img, (int(screenScale * img.get_width() * 0.95), int(screenScale * img.get_height() * 0.95)))
    Ui.image(screen, img, screenWidth//2, screenHeight//2 + 5)

    # Show the pass button.
    img = pygame.image.load("Resources/Challenges/PassButton.png")
    img = pygame.transform.scale(img, (int(screenScale * img.get_width() * 0.95), int(screenScale * img.get_height() * 0.95)))
    if Ui.buttonImage(screen, img, screenWidth//2, screenHeight - 130, mouseClicked):
        return Types.RECIPE_1

    return Types.CHALLENGE_1


def challenge2(screen: pygame.Surface):
    """Draws the challenge page for the chili."""

    mouseClicked = False
    for event in pygameEvents:
        # Check if the mouse was clicked.
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
            mouseClicked = True
        # Go to the next input if enter is pressed.
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and 0 <= logIn.selectedInput <= 2:
            logIn.selectedInput += 1
            pygameEvents.remove(event)

    # Show the whole page.
    img = pygame.image.load("Resources/Challenges/Chili Medio Carne.png")
    img = pygame.transform.scale(img, (int(screenScale * img.get_width() * 0.95), int(screenScale * img.get_height() * 0.95)))
    Ui.image(screen, img, screenWidth//2, screenHeight//2 + 5)

    # Show the pass button.
    img = pygame.image.load("Resources/Challenges/PassButton.png")
    img = pygame.transform.scale(img, (int(screenScale * img.get_width() * 0.95), int(screenScale * img.get_height() * 0.95)))
    if Ui.buttonImage(screen, img, screenWidth//2, screenHeight - 130, mouseClicked):
        return Types.RECIPE_2

    return Types.CHALLENGE_2


def co2menu(screen: pygame.Surface):
    """Menu that shows the CO2 consumption of a recipe."""

    mouseClicked = False
    for event in pygameEvents:
        # Check if the mouse was clicked.
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
            mouseClicked = True
        # Go to the next input if enter is pressed.
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and 0 <= logIn.selectedInput <= 2:
            logIn.selectedInput += 1
            pygameEvents.remove(event)

    # Show the whole page.
    img = pygame.image.load("Resources/Recipe Pages/Co2.png")
    img = pygame.transform.scale(img, (int(screenScale * img.get_width() * 0.95), int(screenScale * img.get_height() * 0.95)))
    Ui.image(screen, img, screenWidth//2, screenHeight//2 + 70)

    # Draw the back button.
    if Ui.button(screen, "<", 95, 50, 55, mouseClicked, (167, 204, 64)):
        return co2menu.lastMenu

    return Types.CO2_COUNTER

co2menu.lastMenu = Types.RECIPE_0