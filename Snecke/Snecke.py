##Totally not a snake rip off##

#Imports#
import pygame
pygame.init()
import random
import sys
import tkinter as tk

#Difficulty#
selected_difficulty = "undefined variable"
difficulty = 0
def difficulty_select(difficulty_level):
    global selected_difficulty
    selected_difficulty = difficulty_level
    root.quit()
    root.destroy()
#Making tk window#
root = tk.Tk()
root.title("Select Difficulty")
label = tk.Label(root, text="Select Game Difficulty", font=("Arial",14))
label.pack(pady=10)
#Normal button#
normal_button = tk.Button(root, text="Normal", command=lambda: difficulty_select("Normal"))
normal_button.pack(pady=5)
#Hard button#
hard_button = tk.Button(root, text="Hard", command=lambda: difficulty_select("Hard"))
hard_button.pack(pady=5)
#Insane button#
insane_button = tk.Button(root, text="insane", command=lambda: difficulty_select("Insane"))
insane_button.pack(pady=5)

root.mainloop()

if selected_difficulty == "Normal":
    difficulty = 1
elif selected_difficulty == "Hard":
    difficulty = 2
elif selected_difficulty == "Insane":
    difficulty = 3
elif selected_difficulty == "undefined variable":
    difficulty = 117

#Variables#
x = 500
y = 400
clock = pygame.time.Clock()

#Writing variables#
font_style = pygame.font.SysFont("bahnschrift", 15)
score_font = pygame.font.SysFont("comicsansms", 15)

#Color variables#
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

#Snake variables#
snake_block = 10
if not difficulty == 117:
    snake_speed = 5
if difficulty == 117:
    snake_speed = random.randint(1,15)

#Startup variables#
font = pygame.font.SysFont(None, 100)
if not difficulty == 117:
    startup_message = "Snecke -LKDS"
if difficulty == 117:
    startup_message = "corrupt.null"
startup_message_length = len(startup_message)
Index = 0
startup = True
displayed_text = ""

# Display setup
display = pygame.display.set_mode((x, y))
pygame.display.set_caption("Snecke")

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

#Functions#
def your_score(score):
    value = score_font.render("Your score: " + str(score),True,yellow)
    display.blit(value, [0, 0])
    speed = score_font.render("Your speed: " + str(snake_speed),True,yellow)
    display.blit(speed, [0,20])
    hard = score_font.render("Difficulty: " + str(selected_difficulty),True,yellow)
    display.blit(hard, [0,40])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [x // 6, y // 3])

def gameloop():
    global x,y,snake_speed
    game_over = False
    game_close = False

    x1 = x // 2
    y1 = y // 2
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, x - snake_block) / 10.0) * 10
    foody = round(random.randrange(0, y - snake_block) / 10.0) * 10

    while not game_over:
        while game_close:
            display.fill(blue)
            if not difficulty == 117:
                message("You have lost. Press 'c' to play again or 'q' to quit", red)
            if difficulty == 117:
                display.fill(black)
                message("Error message.variable is undefined", blue)
            if not difficulty == 117:
                your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if not difficulty == 117:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            sys.exit()
                        if event.key == pygame.K_c:
                            snake_speed = 5
                            gameloop()
                            return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_d:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_w:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_s:
                    x1_change = 0
                    y1_change = snake_block

        if x1 >= x or x1 < 0 or y1 >= y or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        display.fill(blue)
        pygame.draw.rect(display, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for part in snake_List[:-1]:
            if part == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        if not difficulty == 117:
            your_score(Length_of_snake - 1)
        if difficulty == 117:
            your_score("Error.Unkown.Corrupt")

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, x - snake_block) / 10.0) * 10
            foody = round(random.randrange(0, y - snake_block) / 10.0) * 10
            Length_of_snake += 1
            if difficulty == 1:
                snake_speed += 1
            if difficulty == 2:
                snake_speed += 2
            if difficulty == 3:
                snake_speed *= 2
            if difficulty == 117:
                snake_speed *= random.randint(1,10)

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameloop()
