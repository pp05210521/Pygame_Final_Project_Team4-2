import pygame
import os
from color_settings import *
from settings import WIN_WIDTH, WIN_HEIGHT, FPS, IMAGE_PATH, SOUND_PATH, game_status,music
# from choose_menu import ChooseMenu
from user_record.user_record import Input_window
from button import Buttons


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
        self.sound = pygame.mixer.Sound(os.path.join(SOUND_PATH, "start.wav"))
        self.sound.set_volume(0.01)

    def play_music(self):
        pygame.mixer.music.load(os.path.join(SOUND_PATH, "menu1.mp3"))
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
        
    def play_music_select(self):
        pygame.mixer.music.load(os.path.join(SOUND_PATH, "level_select.mp3"))
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

    def run(self):
        self.play_music()
        pygame.display.set_caption("一日防疫指揮官")
        clock = pygame.time.Clock()
        while game_status["run"]:
            game_status["go_start_menu"] = False
            clock.tick(FPS)
            self.menu_win.blit(self.bg, (0, 0))
            x, y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_status["run"] = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # check if hit start btn
                    if self.mute_btn.clicked(x, y):
                        pygame.mixer.music.pause()
                        music["mute"] = True
                    elif self.sound_btn.clicked(x, y):
                        pygame.mixer.music.unpause()
                        music["mute"] = False
                    if self.start_btn.clicked(x, y):
                        pygame.mixer.music.stop()
                        self.play_music_select()
                        self.sound.play()
                        if music["mute"]:
                            pygame.mixer.music.pause()
                        i = Input_window(self.menu_win)
                        i.run()

            for bt in self.buttons:
                bt.create_frame(x, y)
                bt.draw_frame(self.menu_win)
            pygame.display.update()
        pygame.quit()



