import pygame

#This initaites pygame window
pygame.init()

#This sets the windows size
display_width = 500
display_height = 500
display = pygame.display.set_mode((display_height, display_width))

#This is the RGB for easy access
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Loads the background of the game
bg = pygame.image.load("bg1.jpeg").convert()

# This loads the intro song
intro_song = pygame.mixer.music.load('Intro_Song.mp3')

# Sound effects
jumpsound = pygame.mixer.Sound('jump.wav')
Pick = pygame.mixer.Sound('coin.wav')
Hurt = pygame.mixer.Sound('Hurt.wav')

# Lists of sprites
entities = pygame.sprite.Group()
floors = []
walls = []
exits = []
vines = []
bullets = []
coins = []
spikes = []
checkpoints = []
enemies = []
diamonds = []
