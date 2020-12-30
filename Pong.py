import pygame

import tkinter as tk
from tkinter import ttk
from Paddle import Paddle
from Ball import Ball
# from DropBox import DropBox
from DropBox2 import DropBox2
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (169, 169, 169)
LIGHT_GREY = (109, 109, 109)

# Define school pride
PURPLE = (51, 0, 111)
CYAN = (0, 255, 255)
GOLD = (232, 211, 162)
Viking_Blue = (0, 63, 135, 40)

playerColors = [PURPLE, Viking_Blue, GOLD, RED]
playerLocations = [[20, 200], [680, 200]]
paddle_ups = {}
paddle_downs = {}
 
pygame.init()


players = DropBox2([' 2',
                    ' 4 (Singles)',
                    ' 4 (Duos)'])

players.draw()
num_players = int(players.value[1])


c_options = [
    ' Q A',
    ' E D',
    ' O L',
    ' W S',
    ' U J',
    ' ↑ ↓']
for i in range(0, num_players):
    controls = DropBox2(c_options)
    controls.draw()

    print(controls.value)
    if(controls.value[1] == '↑'):
        paddle_ups.update(
            {pygame.K_UP: str(i)})
        paddle_downs.update(
            {pygame.K_DOWN: str(i)})
    else:
        paddle_ups.update(
            {pygame.key.key_code(str(controls.value[1])): str(i)})
        paddle_downs.update(
            {pygame.key.key_code(str(controls.value[3])): str(i)})
    c_options.remove(controls.value)


# Set the width and height of the screen [width, height]
width = 700
height = 500
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Dan and Brax Pong")

scoreA = 0
scoreB = 0

 # Give us some paddles UwU
# n = 1
paddle_dict = {}
for i in range(0, num_players):
    paddle_dict["v{}".format(i)] = Paddle(playerColors[i], 10, 100,
                                          playerLocations[i][0],
                                          playerLocations[i][1])

# paddle_ups = {pygame.K_w: '0'}
# paddle_downs = {pygame.K_s: '0'}

ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

sprite_list = pygame.sprite.Group()

for i in paddle_dict.keys():
    sprite_list.add(paddle_dict[i])
sprite_list.add(ball)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Set up the Score Text


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()
    for i in paddle_ups.keys():
        if keys[i]:
            paddle_dict["v{}".format(paddle_ups[i])].moveUp(5)
    for i in paddle_downs.keys():
        if keys[i]:
            paddle_dict["v{}".format(paddle_downs[i])].moveDown(5)
    # --- Game logic should go here
 
    # --- make sure the ball is not our of bounds 
    if (ball.rect.y > height) or (ball.rect.y < 0):
        ball.bounceY()

        # player A scored
    if (ball.rect.x > width):
        goLeft = True
        ball.reset(goLeft)
        scoreA += 1
        

        # player B Scored
    if (ball.rect.x < 0):
        goLeft = False
        ball.reset(goLeft)
        scoreB += 1

    # Detect collisions between the ball and the paddles
    for paddle in paddle_dict.keys():
        if pygame.sprite.collide_mask(ball, paddle_dict[paddle]):
            ball.bounceX()
    # if pygame.sprite.collide_mask(ball, pad_1) or pygame.sprite.collide_mask(ball, pad_2):
    #     ball.bounceX()
    
    sprite_list.update() 
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(GREY)
 
    # --- Drawing code should go here
    sprite_list.draw(screen)


    # Display scores:
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, WHITE, LIGHT_GREY)
    screen.blit(text, (250, 10))
    text = font.render(str(scoreB), 1, WHITE, LIGHT_GREY)
    screen.blit(text, (420, 10))

    pygame.draw.line(screen, WHITE, [width/2, 0], [width/2, height], 5)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
