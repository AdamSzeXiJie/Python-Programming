import pygame
from attributes import *


# This is the class for splash screen
class Splash_Screen():
    alpha = 0
    fade = pygame.Surface((display_width, display_height))
    fade.fill(black)

    # This displays our logo on screen
    def __init__(self):
        display.fill(white)
        self.image = pygame.image.load("/Users/adams/PycharmProjects/Python/Game/logo.png").convert()
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
