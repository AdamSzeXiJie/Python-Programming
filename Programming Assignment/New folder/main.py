import time
import pygame
from Intro import intro
from display import Splash_Screen
from levels import (
    LEVEL,
    Enemy,
    Coin,
    Checkpoint,
    Spike,
    Diamond,
    Floor,
    Wall,
    Exit,
    Vine)


def main():
    
    # This initaites pygame window
    pygame.init()

    # This sets the caption for the window
    pygame.display.set_caption("The adventure of Chestnut")

    # This sets the fps of the game
    Clock = pygame.time.Clock()

    LOGO = Splash_Screen()
    START = intro()
    lvl = LEVEL()

    # Executes the logo fade in and out effect with a 2 second delay in between
    LOGO.fade_in()
    time.sleep(2)
    LOGO.fade_out()

    # This plays the intro song in a loop
    pygame.mixer.music.play(-1)
    
    # Displays starting screen
    START.Game_Title()

    # The fps of the game is set at 60 frames per second
    Clock.tick(60)

if __name__ == '__main__':
    main()
