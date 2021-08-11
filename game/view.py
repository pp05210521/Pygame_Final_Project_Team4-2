import pygame
from settings import WIN_WIDTH, WIN_HEIGHT, BACKGROUND_IMAGE, BLACK, HEALTH_WIDTH, HEALTH_HEIGHT, FPS
from color_settings import *

hero_menu_image = pygame.transform.scale(
    BACKGROUND_IMAGE, (WIN_WIDTH, WIN_HEIGHT))
p_button_image = pygame.transform.scale(
    pygame.image.load("images/p_btn.png"), (80, 80))
godtone_button_image = pygame.transform.scale(
    pygame.image.load("images/godtone_btn.jpg"), (80, 80))
howhow_button_image = pygame.transform.scale(
    pygame.image.load("images/howhow_btn.jpg"), (80, 80))
locked_button_image = pygame.transform.scale(
    pygame.image.load("images/locked.png"), (80, 80))
en_base_image = pygame.transform.scale(
    pygame.image.load("images/en_tower.png"), (150, 200))
hero_base_image = pygame.transform.scale(
    pygame.image.load("images/tower.png"), (150, 150))

UPGRADE_BTN_IMAGE = pygame.transform.scale(
    pygame.image.load("images/upgrade.png"), (160, 50))
SPECIAL_SKILL_BTN_IMAGE = pygame.transform.scale(
    pygame.image.load("images/skill.png"), (160, 50))

MONEY_IMAGE = pygame.transform.scale(
    pygame.image.load("images/coin.png"), (180, 60))


