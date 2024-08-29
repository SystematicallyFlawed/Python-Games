#Totally not a pong rip off#

#Imports#
import pygame
pygame.init()
import random

#General variables#
x = 800
y = 600
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 100)

#Position variables#
#Paddles#
paddle1_pos = 100
paddle2_pos = 100
#Ball#
ball_radius = 5
ball_x = random.randint(200,400)
ball_y = random.randint(100,500)
ball_x_movement = 1
ball_y_movement = 1
ball_hits = 0
ball_movement_increase = 1

#Color variables#
white = (255,255,255)
black = (0,0,0)
blue = (0,0,200)

#Win variables#
p1_win = False
p2_win = False
p1_win_message = "Player 1 has won"
p1_win_text = font.render(p1_win_message, True, white)
p1_win_text_rect = p1_win_text.get_rect(center=(x/2,y/2))
p2_win_message = "Player 2 has won"
p2_win_text = font.render(p2_win_message, True, white)
p2_win_text_rect = p2_win_text.get_rect(center=(x/2,y/2))

#Startup variables#
startup_message = "Ping -LKDS"
startup_message_length = len(startup_message)
Index = 0
startup = True
displayed_text = ""

#Screen set up#
display = pygame.display.set_mode([x,y])
pygame.display.set_caption("ping")

#Startup animation#
while startup:
    display.fill(black)
    if Index < startup_message_length:
        displayed_text += startup_message[Index]
        Index += 1
    startup_text = font.render(displayed_text, True, white)
    startup_text_rect = startup_text.get_rect(center=(x / 2, y / 2))
    display.blit(startup_text, startup_text_rect)
    pygame.display.update()
    clock.tick(10)
    if Index == startup_message_length:
        pygame.time.delay(2000)
        startup = False

#Game loop#
ping_running = True
while ping_running:
    #For game closing#
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ping_running = False

    display.fill(black)

    #Saving ball position#
    old_ball_x = ball_x
    old_ball_y = ball_y
    #Moving the ball#
    ball_x += ball_x_movement
    ball_y += ball_y_movement

    #Collision#
    #Top and bottom collision#
    if ball_y - ball_radius <= 50 or ball_y + ball_radius >= 550:
        ball_y_movement *= -1
    #Left paddle collision#
    if 65 <= ball_x <= 75 and paddle1_pos <= ball_y <= paddle1_pos + 50:
        ball_x_movement *= -1
        ball_movement_increase *= -1
        ball_hits += 1
    if 50 <= ball_x <= 70 and ball_y == paddle1_pos:
        ball_y_movement *= -1
    #Right paddle collision#
    if 725 <= ball_x <= 735 and paddle2_pos <= ball_y <= paddle2_pos +50:
        ball_x_movement *= -1
        ball_movement_increase *= -1
        ball_hits += 1
    if 730 <= ball_x <= 750 and ball_y == paddle2_pos:
        ball_y_movement *= -1

    #Increasing ball speed#
    if ball_hits == 2:
        ball_x_movement += ball_movement_increase
        ball_hits = 0
    #Moving the paddles#
    #Also paddle collision with the floor and roof#
    keys = pygame.key.get_pressed()
    if 50 < paddle1_pos:
        if keys[pygame.K_w]:
            paddle1_pos -= 5
    if 50 < paddle2_pos:
        if keys[pygame.K_u]:
            paddle2_pos -= 5

    if paddle1_pos < 500:
        if keys[pygame.K_s]:
            paddle1_pos += 5
    if paddle2_pos < 500:
        if keys[pygame.K_j]:
            paddle2_pos += 5

    #Drawing
    # Paddles#
    pygame.draw.rect(display, white, (50, paddle1_pos, 20, 50))
    pygame.draw.rect(display, white, (730, paddle2_pos, 20, 50))
    # Ball#
    pygame.draw.circle(display, white, (ball_x, ball_y), ball_radius)
    # Top and bottom#
    pygame.draw.rect(display, blue, (0, 0, 800, 50))
    pygame.draw.rect(display, blue, (0, 550, 800, 50))

    #Win condition#
    if ball_x >= 810:
        p1_win = True
        ping_running = False
    if ball_x <=-10:
        p2_win = True
        ping_running = False
    #Constanst display update#
    clock.tick(60)
    pygame.display.update()

#p1 win screen#
while p1_win:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            p1_win = False
    display.fill(black)
    display.blit(p1_win_text,p1_win_text_rect)
    pygame.display.update()

#p2 win screen#
while p2_win:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            p2_win = False
    display.fill(black)
    display.blit(p2_win_text,p2_win_text_rect)
    pygame.display.update()

pygame.quit()