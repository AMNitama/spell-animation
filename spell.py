'''
author: nathan trifunovic
date: 1 July 2024
description: animating spells and projectiles in pygame
'''

import pygame

def animate_frames(filepath, scale_var):
    frames = []
    for i in range(1, 10):
        image = scaled_image(load_image(f"{filepath}{i}.png", True), scale=scale_var)
        frames.append(image)
    return frames


def load_image(img_file_name, alpha=False):
    file_name = f"assets/{img_file_name}"
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
    
    images = {"char_idle" : animate_frames("character/Idle/Idle", scale_var),
              "char_run" : animate_frames("character/Run/Run", scale_var)
    
    }  
    return images


pygame.init()

display_width = 800
display_height = 600

window = pygame.display.set_mode((display_width,display_height)) # creates actual game environment
pygame.display.set_caption('Leap Frog') # application name/ hover caption

images = load_images(display_width,display_height)


gameIcon = images["frog_temp"] # application image
pygame.display.set_icon(gameIcon) 

clock = pygame.time.Clock()