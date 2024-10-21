#Imports#
import pygame
pygame.init()
import sys
import random
import tkinter as tk
import time
import Menu

#Variables#
Bugging = False
Width = 800
Height = 600
FPS = 60
clock = pygame.time.Clock()
anti_lag = 0
writing_font = pygame.font.SysFont("cambriamath", 25)
boss_font = pygame.font.SysFont("agencyfb", 50)
#Stage variables#
stage_count = 0
stage_0 = False
stage_1 = False
stage_2 = False
stage_3 = False
stage_4 = False
stage_5 = False
stage_6 = False
stage_7 = False
stage_8 = False
stage_9 = False
stage_10 = False
stage_11 = False
stage_12 = False
stage_13 = False
stage_14 = False
stage_15 = False
stage_16 = False
stage_17 = False
stage_18 = False
stage_19 = False
stage_20 = False
#Boss variables#
boss_tick = 0
#Player variables#
Gravity = 0.5
Player_Jump_Strength = -10
Player_Speed = 5
Player_Attack = 10
Attack_Duration = 10
player_image = pygame.image.load("Assets/Player/player.png")
player_reinforced_image = pygame.image.load("Assets/Player/player-reinforced.png")
ironsword_image = pygame.image.load("Assets/Swords/ironsword.png")
have_ironsword = True
steelsword_image = pygame.image.load("Assets/Swords/steelsword.png")
have_steelsword = False
reinforced_armor = False
attack_speed = 10
attacking = False
attack_cooldown = 0
dash_length = 250
dash_cooldown = 0
points = 0
player_health = 100
iframes = 0
noshop_frames = 0
slide_velocity = 0
sliding = False
slide_friction = 0.9
can_camp = True
#Coin variables#
coin_image = pygame.image.load("Assets/Player/coin.png")
throw_timer = 0
#GUN#
V1_image = pygame.image.load("Assets/Player/The V1 (Better).png")
V1_image_reinforced = pygame.image.load("Assets/Player/The V1 (Better) reinforced armor.png")
V1_empty_image = pygame.image.load("Assets/Player/The V1 Empty (Better).png")
V1_empty_image_reinforced = pygame.image.load("Assets/Player/The V1 Empty (Better) reinforced armor.png")
V1_mag = pygame.image.load("Assets/Player/The V1 Mag.png")
bullet_image = pygame.image.load("Assets/Player/bullet.png")
bullet_count = 4
V1_timer = 0
V1 = None
V1_firing = False
bullets_in_mag = 4
reload_time = 2000
reloading_V1 = False
V1_damage = 100
mag_images = [
    pygame.image.load("Assets/Player/V1 Mag 0.png"),
    pygame.image.load("Assets/Player/V1 Mag 1.png"),
    pygame.image.load("Assets/Player/V1 Mag 2.png"),
    pygame.image.load("Assets/Player/V1 Mag 3.png"),
    pygame.image.load("Assets/Player/V1 Mag 4.png")
    ]
mag_display_time = 5000
mag_display_active = False
display_ammo = False
ammo_display_active = False
ammo_display_start_time = 0
ammo_display_duration = 3000
#Enemy variables#
enemy_health = 100
strong_enemy_health = 200
enemy_jump_strength = -8
enemy_tick = 0
enemy_action_time = 100
enemy_random_gen = 15
enemy_number = enemy_random_gen
Enemy1 = pygame.image.load("Assets/Enemies/enemy1.png")
Enemy1_roll20 = pygame.image.load('Assets/Enemies/enemy1-roll20.png')
Enemy2 = pygame.image.load("Assets/Enemies/enemy2.png")
enemy_damage = 20
strong_enemy_damage = 40
#Boss#
boss_health = 1000
boss_image = pygame.image.load("Assets/Boss/boss.png")
boss_damage = 60
#Colors#
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue  = (0,0,255)
boss_color = (80,80,80)
#Backgrounds#
current_background = None
background0 = pygame.image.load("Assets/Backgrounds/background0.png")
background1 = pygame.image.load("Assets/Backgrounds/background1.png")
background2 = pygame.image.load("Assets/Backgrounds/background2.png")
background3 = pygame.image.load("Assets/Backgrounds/background3.png")
background4 = pygame.image.load("Assets/Backgrounds/background4.png")
background5 = pygame.image.load("Assets/Backgrounds/background5.png")
background6 = pygame.image.load("Assets/Backgrounds/background6.png")
background7 = pygame.image.load("Assets/Backgrounds/background7.png")

