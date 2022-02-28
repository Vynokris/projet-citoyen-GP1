from pickle import TRUE
import pygame


def button(screen: pygame.Surface, caption: str, posX: int, posY: int, textSize: int, color: tuple):
    """Draws a button on the given surface and returns True if it is pressed."""

    # Create the button's caption.
    font = pygame.font.SysFont(None, textSize)
    img = font.render(caption, True, color)

    # Get the button size.
    boundingBox = pygame.Rect(posX - img.get_width() // 2 - 10, posY - img.get_height() // 2 - 10, 
                              img.get_width() + 10, img.get_height() + 10)

    # Draw the button rectangle.
    pygame.draw.rect(screen, color, boundingBox, 2, 5)

    # Draw the button's caption.
    screen.blit(img, (boundingBox.left + 5, boundingBox.top + 5))

    # Check if the button is pressed.
    if boundingBox.contains((pygame.mouse.get_pos(), (1, 1))):
        if pygame.mouse.get_pressed()[0]:
            return True
    return False


def inputStr(screen: pygame.surface, caption: str, input: str, posX: int, posY: int, textSize: int, maxChars: int, color: tuple):
    """Draws a text input box. Returns the input string when it is modified."""

    # Initialize the font.
    font = pygame.font.SysFont(None, textSize)

    # Get the input box's max size.
    img = font.render("W"*maxChars, True, color)
    boundingBox = pygame.Rect(posX - img.get_width() // 2 - 10, posY - img.get_height() // 2 - 10, 
                              img.get_width() + 10, img.get_height() + 10)

    # Draw the caption.
    img = font.render(caption, True, color)
    screen.blit(img, (boundingBox.left + 5, boundingBox.top - boundingBox.height + 5))

    # Draw the input rectangle.
    pygame.draw.rect(screen, color, boundingBox, 2, 5)
