import pygame

WIDTH = 800
HEIGHT = 600
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

#define character values
CHAR = (50,50)
SPEED = 10
JUMP = 15
GRAVITY = 1

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(CHAR, pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT/2
        self.xVel = 0
        self.yVel = 0

    def updatePos(self):

        if self.xVel > 0 or self.xVel < 0:
            self.yVel = self.yVel + 2*GRAVITY
        else: 
            self.yVel = self.yVel + 0.7*GRAVITY

        self.rect.x += self.xVel
        self.rect.y += self.yVel

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT - HEIGHT/4:
            self.rect.bottom = HEIGHT - HEIGHT/4
            self.yVel = 0

        self.xVel = 0
        
###################################################################################################
class Player1(Player):
    def __init__(self, colour, startX):
        super(Player1, self).__init__()
        self.image.fill(colour)
        self.rect.x = startX

    def update(self):

        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_a]:
            self.xVel = -SPEED
        if keystate[pygame.K_d]:
            self.xVel = SPEED
        if keystate[pygame.K_w] and self.rect.bottom == HEIGHT - HEIGHT/4:
            self.yVel = -JUMP

        super(Player1, self).updatePos()

##########################################################################################################

class Player2(Player):
    def __init__(self, colour, startX):
        super(Player2, self).__init__()
        self.image.fill(colour)
        self.rect.x = startX

    def update(self):
        
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_LEFT]:
            self.xVel = -SPEED
        if keystate[pygame.K_RIGHT]:
            self.xVel = SPEED
        if keystate[pygame.K_UP] and self.rect.bottom == HEIGHT - HEIGHT/4:
            self.yVel = -JUMP

        super(Player2, self).updatePos()

#######################################################################################################
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(CHAR, pygame.SRCALPHA)
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT/4
        self.rect.x = WIDTH/2
        self.xVel = 0
        self.yVel = 0

    def update(self):

        if self.rect.bottom < HEIGHT - HEIGHT/4:
            self.yVel += GRAVITY
        

        self.rect.bottom += self.yVel













#237 is y plsyer can jump
def main():

    # initialize pygame and create window
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Soccer!")

    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    player1 = Player1(BLUE, WIDTH/4)
    player2 = Player2(RED, WIDTH - WIDTH/4)
    ball = Ball()
    all_sprites.add(player1)
    all_sprites.add(player2)
    all_sprites.add(ball)
    

    # Game loop
    running = True
    while running:
        # keep loop running at the right speed
        clock.tick(FPS)
        # Process input (events)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False

        # Update
        all_sprites.update()

        # Draw / render
        screen.fill(BLACK)
        pygame.draw.rect(screen, (50,150,0),(0,HEIGHT - HEIGHT/4, WIDTH, HEIGHT/4))
        all_sprites.draw(screen)
        # *after* drawing everything, flip the display
        pygame.display.flip()

    pygame.quit()

########################################################################################
main()