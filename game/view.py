import pygame
from settings import WIN_WIDTH, WIN_HEIGHT, BACKGROUND_IMAGE, BACKGROUND_IMAGE_two, BACKGROUND_IMAGE_three, BLACK, HEALTH_WIDTH, HEALTH_HEIGHT, FPS, IMAGE_PATH, skill_PATH
from color_settings import *
import os
import math

arial = pygame.font.match_font('arial')

# background images
bg_one = pygame.transform.scale(
    BACKGROUND_IMAGE, (WIN_WIDTH, WIN_HEIGHT))
bg_two = pygame.transform.scale(
    BACKGROUND_IMAGE_two, (WIN_WIDTH, WIN_HEIGHT))
bg_three = pygame.transform.scale(
    BACKGROUND_IMAGE_three, (WIN_WIDTH, WIN_HEIGHT))

# hero images
p_button_image = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGE_PATH, "p_btn.png")), (80, 80))
godtone_button_image = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGE_PATH, "godtone_btn.jpg")), (80, 80))
howhow_button_image = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGE_PATH, "howhow_btn.jpg")), (80, 80))
brian_button_image = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGE_PATH, "brian_btn.jpg")), (80, 80))
locked_button_image = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGE_PATH, "locked.png")), (80, 80))

# tower base images
en_base_image = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGE_PATH, "en_tower.png")), (150, 200))
hero_base_image = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGE_PATH, "tower.png")), (150, 150))

# skills button images
UPGRADE_BTN_IMAGE = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGE_PATH, "upgrade.png")), (160, 50))
SPECIAL_SKILL_BTN_IMAGE = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGE_PATH, "skill.png")), (160, 50))

# in-game status images
MONEY_IMAGE = pygame.transform.scale(pygame.image.load(
    os.path.join(IMAGE_PATH, "coin.png")), (180, 60))
game_loss_image = pygame.transform.scale(pygame.image.load(
    os.path.join(IMAGE_PATH, "game_over.png")), (400, 400))
game_win_image = pygame.transform.scale(pygame.image.load(
    os.path.join(IMAGE_PATH, "winning_view.png")), (600, 550))
SKILL_ANIMATION_IMAGE = pygame.transform.scale(pygame.image.load(
    os.path.join(IMAGE_PATH, "skilldisplay.png")), (600, 450))
game_completed_image = pygame.transform.scale(pygame.image.load(
    os.path.join(IMAGE_PATH, "game_completed.png")), (500, 300))


