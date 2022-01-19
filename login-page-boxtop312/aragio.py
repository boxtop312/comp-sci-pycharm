import pygame, random, math

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    KEYUP,
    QUIT,
)


def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


class Food(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Food, self).__init__()
        self.surf = pygame.Surface((12, 12))
        self.surf.fill((0, 0, 0, 0))
        self.surf.set_colorkey("black")
        self.radius = 6
        # Arguments for draw.circle(surface,(R,G,B),(x,y for location on surface),radius, width edge )
        pygame.draw.circle(self.surf, (random_color()), (self.radius, self.radius), self.radius, 3)
        self.rect = self.surf.get_rect()
        self.rect.left = x
        self.rect.top = y


class Player(pygame.sprite.Sprite):
    # Constructor
    def __init__(self):
        super(Player, self).__init__()
        self.radius = 25
        self.surf = pygame.Surface((self.radius * 2, self.radius * 2))
        pygame.draw.circle(self.surf, random_color(), (self.radius, self.radius), self.radius, 10)
        self.rect = self.surf.get_rect()


# Initialize pygame
pygame.init()

# Define constants for the screen width and height
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Group contains all of the food objects
comida = pygame.sprite.Group()
for f in range(20):
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    comida.add(Food(x, y))

all_sprites = pygame.sprite.Group()
all_sprites.add(comida)

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
    screen.fill((0, 128, 128))
    for x in range(0, SCREEN_WIDTH, 25):
        pygame.draw.line(screen, (255, 255, 255), (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, 25):
        pygame.draw.line(screen, (255, 255, 255), (0, y), (SCREEN_WIDTH, y))

    for a in all_sprites:
        screen.blit(a.surf, a.rect)

    # Updates the screen
    pygame.display.update()