class GameView:
    def __init__(self):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        # self.font = pygame.font.SysFont("comicsans", 30)

    def draw_bg(self):
        self.win.blit(hero_menu_image, (0, 0))
        heromenu_background = pygame.Surface((WIN_WIDTH, 100), pygame.SRCALPHA)
        heromenu_background.fill((0, 0, 0, 64))
        self.win.blit(heromenu_background, (0, 500))
        pygame.draw.rect(self.win, BLACK, [315, 510, 80, 80], 10)
        pygame.draw.rect(self.win, BLACK, [435, 510, 80, 80], 10)
        pygame.draw.rect(self.win, BLACK, [555, 510, 80, 80], 10)
        pygame.draw.rect(self.win, BLACK, [195, 510, 80, 80], 10)
        self.win.blit(p_button_image, (315, 510))
        self.win.blit(godtone_button_image, (435, 510))
        self.win.blit(howhow_button_image, (555, 510))
        self.win.blit(locked_button_image, (195, 510))
        self.win.blit(en_base_image, (0, 300))
        self.win.blit(hero_base_image, (875, 350))
        self.win.blit(UPGRADE_BTN_IMAGE, (675, 500))
        self.win.blit(SPECIAL_SKILL_BTN_IMAGE, (675, 550))
        #pygame.draw.rect(self.win, BLACK, [675, 510, 100, 70], 10)

    def draw_enemies(self, enemies):
        for en in enemies.get():
            if(en.en_type == 1):
                # 改敵人大小的話，記得改敵人blit的位置(y)
                self.win.blit(en.image, (en.rect.x, en.rect.y - 25))
                # draw health bar
                bar_width = en.rect.w * (en.health / en.max_health)
                max_bar_width = en.rect.w
                bar_height = 5
                # 改敵人大小的話，記得改血條blit的位置(y)
                pygame.draw.rect(self.win, RED, [en.rect.x, en.rect.y - 35, max_bar_width, bar_height])
                pygame.draw.rect(self.win, GREEN, [en.rect.x, en.rect.y - 35, bar_width, bar_height])
                
            elif(en.en_type == 2):
                # 改敵人大小的話，記得改敵人blit的位置(y)
                self.win.blit(en.image, (en.rect.x, en.rect.y - 25))
                # draw health bar
                bar_width = en.rect.w * (en.health / en.max_health)
                max_bar_width = en.rect.w
                bar_height = 5
                # 改敵人大小的話，記得改血條blit的位置(y)
                pygame.draw.rect(self.win, RED, [en.rect.x, en.rect.y - 35, max_bar_width, bar_height])
                pygame.draw.rect(self.win, GREEN, [en.rect.x, en.rect.y - 35, bar_width, bar_height])
                
            elif(en.en_type == 3):
                # 改敵人大小的話，記得改敵人blit的位置(y)
                self.win.blit(en.image, (en.rect.x, en.rect.y - 50))
                # draw health bar
                bar_width = en.rect.w * (en.health / en.max_health)
                max_bar_width = en.rect.w
                bar_height = 5
                # 改敵人大小的話，記得改血條blit的位置(y)
                pygame.draw.rect(self.win, RED, [en.rect.x, en.rect.y - 45, max_bar_width, bar_height])
                pygame.draw.rect(self.win, GREEN, [en.rect.x, en.rect.y - 45, bar_width, bar_height])
                
            elif(en.en_type == 4):
                # 改敵人大小的話，記得改敵人blit的位置(y)
                self.win.blit(en.image, (en.rect.x, en.rect.y - 45))
                # draw health bar
                bar_width = en.rect.w * (en.health / en.max_health)
                max_bar_width = en.rect.w
                bar_height = 5
                # 改敵人大小的話，記得改血條blit的位置(y)
                pygame.draw.rect(self.win, RED, [en.rect.x, en.rect.y - 55, max_bar_width, bar_height])
                pygame.draw.rect(self.win, GREEN, [en.rect.x, en.rect.y - 55, bar_width, bar_height])

    def draw_heros(self, heros):
        for hero in heros.get():
            self.win.blit(hero.image, hero.rect)
            # draw health bar
            bar_width = hero.rect.w * (hero.health / hero.max_health)
            max_bar_width = hero.rect.w
            bar_height = 5
            pygame.draw.rect(
                self.win, RED, [hero.rect.x, hero.rect.y - 10, max_bar_width, bar_height])
            pygame.draw.rect(self.win, GREEN, [
                             hero.rect.x, hero.rect.y - 10, bar_width, bar_height])
            
            
    def draw_data_p(self):
        x, y = pygame.mouse.get_pos()
        p_btn_rect = p_button_image.get_rect()
        p_btn_rect.center = (355, 550)
        if(p_btn_rect.collidepoint(x, y)):
            p_data = pygame.Surface((100, 100), pygame.SRCALPHA)
            p_data.fill((0, 0, 0, 64))
            self.win.blit(p_data, (310, 390))
            
            Topic = pygame.font.Font(None, 22)
            Topic_text = Topic.render("Initial ability", True, WHITE)
            self.win.blit(Topic_text, (315, 395))
            
            HP = pygame.font.Font(None, 20)        
            HP_text = HP.render(" HP = 10", True, WHITE)
            self.win.blit(HP_text, (310, 420))
            
            Power = pygame.font.Font(None, 20)        
            Power_text = Power.render(" Power = 7", True, WHITE)
            self.win.blit(Power_text, (310, 440))
           
            Attack_range = pygame.font.Font(None, 20)        
            Attack_range_text = Attack_range.render(" Range = 180", True, WHITE)
            self.win.blit(Attack_range_text, (310, 460))
            
    def draw_data_howhow(self):
        x, y = pygame.mouse.get_pos()
        howhow_btn_rect = howhow_button_image.get_rect()
        howhow_btn_rect.center = (595, 550)
        if(howhow_btn_rect.collidepoint(x, y)):
            howhow_data = pygame.Surface((100, 100), pygame.SRCALPHA)
            howhow_data.fill((0, 0, 0, 64))
            self.win.blit(howhow_data, (550, 390))
            
            Topic = pygame.font.Font(None, 22)
            Topic_text = Topic.render("Initial ability", True, WHITE)
            self.win.blit(Topic_text, (555, 395))
            
            HP = pygame.font.Font(None, 20)        
            HP_text = HP.render(" HP = 15", True, WHITE)
            self.win.blit(HP_text, (550, 420))
            
            Power = pygame.font.Font(None, 20)        
            Power_text = Power.render(" Power = 3", True, WHITE)
            self.win.blit(Power_text, (550, 440))
           
            Attack_range = pygame.font.Font(None, 20)        
            Attack_range_text = Attack_range.render(" Range = 60", True, WHITE)
            self.win.blit(Attack_range_text, (550, 460))

    def draw_menu(self, menu):
        self.win.blit(menu.image, menu.rect)
        for btn in menu.buttons:
            self.win.blit(btn.image, btn.rect)

    def draw_money(self, money: int):
        self.win.blit(MONEY_IMAGE, (15, 32))
        Money = pygame.font.Font(None, 40)        
        Money_text = Money.render(f"{money}", True, WHITE)
        self.win.blit(Money_text, (120, 50))

    def draw_mytower_hp(self, lives, max_lives):
        # draw_lives
        pygame.draw.rect(
            self.win, RED, [870+(HEALTH_WIDTH/max_lives*lives), 340, HEALTH_WIDTH/max_lives*(max_lives-lives), HEALTH_HEIGHT])
        pygame.draw.rect(
            self.win, GREEN, [870, 340, HEALTH_WIDTH/max_lives*lives, HEALTH_HEIGHT])

    def draw_entower_hp(self, lives, max_lives):
        # draw_lives
        pygame.draw.rect(
            self.win, RED, [5+(HEALTH_WIDTH/max_lives*lives), 280, HEALTH_WIDTH/max_lives*(max_lives-lives), HEALTH_HEIGHT])
        pygame.draw.rect(
            self.win, GREEN, [5, 280, HEALTH_WIDTH/max_lives*lives, HEALTH_HEIGHT])
