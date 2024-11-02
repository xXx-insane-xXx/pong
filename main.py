import pygame
from sys import exit
from random import randint

pygame.init()


#############
## Display ##
#############
screen_width = 1280
screen_height = 960
display = pygame.display.set_mode((1280, 960))
pygame.display.set_caption("Pong")


#####################
## Game rectangles ##
#####################

ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width-20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)


###############
## Game vars ##
###############

## Ball
ball_speed_x = 7
ball_speed_y = 7

## Game just start
game_just_start = True

############
## Colors ##
############
bg_color = pygame.Color("grey12")
light_grey = (200, 200, 200)


###########
## Clock ##
###########
clock = pygame.time.Clock()



###############
## Game loop ##
############### 
while True:

    for event in pygame.event.get():
        
        ## Check for quit event
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        ## Test event
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            print("Yo")

        

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    
    ###############
    ## Colisions ##
    ###############

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1




    ## Draw
    display.fill(bg_color)
    pygame.draw.rect(display, light_grey, player)
    pygame.draw.rect(display, light_grey, opponent)
    pygame.draw.ellipse(display, light_grey, ball)
    pygame.draw.aaline(display, light_grey, (screen_width/2,0), (screen_width/2, screen_height))
    
        
    ## Log
    # print("test")
    

    ## Update the window
    pygame.display.update()
    clock.tick(60)

