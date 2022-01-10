import pygame, random, time

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


class Player(pygame.sprite.Sprite):
    def __init__(self, ball):
        super(Player, self).__init__()
        self.surf = pygame.Surface((64, 64))
        self.surf.fill((255, 255, 255, 0))
        self.surf.set_colorkey("white")
        self.surf.blit(ball, (0, 0))
        self.rect = self.surf.get_rect()

    # Move the sprite based on key presses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            print("UP")
            self.rect.move_ip(0, -1)
        if pressed_keys[K_DOWN]:
            print("DOWN")
            self.rect.move_ip(0, 1)
        if pressed_keys[K_LEFT]:
            print("LEFT")
            self.rect.move_ip(-1, 0)
        if pressed_keys[K_RIGHT]:
            print("RIGHT")
            self.rect.move_ip(1, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


class OtherThing(pygame.sprite.Sprite):
    def __init__(self,shape):
        super(OtherThing, self).__init__()
        self.surf = pygame.Surface((64, 64))
        self.surf.fill((255, 255, 255, 0))
        self.surf.set_colorkey("white")
        self.surf.blit(shape, (0, 0))
        self.rect = self.surf.get_rect()

    def update(self):
        x = random.randint(-1,1)
        y = random.randint(-1,1)
        self.rect.move_ip(x, y)

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def timer(self, triangle, square, pentagon, hexagon, heptagon, first):
        if time.time() == (first + 1):
            self.surf.blit(square, (0, 0))
        elif time.time() == (first + 2):
            self.surf.blit(pentagon, (0, 0))
        elif time.time() == (first + 3):
            self.surf.blit(hexagon, (0, 0))
        elif time.time() == (first + 4):
            self.surf.blit(heptagon,(0, 0))
        elif time.time() == (first + 5):
            self.surf.blit(triangle,(0, 0))
            first = time.time()
        screen.blit(prize.surf, prize.rect)


# Initialize pygame
pygame.init()

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Caption and Icon for the screen object
pygame.display.set_caption("Prize Chaser")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# Load Screen background
background = pygame.image.load('background.jpg')

ball = pygame.image.load("player.png")
player = Player(ball)

triangle = pygame.image.load("caution.png")
prize = OtherThing(triangle)
square = pygame.image.load("stop.png")
pentagon = pygame.image.load("pentagon.png")
hexagon = pygame.image.load("hexagon.png")
heptagon = pygame.image.load("heptagon.png")

# create a group to hold prizes objects and all objects
# prizes = pygame.sprinte.Group()
# for p in range(5):
#     x = random.randint(0,550)
#     y = random.randint(0,100)
#     prizes.add(OtherThing(x, y))

# create a group to hold all spites
# all_sprites = pygame.sprites.Group()
# all_sprites.add(Player(ball))
# all_sprites.add(prizes)

# Variable to keep our main loop running
running = True

# Our main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the window close button? If so, stop the loop
        elif event.type == QUIT:
            running = False

    # # Fill the screen with black
    # screen.fill((102, 43, 104))
    # Background Image
    screen.blit(background, (0, 0))

    # for entity in all_sprites:
    #     screen.blit(entity.surf,entity.rect)

    # Create a Surface object

    screen.blit(player.surf, player.rect)
    screen.blit(prize.surf, prize.rect)

    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()

    # Update the player sprite based on user key presses
    player.update(pressed_keys)
    prize.update()

    # Updates the screen
    pygame.display.update()