background19 = pygame.image.load("Assets/Backgrounds/background19.png")
background20 = pygame.image.load("Assets/Backgrounds/background20.png")
#Background switch#
def background_changing():
    global current_background, stage_0, stage_1, stage_2, stage_3, stage_4, stage_5, stage_6, stage_7,stage_8, stage_9, stage_10, stage_11, stage_12, stage_13, stage_14, stage_15, stage_16, stage_17, stage_18, stage_19, stage_20
    if stage_count == 0:
        stage_0 = True
        stage_1 = False
        stage_2 = False
        stage_3 = False
        stage_4 = False
        stage_5 = False
        stage_6 = False
        stage_7 = False
        stage_8 = False
        stage_9 = False
        stage_10 = False
        stage_11 = False
        stage_12 = False
        stage_13 = False
        stage_14 = False
        stage_15 = False
        stage_16 = False
        stage_17 = False
        stage_18 = False
        stage_19 = False
        stage_20 = False
    if stage_count == 1:
        stage_0 = False
        stage_1 = True
        stage_2 = False
        stage_3 = False
        stage_4 = False
        stage_5 = False
        stage_6 = False
        stage_7 = False
        stage_8 = False
        stage_9 = False
        stage_10 = False
        stage_11 = False
        stage_12 = False
        stage_13 = False
        stage_14 = False
        stage_15 = False
        stage_16 = False
        stage_17 = False
        stage_18 = False
        stage_19 = False
        stage_20 = False
    if stage_count == 2:
        stage_0 = False
        stage_1 = False
        stage_2 = True
        stage_3 = False
        stage_4 = False
        stage_5 = False
        stage_6 = False
        stage_7 = False
        stage_8 = False
        stage_9 = False
        stage_10 = False
        stage_11 = False
        stage_12 = False
        stage_13 = False
        stage_14 = False
        stage_15 = False
        stage_16 = False
        stage_17 = False
        stage_18 = False
        stage_19 = False
        stage_20 = False
    if stage_count == 3:
        stage_0 = False
        stage_1 = False
        stage_2 = False
        stage_3 = True
        stage_4 = False
        stage_5 = False
        stage_6 = False
        stage_7 = False
        stage_8 = False
        stage_9 = False
        stage_10 = False
        stage_11 = False
        stage_12 = False
        stage_13 = False
        stage_14 = False
        stage_15 = False
        stage_16 = False
        stage_17 = False
        stage_18 = False
        stage_19 = False
        stage_20 = False
    if stage_count == 4:
        stage_0 = False
        stage_1 = False
        stage_2 = False
        stage_3 = False
        stage_4 = True
        stage_5 = False
        stage_6 = False
        stage_7 = False
        stage_8 = False
        stage_9 = False
        stage_10 = False
        stage_11 = False
        stage_12 = False
        stage_13 = False
        stage_14 = False
        stage_15 = False
        stage_16 = False
        stage_17 = False
        stage_18 = False
        stage_19 = False
        stage_20 = False
    if stage_count == 5:
        stage_0 = False
        stage_1 = False
        stage_2 = False
        stage_3 = False
        stage_4 = False
        stage_5 = True
        stage_6 = False
        stage_7 = False
        stage_8 = False
        stage_9 = False
        stage_10 = False
        stage_11 = False
        stage_12 = False
        stage_13 = False
        stage_14 = False
        stage_15 = False
        stage_16 = False
        stage_17 = False
        stage_18 = False
        stage_19 = False
        stage_20 = False
    if stage_count == 6:
        stage_0 = False
        stage_1 = False
        stage_2 = False
        stage_3 = False
        stage_4 = False
        stage_5 = False
        stage_6 = True
        stage_7 = False
        stage_8 = False
        stage_9 = False
        stage_10 = False
        stage_11 = False
        stage_12 = False
        stage_13 = False
        stage_14 = False
        stage_15 = False
        stage_16 = False
        stage_17 = False
        stage_18 = False
        stage_19 = False
        stage_20 = False
    if stage_count == 7:
        stage_0 = False
        stage_1 = False
        stage_2 = False
        stage_3 = False
        stage_4 = False
        stage_5 = False
        stage_6 = False
        stage_7 = True
        stage_8 = False
        stage_9 = False
        stage_10 = False
        stage_11 = False
        stage_12 = False
        stage_13 = False
        stage_14 = False
        stage_15 = False
        stage_16 = False
        stage_17 = False
        stage_18 = False
        stage_19 = False
        stage_20 = False
    if stage_count == 8:
        stage_0 = False
        stage_1 = False
        stage_2 = False
        stage_3 = False
        stage_4 = False
        stage_5 = False
        stage_6 = False
        stage_7 = False
        stage_8 = True
        stage_9 = False
        stage_10 = False
        stage_11 = False
        stage_12 = False
        stage_13 = False
        stage_14 = False
        stage_15 = False
        stage_16 = False
        stage_17 = False
        stage_18 = False
        stage_19 = False
        stage_20 = False
    if stage_count == 9:
        stage_0 = False
        stage_1 = False
        stage_2 = False
        stage_3 = False
        stage_4 = False
        stage_5 = False
        stage_6 = False
        stage_7 = False
        stage_8 = False
        stage_9 = True
        stage_10 = False
        stage_11 = False
        stage_12 = False
        stage_13 = False
        stage_14 = False
        stage_15 = False
        stage_16 = False
        stage_17 = False
        stage_18 = False
        stage_19 = False
        stage_20 = False
    if stage_count == 10:
        stage_0 = False
        stage_1 = False
        stage_2 = False
        stage_3 = False
        stage_4 = False
        stage_5 = False
        stage_6 = False
        stage_7 = False
        stage_8 = False
        stage_9 = False
        stage_10 = True
        stage_11 = False
        stage_12 = False
        stage_13 = False
        stage_14 = False
        stage_15 = False
        stage_16 = False
        stage_17 = False
        stage_18 = False
        stage_19 = False
        stage_20 = False
    if stage_count == 11:
        stage_0 = False
        stage_1 = False
        stage_2 = False
        stage_3 = False
        stage_4 = False
        stage_5 = False
        stage_6 = False
        stage_7 = False
        stage_8 = False
        stage_9 = False
        stage_10 = False
        stage_11 = True
        stage_12 = False
        stage_13 = False
        stage_14 = False
        stage_15 = False
        stage_16 = False
        stage_17 = False
        stage_18 = False
        stage_19 = False
        stage_20 = False
    if stage_count == 12:
        stage_0 = False
        stage_1 = False
        stage_2 = False
        stage_3 = False
        stage_4 = False
        stage_5 = False
        stage_6 = False
        stage_7 = False
        stage_8 = False
        stage_9 = False
        stage_10 = False
        stage_11 = False
        stage_12 = True
        stage_13 = False
        stage_14 = False
        stage_15 = False
        stage_16 = False
        stage_17 = False
        stage_18 = False
        stage_19 = False
        stage_20 = False
    if stage_count == 13:
        stage_0 = False
        stage_1 = False
        stage_2 = False
        stage_3 = False
        stage_4 = False
        stage_5 = False
        stage_6 = False
        stage_7 = False
        stage_8 = False
        stage_9 = False
        stage_10 = False
        stage_11 = False
        stage_12 = False
        stage_13 = True
        stage_14 = False
        stage_15 = False
        stage_16 = False
        stage_17 = False
        stage_18 = False
        stage_19 = False
        stage_20 = False
    if stage_count == 14:
        stage_0 = False
        stage_1 = False
        stage_2 = False
        stage_3 = False
        stage_4 = False
        stage_5 = False
        stage_6 = False
        stage_7 = False
        stage_8 = False
        stage_9 = False
        stage_10 = False
        stage_11 = False
        stage_12 = False
        stage_13 = False
        stage_14 = True
        stage_15 = False
        stage_16 = False
        stage_17 = False
        stage_18 = False
        stage_19 = False
        stage_20 = False
    if stage_count == 15:
        stage_0 = False
        stage_1 = False
        stage_2 = False
        stage_3 = False
        stage_4 = False
        stage_5 = False
        stage_6 = False
        stage_7 = False
        stage_8 = False
        stage_9 = False
        stage_10 = False
        stage_11 = False
        stage_12 = False
        stage_13 = False
        stage_14 = False
        stage_15 = True
        stage_16 = False
        stage_17 = False
        stage_18 = False
        stage_19 = False
        stage_20 = False
    if stage_count == 16:
        stage_0 = False
        stage_1 = False
        stage_2 = False
        stage_3 = False
        stage_4 = False
        stage_5 = False
        stage_6 = False
        stage_7 = False
        stage_8 = False
        stage_9 = False
        stage_10 = False
        stage_11 = False
        stage_12 = False
        stage_13 = False
        stage_14 = False
        stage_15 = False
        stage_16 = True
        stage_17 = False
        stage_18 = False
        stage_19 = False
        stage_20 = False
    if stage_count == 17:
        stage_0 = False
        stage_1 = False
        stage_2 = False
        stage_3 = False
        stage_4 = False
        stage_5 = False
        stage_6 = False
        stage_7 = False
        stage_8 = False
        stage_9 = False
        stage_10 = False
        stage_11 = False
        stage_12 = False
        stage_13 = False
        stage_14 = False
        stage_15 = False
        stage_16 = False
        stage_17 = True
        stage_18 = False
        stage_19 = False
        stage_20 = False
    if stage_count == 18:
        stage_0 = False
        stage_1 = False
        stage_2 = False
        stage_3 = False
        stage_4 = False
        stage_5 = False
        stage_6 = False
        stage_7 = False
        stage_8 = False
        stage_9 = False
        stage_10 = False
        stage_11 = False
        stage_12 = False
        stage_13 = False
        stage_14 = False
        stage_15 = False
        stage_16 = False
        stage_17 = False
        stage_18 = True
        stage_19 = False
        stage_20 = False

    if boss_tick == 39:
        stage_0 = False
        stage_1 = False
        stage_2 = False
        stage_3 = False
        stage_4 = False
        stage_5 = False
        stage_6 = False
        stage_7 = False
        stage_8 = False
        stage_9 = False
        stage_10 = False
        stage_11 = False
        stage_12 = False
        stage_13 = False
        stage_14 = False
        stage_15 = False
        stage_16 = False
        stage_17 = False
        stage_18 = False
        stage_19 = True
        stage_20 = False

    if boss_tick == 40:
        stage_0 = False
        stage_1 = False
        stage_2 = False
        stage_3 = False
        stage_4 = False
        stage_5 = False
        stage_6 = False
        stage_7 = False
        stage_8 = False
        stage_9 = False
        stage_10 = False
        stage_11 = False
        stage_12 = False
        stage_13 = False
        stage_14 = False
        stage_15 = False
        stage_16 = False
        stage_17 = False
        stage_18 = False
        stage_19 = False
        stage_20 = True

    if stage_0:
        current_background = background0
    if stage_1:
        current_background = background1
    if stage_2:
        current_background = background2
    if stage_3:
        current_background = background3
    if stage_4:
        current_background = background4
    if stage_5:
        current_background = background5
    if stage_6:
        current_background = background6
    if stage_7:
        current_background = background7

    if stage_19:
        current_background = background19
    if stage_20:
        current_background = background20

