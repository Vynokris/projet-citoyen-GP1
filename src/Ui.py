import pygame


def button(screen: pygame.Surface, caption: str, posX: int, posY: int, textSize: int, mouseClicked: bool, color: tuple = (0, 0, 0)):
    """Draws a button on the given surface and returns True if it is pressed."""

    # Create the button's caption.
    font = pygame.font.SysFont(None, textSize)
    img = font.render(caption, True, color)

    # Get the button size.
    boundingBox = pygame.Rect(posX - img.get_width()  // 2 - 10, 
                              posY - img.get_height() // 2 - 10, 
                              img.get_width()  + 10,
                              img.get_height() + 10)

    # Draw the button rectangle.
    pygame.draw.rect(screen, color, boundingBox, 2, 5)

    # Draw the button's caption.
    screen.blit(img, (boundingBox.left + 5, boundingBox.top + 5))

    # Check if the button is pressed.
    if mouseClicked and boundingBox.contains((pygame.mouse.get_pos(), (1, 1))):
        return True
    return False


def checkbox(screen: pygame.surface, caption: str, state: bool, posX: int, posY: int, textSize: int, mouseClicked: bool, color: tuple = (0, 0, 0)):
    """Draws a checkbox. Returns true when it is on, and false when it is off."""
    
    # Create the checkbox's caption.
    font = pygame.font.SysFont(None, textSize)
    img = font.render(caption, True, color)

    # Get the checkbox size.
    boundingBox = pygame.Rect(posX - img.get_width()  // 2 - 15 - img.get_height(), 
                              posY - img.get_height() // 2 - 10, 
                              img.get_width()  + 15, 
                              img.get_height() + 10)
    
    # Draw the checkbox rectangle.
    pygame.draw.rect(screen, color, (boundingBox.left, boundingBox.top, img.get_height()+5, img.get_height()+5), 2, 5)
    if state:
        pygame.draw.rect(screen, color, (boundingBox.left + 3, boundingBox.top + 3, img.get_height() - 1, img.get_height() - 1), 0, 5)

    # Draw the checkbox's caption.
    screen.blit(img, (boundingBox.left + img.get_height() + 10, boundingBox.top + 5))

    # Check if the user clicked on the checkbox.
    if mouseClicked and boundingBox.contains((pygame.mouse.get_pos(), (1, 1))):
        state = not state
    return state


def inputStr(screen: pygame.surface, caption: str, selected: bool, input: str, posX: int, posY: int, width: int, textSize: int, events: pygame.event, mouseClicked: bool, maxChars: int = 0, onlyNumbers: bool = False, hideInput: bool = False, color: tuple = (0, 0, 0)):
    """Draws a text input box. Returns a tuple: True when it is selected, False when it isn't and the input string."""

    # Initialize the font.
    font = pygame.font.SysFont(None, textSize)

    # Get the input box's max size.
    img = font.render("W", True, color)
    boundingBox = pygame.Rect(posX - width // 2 - 10, posY - img.get_height() // 2 - 10, 
                              width + 10, img.get_height() + 10)

    # Draw the caption.
    img = font.render(caption, True, color)
    screen.blit(img, (boundingBox.left + 5, boundingBox.top - boundingBox.height + 5))

    # Draw the input rectangle.
    pygame.draw.rect(screen, color, boundingBox, 2, 5)

    # Draw the input text.
    if not hideInput:
        img = font.render(input, True, color)
    else:
        img = font.render("•"*len(input), True, color)
    screen.blit(img, (boundingBox.left + 5, boundingBox.top + 5))

    # Check if the checkbox is selected.
    if mouseClicked:
        if boundingBox.contains((pygame.mouse.get_pos(), (1, 1))):
            selected = True
        else:
            selected = False

    if selected:
        # Draw the cursor.
        pygame.draw.rect(screen, color, (boundingBox.left + 5 + img.get_width(), boundingBox.top + 5, 2, boundingBox.height - 10))

        # Get keyboard input.
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    input = input[:-1]
                elif onlyNumbers:
                    if (89 <= event.scancode <= 98):
                        input += event.unicode
                else:
                    input += event.unicode
        
        # Limit the input to the box width.
        img = font.render(input, True, color)
        if img.get_width() > width:
            input = input[:-1]
        
        # Limit the input to the max number of characters.
        if maxChars > 0 and len(input) > maxChars:
            input = input[:-1]

    return (selected, input)
