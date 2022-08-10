import pygame
from attributes import *


# Creates level
class LEVEL():
    def __init__(self):
        # Creates the level
        self.level = 0
        if self.level == 0:
            level = ["wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
                     "wC                                                    w",
                     "w    cc E     ccc                                     w",
                     "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww   w",
                     "wdddww                                                w",
                     "wdddww                                                w",
                     "wdddww                                                w",
                     "w s ww                                                w",
                     "w   ww                                                w",
                     "ws sww                                                w",
                     "w   ww                                                w",
                     "w s ww                                                w",
                     "w                                                     w",
                     "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww   w",
                     "w    w      s     ss                     ww           w",
                     "w  w      w           ss    E    EE                   w",
                     "fffffffffffffffffffffffffffffffffffffffffffffffffffffff", ]

        elif self.level == 1:
            level = ["w                                                     w",
                     "w                                                     w",
                     "w                                                     w",
                     "w                                                     w",
                     "w                                        ww           w",
                     "w                                                     w",
                     "w                                               ww    w",
                     "w              ww                        ww           w",
                     "w             eww         ww                          w",
                     "ffffffffffffffffff     ffffffffffffffffffffffffffffffff", ]

        x = y = 0
        for row in level:
            for col in row:
                if col == "f":
                    f = Floor(x, y)

                if col == "w":
                    w = Wall(x, y)

                if col == "e":
                    e = Exit(x, y)

                if col == "v":
                    v = Vine(x, y)

                if col == "c":
                    c = Coin(x, y)

                if col == "s":
                    s = Spike(x, y)

                if col == "C":
                    C = Checkpoint(x, y)

                if col == "E":
                    E = Enemy(x, y)

                if col == "d":
                    d = Diamond(x, y)

                x += 50
            y += 50
            x = 0

    def nextlevel(self):
        self.level = 0
        for e in exits:
            if player.rect.colliderect(e.rect):
                self.level += 1


# Creates floor
class Floor(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Loads the image of the floor on the display
        self.image = pygame.image.load("/Users/adams/PycharmProjects/Python/Game/floor1.png").convert()
        # Set the width, length and position of the floor
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Add the floor to the list
        floors.append(self)
        entities.add(self)


# Creates Wall
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Loads the image of the wall on the display
        self.image = pygame.image.load("/Users/adams/PycharmProjects/Python/Game/WALL.png").convert()
        # Set the width, length and position of the wall
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Add the wall to the list
        walls.append(self)
        entities.add(self)


# Creates Exit
class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Loads the image of the exit on the display
        self.image = pygame.image.load("/Users/adams/PycharmProjects/Python/Game/Door.png")
        # Set the width, length and position of the exit
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Add the exit to the list
        exits.append(self)
        entities.add(self)


# Creates Vine
class Vine(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Loads the image of the vine on the display
        self.image = pygame.image.load("/Users/adams/PycharmProjects/Python/Game/Vine.png")
        # Set the width, length and position of the vine
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Add the vine to the list
        vines.append(self)
        entities.add(self)


# Creates Coin
class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Loads the image of the coin on the display
        self.image = pygame.image.load("/Users/adams/PycharmProjects/Python/Game/coin.png")
        # Set the width, length and position of the coin
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Add the coin to the list
        coins.append(self)
        entities.add(self)


# Creates Diamond
class Diamond(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Loads the image of the diamond on the display
        self.image = pygame.image.load("/Users/adams/PycharmProjects/Python/Game/DIAMOND.png")
        # Set the width, length and position of the diamond
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Add the diamond to the list
        diamonds.append(self)
        entities.add(self)


# Creates Spike
class Spike(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Loads the image of the spike on the display
        self.image = pygame.image.load("/Users/adams/PycharmProjects/Python/Game/spike.png")
        # Set the width, length and position of the spike
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Add the spike to the list
        spikes.append(self)
        entities.add(self)


# Creates Checkpoint
class Checkpoint(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Loads the image of the checkpoint on the display
        self.image = pygame.image.load("/Users/adams/PycharmProjects/Python/Game/checkpoint.png")
        # Set the width, length and position of the checkpoint
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Add the checkpoint to the list
        checkpoints.append(self)
        entities.add(self)


# Creates Enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Loads the image of the enemy on the display
        self.image = pygame.image.load("/Users/adams/PycharmProjects/Python/Game/enemy.png")
        # Set the width, length and position of the enemy
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Add the enemy to the list
        enemies.append(self)
        entities.add(self)
