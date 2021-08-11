import pygame
#from tower.towers import Tower, Vacancy
from settings import SOUND_PATH
import os

"""This module is import in model.py"""

"""
Here we demonstrate how does the Observer Pattern work
Once the subject updates, if will notify all the observer who has register the subject
"""


class RequestSubject:
    def __init__(self, model):
        self.__observers = []
        self.model = model

    def register(self, observer):
        self.__observers.append(observer)

    def notify(self, user_request):
        for o in self.__observers:
            o.update(user_request, self.model)


class EnemyGenerator:
    def __init__(self, subject):
        subject.register(self)
        self.cd = 900
        self.max_cd = 900

    def update(self, user_request: str, model):
        """add new enemy"""
        if(self.cd >= self.max_cd):
            if user_request == "start new wave":
                model.enemies.add(3)  # generate n enemy
                self.cd = 0
        else:
            self.cd += 1


class Music:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """music on"""
        if user_request == "music":
            pygame.mixer.music.unpause()
            model.sound.play()


class Muse:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """music off"""
        if user_request == "mute":
            pygame.mixer.music.pause()
            model.sound.play()


class Hero_howhow:
    def __init__(self, subject):
        subject.register(self)
        #self.howhow_music = pygame.mixer.Sound("./sound/howhow_sound.mp3")
        self.howhow_music = pygame.mixer.Sound(os.path.join(SOUND_PATH,"howhow_sound.mp3"))
    def update(self, user_request: str, model):
        if user_request == "howhow":
            if model.money >= 100:
                model.money -= 100
                model.heros.add('howhow')
                self.howhow_music.set_volume(0.4)
                pygame.mixer.Channel(2).play(self.howhow_music)
                print('summon howhow')

class Hero_godtone:
    def __init__(self, subject):
        subject.register(self)
        self.godtone_music = pygame.mixer.Sound(os.path.join(SOUND_PATH,"tone_sound.mp3"))
    def update(self, user_request: str, model):
        if user_request == "godtone":
            if model.money >= 50:
                model.money -= 50
                model.heros.add("godtone")
                self.godtone_music.set_volume(0.03)
                pygame.mixer.Channel(2).play(self.godtone_music)
                print('summon godtone')


class Hero_p:
    def __init__(self, subject):
        subject.register(self)
        subject.register(self)
        self.p_music = pygame.mixer.Sound(os.path.join(SOUND_PATH,"p_sound.mp3"))
    def update(self, user_request: str, model):
        if user_request == "p":
            if model.money >= 200:
                model.money -= 200
                model.heros.add("p")
                self.p_music.set_volume(0.8)
                pygame.mixer.Channel(2).play(self.p_music)
                print('summon p')


class Special:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        if user_request == "special" and model.en.expedition:
            if model.money >= 200:
                model.money -= 200
                for en in model.en.expedition:
                    en.health = en.health // 2


class Upgrade:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        if user_request == "upgrade":
            if model.money >= 100:
                model.money -= 100
                for h in model.he.expedition:
                    h.max_health += 5
                    h.health += 5
