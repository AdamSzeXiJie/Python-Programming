import pygame
from attributes import *


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
