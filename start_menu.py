import pygame
import os
from color_settings import *
from settings import WIN_WIDTH, WIN_HEIGHT, FPS,IMAGE_PATH,SOUND_PATH


pygame.init()
pygame.mixer.init()


class StartMenu:
    def __init__(self):
        # win
        self.menu_win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        # background
        self.bg = pygame.transform.scale(pygame.image.load(os.path.join(
            IMAGE_PATH, "start_background.png")), (WIN_WIDTH, WIN_HEIGHT))

        # button
        self.start_btn = Buttons(412, 195, 200, 100)
        self.sound_btn = Buttons(522, 312, 80, 80)
        self.mute_btn = Buttons(522, 402, 80, 80)
        self.buttons = [self.start_btn,
                        self.sound_btn,
                        self.mute_btn]
        # music and sound
        self.sound = pygame.mixer.Sound(os.path.join(SOUND_PATH,"start.wav"))

    def play_music(self):
        pygame.mixer.music.load(os.path.join(SOUND_PATH,"menu1.mp3"))
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)
        self.sound.set_volume(0.5)


class Buttons:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.frame = None

    def clicked(self, x: int, y: int) -> bool:
        if self.rect.collidepoint(x, y):
            return True
        return False

    def create_frame(self, x: int, y: int):
        if self.clicked(x, y):
            x, y, w, h = self.rect
            self.frame = pygame.Rect(x - 5, y - 5, w + 10, h + 5)
        else:
            self.frame = None

    def draw_frame(self, win):
        if self.frame is not None:
            pygame.draw.rect(win, WHITE, self.frame, 5)