class GameView:
    def __init__(self, checkpoint):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.point = checkpoint
        # use for skill animation
        self.skill_move_path = skill_PATH
        self.path_index = 0
        self.move_count = 0
        self.stride = 5
        self.skillimage = SKILL_ANIMATION_IMAGE
        self.rect = self.skillimage.get_rect()
        self.rect.center = self.skill_move_path[self.path_index]

    def draw_bg(self):
        '''draw background & and all needed images according to checkpoint'''
        if(self.point == 1):
            self.win.blit(bg_one, (0, 0))
        elif(self.point == 2):
            self.win.blit(bg_two, (0, 0))
        elif(self.point == 3):
            self.win.blit(bg_three, (0, 0))
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
        if self.point == 1:
            self.win.blit(locked_button_image, (195, 510))
        else:
            self.win.blit(brian_button_image, (195, 510))
        self.win.blit(en_base_image, (0, 300))
        self.win.blit(hero_base_image, (875, 350))
        self.win.blit(UPGRADE_BTN_IMAGE, (675, 500))
        self.win.blit(SPECIAL_SKILL_BTN_IMAGE, (675, 550))

    def draw_enemies(self, enemies):
        for en in enemies.get():
            if(en.en_type == 1):
                # ???????????????????????????????????????blit?????????(y)
                self.win.blit(en.image, (en.rect.x, en.rect.y - 25))
                # draw health bar
                bar_width = en.rect.w * (en.health / en.max_health)
                max_bar_width = en.rect.w
                bar_height = 5
                # ???????????????????????????????????????blit?????????(y)
                pygame.draw.rect(
                    self.win, RED, [en.rect.x, en.rect.y - 35, max_bar_width, bar_height])
                pygame.draw.rect(self.win, GREEN, [
                                 en.rect.x, en.rect.y - 35, bar_width, bar_height])

            elif(en.en_type == 2):
                # ???????????????????????????????????????blit?????????(y)
                self.win.blit(en.image, (en.rect.x, en.rect.y - 25))
                # draw health bar
                bar_width = en.rect.w * (en.health / en.max_health)
                max_bar_width = en.rect.w
                bar_height = 5
                # ???????????????????????????????????????blit?????????(y)
                pygame.draw.rect(
                    self.win, RED, [en.rect.x, en.rect.y - 35, max_bar_width, bar_height])
                pygame.draw.rect(self.win, GREEN, [
                                 en.rect.x, en.rect.y - 35, bar_width, bar_height])

            elif(en.en_type == 3):
                # ???????????????????????????????????????blit?????????(y)
                self.win.blit(en.image, (en.rect.x, en.rect.y - 50))
                # draw health bar
                bar_width = en.rect.w * (en.health / en.max_health)
                max_bar_width = en.rect.w
                bar_height = 5
                # ???????????????????????????????????????blit?????????(y)
                pygame.draw.rect(
                    self.win, RED, [en.rect.x, en.rect.y - 45, max_bar_width, bar_height])
                pygame.draw.rect(self.win, GREEN, [
                                 en.rect.x, en.rect.y - 45, bar_width, bar_height])

            elif(en.en_type == 4):
                # ???????????????????????????????????????blit?????????(y)
                self.win.blit(en.image, (en.rect.x, en.rect.y - 45))
                # draw health bar
                bar_width = en.rect.w * (en.health / en.max_health)
                max_bar_width = en.rect.w
                bar_height = 5
                # ???????????????????????????????????????blit?????????(y)
                pygame.draw.rect(
                    self.win, RED, [en.rect.x, en.rect.y - 55, max_bar_width, bar_height])
                pygame.draw.rect(self.win, GREEN, [
                                 en.rect.x, en.rect.y - 55, bar_width, bar_height])

            elif(en.en_type == 5):
                # ???????????????????????????????????????blit?????????(y)
                self.win.blit(en.image, (en.rect.x, en.rect.y - 100))
                # draw health bar
                bar_width = en.rect.w * (en.health / en.max_health)
                max_bar_width = en.rect.w
                bar_height = 5
                # ???????????????????????????????????????blit?????????(y)
                pygame.draw.rect(
                    self.win, RED, [en.rect.x, en.rect.y - 100, max_bar_width, bar_height])
                pygame.draw.rect(self.win, GREEN, [
                                 en.rect.x, en.rect.y - 100, bar_width, bar_height])

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
            p_data = pygame.Surface((110, 100), pygame.SRCALPHA)
            p_data.fill((0, 0, 0, 64))
            self.win.blit(p_data, (310, 390))

            Topic = pygame.font.Font(arial, 22)
            Topic_text = Topic.render("Initial ability", True, WHITE)
            self.win.blit(Topic_text, (315, 390))

            HP = pygame.font.Font(arial, 20)
            HP_text = HP.render(" HP = 10", True, WHITE)
            self.win.blit(HP_text, (310, 410))

            Power = pygame.font.Font(arial, 20)
            Power_text = Power.render(" Power = 7", True, WHITE)
            self.win.blit(Power_text, (310, 430))

            Attack_range = pygame.font.Font(arial, 20)
            Attack_range_text = Attack_range.render(
                " Range = 180", True, WHITE)
            self.win.blit(Attack_range_text, (310, 450))

            Cost = pygame.font.Font(arial, 20)
            Cost_text = Cost.render(" Cost = 200", True, WHITE)
            self.win.blit(Cost_text, (310, 470))

    def draw_data_howhow(self):
        x, y = pygame.mouse.get_pos()
        howhow_btn_rect = howhow_button_image.get_rect()
        howhow_btn_rect.center = (595, 550)
        if(howhow_btn_rect.collidepoint(x, y)):
            howhow_data = pygame.Surface((100, 100), pygame.SRCALPHA)
            howhow_data.fill((0, 0, 0, 64))
            self.win.blit(howhow_data, (550, 390))

            Topic = pygame.font.Font(arial, 22)
            Topic_text = Topic.render("Initial ability", True, WHITE)
            self.win.blit(Topic_text, (555, 390))

            HP = pygame.font.Font(arial, 20)
            HP_text = HP.render(" HP = 15", True, WHITE)
            self.win.blit(HP_text, (550, 410))

            Power = pygame.font.Font(arial, 20)
            Power_text = Power.render(" Power = 3", True, WHITE)
            self.win.blit(Power_text, (550, 430))

            Attack_range = pygame.font.Font(arial, 20)
            Attack_range_text = Attack_range.render(" Range = 60", True, WHITE)
            self.win.blit(Attack_range_text, (550, 450))

            Cost = pygame.font.Font(arial, 20)
            Cost_text = Cost.render(" Cost = 70", True, WHITE)
            self.win.blit(Cost_text, (550, 470))

    def draw_data_godtone(self):
        x, y = pygame.mouse.get_pos()
        godtone_btn_rect = godtone_button_image.get_rect()
        godtone_btn_rect.center = (475, 550)
        if(godtone_btn_rect.collidepoint(x, y)):
            godtone_data = pygame.Surface((100, 95), pygame.SRCALPHA)
            godtone_data.fill((0, 0, 0, 64))
            self.win.blit(godtone_data, (430, 395))

            Topic_1 = pygame.font.Font(arial, 30)
            Topic_1_text = Topic_1.render("   I   am    ", True, WHITE)
            self.win.blit(Topic_1_text, (433, 385))

            Topic_2 = pygame.font.Font(arial, 30)
            Topic_2_text = Topic_2.render("  Toyz's   ", True, RED)
            self.win.blit(Topic_2_text, (435, 420))

            Topic_3 = pygame.font.Font(arial, 30)
            Topic_3_text = Topic_3.render("    dog   ", True, WHITE)
            self.win.blit(Topic_3_text, (435, 455))

            """
            Topic = pygame.font.Font(arial, 22)
            Topic_text = Topic.render("Initial ability", True, WHITE)
            self.win.blit(Topic_text, (435, 395))
            
            HP = pygame.font.Font(arial, 20)        
            HP_text = HP.render(" HP = 30", True, WHITE)
            self.win.blit(HP_text, (430, 415))
            
            Power = pygame.font.Font(arial, 20)        
            Power_text = Power.render(" Power = 2", True, WHITE)
            self.win.blit(Power_text, (430, 435))
           
            Attack_range = pygame.font.Font(arial, 20)        
            Attack_range_text = Attack_range.render(" Range = 60", True, WHITE)
            self.win.blit(Attack_range_text, (430, 455))
            
            Cost = pygame.font.Font(arial, 20)        
            Cost_text = Cost.render(" Cost = 50", True, WHITE)
            self.win.blit(Cost_text, (550, 475))
            """

    def draw_data_brian(self):
        x, y = pygame.mouse.get_pos()
        brian_btn_rect = brian_button_image.get_rect()
        brian_btn_rect.center = (235, 550)
        if(brian_btn_rect.collidepoint(x, y)):
            brian_data = pygame.Surface((220, 100), pygame.SRCALPHA)
            brian_data.fill((0, 0, 0, 64))
            self.win.blit(brian_data, (190, 390))

            Topic = pygame.font.Font(arial, 22)
            Topic_text = Topic.render(
                " Unlock after checkpoint 1", True, WHITE)
            self.win.blit(Topic_text, (195, 390))

            HP = pygame.font.Font(arial, 20)
            HP_text = HP.render(" HP = 1, attack then die", True, WHITE)
            self.win.blit(HP_text, (195, 410))

            Power = pygame.font.Font(arial, 20)
            Power_text = Power.render(" Power = 7, AOE", True, WHITE)
            self.win.blit(Power_text, (195, 430))

            Attack_range = pygame.font.Font(arial, 20)
            Attack_range_text = Attack_range.render(" Range = 60", True, WHITE)
            self.win.blit(Attack_range_text, (195, 450))

            Cost = pygame.font.Font(arial, 20)
            Cost_text = Cost.render(" Cost = 70", True, WHITE)
            self.win.blit(Cost_text, (195, 470))

    def draw_locked_brian(self):
        x, y = pygame.mouse.get_pos()
        locked_btn_rect = locked_button_image.get_rect()
        locked_btn_rect.center = (235, 550)
        if (locked_btn_rect.collidepoint(x, y)):
            brian_data = pygame.Surface((155, 100), pygame.SRCALPHA)
            brian_data.fill((0, 0, 0, 64))
            self.win.blit(brian_data, (190, 390))

            Topic_1 = pygame.font.Font(arial, 20)
            Topic_1_text = Topic_1.render(" This hero will", True, WHITE)
            self.win.blit(Topic_1_text, (190, 395))

            Topic_2 = pygame.font.Font(arial, 20)
            Topic_2_text = Topic_2.render(" be unclocked", True, WHITE)
            self.win.blit(Topic_2_text, (190, 430))

            Topic_3 = pygame.font.Font(arial, 20)
            Topic_3_text = Topic_3.render(
                " in further checkpoint", True, WHITE)
            self.win.blit(Topic_3_text, (190, 465))

    def draw_skill_data(self):
        x, y = pygame.mouse.get_pos()
        skill_btn_rect = SPECIAL_SKILL_BTN_IMAGE.get_rect()
        skill_btn_rect.center = (755, 575)
        if(skill_btn_rect.collidepoint(x, y)):
            skill_data = pygame.Surface((185, 50), pygame.SRCALPHA)
            skill_data.fill((0, 0, 0, 128))
            self.win.blit(skill_data, (835, 500))

            Cost = pygame.font.Font(arial, 20)
            Cost_text = Cost.render("Cost = 200", True, WHITE)
            self.win.blit(Cost_text, (840, 505))

            Ability = pygame.font.Font(arial, 20)
            Ability_text = Ability.render("Enemy's hp is halved", True, WHITE)
            self.win.blit(Ability_text, (840, 525))

    def draw_upgrade_data(self):
        x, y = pygame.mouse.get_pos()
        upgrade_btn_rect = UPGRADE_BTN_IMAGE.get_rect()
        upgrade_btn_rect.center = (755, 525)
        if(upgrade_btn_rect.collidepoint(x, y)):
            upgrade_data = pygame.Surface((185, 90), pygame.SRCALPHA)
            upgrade_data.fill((0, 0, 0, 128))
            self.win.blit(upgrade_data, (835, 500))

            Initial = pygame.font.Font(arial, 20)
            Initial_text = Initial.render("Initial level = 0", True, WHITE)
            self.win.blit(Initial_text, (840, 505))

            Max = pygame.font.Font(arial, 20)
            Max_text = Max.render("Max level = 3", True, WHITE)
            self.win.blit(Max_text, (840, 525))

            Cost = pygame.font.Font(arial, 20)
            Cost_text = Cost.render("Cost = 100,150,200", True, WHITE)
            self.win.blit(Cost_text, (840, 545))

            Upgrade_mul = pygame.font.Font(arial, 20)
            Upgrade_mul_text = Upgrade_mul.render(
                "power and hp * 1.15", True, WHITE)
            self.win.blit(Upgrade_mul_text, (840, 565))

    def draw_menu(self, menu):
        self.win.blit(menu.image, menu.rect)
        for btn in menu.buttons:
            self.win.blit(btn.image, btn.rect)

    def draw_attack_en(self, en_group):
        for en in en_group:
            if en.attack_light == 1:
                AL = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
                AL.fill(WHITE)
                self.win.blit(AL, (0, 0))

    def draw_attack_he(self, he_group, en_group, en_tower_hp):
        for he in he_group:
            if he.attack_light == 1:
                he.draw_atk_counter = 0
            if he.draw_atk_counter <= 4 and en_group:
                self.win.blit(he.attack_image,
                              (en_group[0].rect.x+20, en_group[0].rect.y-20))
                he.draw_atk_counter += 1
            elif he.draw_atk_counter <= 4 and en_tower_hp > 0:
                self.win.blit(he.attack_image, (he.rect.centerx -
                                                he.attack_location_x, he.rect.centery))
                he.draw_atk_counter += 1
            else:
                he.draw_atk_counter = 100

    def draw_money(self, money: int):
        self.win.blit(MONEY_IMAGE, (15, 32))
        Money = pygame.font.Font(arial, 40)
        Money_text = Money.render(f"{money}", True, WHITE)
        self.win.blit(Money_text, (120, 40))

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

    def draw_game_over(self):
        transparent_surface = pygame.Surface(
            self.win.get_size(), pygame.SRCALPHA)
        transparency = 180
        pygame.draw.rect(transparent_surface,
                         (0, 0, 0, transparency), [0, 0, 1024, 600], 0)
        over = pygame.font.Font(arial, 30)
        game_over_text = over.render("click to continue...", True, WHITE)
        self.win.blit(transparent_surface, (0, 0))
        self.win.blit(game_over_text, (830, 560))
        self.win.blit(game_loss_image, (312, 100))

    def draw_game_win(self):
        transparent_surface = pygame.Surface(
            self.win.get_size(), pygame.SRCALPHA)
        transparency = 180
        pygame.draw.rect(transparent_surface,
                         (0, 0, 0, transparency), [0, 0, 1024, 600], 0)
        over = pygame.font.Font(arial, 30)
        game_win_text = over.render("click to continue...", True, WHITE)
        self.win.blit(transparent_surface, (0, 0))
        self.win.blit(game_win_text, (830, 560))
        self.win.blit(game_win_image, (212, 20))

    def draw_skill_animation(self):
        x1, y1 = self.skill_move_path[self.path_index]
        x2, y2 = self.skill_move_path[self.path_index + 1]
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        max_count = int(distance / self.stride)
        # compute the unit vector
        unit_vector_x = (x2 - x1) / distance
        unit_vector_y = (y2 - y1) / distance
        # compute the movement
        delta_x = unit_vector_x * self.stride * self.move_count
        delta_y = unit_vector_y * self.stride * self.move_count
        # update the position and counter
        if self.move_count <= max_count:
            self.rect.center = (x1 + delta_x, y1 + delta_y)
            self.move_count += 1
        else:
            self.move_count = 0
            self.rect.center = self.skill_move_path[self.path_index]

        self.win.blit(self.skillimage, self.rect)

    def draw_finish_win(self):
        transparent_surface = pygame.Surface(
            self.win.get_size(), pygame.SRCALPHA)
        transparency = 180
        pygame.draw.rect(transparent_surface, (8, 46, 87,
                                               transparency), [0, 0, 1024, 600], 0)
        over = pygame.font.Font(arial, 30)
        complete = pygame.font.Font(arial, 80)
        text = pygame.font.Font(arial, 40)
        game_win_text = over.render("click to back to menu", True, WHITE)
        game_finish_text = text.render(
            "now you can try to use less time!", True, WHITE)
        congrats = complete.render("CONGRATS", True, WHITE)
        self.win.blit(transparent_surface, (0, 0))
        self.win.blit(congrats, (350, 15))
        self.win.blit(game_finish_text, (300, 100))
        self.win.blit(game_win_text, (800, 560))
        self.win.blit(game_completed_image, (262, 150))

    def draw_game_time(self, time):
        timer = pygame.font.Font(arial, 30)
        time_text = timer.render(f"Time: {time}", True, WHITE)
        self.win.blit(time_text, (WIN_WIDTH-180, WIN_HEIGHT-65))
