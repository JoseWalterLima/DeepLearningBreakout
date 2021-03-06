#Import the pygame library and initialise the game engine
import pygame
from paddle import Paddle
from ball import Ball
from brick import Brick
import time
pygame.init()

# Create game window
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout Game by José Mota")

# Define colors palette
BLACK = (0,0,0)
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
BLUE = (0,191,255)
PURPLE = (138,43,226)
GREEN = (0,128,0)
YELLOW = (255,255,0)

# Global variables for Score and Lives
SCORE = 0
LIVES = 3

#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()

#Create the Paddle
paddle = Paddle(WHITE, 100, 10)
paddle.rect.x = 350
paddle.rect.y = 560

#Create the ball sprite
ball = Ball(WHITE,10,10)
ball.rect.x = 400
ball.rect.y = 500

#Create the brick sprite
all_bricks = pygame.sprite.Group()
START = 90
for color in [RED, PURPLE, GREEN, ORANGE, YELLOW]:
#for color in [RED, RED, RED, RED]:
    START += 20
    for i in range(40):
        brick = Brick(color,20,20)
        brick.rect.x = i*20
        brick.rect.y = START
        all_sprites_list.add(brick)
        all_bricks.add(brick)

# Add the paddle to the list of sprites
all_sprites_list.add(paddle)
all_sprites_list.add(ball)

# The loop will carry on until the user exits the game (e.g. clicks the close button).
CARRYON = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while CARRYON:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            CARRYON = False # Flag that we are done so we exit this loop

    #Moving the paddle when the use uses the arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.moveLeft(6)
    if keys[pygame.K_RIGHT]:
        paddle.moveRight(6)

    # Allow paddle to move Up and Down
    # if keys[pygame.K_UP]:
    #     paddle.moveUp(2)
    # if keys[pygame.K_DOWN]:
    #     paddle.moveDown(2)

    # --- Game logic should go here
    all_sprites_list.update()

    #Check if the ball is bouncing against any of the 4 walls:
    if ball.rect.x>=790:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>590:
        ball.velocity[1] = -ball.velocity[1]
        LIVES -= 1
        if LIVES == 0:
            #Display Game Over Message for 3 seconds
            font = pygame.font.Font(None, 74)
            text = font.render("GAME OVER", 1, WHITE)
            screen.blit(text, (250,300))
            pygame.display.flip()
            pygame.time.wait(3000)

            #Stop the Game
            CARRYON=False
    if ball.rect.y<40:
        ball.velocity[1] = -ball.velocity[1]

    #Detect collisions between the ball and the paddles
    if pygame.sprite.collide_mask(ball, paddle):
        ball.bounce()

    #Check if there is the ball collides with any of bricks
    brick_collision_list = pygame.sprite.spritecollide(ball,all_bricks,False)
    remaining_bricks = len(all_bricks)
    for brick in brick_collision_list:
        #ball.velocity[0] = ball.velocity[0]
        ball.velocity[1] = -ball.velocity[1]
        SCORE += 1
        brick.kill()
        remaining_bricks -= 1
        if remaining_bricks == 0:
            #Display Level Complete Message for 3 seconds
            font = pygame.font.Font(None, 74)
            text = font.render("LEVEL COMPLETE", 1, WHITE)
            screen.blit(text, (200,300))
            pygame.display.flip()
            pygame.time.wait(3000)
            #Stop the Game after destroying all blocks
            CARRYON=False

    # --- Drawing code should go here
    # First, clear the screen to dark blue.
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)

    #Display the score and the number of lives at the top of the screen
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(SCORE), 1, WHITE)
    screen.blit(text, (20,10))
    text = font.render("Lives: " + str(LIVES), 1, WHITE)
    screen.blit(text, (650,10))

    #Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
    all_sprites_list.draw(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

#Once we have exited the main program loop we can stop the game engine:
pygame.quit()