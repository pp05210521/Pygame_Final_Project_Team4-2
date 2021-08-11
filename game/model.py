import pygame
import os
from enemy.enemies import EnemyGroup
from hero import HeroGroup
from menu.menus import MainMenu
from game.user_request import RequestSubject, EnemyGenerator, Muse, Music, Hero_howhow, Hero_godtone, Hero_p, Special, Upgrade
from settings import WIN_WIDTH, WIN_HEIGHT, BACKGROUND_IMAGE
from hero import HeroGroup


class GameModel:
    def __init__(self):
        # data
        self.bg_image = pygame.transform.scale(
            BACKGROUND_IMAGE, (WIN_WIDTH, WIN_HEIGHT))
        self.__enemies = EnemyGroup()
        self.en = self.__enemies
        self.__heros = HeroGroup()
        self.he = self.__heros
        self.__menu = None
        self.__main_menu = MainMenu()
        self.selected_button = None
        # apply observer pattern
        self.subject = RequestSubject(self)
        self.generator = EnemyGenerator(self.subject)
        self.muse = Muse(self.subject)
        self.music = Music(self.subject)
        self.hero_howhow = Hero_howhow(self.subject)
        self.hero_godtone = Hero_godtone(self.subject)
        self.hero_p = Hero_p(self.subject)
        self.special = Special(self.subject)
        self.upgrade = Upgrade(self.subject)
        #self.wave = 0
        self.money = 100
        self.mytower_max_hp = 70
        self.mytower_hp = self.mytower_max_hp
        self.entower_max_hp = 70
        self.entower_hp = self.entower_max_hp
        self.sound = pygame.mixer.Sound(os.path.join(
            "sound", "start.wav")).set_volume(0.1)
        self.money_cd = 0
        self.money_max_cd = 5

    def user_request(self, user_request: str):
        """ add tower, sell tower, upgrade tower"""
        self.subject.notify(user_request)

    def get_request(self, events: dict) -> str:
        """get keyboard response or button response"""
        # initial
        self.selected_button = None
        # mouse event
        if events["mouse position"] is not None:
            x, y = events["mouse position"]
            self.select(x, y)
            if self.selected_button is not None:
                return self.selected_button.response
            return "nothing"
        # key event
        if events["keyboard key"] is not None:
            return "start new wave"
        return "nothing"

    def select(self, mouse_x: int, mouse_y: int) -> None:
        if self.__menu is not None:
            for btn in self.__menu.buttons:
                if btn.clicked(mouse_x, mouse_y):
                    self.selected_button = btn
            if self.selected_button is None:
                self.selected_tower = None
        # menu btn
        for btn in self.__main_menu.buttons:
            if btn.clicked(mouse_x, mouse_y):
                self.selected_button = btn

    def enemies_advance(self):
        self.__enemies.advance(self)

    def heros_advance(self):
        self.__heros.advance(self)

    @property
    def enemies(self):
        return self.__enemies

    @property
    def heros(self):
        return self.__heros

    @property
    def menu(self):
        return self.__menu

    @menu.setter
    def menu(self, new_menu):
        self.__menu = new_menu
