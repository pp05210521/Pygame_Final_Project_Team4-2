import pygame
from game.controller import GameControl
from game.model import GameModel
from game.view import GameView
from settings import FPS
from choose_menu import ChooseMenu
from start_menu import StartMenu


class Game:
    def __init__(self):
        #完成關卡就+1
        self.finish = 0

    def run(self):
        '''game start'''

        # initialization
        pygame.init()
        game_model = GameModel()  # core of the game (database, game logic...)
        game_view = GameView()  # render everything
        # deal with the game flow and user request
        game_control = GameControl(game_model, game_view)

        quit_game = False

        while not quit_game:
            pygame.time.Clock().tick(FPS)  # control the frame rate
            game_control.receive_user_input()  # receive user input
            game_control.money_counter()
            game_control.update_model()  # update the model
            game_control.update_view()  # update the view
            pygame.display.update()
            quit_game = game_control.quit_game


class pre_game():
    '''start menu'''

    def run(self):
        pygame.init()
        m = StartMenu()
        n = ChooseMenu()
        run = True
        clock = pygame.time.Clock()
        pygame.display.set_caption("一日防疫指揮官")
        m.play_music()

        while run:
            clock.tick(FPS)
            m.menu_win.blit(m.bg, (0, 0))
            x, y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                # quit
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # check if hit start btn
                    if m.mute_btn.clicked(x, y):
                        pygame.mixer.music.pause()
                    elif m.sound_btn.clicked(x, y):
                        pygame.mixer.music.unpause()

                    if m.start_btn.clicked(x, y):
                        m.sound.play()
                        run = True
                        clock = pygame.time.Clock()
                        pygame.display.set_caption("一日防疫指揮官")
                        # 選擇關卡
                        # 選擇關卡
                        while run:
                            clock.tick(FPS)
                            n.menu_win.blit(n.bg, (0, 0))
                            n.menu_win.blit(n.title_image, (402, 30))
                            n.menu_win.blit(n.level1_image, (437, 180))
                            n.menu_win.blit(n.level2_image, (437, 300))
                            n.menu_win.blit(n.level3_image, (437, 420))
                            game = Game()
                            transparent_surface = pygame.Surface(n.menu_win.get_size(), pygame.SRCALPHA)  # 製作畫布
                            transparency = 180
                            # 破關鎖定
                            if game.finish == 0:
                                pygame.draw.rect(transparent_surface, (0, 0, 0, transparency), [437, 300, 150, 80], 0)
                                pygame.draw.rect(transparent_surface, (0, 0, 0, transparency), [437, 420, 150, 80], 0)
                                n.menu_win.blit(transparent_surface, (0, 0))
                                n.menu_win.blit(n.lock_image, (472, 295))
                                n.menu_win.blit(n.lock_image, (472, 415))
                            else:
                                n.unlock(n.level2_btn)
                                pygame.draw.rect(transparent_surface, (0, 0, 0, transparency), [437, 420, 150, 80], 0)
                                n.menu_win.blit(transparent_surface, (0, 0))
                                n.menu_win.blit(n.lock_image, (472, 415))

                            n.menu_win.blit(n.back_image, (5, 5))
                            x, y = pygame.mouse.get_pos()
                            for event in pygame.event.get():
                                # quit
                                if event.type == pygame.QUIT:
                                    run = False
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    # check if hit start btn
                                    if n.level1_btn.clicked(x, y):
                                        n.sound.play()
                                        game.run()
                                        run = False
                                    elif n.level2_btn.clicked(x, y):
                                        pass
                                    elif n.level3_btn.clicked(x, y):
                                        pass
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if n.back_or_not(x, y):
                                    break
                            for bt in n.buttons:
                                x, y = pygame.mouse.get_pos()
                                bt.create_frame(x, y)
                                bt.draw_frame(n.menu_win)

                            pygame.display.update()

            for bt in m.buttons:
                bt.create_frame(x, y)
                bt.draw_frame(m.menu_win)
            pygame.display.update()
        pygame.quit()