#Screen setup#
screen = pygame.display.set_mode((Width,Height))
pygame.display.set_caption("Bugged")

#Main menu stuff#
game_state = "menu"

#Functions#
def game_end():
    global game_state
    game_over = True
    font = pygame.font.SysFont("inkfree", 100)
    lost_message = "Run Corrupted"
    lost_message_length = len(lost_message)
    Index = 0
    displayed_text = ""
    while game_over:
        screen.fill(black)
        if Index < lost_message_length:
            displayed_text += lost_message[Index]
            Index += 1
        lost_text = font.render(displayed_text, True, white)
        lost_text_rect = lost_text.get_rect(center=(Width / 2, Height / 2))
        screen.blit(lost_text, lost_text_rect)
        pygame.display.update()
        clock.tick(10)
        if Index == lost_message_length:
            pygame.time.delay(2000)
            game_over = False
            game_state = "menu"

def game_won():
    global game_state
    game_win = True
    font = pygame.font.SysFont("inkfree", 100)
    win_message = "Corruption Purged"
    win_message_length = len(win_message)
    Index = 0
    displayed_text = ""
    while game_win:
        screen.fill(black)
        if Index < win_message_length:
            displayed_text += win_message[Index]
            Index += 1
        lost_text = font.render(displayed_text, True, white)
        lost_text_rect = lost_text.get_rect(center=(Width / 2, Height / 2))
        screen.blit(lost_text, lost_text_rect)
        pygame.display.update()
        clock.tick(10)
        if Index == win_message_length:
            pygame.time.delay(2000)
            game_win = False
            game_state = "menu"

#Swords#
def buy_steelsword():
    global points, have_steelsword, have_ironsword
    if points >= 5:
        points -= 5
        have_ironsword = False
        have_steelsword = True

#Potions#
def buy_health():
    global points, player_health
    if points >= 3:
        points -= 3
        player_health += 20

#Bullets#
def buy_bullets():
    global points, bullet_count
    if points >= 5:
        points -= 5
        bullet_count += 4

#Armor upgrades#
def buy_reinforced_armor():
    global points, reinforced_armor
    if points >= 20:
        points -= 20
        reinforced_armor = True

