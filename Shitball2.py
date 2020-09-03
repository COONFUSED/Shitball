import pygame
# Initialize pygame
pygame.init ()

# Hide mouse cursor
# pygame.mouse.set_visible(False)

# Clock no idea what its for but i see it all the time
mainClock = pygame.time.Clock()

# so you can write QUIT instead of pygame.QUIT
from pygame.locals import *

# Screen display and size
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Shitball")
icon = pygame.image.load('poop.png')
pygame.display.set_icon(icon)

# Ball
ballImg = pygame.image.load('poopS.png')
ballX = 100
ballY = 100
ballX_change = 0
offset = [0, 0]

# Position variables 
x = 0
y = 0
x1 = 736
y1 = 536

# Permanent Variable changer function
def variableChangerx():
    global x
    x = mx -32

def variableChangery():
    global y
    y = my -32

# Clicking variables
clicking = False
right_clicking = False
middle_clicking = False

# Cursor visibility
pygame.mouse.set_visible = False
   
# Game Loop 
running = True
while running:
    
    # Fills screen with color (RGB - Red, Green, Blue)
    screen.fill((50, 130, 100))

    # Captures Mouse Location
    mx, my = pygame.mouse.get_pos()


    # Mouse rotation and Location
    rot = 0
    loc = [x, y]
    mloc = [mx, my]

    # Clicking effects
    if clicking:
        loc[0] = mx -32
        loc[1] = my -32
        print(loc[0], loc[1])
    if right_clicking:
        loc = [x1, y1]
    if middle_clicking:
        rot += 180

    # Border Collision after clicking effects so it overrides
    if loc[0] < 0:
        loc[0] = 0
    if loc[1] < 0:
        loc[1] = 0
    if loc[0] > 736:
        loc[0] = 736
    if loc[1] > 536:
        loc[1] = 536
    
    for event in pygame.event.get ():
        if event.type == QUIT:
            running = False
            
        
        # keydown to see if pressed, K_ESCAPE to quit game
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        
        # Check if mousebuttons are pressed
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                clicking = True
            if event.button == 3:
                right_clicking = True
            if event.button == 2:
                middle_clicking = not middle_clicking
            if event.button == 4:
                offset[1] -= 50
            if event.button == 5:
                offset[1] += 50
        
        # Check if mousebuttons are let go
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                clicking = False
                variableChangerx()
                variableChangery()

            if event.button == 3:
                right_clicking = False
    
    
    screen.blit(pygame.transform.rotate(ballImg, rot), ((loc[0]) + offset[0], (loc[1]) + offset[1]))

    print(loc)

                

        
    
    
    
    
    # Updating display 
    pygame.display.update()