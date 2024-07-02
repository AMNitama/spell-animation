'''
author: nathan trifunovic
date: 1 July 2024
description: animating spells and projectiles in pygame
'''

import pygame

def animate_frames(filepath, scale_var):
    frames = []
    for i in range(1, 10):
        image = scaled_image(load_image(f"{i}.png", True), scale=scale_var)
        frames.append(image)
    return frames


def load_image(img_file_name, alpha=False):
    file_name = f"assets/images/{img_file_name}"
    # loads images from asseset/images file, if alpha = True then it has a transparent background
    img = pygame.image.load(file_name).convert_alpha() if alpha else pygame.image.load(file_name).convert()
    return img


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


def load_images(display_width, display_height):
    scale_var = min(display_width, display_height) / 250
    
    images = {"intro_bg": scaled_image(load_image("City Background.png", True), display_width, display_height), # cityscape in intro background
           "intro_fg" : scaled_image(load_image("City Foreground.png", True), display_width, display_height),   # foreground city used in parallax animation
           "intro_sky" : scaled_image(load_image("Sky.png"), display_width, display_height),    # sky within intro background
           "frog_temp" : load_image("frog.png", True),  # icon on the taskbar
           "options" : scaled_image(load_image("configure.png", True), scale=scale_var),    # NOT IN USE
           "options_hover" : scaled_image(load_image("configure hover.png", True), scale=scale_var),    # NOT IN USE
           "exit" : scaled_image(load_image("no.png",True), scale=scale_var),   # used for exit button
           "R_jump": scaled_image(load_image("GreenBrown/hop/gb_hop4.png", True), scale=scale_var), # jumping looking right
           "R_fall": scaled_image(load_image("GreenBrown/hop/gb_hop6.png", True), scale=scale_var), # falling looking right
           "idle": scaled_image(load_image("GreenBrown/idle/gb_idle1.png", True), scale=scale_var), # idle animation
           "death" : load_death_frames(scale_var) # list of each death frame, scaled and alpha
    }  
    return images