import pygame 

#######################################################################################################
class Object():
    def __init__(self, width, height, xCord, yCord, xVel, yVel): #collidable):
        self.width = width
        self.height = height
        self.xCord = xCord
        self.yCord = yCord
        self.xVel = xVel
        self.yVel = yVel
        #self.collidable = collidable

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height

    def setXCord(self, xCord):
        self.xCord = xCord

    def setYCord(self, yCord):
        self.yCord = yCord

    def setXVel(self, xVel):
        self.xVel = xVel

    def setYVel(self, yVel):
        self.yVel = yVel

#    def setCollidable(self, collidable):
#        self.collidable = collidable

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getXCord(self):
        return self.xCord

    def getYCord(self):
        return self.yCord
        
    def getXVel(self):
        return self.xVel

    def getYVel(self):
        return self.yVel

#    def getCollidable(self):
#        return self.collidable 

#(255,0,0) = red
#(0,255,0) = green
#(0,0,255) = blue
#######################################################################################################
def main():
    
    pygame.init()

    screenWidth = 1000
    screenHeight = 700
    charWidth = screenWidth/10
    charHeight = charWidth
    ballWidth = screenWidth/40
    ballHeight = ballWidth
    delayTime = 50 #time to delay, in miliseconds 1000 = 1 second
    floorRatio = 4 #1/4 of screen height
    gravity = 1 #how fast ball falls 
    friction = 1 #how fast ball slows down
    charSpeed = 20 #how fast the character can move
    
    #width, height, xCord, yCord, xVel, yVel)
    ball = Object(ballWidth, ballHeight, screenWidth/2, 100, 0, 1)
    #ballBox = Object(ballWidth, ballHeight, ball.getXCord(), ball.getYCord(), 
    #    ball.getXVel(), ball.getYVel())
    charOne = Object(charWidth, charHeight, 100, screenHeight/2, 0, 3)
    #charOneBottom = Object(charWidth, charHeight, charOne.getXCord(), 
    #    charOne.getYCord(), charOne.getXVel(), charOne.getYVel())
    floor = Object(screenWidth, screenHeight/floorRatio, 0, screenHeight - screenHeight/floorRatio, 0, 0)

    pygame.display.set_caption("Semi Soccer")
    win = pygame.display.set_mode((screenWidth, screenHeight)) #width and height

    run = True
    while run:
        #screen
        pygame.draw.rect(win, (0,0,0), (0,0, screenWidth, screenHeight))

        #character One
        pygame.draw.circle(win, (255, 0, 0), (charOne.getXCord(), charOne.getYCord()), 
            charOne.getWidth()/2)
        pygame.draw.rect(win, (0,0,0), (charOne.getXCord() - charOne.getWidth()/2, charOne.getYCord(), 
            charOne.getWidth(), charOne.getHeight()/2))
        
        #ball
        #pygame.draw.rect(win, (0,0,0), (ball.getXCord() - ball.getWidth()/2, 
        #    ball.getYCord() - ball.getHeight()/2, ball.getWidth(), ball.getHeight()))
        pygame.draw.circle(win, (255, 255, 255), (ball.getXCord(), ball.getYCord()), ball.getWidth()/2)
        #floor
        pygame.draw.rect(win,(50,150,0), (floor.getXCord(),
            floor.getYCord(), floor.getWidth(), floor.getHeight()))

        pygame.time.delay(delayTime) #100 = 0.1 secons and 1000 = 1 second
    	pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        #ball
        if(ball.getYVel() > 0):
            ball.setYVel(ball.getYVel() + gravity)
            ball.setYCord(ball.getYCord() + ball.getYVel())
        elif(ball.getYVel() < 0):
            ball.setYVel(ball.getYVel() + 2*gravity)
            ball.setYCord(ball.getYCord() + ball.getYVel())
        elif(ball.getYVel() == 0 and ball.getYCord() + ball.getHeight()/2 < floor.getYCord()):
            ball.setYVel(1)

        if(ball.getYCord() + ball.getHeight()/2 >= floor.getYCord()):
            ball.setYCord(floor.getYCord() - ball.getHeight()/2)
            ball.setYVel(-ball.getYVel())
            if(ball.getXVel() > 0):
                ball.setXVel(ball.getXVel() - friction)
            elif(ball.getXVel() < 0):
                ball.setXVel(ball.getXVel() + friction)
        
        if(ball.getXVel() > 0):
            ball.setXCord(ball.getXCord() + ball.getXVel())
        elif(ball.getXVel() < 0):
            ball.setXCord(ball.getXCord() + ball.getXVel())
        
        if(ball.getXCord() + ball.getWidth() > screenWidth or 
            ball.getXCord() - ball.getWidth() <= 0):
            ball.setXVel(-ball.getXVel())

        if(ball.getXCord() - ball.getWidth()/2 < charOne.getXCord() + charOne.getWidth()/2 
            and ball.getXCord() - ball.getWidth()/2 > charOne.getXCord()):
            ball.setXCord(charOne.getXCord() + charOne.getWidth()/2)
            ball.setXVel(20)

        #player One
        if(charOne.getYVel() > 0):
            if(charOne.getXVel() == 0):
                charOne.setYVel(charOne.getYVel() + gravity)
            else:
                charOne.setYVel(charOne.getYVel() + 2*gravity)
            charOne.setYCord(charOne.getYCord() + charOne.getYVel())
        elif(charOne.getYVel() < 0):
            if (charOne.getXVel() == 0):
                charOne.setYVel(charOne.getYVel() + gravity)
            else:
                charOne.setYVel(charOne.getYVel() + 2*gravity)
            charOne.setYCord(charOne.getYCord() + charOne.getYVel())
        elif(charOne.getYVel() == 0 and charOne.getYCord() < floor.getYCord()):
            charOne.setYVel(1)

        if(charOne.getYCord() >= floor.getYCord()): #checks for collision with floor
            charOne.setYCord(floor.getYCord())
            charOne.setYVel(0)
            charOne.setXVel(0)

        #player Two

        #players
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:  #to move left
            charOne.setXCord(charOne.getXCord() - charSpeed)
            charOne.setXVel(-1)
        if keys[pygame.K_d]:
            charOne.setXCord(charOne.getXCord() + charSpeed)
            charOne.setXVel(1)
        if keys[pygame.K_w] and charOne.getYCord() == floor.getYCord():
            charOne.setYVel(-20)
       
        #ball
        if(ball.getYVel() > 0):
            ball.setYVel(ball.getYVel() + gravity)
            ball.setYCord(ball.getYCord() + ball.getYVel())
        elif(ball.getYVel() < 0):
            ball.setYVel(ball.getYVel() + 2*gravity)
            ball.setYCord(ball.getYCord() + ball.getYVel())
        elif(ball.getYVel() == 0 and ball.getYCord() + ball.getHeight()/2 < floor.getYCord()):
            ball.setYVel(1)

        if(ball.getYCord() + ball.getHeight()/2 >= floor.getYCord()):
            ball.setYCord(floor.getYCord() - ball.getHeight()/2)
            ball.setYVel(-ball.getYVel())
            if(ball.getXVel() > 0):
                ball.setXVel(ball.getXVel() - friction)
            elif(ball.getXVel() < 0):
                ball.setXVel(ball.getXVel() + friction)
        
        if(ball.getXVel() > 0):
            ball.setXCord(ball.getXCord() + ball.getXVel())
        elif(ball.getXVel() < 0):
            ball.setXCord(ball.getXCord() + ball.getXVel())
        
        if(ball.getXCord() + ball.getWidth() > screenWidth or 
            ball.getXCord() - ball.getWidth() <= 0):
            ball.setXVel(-ball.getXVel())

       
        
        #ball.setXCord(ball.getWidth()/2)
        

    pygame.quit()


        


#######################################################################################################
main()
