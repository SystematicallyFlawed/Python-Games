#Imports#
import pygame
pygame.init()
import sys
import random

#Variables#
Width = 800
Height = 600
FPS = 60
clock = pygame.time.Clock()
anti_lag = 0
#Stage variables#
stage_count = 0
stage_0 = False
stage_1 = False
stage_2 = False
#Player variables#
Gravity = 0.5
Player_Jump_Strength = -10
Player_Attack = 10
Attack_Duration = 10
player_image = pygame.image.load("player.png")
sword_image = pygame.image.load("sword1.png")
attack_speed = 10
attacking = False
attack_cooldown = 0
dash_length = 250
dash_cooldown = 0
points = 0
#Enemy variables#
enemy_health = 100
enemy_jump_strength = -8
enemy_tick = 0
enemy_action_time = 100
enemy_random_gen = 15
enemy_number = enemy_random_gen
#Colors#
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue  = (0,0,255)
#Backgrounds#
current_background = None
background0 = pygame.image.load("background0.png")
background1 = pygame.image.load("background1.png")
#Background switch#
def background_changing():
    global current_background, background0, background1, stage_0, stage_1, stage_2
    if stage_count == 0:
        stage_0 = True
    if stage_count == 1:
        stage_0 = False
        stage_1 = True

    if stage_0:
        current_background = background0
    if stage_1:
        current_background = background1

#Screen setup#
screen = pygame.display.set_mode((Width,Height))
pygame.display.set_caption("Bugged")

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

        #Attack hitbox setup#
        self.attack_hitbox = pygame.Rect(self.rect.right,self.rect.y,40,50)

        #Attack overlay setup#
        self.attack_overlay = sword_image
        self.attack_overlay_rect = self.attack_overlay.get_rect()

    def update(self):
        global attacking, dash_cooldown
        keys = pygame.key.get_pressed()

        #Left & Right movement#
        if keys[pygame.K_a]:
            self.rect.x -= 5
            if self.facing != "left":
                self.facing = "left"
                self.image = pygame.transform.flip(self.image,True,False)
        if keys[pygame.K_d]:
            self.rect.x += 5
            if self.facing != "right":
                self.facing = "right"
                self.image = pygame.transform.flip(self.image,True,False)

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


#Platform class#
class Platform(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        super().__init__()
        self.image = pygame.Surface((width,height))
        self.image.fill(black)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

#Enemy class#
class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y,player):
        super().__init__()
        self.player = player
        self.image = pygame.image.load("enemy1.png")
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
                    self.image = pygame.transform.flip(self.image, True, False)
        #Enemy movement bug#
        if enemy_number == 20:
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

    def take_damage(self,amount,points):
        self.health -= amount
        if self.health <= 0:
            points += 1
            self.kill()
        return points

#Create *things*#
#Collision boxes#
collision_box = pygame.sprite.Group()
collision_box.add(Platform(790, Height - 80,60,60))
#Player#
player = Player()
#Platforms#
platforms = pygame.sprite.Group()
platforms.add(Platform(0,Height - 20,Width,20))
#Enemies#
enemies = pygame.sprite.Group()

#Sprite group#
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(platforms)
all_sprites.add(enemies)

#Game loop#
while True:
    background_changing()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #Attack#
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and player.attack_timer <= 0 and attack_cooldown <= 0:
            player.attack = True
            player.attack_timer = Attack_Duration
            attack_cooldown = 75


    if player.attack:
        player.attack_timer -= 1
    if player.attack_timer <= 0:
        player.attack = False
    attack_cooldown -= 1
    dash_cooldown -= 1

    all_sprites.update()

    if player.attack:
        hits_enemy = [enemy for enemy in enemies if player.attack_hitbox.colliderect(enemy.rect)]
        for enemy in hits_enemy:
            enemy.take_damage(Player_Attack, points)
    #Collision#
    hits_platform = pygame.sprite.spritecollide(player,platforms,False)
    if hits_platform:
        if player.velocity_y > 0:
            player.rect.bottom = hits_platform[0].rect.top
            player.velocity_y = 0
            player.on_ground = True
    bumps_enemy = pygame.sprite.spritecollide(player,enemies,False)
    if bumps_enemy:
        '''pygame.quit()
        sys.exit()'''
    collision_box_hit = pygame.sprite.spritecollide(player,collision_box,False)
    if collision_box_hit:
        stage_count += 1
        anti_lag = 1
        platforms.empty()
        enemies.empty()
        all_sprites.remove(*all_sprites)
        player.rect.x = 0
        player.rect.y = Height - 20 - player.rect.height
    if stage_1 == True and anti_lag == 1:
        platforms.add(Platform(100, Height - 100, 200, 20))
        platforms.add(Platform(400, Height - 200, 300, 20))
        enemies.add(Enemy(200, Height - 150, player))
        #Base platform#
        platforms.add(Platform(0, Height - 20, Width, 20))
        anti_lag = 0
    all_sprites.add(player)
    all_sprites.add(platforms)
    all_sprites.add(enemies)

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
    collision_box.draw(screen)

    #Refreshing and updating screen#
    pygame.display.update()
    clock.tick(FPS)

    '''print(f"On ground: {player.on_ground}")
    print(f"Facing: {player.facing}")
    print(f"Attacking: {player.attack}")
    print(f"Enemy tick: {enemy_tick}")
    print(enemy_random_gen)
    print(enemy_number)'''
    print(points)