"""
Name: Nathan Trifunovic
Date: 27 July 2024
Description: This file is specifically for loading things from asset folder, to make it more organized
             and simplify the main function's layout, and allow for clarity and organization
"""

import pygame

# creates a list for each image/frame used within the death animation
# def load_death_frames(scale_var):
#     frames = []
#     for i in range(1, 10):
#         image = scaled_image(load_image(f"GreenBrown/death/death{i}.png", True), scale=scale_var)
#         frames.append(image)
#     return frames

def animate(scale_var, fm, path):
    frames = []
    for i in range(1, fm+1): 
        image = scaled_image(load_image(f"{path}{i}.png", True), scale=scale_var)
        frames.append(image)
    return frames

def load_image(img_file_name, alpha=False):
    file_name = f"assets/{img_file_name}"
    # loads images from asseset/images file, if alpha = True then it has a transparent background
    img = pygame.image.load(file_name).convert_alpha() if alpha else pygame.image.load(file_name).convert()
    return img

# for scaling background/icons/sprites if window changes
def scaled_image(img, width=None, height=None, scale=None, flip_Hor=False, flip_Ver=False):
    # check if scaling factor is given, calculates new width and height of image
    if scale:
        width = int(img.get_rect().width * scale)
        height = int(img.get_rect().height * scale)
    
    # checks if image should be flipped
    img = pygame.transform.flip(img, flip_Hor, flip_Ver)
    
    # checks if new dimensions are specified
    if width is not None or height is not None:
        img = pygame.transform.scale(img, (width,height))
    return img

# dictionary that loads all the images
def load_images(display_width, display_height):
    scale_var = min(display_width, display_height) / 250
    
    # images = {"intro_bg": scaled_image(load_image("City Background.png", True), display_width, display_height), # cityscape in intro background
    #        "intro_fg" : scaled_image(load_image("City Foreground.png", True), display_width, display_height),   # foreground city used in parallax animation
    #        "intro_sky" : scaled_image(load_image("Sky.png"), display_width, display_height),    # sky within intro background
    #        "frog_temp" : load_image("frog.png", True),  # icon on the taskbar
    #        "options" : scaled_image(load_image("configure.png", True), scale=scale_var),    # NOT IN USE
    #        "options_hover" : scaled_image(load_image("configure hover.png", True), scale=scale_var),    # NOT IN USE
    #        "exit" : scaled_image(load_image("no.png",True), scale=scale_var),   # used for exit button
    #        "R_jump": scaled_image(load_image("GreenBrown/hop/gb_hop4.png", True), scale=scale_var), # jumping looking right
    #        "R_fall": scaled_image(load_image("GreenBrown/hop/gb_hop6.png", True), scale=scale_var), # falling looking right
    #        "idle": scaled_image(load_image("GreenBrown/idle/gb_idle1.png", True), scale=scale_var), # idle animation
    #        "death" : load_death_frames(scale_var) # list of each death frame, scaled and alpha
    # }

    images = {"run" : animate(scale_var, 6,"character/Run/Run"),
              "idle" : animate(scale_var, 6, "character/Idle/Idle")

    }
    # for left movement of sprite
    # images["L_jump"] = scaled_image(images["R_jump"], flip_Hor=True)
    # images["L_fall"] = scaled_image(images["R_fall"], flip_Hor=True)
    
    # # flip sky for seem-less scroll effect
    # images["flip_sky"] = scaled_image(images["intro_sky"], flip_Ver=True )    
    return images


# dictionary of all musics
def load_playlist():
    # return{
    #     "intro" : "00 intro_0.ogg",
    #     "bgm1" : "07 high in the mountains.ogg",
    #     "bgm2" : "02 lava city.ogg",
    #     "game_over" : "1x game over.ogg"
    # }
    return None

# takes a dictionary and plays the music, allows for volume adjust
def play_music(playlist, track_name, volume=0.3, loop=-1):
    if track_name in playlist:
        file_name = f"assets/music/{playlist[track_name]}"
        pygame.mixer.music.load(file_name)
        pygame.mixer.music.play(loop)
        pygame.mixer.music.set_volume(volume)
    else:
        print("Track not found!")


# dictionary of sound effects
def load_effect():
    # return{
    #     "squish" : "slime1.wav",
    #     "interact" : "interface1.wav",
    #     "death" : "Explosion.wav",
    #     "coin" : "Coin01.aif"
    # }
    return None

# uses dictionary of sound effects, plays sound
def play_sfx(effects, fx_name, volume=0.3):
    if fx_name in effects:
        filename = f"assets/sfx/{effects[fx_name]}"
        sound = pygame.mixer.Sound(filename)
        sound.set_volume(volume)
        sound.play()
    else:
        print("Sound not found!")

