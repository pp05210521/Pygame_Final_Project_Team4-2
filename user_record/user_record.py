import os
import pygame
import operator
from choose_menu import ChooseMenu
from settings import IMAGE_PATH, FPS, WIN_WIDTH, WIN_HEIGHT, RECORD_PATH, COLOR_INACTIVE, COLOR_ACTIVE, game_status, user_info, SOUND_PATH, music
from button import Buttons
from color_settings import *


FONT_BIG = pygame.font.Font(None, 50)
FONT_SMALL = pygame.font.Font(None, 35)


def show_player(which: int) -> list:
    '''指定要讀取第幾個txt檔'''

    which_file = ['records.txt', 'records2.txt', 'records3.txt']
    last_records = ''
    # 絕對路徑！
    with open(os.path.join(RECORD_PATH, which_file[which]), 'rt') as file:
        records = file.readlines()
        for line in records:
            last_records += f'{line}'

    last_records = last_records.split('\n')
    last_records.pop(-1)
    last_records_list = []
    for i in last_records:
        name, score = i.split('--')
        last_records_list.append((name, float(score)))
    last_records_list = sorted(
        last_records_list, key=operator.itemgetter(1))  # sorted scores
    person_to_show = []
    for line in range(len(last_records_list)):
        each = f'{line+1}. {last_records_list[line]}s'
        new_each = ''
        for i in each:
            if i not in ("(", ")", "'"):
                new_each += i
        person_to_show.append(new_each)
    return person_to_show


def draw_text(screen, text, x, y, size: int):
    '''畫布/文字/座標/字體大小'''
    FONT = pygame.font.Font(None, size)
    txt_surface = FONT.render(str(text), True, WHITE)
    screen.blit(txt_surface, (x, y))


class InputBox:

    def __init__(self):
        self.rect = pygame.Rect((WIN_WIDTH/2)-100, (WIN_HEIGHT/3)-30, 140, 40)
        self.color = COLOR_INACTIVE
        self.text = ''  # user's name
        self.txt_surface = FONT_BIG.render(self.text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(f'player: {self.text}')
                    user_info['user_name'] = self.text

                    c = ChooseMenu()
                    c.run()
                    game_status['go_input_window'] = True

                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT_SMALL.render(
                    self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

    def get_text(self):
        return self.text


class Input_window:
    def __init__(self, screen):
        self.screen = screen

        self.bg = pygame.transform.scale(pygame.image.load(os.path.join(
            IMAGE_PATH, "level_background.png")), (WIN_WIDTH, WIN_HEIGHT))
        self.back_image = pygame.transform.scale(
            pygame.image.load(os.path.join(IMAGE_PATH, "back.png")), (80, 80))
        self.clock = pygame.time.Clock()
        self.input_box1 = InputBox()
        self.input_boxes = [self.input_box1]
        self.intro_text_1 = 'Input Name To Save Record'
        self.intro_text_2 = 'Hit `ENTER` When Ready'
        self.intro_text_3 = 'Highest scores:'
        self.intro_text_4 = 'Level 1'
        self.intro_text_5 = 'Level 2'
        self.intro_text_6 = 'Level 3'
        self.back_btn = Buttons(5, 5, 80, 80)
        self.buttons = [self.back_btn]

    def back_or_not(self, x, y):
        if self.back_btn.clicked(x, y):
            pygame.mixer.music.stop()
            self.play_music()
            if music["mute"]:
                pygame.mixer.music.pause()
            return True
        return False

    def play_music(self):
        pygame.mixer.music.load(os.path.join(SOUND_PATH, "menu1.mp3"))
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

    def run(self):
        while game_status["run"] and not game_status["go_start_menu"]:
            game_status["go_input_window"] = False
            x, y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_status["run"] = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.back_or_not(x, y):
                        game_status["go_start_menu"] = True

                for box in self.input_boxes:
                    box.handle_event(event)

            for box in self.input_boxes:
                box.update()

            self.screen.blit(self.bg, (0, 0))
            self.screen.blit(self.back_image, (5, 5))
            for bt in self.buttons:
                x, y = pygame.mouse.get_pos()
                bt.create_frame(x, y)
                bt.draw_frame(self.screen)
            draw_text(self.screen, self.intro_text_1,
                      WIN_WIDTH/2 - 220, (WIN_HEIGHT/3)-150, size=50)
            draw_text(self.screen, self.intro_text_2,
                      WIN_WIDTH/2 - 200, (WIN_HEIGHT/3)-100, size=50)
            draw_text(self.screen, self.intro_text_3,
                      WIN_WIDTH/2 - 130, (WIN_HEIGHT/2)-70, size=50)

            # level 1
            draw_text(self.screen, self.intro_text_4,
                      WIN_WIDTH/4 - 190, WIN_HEIGHT/2, size=50)
            for i in range(len(show_player(0))):
                draw_text(
                    self.screen, show_player(0)[i], WIN_WIDTH/4 - 190, WIN_HEIGHT/2+50+(i*50), 30)

            # level 2
            draw_text(self.screen, self.intro_text_5,
                      WIN_WIDTH/3 + 70, WIN_HEIGHT/2, size=50)
            for i in range(len(show_player(1))):
                draw_text(
                    self.screen, show_player(1)[i], WIN_WIDTH/3 + 70, WIN_HEIGHT/2+50+(i*50), 30)

            # level 3
            draw_text(self.screen, self.intro_text_6,
                      WIN_WIDTH/2 + 210, WIN_HEIGHT/2, size=50)
            for i in range(len(show_player(2))):
                draw_text(
                    self.screen, show_player(2)[i], WIN_WIDTH/2 + 210, WIN_HEIGHT/2+50+(i*50), 30)

            for box in self.input_boxes:
                box.draw(self.screen)

            for box in self.input_boxes:
                box.update()

            pygame.display.update()
            self.clock.tick(FPS)
