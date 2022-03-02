import pygame



screenScale = 1

def setScreenScale(scale: int):
    global screenScale
    screenScale = scale


def button(screen: pygame.Surface, caption: str, posX: int, posY: int, textSize: int, mouseClicked: bool, color: tuple = (0, 0, 0)):
    """Draws a button on the given surface and returns True if it is pressed."""

    # Create the button's caption.
    font = pygame.font.SysFont(None, int(screenScale * textSize))
    img = font.render(caption, True, color)

    # Get the button size.
    boundingBox = pygame.Rect(posX * screenScale - img.get_width()  // 2 - 10 * screenScale, 
                              posY * screenScale - img.get_height() // 2 - 10 * screenScale, 
                              img.get_width()  + 10 * screenScale, 
                              img.get_height() + 10 * screenScale) 

    # Draw the button rectangle.
    pygame.draw.rect(screen, color, boundingBox, int(2 * screenScale), 5)

    # Draw the button's caption.
    screen.blit(img, (boundingBox.left + 5 * screenScale, boundingBox.top + 5 * screenScale))

    # Check if the button is pressed.
    if mouseClicked and boundingBox.contains((pygame.mouse.get_pos(), (1, 1))):
        return True
    return False


def checkbox(screen: pygame.surface, caption: str, state: bool, posX: int, posY: int, textSize: int, mouseClicked: bool, color: tuple = (0, 0, 0)):
    """Draws a checkbox. Returns true when it is on, and false when it is off."""
    
    # Create the checkbox's caption.
    font = pygame.font.SysFont(None, int(textSize * screenScale))
    img = font.render(caption, True, color)

    # Get the checkbox size.
    boundingBox = pygame.Rect(posX * screenScale - img.get_width()  // 2 - 15 * screenScale - img.get_height(), 
                              posY * screenScale - img.get_height() // 2 - 10 * screenScale, 
                              img.get_width()  + 15 * screenScale, 
                              img.get_height() + 10 * screenScale) 
    
    # Draw the checkbox rectangle.
    pygame.draw.rect(screen, color, (boundingBox.left, boundingBox.top, img.get_height()+5*screenScale, img.get_height()+5*screenScale), int(2 * screenScale), 5)
    if state:
        pygame.draw.rect(screen, color, (boundingBox.left + 3*screenScale, boundingBox.top + 3*screenScale, img.get_height() - screenScale, img.get_height() - screenScale), 0, 5)

    # Draw the checkbox's caption.
    screen.blit(img, (boundingBox.left + img.get_height() + 10*screenScale, boundingBox.top + 5*screenScale))

    # Check if the user clicked on the checkbox.
    if mouseClicked and boundingBox.contains((pygame.mouse.get_pos(), (1, 1))):
        state = not state
    return state


def inputStr(screen: pygame.surface, caption: str, selected: bool, input: str, posX: int, posY: int, width: int, textSize: int, events: pygame.event, mouseClicked: bool, maxChars: int = 0, onlyNumbers: bool = False, hideInput: bool = False, color: tuple = (0, 0, 0)):
    """Draws a text input box. Returns a tuple: True when it is selected, False when it isn't and the input string."""

    # Initialize the font.
    font = pygame.font.SysFont(None, int(textSize*screenScale))

    # Get the input box's max size.
    img = font.render("W", True, color)
    boundingBox = pygame.Rect((posX - width // 2 - 10) * screenScale, 
                              posY * screenScale - img.get_height() // 2 - 10 * screenScale, 
                              (width + 10) * screenScale, 
                              img.get_height() + 10 * screenScale) 

    # Draw the caption.
    img = font.render(caption, True, color)
    screen.blit(img, (boundingBox.left + 5 * screenScale, boundingBox.top - boundingBox.height + 5 * screenScale))

    # Draw the input rectangle.
    pygame.draw.rect(screen, color, boundingBox, int(2 * screenScale), 5)

    # Draw the input text.
    if not hideInput:
        img = font.render(input, True, color)
    else:
        img = font.render("•"*len(input), True, color)
    screen.blit(img, (boundingBox.left + 5 * screenScale, boundingBox.top + 5 * screenScale))

    # Check if the checkbox is selected.
    if mouseClicked:
        if boundingBox.contains((pygame.mouse.get_pos(), (1, 1))):
            selected = True
        else:
            selected = False

    if selected:
        # Draw the cursor.
        pygame.draw.rect(screen, color, (boundingBox.left + 5 * screenScale + img.get_width(), 
                                         boundingBox.top + 5 * screenScale, 
                                         int(2 * screenScale), 
                                         boundingBox.height - 10 * screenScale))

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
        if img.get_width() > width * screenScale:
            input = input[:-1]
        
        # Limit the input to the max number of characters.
        if maxChars > 0 and len(input) > maxChars:
            input = input[:-1]

    return (selected, input)
