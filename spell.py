'''
author: nathan trifunovic
date: 27     July 2024
description: animating spells and projectiles in pygame
links:  https://www.youtube.com/watch?v=MYaxPa_eZS0&t=290s      Animation w/ sprites
        https://github.com/clear-code-projects/animation        Animation w/ sprites tutorial github
        https://www.youtube.com/watch?v=M6e3_8LHc7A             Loading Sprite sheets
        https://www.youtube.com/watch?v=NGFk44fY0O4             Lighting/particles
'''


import pygame
import load_assets as pic

class Player(pygame.sprite.Sprite):
    def __init__(self, animations, pos_x, pos_y, speed):
        super().__init__()
        # self.run_animation = False
        # self.frames = frames
        # self.sprites = []
        # self.current_sprite = 0
        # self.image = self.sprites[self.current_sprite]

        self.animations = animations    # getting dictionary of character animations
        self.current_animation = "idle" # the dictionary key for the frames list
        self.frames = self.animations[self.current_animation]   # list of pictures used in animation frames
        self.current_frame = 0  # index of picture
        self.speed = speed # animation speed
        self.image = self.frames[self.current_frame]    # what is displayed


        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.animation_time = 0

    def set_animation(self, animation_name):
        if animation_name in self.animations:
            self.current_animation = animation_name
            self.frames = self.animations[self.current_animation]

    # def run(self):
    #     self.sprites = images["run"]
    #     self.run_animation = True

    # def update(self, speed):
    #     if self.run_animation == True: 
    #         self.current_sprite += speed
    #         if self.current_sprite >= len(self.sprites):
    #             self.current_sprite = 0
    #             self.run_animation = False 

    #     self.image = self.sprites[int(self.current_sprite)]
    def update(self, dt):
        self.animation_time += dt
        if self.animation_time >= self.speed:
            self.animation_time = 0
            self.current_frame += 1
            if self.current_frame >= len(self.frames):
                self.current_frame = 0
            self.image = self.frames[self.current_frame]





pygame.init()
clock = pygame.time.Clock()
FPS = 60


display_width = 1280
display_height = 800



screen = pygame.display.set_mode((display_width,display_height), pygame.RESIZABLE) # creates actual game environment
pygame.display.set_caption('Spell Test') # application name/ hover caption
gameIcon = pygame.image.load("assets/character/Idle/Idle2.png").convert_alpha()
pygame.display.set_icon(gameIcon)

images = pic.load_images(display_width, display_height)
animations = {
    "run" : images["run"],
    "idle" : images["idle"]
}

moving_sprites = pygame.sprite.Group()
player = Player(animations, display_width//2 , display_height//2, 60)
moving_sprites.add(player)



while True:
    dt = clock.tick(FPS)
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        player.set_animation("run")
    else:
        player.set_animation("idle")
    


    screen.fill((0,0,0))
    moving_sprites.draw(screen)
    #moving_sprites.update(0.25)
    moving_sprites.update(dt)


    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h,), pygame.RESIZABLE)
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                fullscreen = False
                if fullscreen:
                    screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((screen.get_width(), screen.get_height()),pygame.RESIZABLE)


            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            
            # if event.key == pygame.K_SPACE:
            #     player.set_animation("run")

            #player.run(display_width, display_height)

    pygame.display.flip()
    clock.tick(FPS)

