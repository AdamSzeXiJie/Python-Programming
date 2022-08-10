import pygame


#This initaites pygame window
pygame.init()

#This sets the windows size
display_width = 500
display_height = 500
display = pygame.display.set_mode((display_height, display_width), pygame.FULLSCREEN)

#This is the RGB for easy access
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Loads the background of the game
bg = pygame.image.load("Image\\bg1.jpeg").convert()

# Loads the instructions
instruction = pygame.image.load("Image\\instructions.png")

# This loads the intro song
intro_song = pygame.mixer.music.load("Sound\\Intro_Song.mp3")

# Sound effects
jumpsound = pygame.mixer.Sound("Sound\\Jump.wav")
Pick = pygame.mixer.Sound("Sound\\coin.wav")
Hurt = pygame.mixer.Sound("Sound\\Hurt.wav")

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