def shop_menu(points):
    global noshop_frames
    root = tk.Tk()
    root.title("Shop")
    label = tk.Label(root, text="Would you like to buy something?", font=("Arial",15))
    label.pack(pady=10)
    points_label = tk.Label(root, text=f"Points {points}", font=("Arial",10))
    points_label.pack(pady=5)

    #Buying stuff#
    if have_steelsword == False:
        steelsword_button = tk.Button(root, text="Buy Steel Sword (5 points)", command=buy_steelsword)
        steelsword_button.pack(pady=5)

    health_button = tk.Button(root, text="Buy more health (3 points for 20 health)", command=buy_health)
    health_button.pack(pady=5)

    bullets_button = tk.Button(root, text="Buy some bullets (5 points for 4 bullets)",  command=buy_bullets)
    bullets_button.pack(pady=5)

    if reinforced_armor == False:
        reinforced_armor_button = tk.Button(root, text="Buy reinforced armor (20 points)", command=buy_reinforced_armor())
        reinforced_armor_button.pack(pady=5)

    noshop_frames = 300
    root.mainloop()

def stage1():
    global anti_lag
    platforms.add(Platform(100, Height - 100, 200, 20))
    platforms.add(Platform(400, Height - 200, 300, 20))
    enemies.add(Enemy(200, Height - 150, player))
    #Base platform#
    platforms.add(Platform(0, Height - 20, Width, 20))
    #Makes not infinitely spawn sprites#
    anti_lag = 0

def stage2():
    global anti_lag
    enemies.add(Enemy(600, 20, player))
    #Base platform#
    platforms.add(Platform(0, Height - 20, Width, 20))
    #Makes not infinitely spawn sprites#
    anti_lag = 0

def stage3():
    global anti_lag
    #Base platform#
    platforms.add(Platform(0, Height - 20, Width, 20))
    #Collision for merchant#
    '''antipass_box.add(AntiPass(406,501, 37,79))
    antipass_box.add(AntiPass(321,533, 80,47))'''
    shop_box.add(CollisionBox(300,400, 200, 200))
    #Makes not infinitely spawn sprites#
    anti_lag = 0

def stage4():
    global anti_lag
    #Base platform#
    platforms.add(Platform(0, Height - 20, Width, 20))
    #Everything Else#
    platforms.add(Platform(Width/3, Height - 100, Width/3, 20))
    enemies.add(Enemy(Width/2 ,Height - 150, player))
    #Makes not infinitely spawn sprites#
    anti_lag = 0

def stage5():
    global anti_lag
    #Base platform#
    platforms.add(Platform(0, Height - 20, Width, 20))
    #Everything Else#
    walls.add(Wall(Width/2,Height - 220, 20, 200))
    enemy1 = Enemy(600,Height - 50, player)
    enemies.add(enemy1)
    enemy2 = Enemy(200, Height - 50, player)
    enemies.add(enemy2)
    #Makes not infinitely spawn sprites#
    anti_lag = 0

def stage6():
    global anti_lag
    #Base platform#
    platforms.add(Platform(0, Height - 20, Width, 20))
    #Enemy#
    strong_enemies.add(Strong_Enemy(Width - 150, Height - 60, player))
    #Makes not infinitely spawn sprites#
    anti_lag = 0

def stage7():
    global anti_lag
    #Base platform#
    platforms.add(Platform(0, Height - 20, Width, 20))
    #Campfire collision#
    campfire_box.add(Campfire(385,540,30,40))

def stage20():
    global anti_lag
    #Base platform#
    platforms.add(Platform(0, Height - 20, Width, 20))
    #Boss#
    bosses.add(Boss(Width - 300 , Height - 500, player))
    #Makes not infinitely spawn sprites#
    anti_lag = 0

