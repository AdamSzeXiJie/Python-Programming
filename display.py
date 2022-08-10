import pygame
from attributes import *

# Creates score
class SCORE():
    def __init__(self):
        self.font = pygame.font.Font(None, 30)
        self.score = 0
        self.Highscore = 0

    # Displays current score
    def current_score(self):
        self.text = self.font.render("Score: " + str(self.score), False, black, None)
        self.textRect = self.text.get_rect()
        display.blit(self.text, (380, 10))

    # Displays highscore
    def highscore(self):
        self.text1 = self.font.render("High score: " + str(self.set_highscore()), False, black, None)
        self.textRect1 = self.text.get_rect()
        display.blit(self.text1, (332, 30))

    # Sets the highscore
    def set_highscore(self):
        # Opens the text file
        f = open("score.txt", "r")

        # Read lines in text file
        file = f.readlines()
        self.Highscore = int(file[0])

        if self.Highscore < int(self.score):
            # Closes read file
            f.close()

            # Opens a write file
            file = open("score.txt", "w")

            # Sets the highscore equal to score
            file.write(str(self.score))

            # Closes the write file
            file.close()

            # Returns score
            return self.score

        # Returns highscore
        return self.Highscore

# Creates timer
class timer():
    def __init__(self):
        self.timer_started = False
        self.passed_time = 62000

    def display_timer(self):
        # Creates the attribute of the timer
        self.font = pygame.font.Font(None, 30)
        self.text = self.font.render("Time: " + str(self.passed_time), False, black, None)
        self.textRect = self.text.get_rect()
        display.blit(self.text, (20, 20))

    def time_count(self):
        # starts the timer
        if self.timer_started:
            # converts the timer from milisecond to seconds
            self.passed_time = ((60000 - (pygame.time.get_ticks() - self.start_time)) // 1000)

# This is the class for splash screen
class Splash_Screen():
    alpha = 0
    fade = pygame.Surface((display_width, display_height))
    fade.fill(black)

    # This displays our logo on screen
    def __init__(self):
        display.fill(white)
        self.image = pygame.image.load("Image\\logo.png").convert()
        self.imageRect = self.image.get_rect()
        self.imageRect.center = (display_width / 2, display_height / 2)

    # This sets the fade in animation for our logo
    def fade_in(self):
        # The for loop will change the transparency of an image
        # 0 = Transparent, 255 = opaque
        for alpha in range(0, 255):
            self.fade.set_alpha(255 - alpha)
            display.blit(self.image, self.imageRect)
            display.blit(self.fade, (0, 0))
            pygame.display.update()
            pygame.time.delay(2)

    # This sets the fade out animation for our logo
    def fade_out(self):
        # The for loop will change the transparency of an image
        # 0 = Transparent, 255 = opaque
        for alpha in range(0, 255):
            self.fade.set_alpha(alpha)
            display.blit(self.image, self.imageRect)
            display.blit(self.fade, (0, 0))
            pygame.display.update()
            pygame.time.delay(2)
