import pygame


# controller
class GameControl:
    def __init__(self, game_model, game_view):
        self.model = game_model
        self.view = game_view
        self.events = {"game quit": False,
                       "mouse position": [0, 0],
                       "keyboard key": 0
                       }
        self.request = None  # response of user input

    def update_model(self):
        """update the model and the view here"""
        self.request = self.model.get_request(self.events)
        self.model.user_request(self.request)
        self.model.enemies_advance()
        self.model.heros_advance()

    def receive_user_input(self):
        """receive user input from the events"""
        # event initialization
        self.events = {"game quit": False,
                       "mouse position": None,
                       "keyboard key": None
                       }
        # update event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.events["game quit"] = True
            # player click action
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                self.events["mouse position"] = [x, y]
        self.events["keyboard key"] = pygame.K_n
        
    def money_counter(self):
        if(self.model.money_cd < self.model.money_max_cd):
            self.model.money_cd += 1
        else:
            self.model.money += 1
            self.model.money_cd = 0
                    
    def update_view(self):
        # render background
        self.view.draw_bg()
        self.view.draw_mytower_hp(
            self.model.mytower_hp, self.model.mytower_max_hp)
        self.view.draw_entower_hp(
            self.model.entower_hp, self.model.entower_max_hp)
        self.view.draw_enemies(self.model.enemies)
        self.view.draw_heros(self.model.heros)
        self.view.draw_money(self.model.money)
        self.view.draw_data_p()
        self.view.draw_data_howhow()
        if self.model.menu is not None:
            self.view.draw_menu(self.model.menu)

    @property
    def quit_game(self):
        return self.events["game quit"]
