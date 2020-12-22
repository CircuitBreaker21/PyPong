<<<<<<< HEAD


import pygame

import tkinter as tk
from tkinter import ttk
from Paddle import Paddle
from Ball import Ball
#from DropBox import DropBox
from DropBox2 import DropBox2
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (169,169,169)
LIGHT_GREY = (109, 109, 109)

# Define school pride
PURPLE = (51, 0, 111)
CYAN = (0, 255, 255)
GOLD = (232,211,162)
Viking_Blue = (0, 63, 135, 40)

playerColors = [PURPLE, Viking_Blue, GOLD, RED]
 
pygame.init()


# Creating tkinter window
window = tk.Tk()
window.geometry('350x100')
# Label
ttk.Label(window, text="Select Player Count :",
          font=("Times New Roman", 10)).grid(column=0,
                                             row=15, padx=10, pady=25)

n = tk.StringVar()
playerCount = ttk.Combobox(window, width=27,
                            textvariable=n)

# Adding combobox drop down list
playerCount['values'] = (' 2',
                         ' 4 (Singles)',
                         ' 4 (Duos)',)

playerCount.grid(column=1, row=15)

# Shows february as a default value
playerCount.current()
window.mainloop()


db = DropBox2()
db.draw()




# Set the width and height of the screen [width, height]
width = 700
height = 500
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Dan and Brax Pong")

scoreA = 0
scoreB = 0

 # Give us some paddles UwU
n = 1
paddle_dict = {}
for i in range(0, n):
    paddle_dict["v{}".format(i)] = Paddle(playerColors[i], 10, 100, 20, 200)

paddle_ups = {pygame.K_w: '0'}
paddle_downs = {pygame.K_s: '0'}

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
        ball.reset()
        scoreA += 1
        

        # player B Scored
    if (ball.rect.x < 0):
        ball.reset()
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
=======


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
>>>>>>> 59411c8d1117c6788ee7342d4b869d4f0d54883a