#Player class#
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = player_image
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (Width // 2, Height // 2)
        self.velocity_y = 0
        self.on_ground = False
        self.attack = False
        self.attack_timer = 0
        self.facing = "right"
        self.rect.x = 60
        self.rect.y = 0
        self.attack_overlay = None
        self.attack_overlay_rect = None

        #Attack hitbox setup#
        self.attack_hitbox = pygame.Rect(self.rect.right,self.rect.y,40,50)

    def update(self):
        global attacking, dash_cooldown
        keys = pygame.key.get_pressed()

        #Reinforced armor check#
        if reinforced_armor:
            self.image = player_reinforced_image
        else:
            self.image = self.original_image.copy()

        #Left & Right movement#
        if keys[pygame.K_a]:
            self.rect.x -= Player_Speed
            if self.facing != "left":
                self.facing = "left"
                self.image = pygame.transform.flip(self.image,True,False)
        if keys[pygame.K_d]:
            self.rect.x += Player_Speed
            if self.facing != "right":
                self.facing = "right"
                self.image = pygame.transform.flip(self.image,True,False)

        #Really make sure the player is facing the right way#
        if self.facing == "left":
            self.image = pygame.transform.flip(self.image, True, False)

        #Jumpies#
        if keys[pygame.K_w] and self.on_ground:
            self.velocity_y = Player_Jump_Strength
            self.on_ground = False

        #Dash#
        if keys[pygame.K_LSHIFT] and dash_cooldown <= 0:
            if self.facing == "right":
                self.rect.x += dash_length
            if self.facing == "left":
                self.rect.x -= dash_length
            dash_cooldown = 300

        #Attack overlay setup#
        if have_ironsword:
            self.attack_overlay = ironsword_image
        if have_steelsword:
            self.attack_overlay = steelsword_image
        self.attack_overlay_rect = self.attack_overlay.get_rect()

        #Attack#
        if self.attack:
            self.attack_timer -= 1
            if self.facing == "right":
                self.attack_overlay_rect.midleft = self.rect.midright
            else:
                self.attack_overlay_rect.midright = self.rect.midleft

        if self.attack_timer <= 0:
            self.attack = False

        #Gravity#
        self.velocity_y += Gravity
        self.rect.y += self.velocity_y

        #Update attack hitbox#
        if self.facing == "right":
            self.attack_hitbox.topleft = (self.rect.right,self.rect.y)
        else:
            self.attack_hitbox.topright = (self.rect.left,self.rect.y)

        #Ground check#
        self.on_ground = False
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits:
            if self.velocity_y > 0:
                self.rect.bottom = hits[0].rect.top
                self.velocity_y = 0
                self.on_ground = True

        #Debugging collision#
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > Width:
            self.rect.right = Width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > Height:
            self.rect.bottom = Height
            self.velocity_y = 0
            self.on_ground = True

    def draw(self):
        screen.blit(self.image, self.rect)
        if self.attack:
            if self.facing == "right":
                screen.blit(self.attack_overlay, self.attack_overlay_rect)
            if self.facing == "left":
                self.attack_overlay_flipped = pygame.transform.flip(self.attack_overlay,True,False)
                screen.blit(self.attack_overlay_flipped, self.attack_overlay_rect)

#Coin class#
class Coin(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        global Width, Height
        self.image = coin_image
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        if player.facing == "right":
            self.velocity_x = 10
        if player.facing == "left":
            self.velocity_x = -10
        self.velocity_y = -15
        self.gravity = 1

    def update(self):
        global coin_held_time, coin_hold_time
        self.velocity_y += self.gravity
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y

        if self.rect.top > Height - 20 or self.rect.right < 0 or self.rect.left > Width:
            self.kill()

#Basically just a gun#
class The_V1(pygame.sprite.Sprite):
    def __init__(self, x, y, player):
        super().__init__()
        if reinforced_armor == False:
            self.image = V1_image
        if reinforced_armor == True:
            self.image = V1_image_reinforced
        if reinforced_armor == False:
            self.empty_image = V1_empty_image
        if reinforced_armor == True:
            self.empty_image = V1_empty_image_reinforced
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.player = player
        self.facing = "right"
        self.reloading = False
        self.reload_timer = 0

    def start_reload(self):
        self.reloading = True
        self.image = self.empty_image
        self.reload_timer = pygame.time.get_ticks()

    def finish_reload(self):
        self.reloading = False
        if reinforced_armor == False:
            self.image = V1_image
        if reinforced_armor == True:
            self.image == V1_image_reinforced

    def update(self):
        if self.player.facing == "right":
            self.rect.x = self.player.rect.right
            if self.facing != "right":
                self.image = pygame.transform.flip(self.image, True, False)
                self.facing = "right"
        if self.player.facing == "left":
            self.rect.x = self.player.rect.left - self.rect.width
            if self.facing != "left":
                self.image = pygame.transform.flip(self.image, True, False)
                self.facing = "left"
        self.rect.y = self.player.rect.y

        if self.reloading and pygame.time.get_ticks() - self.reload_timer > reload_time:
            self.finish_reload()

class V1_Mag(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        global The_V1
        self.image = V1_mag
        self.rect = self.image.get_rect()
        if player.facing == "right":
            self.rect.x = x + 23
        self.rect.y = y
        self.speed_x = 3 if player.facing == "right" else -3
        self.velocity_y = -5
        self.gravity = 0.5

    def update(self):
        self.rect.x += self.speed_x

        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        if self.rect.bottom >= Height:
            self.kill()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = bullet_image
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

        self.speed = 15
        self.direction = player.facing
        if self.direction == "left":
            self.velocity_x = -self.speed
        if self.direction == "right":
            self.velocity_x = self.speed

    def update(self):
        self.rect.x += self.velocity_x

        if self.rect.x < 0 or self.rect.x > Width:
            self.kill()


#Platform class#
class Platform(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        super().__init__()
        self.image = pygame.Surface((width,height))
        self.image.fill(black)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

#Wall class#
class Wall(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        super().__init__()
        self.image = pygame.Surface((width,height))
        self.image.fill(black)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

#Collision boxes to detect collision#
class CollisionBox(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        super().__init__()
        self.image = pygame.Surface((width,height))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

#Anti-pass#
class AntiPass(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        super().__init__()
        self.image = pygame.Surface((width,height))
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

#Campfire#
class Campfire(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        super().__init__()
        self.image = pygame.Surface((width,height))
        self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

#Enemy class#
class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y,player):
        super().__init__()
        self.player = player
        self.image = Enemy1
        self.rect = self.image.get_rect()
        self.rect.center = (Width // 2, Height // 2)
        self.rect.topleft = (x,y)
        self.health = enemy_health
        self.velocity_y = 0
        self.on_ground_enemy = False
        self.facing = "right"

    def update(self):
        #Enemy gravity#
        self.velocity_y += Gravity
        self.rect.y += self.velocity_y
        #Reset sprite#
        if enemy_number != 20:
            self.image = Enemy1
            if self.facing == "left":
                self.image = pygame.transform.flip(self.image,True,False)
        #Enemy pass#
        if 1 <= enemy_number <= 4:
            pass
        #Enemy left & right & up#
        if 5 <= enemy_number <= 19:
            #Enemy jump#
            if self.player.rect.x - 40 < self.rect.x < self.player.rect.x + 40 and self.rect.y > self.player.rect.y + 5 and self.on_ground_enemy:
                self.velocity_y = enemy_jump_strength
                self.on_ground_enemy = False
            #Enemy left#
            if self.player.rect.x < self.rect.x:
                self.rect.x -= 3
                if self.facing != "left":
                    self.facing = "left"
                    self.image = pygame.transform.flip(self.image,True,False)
            #Enemy right#
            if self.player.rect.x > self.rect.x:
                self.rect.x += 3
                if self.facing != "right":
                    self.facing = "right"
                    self.image = pygame.transform.flip(self.image,True,False)
        #Enemy movement bug#
        if enemy_number == 20:
            if self.facing == "right":
                self.image = Enemy1_roll20
            if self.facing == "left":
                self.image = Enemy1_roll20
                self.image = pygame.transform.flip(self.image,True,False)
            if self.player.rect.x < self.rect.x:
                self.rect.x -= 6
                if self.facing != "left":
                    self.facing = "left"
                    self.image = pygame.transform.flip(self.image,True,False)
            if self.player.rect.x - 40 < self.rect.x < self.player.rect.x + 40 and self.rect.y > self.player.rect.y + 5 and self.on_ground_enemy:
                self.velocity_y = enemy_jump_strength * 2
                self.on_ground_enemy = False
            if self.player.rect.x > self.rect.x:
                self.rect.x += 6
                if self.facing != "right":
                    self.facing = "right"
                    self.image = pygame.transform.flip(self.image, True, False)

        #Enemy collision#
        self.on_ground_enemy = False
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits:
            if self.velocity_y > 0:
                self.rect.bottom = hits[0].rect.top
                self.velocity_y = 0
                self.on_ground_enemy = True

        #Artifical enemy bug - Or just debugging#
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > Width:
            self.rect.right = Width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > Height:
            self.rect.bottom = Height
            self.velocity_y = 0
            self.on_ground_enemy = True

    def take_damage(self,amount):
        global points
        self.health -= amount
        if self.health <= 0:
            points += 1
            self.kill()

#Strong enemy#
class Strong_Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y,player):
        super().__init__()
        self.player = player
        self.image = Enemy2
        self.rect = self.image.get_rect()
        self.rect.center = (Width // 2, Height // 2)
        self.rect.topleft = (x,y)
        self.health = strong_enemy_health
        self.velocity_y = 0
        self.on_ground_enemy = False
        self.facing = "right"

    def update(self):
        #Enemy gravity#
        self.velocity_y += Gravity
        self.rect.y += self.velocity_y

        #Enemy pass#
        if 1 <= enemy_number <= 4:
            pass
        #Enemy left & right & up#
        if 5 <= enemy_number <= 20:
            #Enemy left#
            if self.player.rect.x < self.rect.x:
                self.rect.x -= 2
                if self.facing != "left":
                    self.facing = "left"
                    self.image = pygame.transform.flip(self.image,True,False)
            #Enemy right#
            if self.player.rect.x > self.rect.x:
                self.rect.x += 2
                if self.facing != "right":
                    self.facing = "right"
                    self.image = pygame.transform.flip(self.image,True,False)


        #Enemy collision#
        self.on_ground_enemy = False
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits:
            if self.velocity_y > 0:
                self.rect.bottom = hits[0].rect.top
                self.velocity_y = 0
                self.on_ground_enemy = True

        #Artifical enemy bug - Or just debugging#
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > Width:
            self.rect.right = Width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > Height:
            self.rect.bottom = Height
            self.velocity_y = 0
            self.on_ground_enemy = True

    def take_damage(self,amount):
        global points
        self.health -= amount
        if self.health <= 0:
            points += 2
            self.kill()

class Boss(pygame.sprite.Sprite):
    def __init__(self,x,y,player):
        super().__init__()
        self.player = player
        self.image =boss_image
        self.rect = self.image.get_rect()
        self.rect.center = (Width // 2, Height // 2)
        self.rect.topleft = (x,y)
        self.health = boss_health
        self.velocity_y = 0
        self.on_ground_enemy = False
        self.facing = "right"

    def update(self):
        #Enemy gravity#
        self.velocity_y += Gravity
        self.rect.y += self.velocity_y

        #Enemy pass#
        if 1 <= enemy_number <= 2:
            pass
        #Enemy left & right & up#
        if 3 <= enemy_number <= 18:
            #Enemy left#
            if self.player.rect.x < self.rect.x:
                self.rect.x -= 1
                if self.facing != "left":
                    self.facing = "left"
                    self.image = pygame.transform.flip(self.image,True,False)
            #Enemy right#
            if self.player.rect.x > self.rect.x:
                self.rect.x += 1
                if self.facing != "right":
                    self.facing = "right"
                    self.image = pygame.transform.flip(self.image,True,False)
        #Funny little boss attack#
        if 19 <= enemy_number <= 20:
            '''ADD BIG BOSS ATTACK HERE'''
            pass


        #Enemy collision#
        self.on_ground_enemy = False
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits:
            if self.velocity_y > 0:
                self.rect.bottom = hits[0].rect.top
                self.velocity_y = 0
                self.on_ground_enemy = True

        #Artifical enemy bug - Or just debugging#
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > Width:
            self.rect.right = Width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > Height:
            self.rect.bottom = Height
            self.velocity_y = 0
            self.on_ground_enemy = True

    def take_damage(self, Amount):
        global points
        self.health -= Amount
        if self.health <= 0:
            points = 999
            self.kill()

#Create *things*#
#Collision boxes#
collision_box = pygame.sprite.Group()
collision_box.add(CollisionBox(790, Height - 80,60,60))
#Antipass boxes#
antipass_box = pygame.sprite.Group()
antipass_box.add(AntiPass(200,0,30,360))
#Damage boxes#
damage_box = pygame.sprite.Group()
damage_box.add(CollisionBox(230,0,570,360))
#Shop boxes#
shop_box = pygame.sprite.Group()
#Campfire boxes#
campfire_box = pygame.sprite.Group()
#Player#
player = Player()
#Coins#
coins = pygame.sprite.Group()
#Bullets#
bullets = pygame.sprite.Group()
#Platforms#
platforms = pygame.sprite.Group()
platforms.add(Platform(0,Height - 20,Width,20))
#Wall#
walls = pygame.sprite.Group()
#Enemies#
enemies = pygame.sprite.Group()
strong_enemies = pygame.sprite.Group()
bosses = pygame.sprite.Group()

#Sprite group#
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(platforms)
all_sprites.add(enemies)
#Game loop#
Bugging = True
while Bugging:
    if game_state == "menu":
        game_state = Menu.main_menu(screen, game_state)
        player_health = 100
    elif game_state == "game":
        if boss_tick == 39:
            stage_count = 39
        if boss_tick == 40:
            stage_count = 40
        background_changing()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #Suicide#
            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                player_health *= 0
            #Dev buttons#
            '''if event.type == pygame.KEYDOWN and event.key == pygame.K_END:
                boss_tick = 39
                stage_count = 39
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DELETE:
                FPS = 1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_PAGEDOWN:
                V1_damage = 1000'''
            #Attack#
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and player.attack_timer <= 0 and attack_cooldown <= 0:
                player.attack = True
                player.attack_timer = Attack_Duration
                attack_cooldown = 75
            #Coin throw#
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e and throw_timer <= 0 and len(coins) == 0:
                    new_coin = Coin(player.rect.centerx, player.rect.centery)
                    all_sprites.add(new_coin)
                    coins.add(new_coin)
            #GUN BANG#
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f and bullets_in_mag > 0 and not reloading_V1:
                V1_firing = True
                bullets_in_mag -= 1
                if V1 is None:
                    V1 = The_V1(player.rect.centerx, player.rect.centery, player)
                    all_sprites.add(V1)
                    V1_timer = pygame.time.get_ticks()

                V1.rect.x = player.rect.right if player.facing == "right" else player.rect.left - V1.rect.width
                V1.rect.y = player.rect.centery

                if player.facing == "right":
                    new_bullet = Bullet(V1.rect.right - 12, V1.rect.centery - 28)
                if player.facing == "left":
                    new_bullet = Bullet(V1.rect.left - 28, V1.rect.centery - 28)

                all_sprites.add(new_bullet)
                bullets.add(new_bullet)

            #Reloading#
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r and bullets_in_mag == 0 and bullet_count > 0 and not reloading_V1:
                if V1 is None:
                    V1 = The_V1(player.rect.centerx, player.rect.centery, player)
                    all_sprites.add(V1)

                reloading_V1 = True
                reload_start_time = pygame.time.get_ticks()
                V1.start_reload()
                ejected_mag = V1_Mag(V1.rect.x, V1.rect.y)
                all_sprites.add(ejected_mag)
            if reloading_V1:
                if pygame.time.get_ticks() - reload_start_time > reload_time:
                    reloading_V1 = False
                    bullets_in_mag += 4
                    bullet_count -= 4
                    if V1 is not None:
                        V1.finish_reload()

            #Checking mag#
            if event.type == pygame.KEYDOWN and event.key == pygame.K_t:
                if not mag_display_active:
                    mag_display_start_time = pygame.time.get_ticks()
                    mag_display_active = True

            #Checking ammo#
            if event.type == pygame.KEYDOWN and event.key == pygame.K_y:
                ammo_display_active = True
                ammo_display_start_time = pygame.time.get_ticks()

        #Holstering the V1#
        if len(bullets) == 0:
            if V1_firing:
                V1_timer = pygame.time.get_ticks()
                V1_firing = False
        else:
            V1_timer = pygame.time.get_ticks()

        if V1 is not None and pygame.time.get_ticks() - V1_timer > 750 and reloading_V1 is not True:
            all_sprites.remove(V1)
            V1.kill()
            V1 = None


        if player.attack:
            player.attack_timer -= 1
        if player.attack_timer <= 0:
            player.attack = False
        attack_cooldown -= 1
        dash_cooldown -= 1

        all_sprites.update()

        if have_steelsword:
            Player_Attack = 20
        if player.attack:
            hits_enemy = [enemy for enemy in enemies if player.attack_hitbox.colliderect(enemy.rect)]
            for enemy in hits_enemy:
                enemy.take_damage(Player_Attack)

            hits_strong_enemy = [strong_enemy for strong_enemy in strong_enemies if player.attack_hitbox.colliderect(strong_enemy.rect)]
            for strong_enemy in hits_strong_enemy:
                strong_enemy.take_damage(Player_Attack)

            hits_boss = [boss for boss in bosses if player.attack_hitbox.colliderect(boss.rect)]
            for boss in hits_boss:
                boss.take_damage(Player_Attack)
        #Special interaction#
        for bullet in bullets:
            shot_enemy = [enemy for enemy in enemies if bullet.rect.colliderect(enemy.rect)]
            for enemy in shot_enemy:
                enemy.take_damage(V1_damage)
                bullet.kill()
            shot_strong_enemy = [strong_enemy for strong_enemy in strong_enemies if bullet.rect.colliderect(strong_enemy.rect)]
            for strong_enemy in shot_strong_enemy:
                strong_enemy.take_damage(V1_damage)
                bullet.kill()
            shot_boss = [boss for boss in bosses if bullet.rect.colliderect(boss.rect)]
            for boss in shot_boss:
                boss.take_damage(V1_damage)
                bullet.kill()

            coin_shot = pygame.sprite.spritecollide(bullet,coins,True)
            if coin_shot:
                if len(enemies) > 0:
                    enemy = enemies.sprites()[0]
                    enemy.take_damage(200)
                if len(strong_enemies) > 0:
                    strong_enemy = strong_enemies.sprites()[0]
                    strong_enemy.take_damage(200)
                if len(bosses) > 0:
                    boss = bosses.sprites()[0]
                    boss.take_damage(200)

        # Damage stuff#
        if reinforced_armor:
            enemy_damage = 10
            strong_enemy_damage = 20
            boss_damage = 30

        #Collision#
        hits_platform = pygame.sprite.spritecollide(player,platforms,False)
        if hits_platform:
            if player.velocity_y > 0:
                player.rect.bottom = hits_platform[0].rect.top
                player.velocity_y = 0
                player.on_ground = True

        hits_wall = pygame.sprite.spritecollide(player,walls,False)
        if hits_wall:
            if player.facing == "right":
                player.rect.x = player.rect.x - 10
            if player.facing == "left":
                player.rect.x = player.rect.x + 10
        if (stage_5 == True and stage_count == 5):
            for enemy in enemies:
                enemy_hits_wall = pygame.sprite.spritecollide(enemy,walls,False)
                if enemy_hits_wall:
                    if enemy.facing == "right":
                        enemy.rect.x = enemy.rect.x - 10
                    if enemy.facing == "left":
                        enemy.rect.x = enemy.rect.x + 10

        hits_anti = pygame.sprite.spritecollide(player,antipass_box,False)
        if hits_anti:
            if player.facing == "right":
                player.rect.x = player.rect.x - 10
            if player.facing == "left":
                player.rect.x = player.rect.x + 10

        hits_campfire = pygame.sprite.spritecollide(player,campfire_box,False)
        if hits_campfire and can_camp == True:
            player_health += 20
            can_camp = False
            screen.fill(black)
            pygame.display.update()
            time.sleep(0.5)

        #Player taking damage#
        bumps_enemy = pygame.sprite.spritecollide(player,enemies,False)
        iframes -= 1
        if bumps_enemy and iframes <= 0:
            player_health -= enemy_damage
            iframes = 60
        bumps_strong_enemy = pygame.sprite.spritecollide(player,strong_enemies,False)
        if bumps_strong_enemy and iframes <= 0:
            player_health -= strong_enemy_damage
            iframes = 5
            for strong_enemy in strong_enemies:
                if strong_enemy.facing == "left":
                    slide_velocity = -10
                if strong_enemy.facing == "right":
                    slide_velocity = 10
            sliding = True
        bumps_boss = pygame.sprite.spritecollide(player,bosses,False)
        if bumps_boss and iframes <= 0:
            player_health -= boss_damage
            iframes = 10
            for boss in bumps_boss:
                if boss.facing == "left":
                    slide_velocity = -15
                if boss.facing == "right":
                    slide_velocity = 15
            sliding = True

        #Sliding#
        if sliding:
            player.rect.x += slide_velocity
            slide_velocity *= slide_friction
            if abs(slide_velocity) < 0.1:
                slide_velocity = 0
                sliding = False

        if player_health <= 0:
            if boss_tick < 41:
                game_end()
                platforms.empty()
                enemies.empty()
                all_sprites.empty()
                damage_box.empty()
                walls.empty()
                damage_box.empty()
                shop_box.empty()
                antipass_box.empty()
                strong_enemies.empty()
                campfire_box.empty()
                bullets.empty()
                bosses.empty()
                stage_count = 0
                boss_tick = 0
                points //= 2
                bullets_in_mag = 4
                bullet_count = 4
                player.rect.x = 50
                player.rect.y = Height - 500 - player.rect.height
                platforms.add(Platform(0, Height - 20, Width, 20))

        damage_box_in = pygame.sprite.spritecollide(player,damage_box,False)
        if damage_box_in and iframes <= 0:
            player_health -= 10
            iframes += 45
        if damage_box_in:
            player.rect.x = player.rect.x
            player.velocity_y = 0
            player.rect.y = player.rect.y - 1

        #Shoppping trigger#
        noshop_frames -= 1
        shop_trigger = pygame.sprite.spritecollide(player,shop_box,False)
        if shop_trigger and noshop_frames <= 0:
            shop_menu(points)

        #Switching stages#
        collision_box_hit = pygame.sprite.spritecollide(player,collision_box,False)
        if collision_box_hit and len(bosses) > 0:
            forcedcombat_message = boss_font.render("The portal is too corrupted to function", True, boss_color)
            screen.blit(forcedcombat_message, [Width / 7, Height / 2])
            pygame.display.update()
        if collision_box_hit and len(bosses) == 0:
            boss_tick += 1
            if 1 < stage_count and (boss_tick != 19 or boss_tick != 20):
                stage_count = random.randint(2,7)
            if stage_count <= 1:
                stage_count += 1
            if boss_tick == (39 or 40):
                stage_count = boss_tick
            if boss_tick == 41:
                Bugging = False
            anti_lag = 1
            platforms.empty()
            enemies.empty()
            all_sprites.empty()
            damage_box.empty()
            player.rect.x = 0
            walls.empty()
            damage_box.empty()
            shop_box.empty()
            antipass_box.empty()
            strong_enemies.empty()
            campfire_box.empty()
            bullets.empty()
            bosses.empty()
            player.rect.y = Height - 20 - player.rect.height
            can_camp = True
        if stage_1 == True and anti_lag == 1 and stage_count == 1:
            stage1()
        if stage_2 == True and anti_lag == 1 and stage_count == 2:
            stage2()
        if stage_3 == True and anti_lag == 1 and stage_count == 3:
            stage3()
        if stage_4 == True and anti_lag == 1 and stage_count == 4:
            stage4()
        if stage_5 == True and anti_lag == 1 and stage_count == 5:
            stage5()
        if stage_6 == True and anti_lag == 1 and stage_count == 6:
            stage6()
        if stage_7 == True and anti_lag == 1 and stage_count == 7:
            stage7()

        if stage_20 == True and anti_lag == 1 and stage_count == 40:
            stage20()

        all_sprites.add(player)
        all_sprites.add(platforms)
        all_sprites.add(enemies)
        all_sprites.add(strong_enemies)

        #Enemy 'ai'#
        enemy_tick += 1
        if enemy_tick >= enemy_action_time:
            enemy_random_gen = random.randint(1, 20)
            enemy_tick = 0
        enemy_number = enemy_random_gen

        #Drawings#
        screen.blit(current_background,[0,0])
        all_sprites.draw(screen)
        player.draw()
        bullets.draw(screen)
        bullets.update()
        collision_box.draw(screen)
        bosses.draw(screen)
        bosses.update()
        '''damage_box.draw(screen)'''
        walls.draw(screen)
        '''shop_box.draw(screen)
        campfire_box.draw(screen)'''
        if mag_display_active:
            current_time = pygame.time.get_ticks()
            if current_time - mag_display_start_time < mag_display_time:
                mag_image = mag_images[bullets_in_mag]
                screen.blit(mag_image, (0, 70))
                pygame.display.update()
            else:
                mag_display_active = False

        if ammo_display_active:
            current_time = pygame.time.get_ticks()
            if current_time - ammo_display_start_time < ammo_display_duration:
                current_ammo_held = writing_font.render(f"Ammo in bag: {bullet_count}", True, white)
                screen.blit(current_ammo_held, [0, 125])
            else:
                ammo_display_active = False
        #Stats#
        current_health = writing_font.render(f"Current Health: {player_health}",True,red)
        screen.blit(current_health, [0,0])
        current_points = writing_font.render(f"Points : {points}",True,green)
        screen.blit(current_points, [0,30])
        boss_amount = writing_font.render(f"{boss_tick}", True, blue)
        screen.blit(boss_amount, [770,0])

        #Refreshing and updating screen#
        pygame.display.update()
        clock.tick(FPS)

        '''print(f"On ground: {player.on_ground}")
        print(f"Facing: {player.facing}")
        print(f"Attacking: {player.attack}")
        print(f"Enemy tick: {enemy_tick}")
        print(enemy_random_gen)
        print(enemy_number)
        print(points)
        print(f"Stage count:{stage_count}")
        print(f"Boss tick: {boss_tick}")
        print(V1)
        print(reinforced_armor)
        print(ammo_display_active)'''

if boss_tick >= 41:
    game_won()
    platforms.empty()
    enemies.empty()
    all_sprites.empty()
    damage_box.empty()
    walls.empty()
    damage_box.empty()
    shop_box.empty()
    antipass_box.empty()
    strong_enemies.empty()
    campfire_box.empty()
    bullets.empty()
    bosses.empty()

sys.exit()