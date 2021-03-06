import pygame



screenScale, widthOffset, heightOffset = 1, 0, 0
path = ""

def setScreenScale(scale: int, offsetW: int, offsetH: int):
    global screenScale, widthOffset, heightOffset
    screenScale  = scale
    widthOffset  = offsetW
    heightOffset = offsetH


def text(screen: pygame.Surface, caption: str, posX: int, posY: int, textSize: int, color: tuple = (0, 0, 0)):
    """Draws text on the given surface."""

    # Transform the position according to the screen.
    posX = posX * screenScale + widthOffset 
    posY = posY * screenScale + heightOffset

    # Draw the text.
    font = pygame.font.Font(path + "Resources/arial.ttf", int(screenScale * textSize))
    img = font.render(caption, True, color)
    screen.blit(img, (posX - img.get_width() // 2, posY - img.get_height() // 2))


def image(screen: pygame.Surface, img: pygame.image, posX: int, posY: int):
    """Draws an image on the given surface."""

    # Transform the position according to the screen.
    posX = posX * screenScale + widthOffset
    posY = posY * screenScale + heightOffset

    # Draw the image.
    screen.blit(img, (posX - img.get_width() // 2, posY - img.get_height() // 2))


def button(screen: pygame.Surface, caption: str, posX: int, posY: int, textSize: int, mouseClicked: bool, color: tuple = (0, 0, 0)):
    """Draws a button on the given surface and returns True if it is pressed."""

    # Transform the position according to the screen.
    posX = posX * screenScale + widthOffset 
    posY = posY * screenScale + heightOffset

    # Create the button's caption.
    font = pygame.font.Font(path + "Resources/arial.ttf", int(screenScale * textSize))
    img = font.render(caption, True, color)

    # Get the button size.
    boundingBox = pygame.Rect(posX - img.get_width()  // 2 - 10 * screenScale, 
                              posY - img.get_height() // 2 - 10 * screenScale, 
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


def buttonCircle(screen: pygame.Surface, posX: int, posY: int, radius: int, mouseClicked: bool, width: int = 0, color: tuple = (0, 0, 0), filled: bool = False, fillColor: tuple = (0, 0, 0)):
    """"Draws a circular button on the given surface and returns True if it is pressed."""

    # Transform the position according to the screen.
    posX = posX * screenScale + widthOffset 
    posY = posY * screenScale + heightOffset

    # Draw the button circle.
    if filled:
        pygame.draw.circle(screen, fillColor, (posX, posY), radius * screenScale)
    pygame.draw.circle(screen, color, (posX, posY), radius * screenScale, width)

    # Get the button's bounding box.
    boundingBox = pygame.Rect(posX - radius, posY - radius, radius * 2, radius * 2) 

    # Check if the button is pressed.
    if mouseClicked and boundingBox.contains((pygame.mouse.get_pos(), (1, 1))):
        return True
    return False

def buttonImage(screen: pygame.Surface, img: pygame.image, posX: int, posY: int, mouseClicked: bool):
    """Draw a button with an image and returns True if it is pressed."""

    # Transform the position according to the screen.
    posX = posX * screenScale + widthOffset 
    posY = posY * screenScale + heightOffset

    # Get the button size.
    boundingBox = pygame.Rect(posX - img.get_width()  // 2 - 10 * screenScale, 
                              posY - img.get_height() // 2 - 10 * screenScale, 
                              img.get_width()  + 10 * screenScale, 
                              img.get_height() + 10 * screenScale) 

    # Draw the button's caption.
    screen.blit(img, (boundingBox.left, boundingBox.top))

    # Check if the button is pressed.
    if mouseClicked and boundingBox.contains((pygame.mouse.get_pos(), (1, 1))):
        return True
    return False


def checkbox(screen: pygame.surface, caption: str, state: bool, posX: int, posY: int, textSize: int, mouseClicked: bool, color: tuple = (0, 0, 0)):
    """Draws a checkbox. Returns true when it is on, and false when it is off."""

    # Transform the position according to the screen.
    posX = posX * screenScale + widthOffset 
    posY = posY * screenScale + heightOffset
    
    # Create the checkbox's caption.
    font = pygame.font.Font(path + "Resources/arial.ttf", int(textSize * screenScale))
    img = font.render(caption, True, color)

    # Get the checkbox size.
    boundingBox = pygame.Rect(posX - img.get_width()  // 2 - 15 * screenScale - img.get_height(), 
                              posY - img.get_height() // 2 - 10 * screenScale, 
                              img.get_width()  + 15 * screenScale, 
                              img.get_height() + 10 * screenScale) 
    
    # Draw the checkbox rectangle.
    pygame.draw.rect(screen, color, (boundingBox.left, boundingBox.top, img.get_height()+5*screenScale, img.get_height()+5*screenScale), int(2 * screenScale), 5)
    if state:
        pygame.draw.rect(screen, color, (boundingBox.left + 3*screenScale, boundingBox.top + 3*screenScale, img.get_height() - int(1*screenScale), img.get_height() - int(1*screenScale)), 0, 5)

    # Draw the checkbox's caption.
    screen.blit(img, (boundingBox.left + img.get_height() + 10*screenScale, boundingBox.top + 5*screenScale))

    # Check if the user clicked on the checkbox.
    if mouseClicked and boundingBox.contains((pygame.mouse.get_pos(), (1, 1))):
        state = not state
    return state


def inputStr(screen: pygame.surface, caption: str, selected: bool, input: str, posX: int, posY: int, width: int, textSize: int, events: pygame.event, mouseClicked: bool, maxChars: int = 0, onlyNumbers: bool = False, hideInput: bool = False, color: tuple = (0, 0, 0)):
    """Draws a text input box. Returns a tuple: True when it is selected, False when it isn't and the input string."""

    # Transform the position according to the screen.
    posX = posX * screenScale + widthOffset
    posY = posY * screenScale + heightOffset

    # Initialize the font.
    font = pygame.font.Font(path + "Resources/arial.ttf", int(textSize*screenScale))

    # Get the input box's max size.
    img = font.render("W", True, color)
    boundingBox = pygame.Rect(posX - (width // 2 + 10) * screenScale, 
                              posY - img.get_height() // 2 - 10 * screenScale, 
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
        img = font.render("???"*len(input), True, color)
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
