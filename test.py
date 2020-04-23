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
BALL = (20,20)
SPEED = 10
JUMP = 15
GRAVITY = 1
FRICTION = 1
XBOUNCE = 2
YBOUNCE = 2


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
        if keystate[pygame.K_s]:
            self.yVel = JUMP

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
        if keystate[pygame.K_DOWN]:
            self.yVel = JUMP

        super(Player2, self).updatePos()

#######################################################################################################
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(BALL, pygame.SRCALPHA)
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT/4
        self.rect.x = WIDTH/2
        self.xVel = 0
        self.yVel = 0

    def update(self):

        #yVel
        if self.yVel > 0:
            self.yVel += GRAVITY
            self.rect.bottom += self.yVel
        elif self.yVel < 0:
            self.yVel += 2*GRAVITY
            self.rect.bottom += self.yVel
        elif self.yVel == 0 and self.rect.bottom < HEIGHT - HEIGHT/4:
            self.yVel = 1

        if  self.rect.bottom >= HEIGHT - HEIGHT/4:
            self.rect.bottom = HEIGHT - HEIGHT/4
            self.yVel = -self.yVel
            if self.xVel > 0:
                self.xVel -= FRICTION
            elif self.xVel < 0:
                self.xVel += FRICTION
            
        self.rect.x += self.xVel
        
        if self.rect.x > WIDTH - 50 or self.rect.x < 0:
            self.xVel = -self.xVel

        
    def collision(self, player):

        self.xVel = (self.rect.x - player.rect.x)/XBOUNCE
        self.yVel = (self.rect.bottom + self.rect.y - player.rect.bottom)/YBOUNCE
        if self.xVel > 15:
            self.xVel = 15
        if self.yVel > -15:
            self.yVel = -15


    def goal(self):
        if self.rect.x < WIDTH/16 and self.rect.bottom > HEIGHT/2 or self.rect.x > WIDTH - WIDTH/16 and self.rect.bottom > HEIGHT/2:
            xVel = 0
            yVel = 0
            return True
        else:
            return False

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
        #all_sprites.update()

        p1 = pygame.sprite.collide_circle(ball, player1)
        p2 = pygame.sprite.collide_circle(ball, player2)

        if bool(p1):
            ball.collision(player1)
        if bool(p2):
            ball.collision(player2)

        # Update
        all_sprites.update()

        # Draw / render
        screen.fill(BLACK)
        pygame.draw.rect(screen, (50,150,0),(0,HEIGHT - HEIGHT/4, WIDTH, HEIGHT/4))#ground
        pygame.draw.rect(screen, YELLOW, (0, HEIGHT/2, WIDTH/16, HEIGHT/4)) #left goal
        pygame.draw.rect(screen, YELLOW, (WIDTH-50, HEIGHT/2, WIDTH/16, HEIGHT/4))#rigth goal
        all_sprites.draw(screen)
        # *after* drawing everything, flip the display
        pygame.display.flip()
        running = not ball.goal()
    pygame.quit()

########################################################################################
main()