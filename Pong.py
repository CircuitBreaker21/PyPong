

import pygame
from Paddle import Paddle
from Ball import Ball
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (169,169,169)

# Define school pride
PURPLE = (51, 0, 111)
CYAN = (0, 255, 255)
GOLD = (232,211,162)
Viking_Blue = (0, 63, 135, 40)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
width = 700
height = 500
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Dan and Brax Pong")

scoreA = 0
scoreB = 0

 # Give us some paddles UwU
pad_1 = Paddle(PURPLE, 10, 100)
pad_1.rect.x = 20
pad_1.rect.y = 200

pad_2 = Paddle(Viking_Blue, 10, 100)
pad_2.rect.x = 670
pad_2.rect.y = 200

ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

sprite_list = pygame.sprite.Group()

sprite_list.add(pad_1)
sprite_list.add(pad_2)
sprite_list.add(ball)

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        pad_1.moveUp(5)
    if keys[pygame.K_s]:
        pad_1.moveDown(5)
    if keys[pygame.K_UP]:
        pad_2.moveUp(5)
    if keys[pygame.K_DOWN]:
        pad_2.moveDown(5)
    # --- Game logic should go here
    
    # --- make sure the ball is not our of bounds 
    if (ball.rect.y > height) or (ball.rect.y < 0):
        ball.bounceY()

        #player A scored
    if (ball.rect.x > width):
        ball.bounceX()
        scoreA += 1

        #player B Scored
    if (ball.rect.x < 0):
        ball.bounceX()
        scoreB += 1

    #Detect collisions between the ball and the paddles
    if pygame.sprite.collide_mask(ball, pad_1) or pygame.sprite.collide_mask(ball, pad_2):
      ball.bounceX()    
    
    sprite_list.update() 
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(GREY)
 
    # --- Drawing code should go here
    sprite_list.draw(screen)
 



 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
