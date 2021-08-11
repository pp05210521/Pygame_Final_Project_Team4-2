import pygame
import os

# screen size
WIN_WIDTH = 1024
WIN_HEIGHT = 600

HEALTH_WIDTH, HEALTH_HEIGHT = 150, 10

# frame rate
FPS = 60

# color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (147, 0, 147)

# enemy path
en_PATH = [(100, 480), (1024, 480)]
hero_PATH = [(954, 435), (100, 435)]

# base
hero_BASE = pygame.Rect(874, 350, 150, 150)
en_BASE = pygame.Rect(0, 300, 150, 200)

# image
IMAGE_PATH=os.path.join(os.path.dirname(__file__),"images")
SOUND_PATH=os.path.join(os.path.dirname(__file__),"sound")
BACKGROUND_IMAGE = pygame.image.load(os.path.join(IMAGE_PATH, "dessert.jpg"))

