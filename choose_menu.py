import pygame
import os
from color_settings import *
from settings import WIN_WIDTH, WIN_HEIGHT, IMAGE_PATH, SOUND_PATH



pygame.init()
pygame.mixer.init()


class ChooseMenu:
    def __init__(self):
        # win
        self.menu_win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        # background
        self.bg = pygame.transform.scale(pygame.image.load(os.path.join(
            IMAGE_PATH, "level_background.png")), (WIN_WIDTH, WIN_HEIGHT))
        #title and button
        self.title_image = pygame.transform.scale(pygame.image.load(
            os.path.join(IMAGE_PATH, "choose.png")), (220, 80))
        self.level1_image = pygame.transform.scale(pygame.image.load(
            os.path.join(IMAGE_PATH, "level_1.png")), (150, 80))
        self.level2_image = pygame.transform.scale(pygame.image.load(
            os.path.join(IMAGE_PATH, "level_2.png")), (150, 80))
        self.level3_image = pygame.transform.scale(pygame.image.load(
            os.path.join(IMAGE_PATH, "level_3.png")), (150, 80))
        self.back_image = pygame.transform.scale(
            pygame.image.load(os.path.join(IMAGE_PATH, "back.png")), (80, 80))
        self.back_image = pygame.transform.scale(
            pygame.image.load(os.path.join(IMAGE_PATH, "back.png")), (80, 80))
        self.lock_image = pygame.transform.scale(
            pygame.image.load(os.path.join(IMAGE_PATH, "lock.png")), (80, 80))
        # button
        self.level1_btn = Buttons(437, 180, 150, 80)  # x, y, width, height
        self.level2_btn = Buttons(437, 300, 150, 80)
        self.level3_btn = Buttons(437, 420, 150, 80)
        self.back_btn = Buttons(5, 5, 80, 80)
        self.buttons = [self.level1_btn,
                        #self.level2_btn,
                        #self.level3_btn,
                        self.back_btn]
        # music and sound
        self.sound = pygame.mixer.Sound(os.path.join(SOUND_PATH,"start.wav"))
        self.sound.set_volume(0.5)

    def back_or_not(self, x, y):
        if self.back_btn.clicked(x, y):
            return True
        return False

    def unlock(self,button):
        self.buttons.append(button)


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
