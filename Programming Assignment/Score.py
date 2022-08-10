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
