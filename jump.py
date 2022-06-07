
from math import fabs
from platform import platform
from tkinter.tix import Tree
import pygame
import os
import random
import time


class Setting:
    window_width = 750
    window_height = 900
    frames = 60
    path_file = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(path_file, "Images")
    sound_path = os.path.join(path_file, "Sounds")
    score = "score.txt"
    title = "Spiel mit Sprung"
    jump_speed = 0
    punkte = 0
    gravity = 0.2
    upscroll = False
    hit = False
    loose = False
    count_plat = 0
    max_plat = 25
    scale_x = 125
    scale_y = 15
    play_music = True
    score = 0
    highscore = 0





class Button:
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(
                self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(
                self.text_input, True, self.base_color)


class Background:
    def __init__(self, filename="background.png") -> None:
        super().__init__()
        self.image = pygame.image.load(os.path.join(
            Setting.image_path, filename)).convert()
        self.image = pygame.transform.scale(
            self.image, (Setting.window_width, Setting.window_height))

    def draw(self, screen):
        screen.blit(self.image, (0, 0))

    def update(self):
        pass


class First_Plat(pygame.sprite.Sprite):
    def __init__(self, picturefile) -> None:
        super().__init__()
        self.image = pygame.image.load(os.path.join(
            Setting.image_path, picturefile)).convert_alpha()
        self.scalex = Setting.scale_x
        self.scaley = Setting.scale_y
        self.image = pygame.transform.scale(
            self.image, (self.scalex, self.scaley))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx = Setting.window_width//2
        self.rect.centery = Setting.window_height

    def update(self):

        if Setting.upscroll == True:
            if Setting.jump_speed <= 0:
                self.rect.centery += Setting.jump_speed*-1
        if self.rect.top >= Setting.window_height:
            self.kill()
            Setting.punkte += 1
            Setting.count_plat += 1
        if Setting.loose == True:
            self.kill()
            Setting.count_plat -= 1


class Movingp(pygame.sprite.Sprite):
    def __init__(self, picturefile) -> None:
        super().__init__()
        self.image = pygame.image.load(os.path.join(
            Setting.image_path, picturefile)).convert_alpha()
        self.scalex = Setting.scale_x
        self.scaley = Setting.scale_y
        self.imageindex = 0
        self.image = pygame.transform.scale(
            self.image, (self.scalex, self.scaley))
        self.rect = self.image.get_rect()
        self.xspeed = 1 or -1
        self.xmove = self.xspeed
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx = random.randint(10, Setting.window_width - 10)
        self.rect.centery = random.randint(10, Setting.window_height / 1.5)

    def update(self):

        if self.rect.right == Setting.window_width:
            self.xmove = self.xspeed * -1
        if self.rect.left == 0:
            self.xmove = self.xspeed * 1

        if Setting.upscroll == True:
            if Setting.jump_speed <= 0:
                self.rect.centery += Setting.jump_speed*-1
        self.rect.move_ip((self.xmove, 0))
        if self.rect.top >= Setting.window_height:
            self.kill()
            Setting.punkte += 1
            Setting.count_plat -= 1
        if Setting.loose == True:
            self.kill()
            Setting.count_plat -= 1


class Plattform(pygame.sprite.Sprite):
    def __init__(self, picturefile) -> None:
        super().__init__()
        self.image = pygame.image.load(os.path.join(
            Setting.image_path, picturefile)).convert_alpha()
        self.scalex = Setting.scale_x
        self.scaley = Setting.scale_y
        self.imageindex = 0
        self.image = pygame.transform.scale(
            self.image, (self.scalex, self.scaley))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx = random.randint(10, Setting.window_width - 10)
        self.rect.centery = random.randint(10, Setting.window_height / 1.5)

    def update(self):
        if Setting.upscroll == True:
            if Setting.jump_speed <= 0:
                self.rect.centery += Setting.jump_speed*-1
        if self.rect.top >= Setting.window_height:
            self.kill()
            Setting.punkte += 1
            Setting.count_plat -= 1
        if Setting.loose == True:
            self.kill()
            Setting.count_plat -= 1


class BreakingPlat(pygame.sprite.Sprite):
    def __init__(self, picturefile) -> None:
        super().__init__()
        self.image = pygame.image.load(os.path.join(
            Setting.image_path, picturefile)).convert_alpha()
        self.scalex = Setting.scale_x
        self.scaley = Setting.scale_y
        self.imageindex = 0
        self.image = pygame.transform.scale(
            self.image, (self.scalex, self.scaley))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx = random.randint(10, Setting.window_width - 10)
        self.rect.centery = random.randint(10, Setting.window_height / 1.5)

    def update(self):
        if Setting.upscroll == True:
            if Setting.jump_speed <= 0:
                self.rect.centery += Setting.jump_speed*-1
        if self.rect.top >= Setting.window_height:
            self.kill()
            Setting.punkte += 1
            Setting.count_plat -= 1
        if Setting.loose == True:
            self.kill()
            Setting.count_plat -= 1


class BreakingPlat_move(pygame.sprite.Sprite):
    def __init__(self, picturefile) -> None:
        super().__init__()
        self.image = pygame.image.load(os.path.join(
            Setting.image_path, picturefile)).convert_alpha()
        self.scalex = Setting.scale_x
        self.scaley = Setting.scale_y
        self.imageindex = 0
        self.image = pygame.transform.scale(
            self.image, (self.scalex, self.scaley))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx = random.randint(10, Setting.window_width - 10)
        self.rect.centery = random.randint(10, Setting.window_height / 1.5)
        self.xspeed = 1 or -1
        self.xmove = self.xspeed

    def update(self):
        if self.rect.right == Setting.window_width:
            self.xmove = self.xspeed * -1
        if self.rect.left == 0:
            self.xmove = self.xspeed * 1

        if Setting.upscroll == True:
            if Setting.jump_speed <= 0:
                self.rect.centery += Setting.jump_speed*-1
        self.rect.move_ip((self.xmove, 0))
        if self.rect.top >= Setting.window_height:
            self.kill()
            Setting.punkte += 1
            Setting.count_plat -= 1
        if Setting.loose == True:
            self.kill()
            Setting.count_plat -= 1


class Spieler(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image_org = pygame.image.load(os.path.join(
            Setting.image_path, "jumper.png")).convert_alpha()
        self.image = self.image_org
        self.rect = self.image.get_rect()
        self.radius = self.rect.width // 2
        self.imageindex = 0
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx = Setting.window_width // 2
        self.rect.centery = Setting.window_height // 2
        self.speed = 0
        self.x_movement = 0

    def update(self):

        if Setting.hit == False:
            Setting.jump_speed += Setting.gravity
        if Setting.hit == True:
            Setting.jump_speed = -13
            Setting.hit = False
        if self.rect.left >= Setting.window_width:
            self.rect.centerx = 0
        if self.rect.right < 0:
            self.rect.centerx = Setting.window_width
        self.rect.move_ip((self.x_movement, Setting.jump_speed))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def left(self):
        self.x_movement = -5
        self.image = pygame.transform.flip(self.image_org, True, False)

    def right(self):
        self.x_movement = 5
        self.image = self.image_org

    def check_pos(self):
        if self.rect.top <= 0:
            Setting.upscroll = True
        else:
            Setting.upscroll = False

    def loose(self):
        if self.rect.top >= Setting.window_height:
            Setting.loose = True


class Game(object):
    def __init__(self) -> None:
        super().__init__()
        os.environ['SDL_VIDEO_WINDOW_POS'] = "50,30"

        pygame.init()
        pygame.display.set_caption(Setting.title)
        self.screen = pygame.display.set_mode(
            (Setting.window_width, Setting.window_height))
        self.clock = pygame.time.Clock()
        self.running = False
        self.counter = 0
        self.duration = 120
        self.spieler = Spieler()
        self.first = pygame.sprite.Group()
        self.breakingp = pygame.sprite.Group()
        self.all_obstacles = pygame.sprite.Group()
        self.font = pygame.font.Font(pygame.font.get_default_font(), 24)
        self.breakingp_move = pygame.sprite.Group()
        self.all_obstacles.add(Plattform("platform.png"))
        self.sound()
        self.background = Background()
        self.score = 0

    def get_font(size):  # Returns Press-Start-2P in the desired size
        return pygame.font.Font("assets/font.ttf", size)

    def draw(self, screen):
        screen.blit(self.image, (0, 0))

    def sound(self):
        self.volume = 0.4
        self.jump_sound = pygame.mixer.Sound(
            os.path.join(Setting.sound_path, "Jump.mp3"))
        self.background_music = pygame.mixer.Sound(
            os.path.join(Setting.sound_path, "background.mp3"))
        self.background_music = pygame.mixer.Sound(
            os.path.join(Setting.sound_path, "background.mp3"))
        self.break_sound = pygame.mixer.Sound(
            os.path.join(Setting.sound_path, "break.mp3"))
        self.background_music.set_volume(self.volume)
        self.jump_sound.set_volume(self.volume)
        self.break_sound.set_volume(self.volume)
        self.background_music.play(-1)



    def mute(self):
        if Setting.play_music == False:
            self.volume = 0
            self.background_music.set_volume(self.volume)
        
    def unmute(self):
        if Setting.play_music == True:
            self.volume = 0.5
            self.background_music.set_volume(self.volume)

    def scores(self):
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

          
            self.screen.blit(self.background.image, (0, 0))
            OPTIONS_TEXT = self.font.render(
                "Highscore", True, "Black")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(
                center=(Setting.window_width/2, Setting.window_height//5))

            NOWW_TEXT = self.font.render(
                "Letzter Score", True, "Black")
            NOWW_RECT = OPTIONS_TEXT.get_rect(
                center=(Setting.window_width/2, Setting.window_height/2.5))

            SCORE_TEXT = self.font.render(
                str(Setting.highscore), True, "Black")
            SCORE_RECT = SCORE_TEXT.get_rect(
                center=(Setting.window_width/2, Setting.window_height//4))

            NOW_TEXT = self.font.render(str(Setting.punkte), True, "Black")
            NOW_RECT = SCORE_TEXT.get_rect(
                center=(Setting.window_width/2, Setting.window_height//2))

            OPTIONS_BACK = Button(image=None, pos=(640, 850),
                                  text_input="BACK", font=self.font, base_color="Black", hovering_color="Green")

            PLAY = Button(image=None, pos=(Setting.window_width/2, 850),
                          text_input="PLAY", font=self.font, base_color="Black", hovering_color="Green")

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(self.screen)
            PLAY.changeColor(OPTIONS_MOUSE_POS)
            PLAY.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.run()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        self.main_menu()
                    if PLAY.checkForInput(OPTIONS_MOUSE_POS):
                        self.run()
                        break

            self.screen.blit(OPTIONS_TEXT, OPTIONS_RECT)
            self.screen.blit(SCORE_TEXT, SCORE_RECT)
            self.screen.blit(NOWW_TEXT, NOWW_RECT)
            self.screen.blit(NOW_TEXT, NOW_RECT)
            pygame.display.flip()

            pygame.display.update()

    def main_menu(self):
        while True:
          

            self.screen.blit(self.background.image, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = self.font.render("MAIN MENU", True, "Black")
            MENU_RECT = MENU_TEXT.get_rect(
                center=(Setting.window_width // 2, 100))

            PLAY_BUTTON = Button(image=None, pos=(Setting.window_width // 2, 250),
                                 text_input="Play", font=self.font, base_color="Black", hovering_color="White")
            OPTIONS_BUTTON = Button(image=None, pos=(Setting.window_width // 2, 400),
                                    text_input="Score", font=self.font, base_color="Black", hovering_color="White")
            QUIT_BUTTON = Button(image=None, pos=(Setting.window_width // 2, 550),
                                 text_input="Quit", font=self.font, base_color="Black", hovering_color="White")
            if Setting.play_music == True:
                VOLUME_BUTTON = Button(image=pygame.image.load(os.path.join(
                    Setting.image_path, "play.png")), pos=(Setting.window_width // 2, 800),
                    text_input="-", font=self.font, base_color="Black", hovering_color="Green")
            if Setting.play_music == False:
                VOLUME_BUTTON = Button(image=pygame.image.load(os.path.join(
                    Setting.image_path, "mute.png")), pos=(Setting.window_width // 2, 800),
                    text_input="-", font=self.font, base_color="Black", hovering_color="Green")

            self.screen.blit(MENU_TEXT, MENU_RECT)

            for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON, VOLUME_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.screen)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.run()

                    if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.scores()
                    if VOLUME_BUTTON.checkForInput(MENU_MOUSE_POS):
                        if Setting.play_music == True:
                            Setting.play_music = False
                            self.mute() 

                            pygame.mixer.music.pause()
                        elif Setting.play_music == False:
                            Setting.play_music = True
                            self.unmute()

                            pygame.mixer.music.unpause()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()

            pygame.display.update()
            pygame.display.flip()

    def groupcollide(self):
        if pygame.sprite.spritecollide(self.spieler, self.all_obstacles, False):
            Setting.hit = True
            self.jump_sound.play()
        elif pygame.sprite.spritecollide(self.spieler, self.first, False):
            Setting.hit = True
            self.jump_sound.play()
        elif pygame.sprite.spritecollide(self.spieler, self.breakingp, True):
            Setting.hit = True
            self.break_sound.play()
        elif pygame.sprite.spritecollide(self.spieler, self.breakingp_move, True):
            Setting.hit = True
            self.break_sound.play()
        else:
            Setting.hit = False

    def reset(self):
        self.spieler.rect.x = Setting.window_width // 2
        self.spieler.rect.y = Setting.window_height // 2
        Setting.jump_speed = 0
        self.spieler.x_movement = 0
        self.screen.blit(self.background.image, (0, 0))
        Setting.loose = False
        self.all_obstacles.empty()
        self.breakingp_move.empty()
        self.breakingp.empty()
        self.first.add(First_Plat("platform.png"))
        Setting.count_plat =  0
        self.running= True

    def highscore(self):
        if Setting.punkte >= Setting.highscore:
            Setting.highscore = Setting.punkte  
        else:
            pass

    def read_score(self):
        self.file = open("score.txt", "r")
        self.read = self.file.read()
        Setting.highscore = int(self.read)
        self.file.close()
        return self.score

    def write_score(self):
        self.file = open("score.txt", "w")
        if Setting.score > Setting.highscore:

            self.file.write(str(Setting.score))
            self.file.close()
        else:
            self.file.close()

    def run(self):
        self.reset()
        Setting.punkte = 0
        self.screen.blit(self.background.image, (0, 0))
        
        while self.running:
            self.clock.tick(Setting.frames)

            # Eventverarbeitung
            self.watch_for_events()
            # Update
            self.all_obstacles.update()
            self.spieler.update()
            self.first.update()
            self.breakingp.update()
            self.breakingp_move.update()

            # Bildschirmausgabe
            self.background.draw(self.screen)
            self.all_obstacles.draw(self.screen)
            self.spieler.draw(self.screen)
            self.first.draw(self.screen)
            self.breakingp.draw(self.screen)
            self.breakingp_move.draw(self.screen)
            text_surface_modus = self.font.render(
                "Punktzahl: {0}".format(Setting.punkte), True, (0, 0, 0))
            self.screen.blit(text_surface_modus, dest=(
                10, Setting.window_height-900))

            self.groupcollide()
            self.more()
            self.spieler.check_pos()
            self.spieler.loose()
            self.end()
            self.mute()
            self.unmute()
            pygame.display.flip()

    def watch_for_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif self.running == True:
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_LEFT:
                        self.spieler.left()
                    elif event.key == pygame.K_RIGHT:
                        self.spieler.right()

    def end(self):
        if Setting.loose == True:
            self.highscore()
            #self.write_score()
            self.scores()

    def more(self):
        self.spawnrate = 5
        self.counter += 1
        if self.counter >= self.duration:
            if Setting.count_plat <= Setting.max_plat:
                if Setting.punkte >= 15:
                    for i in range(1):
                        
                        if Setting.punkte >= 15:
                            self.all_obstacles.add(Movingp("platform_move.png"))
                            Setting.count_plat += 1
                            self.counter = 0
                        if Setting.punkte >= 30:
                            self.breakingp.add(BreakingPlat("platform_break.png"))
                            Setting.count_plat += 1
                            self.counter = 0
                        if Setting.punkte >= 40:
                            self.breakingp_move.add(BreakingPlat_move("platform_break_move.png"))
                            Setting.count_plat += 1
                            self.counter = 0
                         
                
                
                else:
                    for i in range(2):
                        self.all_obstacles.add(Plattform("platform.png"))
                        self.counter = 0
                        Setting.count_plat += 1


if __name__ == "__main__":
    game = Game()
    game.main_menu()

################################

                #       #

            #               #
            ###############



#################################
# Menu with help from yt https://www.youtube.com/watch?v=GMBqjxcKogA&ab_channel=BaralTech
# Jumper Graphic from https://favpng.com/png_view/doodle-vector-doodle-jump-kinect-video-game-iphone-png/UVAWVSjC
# Jump Sound https://www.youtube.com/watch?v=cxPQ2vk-oDk&ab_channel=LatifKhan
# Breaking Sound https://www.youtube.com/watch?v=5kdSouOn09M&ab_channel=Music%26SoundsEffectLibrary
# Hintergrundmusik https://www.youtube.com/watch?v=MF_zoKQysfI&ab_channel=AudioLibrary%E2%80%94Musicforcontentcreator

