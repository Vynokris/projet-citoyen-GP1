import email
import pygame
import Ui
from enum import IntEnum



screenWidth, screenHeight = 0, 0

class Types(IntEnum):
    NOT_LOGGED_IN = 0
    LOG_IN = 1
    SIGN_UP = 2
    MAIN = 3

def setScreenSize(width: int, height: int):
    """Sets the screen size to be used by the menus."""
    global screenWidth, screenHeight
    screenWidth  = width
    screenHeight = height

def notLoggedIn(screen: pygame.Surface):
    """Shows the menu for when the user isn't logged in."""

    # Draw circles.
    pygame.draw.circle(screen, (0, 0, 0), (screenWidth // 2, -30), 700, 2)
    pygame.draw.circle(screen, (0, 0, 0), (screenWidth // 2,  300), 163+80)
    pygame.draw.circle(screen, (255, 255, 255), (screenWidth // 2,  300), 145+80, 2)
    pygame.draw.circle(screen, (255, 255, 255), (screenWidth // 2,  300), 155+80, 2)

    # Sign up and Login buttons.
    if Ui.button(screen, "Sign up", screenWidth//2, 800, 100, (0, 0, 0)):
        return Types.SIGN_UP
    if Ui.button(screen, "Login", screenWidth//2, 950, 60, (0, 0, 0)):
        return Types.LOG_IN
    return Types.NOT_LOGGED_IN


def signUp(screen: pygame.Surface):
    """Shows the sign up menu."""
    
    # Draw circles.
    pygame.draw.circle(screen, (0, 0, 0), (screenWidth // 2, -1100), 1300, 2)
    pygame.draw.circle(screen, (0, 0, 0), (screenWidth // 2, screenHeight + 950), 1300, 2)

    # Draw text.
    font = pygame.font.SysFont(None, 80)
    img = font.render("Sign up", True, (0, 0, 0))
    screen.blit(img, (screenWidth//2 - img.get_width()//2, 60))

    # Define the input strings.
    surnameStr    = ""
    nameStr       = ""
    emailStr      = ""
    adressStr     = ""
    cityStr       = ""
    postalCodeStr = ""

    # Draw the input boxes.
    Ui.inputStr(screen, "Nom",         surnameStr,    187, 300, 40, 12, (0, 0, 0))
    Ui.inputStr(screen, "Prénom",      nameStr,       540, 300, 40, 12, (0, 0, 0))
    Ui.inputStr(screen, "E-mail",      emailStr,      screenWidth//2, 400, 40, 26, (0, 0, 0))
    Ui.inputStr(screen, "Adresse",     adressStr,     screenWidth//2, 500, 40, 26, (0, 0, 0))
    Ui.inputStr(screen, "Ville",       cityStr,       187, 600, 40, 12, (0, 0, 0))
    Ui.inputStr(screen, "Code postal", postalCodeStr, 540, 600, 40, 12, (0, 0, 0))

    return Types.SIGN_UP
    
    
def logIn(screen: pygame.Surface):
    """Shows the log in menu."""
    return Types.LOG_IN


def main(screen: pygame.Surface):
    """Shows the main menu."""
    return Types.MAIN