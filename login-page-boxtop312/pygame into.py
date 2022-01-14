import pygame
import random
import time
import math

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
    def __init__(self):
        super(Player, self).__init__()
        ball = pygame.image.load("player.png")
        self.surf = pygame.Surface((64, 64))
        self.surf.fill((255, 255, 255, 0))
        self.surf.set_colorkey("white")
        self.surf.blit(ball, (0, 0))
        self.rect = self.surf.get_rect()

    # Move the sprite based on key presses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -1)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 1)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1, 0)
        if pressed_keys[K_RIGHT]:
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
    def __init__(self, shape):
        super(OtherThing, self).__init__()
        self.surf = pygame.Surface((64, 64))
        self.surf.fill((255, 255, 255, 0))
        self.surf.set_colorkey("white")
        self.surf.blit(shape, (0, 0))
        self.rect = self.surf.get_rect()
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)
        self.deltaX = random.choice([-.1, .1])
        self.deltaY = .1

    def update(self):
        if monster:
            x1 = player.rect.right - self.rect.right
            y1 = player.rect.top - self.rect.top
            hyp = math.sqrt((x1 ** 2) + (y1 ** 2))
            if hyp == 0:
                hyp = 0.000001
            self.deltaX = ((0.34 * x1) / hyp)
            self.deltaY = ((0.34 * y1) / hyp)

            self.x += self.deltaX
            self.y += self.deltaY
            self.rect.right = self.x
            self.rect.top = self.y

            if self.rect.left < 0:
                self.deltaX = .1
            if self.rect.right > 800:
                self.deltaX = -.1
            if self.rect.top < 0:
                self.deltaY = .1
            if self.rect.bottom > 600:
                self.deltaY = -.1
        else:
            self.x += self.deltaX
            self.y += self.deltaY
            self.rect.right = self.x
            self.rect.top = self.y

            if self.rect.left < 0:
                self.deltaX = .1
            if self.rect.right > 800:
                self.deltaX = -.1
            if self.rect.top < 0:
                self.deltaY = .1
            if self.rect.bottom > 600:
                self.deltaY = -.1

    def changer(self, triangle, square, pentagon, hexagon, heptagon, start):
        if monster:
            self.surf.fill((255, 255, 255, 0))
            self.surf.blit(heptagon, (0, 0))
        else:
            if (time.time() - start) > 5:
                self.surf.fill((255, 255, 255, 0))
                self.surf.blit(heptagon, (0, 0))
            elif (time.time() - start) > 4:
                self.surf.fill((255, 255, 255, 0))
                self.surf.blit(hexagon, (0, 0))
            elif (time.time() - start) > 3:
                self.surf.fill((255, 255, 255, 0))
                self.surf.blit(pentagon, (0, 0))
            elif (time.time() - start) > 2:
                self.surf.fill((255, 255, 255, 0))
                self.surf.blit(square, (0, 0))
            elif (time.time() - start) > 1 or 0:
                self.surf.fill((255, 255, 255, 0))
                self.surf.blit(triangle, (0, 0))

    def killed(self):
        if monster:
            pass
        else:
            self.x = random.randint(0, SCREEN_WIDTH)
            self.y = random.randint(0, SCREEN_HEIGHT)
            self.deltaX = random.choice([-.1, .1])
            self.deltaY = .1

            self.x += self.deltaX
            self.y += self.deltaY
            self.rect.right = self.x
            self.rect.top = self.y

            if self.rect.left < 0:
                self.deltaX = .1
            if self.rect.right > 800:
                self.deltaX = -.1
            if self.rect.top < 0:
                self.deltaY = .1
            if self.rect.bottom > 600:
                self.deltaY = -.1


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


triangle = pygame.image.load("caution.png")
square = pygame.image.load("stop.png")
pentagon = pygame.image.load("pentagon.png")
hexagon = pygame.image.load("hexagon.png")
heptagon = pygame.image.load("heptagon.png")
blank = pygame.image.load("blank.png")
player = Player()
prize = OtherThing(blank)

# create a group to hold prizes objects and all objects
prizes = pygame.sprite.Group()
for p in range(10):
    prizes.add(OtherThing(triangle))

# create a group to hold all spites
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(prizes)

# Variable to keep our main loop running
running = True
monster = False
start = time.time()
score = 0

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

    # Background Image
    screen.blit(background, (0, 0))

    # Create a Surface object

    screen.blit(player.surf, player.rect)
    screen.blit(prize.surf, prize.rect)

    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()

    # Update the player sprite based on user key presses
    player.update(pressed_keys)
    prize.update()

    for p in prizes:
        p.update()
        p.changer(triangle, square, pentagon, hexagon, heptagon, start)

    if (time.time() - start) > 5:
        if monster:
            monster = False
        else:
            monster = True
        start = time.time()

    # Colision
    if pygame.sprite.spritecollide(player, prizes, False):
        prize_list = pygame.sprite.spritecollide(player, prizes, False)
        for p in prize_list:
            if monster:
                player.kill()
                running = False
            else:
                p.killed()
                score += 100
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    # Updates the screen
    pygame.display.update()
# creates things for displaying text
font = pygame.font.Font("arial.ttf", 32)
text = font.render(("Game Over Your Score is: " + str(score)), True, (0, 0, 0))
textRect = text.get_rect()
textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
screen.blit(text, textRect)
pygame.display.update()
time.sleep(2)
