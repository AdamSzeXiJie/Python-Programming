import pygame
from attributes import *
from display import SCORE, timer

scr = SCORE()
t = timer()

# Creates level
class LEVEL():
    def __init__(self):
        # Creates the level
        self.level = 0
        if self.level == 0:
            level = [
                "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
                "w                                                                                                  w",
                "w                                                                                                  w",
                "w                                            dd                                                    w",
                "w                   c        cc          c        cc                                          dddddw",
                "w                  www       ww         www       ww   ww                    dd               wwwwww",
                "w                                                         ddd          cc            cc            w",
                "w          dd                                             www         wwww          wwww           w",
                "w          ww                              ccccc                                                   w",
                "w                                          wwwww    ww    dd                                       w",
                "we                                                       wwwww                                     w",
                "wwwwwwwwwww                                                           wwwwwwwwwwwwwwww    wwwww    w",
                "w                                                                                    w      w      w",
                "w                                                                                    www    w    www",
                "w                                                                                    w      w      w",
                "w                                                                                    w    wwwww    w",
                "w                                                                                    w      w      w",
                "w            s       s                       www                                     www    w    www",
                "w                                s                               s           s       w      w   dddw",
                "w         E    cccc     E   cccc s cccc   EE      ss  ww  E      s       E   s   E        wwwww dddw",
                "w     wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
                "w                                                                                                  w",
                "wwww                                                                                               w",
                "wwwwwwwwwww                                                                       dd               w",
                "wddd     ss  www   ccccc                                                    ccccc ww               w",
                "wddd               wwwww                                                    wwwww    wc            w",
                "wddd s                   ww        E                 E                E     wwwwwssssww            w",
                "wwwwwwwwwwwwwwsswwwwwwwwwwwwsswwwwwwwwsswwsswwwwwsswwwwwwwwwssswwwwwwwwwwwwwwwwwwwwwwwwwwwww       w",
                "w     s      d         sss                           ddd       s                           wwww    w",
                "wC        c     c                                                                          wsss  www",
                "w    ccc     E                     cccccccccdcccccccc      E   d   E                            wwww",
                "ffffffffffffffffffffffffffffffffsssffffffffffffffffffsssffffffffffffffffffffffffffffffffffffffffffff", ]

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


# Creates floor
class Floor(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Loads the image of the floor on the display
        self.image = pygame.image.load("Image\\floor1.png").convert()
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
        self.image = pygame.image.load("Image\\WALL.png").convert()
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
        self.image = pygame.image.load("Image\\Door.png")
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
        self.image = pygame.image.load("Image\\Vine.png")
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
        self.image = pygame.image.load("Image\\coin.png")
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
        self.image = pygame.image.load("Image\\DIAMOND.png")
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
        self.image = pygame.image.load("Image\\SPIKE.png")
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
        self.image = pygame.image.load("Image\\checkpoint.png")
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
        self.image = pygame.image.load("Image\\enemy.png")
        # Set the width, length and position of the enemy
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Add the enemy to the list
        enemies.append(self)
        entities.add(self)


# Creates endscreen
class endscreen():
    def Surface(self):
        self.surface = pygame.Surface((500, 500))
        self.surface.fill((255, 255, 255))
        display.blit(self.surface, (0, 0))

    # Creates end text
    def end_text(self):
        # Displays "TIMES OUT"
        self.font = pygame.font.Font(None, 70)
        self.text = self.font.render("TIMES OUT", False, (0, 0, 0), None)
        display.blit(self.text, (130, 100))

        # Creates score and highscore
        self.font1 = pygame.font.Font(None, 50)
        self.text1 = self.font1.render("Score: " + str(scr.score), False, (0, 0, 0), None)
        self.text2 = self.font1.render("High score: " + str(scr.set_highscore()), False, (0, 0, 0), None)
        display.blit(self.text1, (150, 250))
        display.blit(self.text2, (150, 300))

    def display_endscreen(self):
        # Check if timer is less than 0
        if t.passed_time < 0:
            self.Surface()
            self.end_text()

# Creates player
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Image\\nutf2.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel = 5
        self.change = 0
        self.worldshift_x = 0
        self.left_viewbox = 200
        self.right_viewbox = 300
        self.worldshift_y = 0
        self.up_viewbox = 200
        self.down_viewbox = 300
        self.resting = False
        self.i = 0

    # Shifts the object
    def shift_world(self, shift_x, shift_y):
        # Shifts the object on the x-axis
        self.worldshift_x += shift_x
        for f in floors:
            f.rect.x += shift_x

        for w in walls:
            w.rect.x += shift_x

        for e in exits:
            e.rect.x += shift_x

        for v in vines:
            v.rect.x += shift_x

        for c in coins:
            c.rect.x += shift_x

        for s in spikes:
            s.rect.x += shift_x

        for C in checkpoints:
            C.rect.x += shift_x

        for E in enemies:
            E.rect.x += shift_x

        for d in diamonds:
            d.rect.x += shift_x

        # Shifts the object on the y-axis
        self.worldshift_y += shift_y
        for f in floors:
            f.rect.y += shift_y

        for w in walls:
            w.rect.y += shift_y

        for e in exits:
            e.rect.y += shift_y

        for v in vines:
            v.rect.y += shift_y

        for c in coins:
            c.rect.y += shift_y

        for s in spikes:
            s.rect.y += shift_y

        for C in checkpoints:
            C.rect.y += shift_y

        for E in enemies:
            E.rect.y += shift_y

        for d in diamonds:
            d.rect.y += shift_y

    # Viewbox of the player
    def viewbox(self):

        # Moves the viewbox to the left when player move left
        if self.rect.x <= self.left_viewbox:
            view_difference = self.left_viewbox - self.rect.x
            self.rect.x = self.left_viewbox
            self.shift_world(view_difference, 0)

        # Moves the viewbox to the right when player move right
        if self.rect.x >= self.right_viewbox:
            view_difference = self.right_viewbox - self.rect.x
            self.rect.x = self.right_viewbox
            self.shift_world(view_difference, 0)

        # Moves the viewbox to the up when player move up
        if self.rect.y <= self.up_viewbox:
            view_difference = self.up_viewbox - self.rect.y
            self.rect.y = self.up_viewbox
            self.shift_world(0, view_difference)

        # Moves the viewbox to the down when player move down
        if self.rect.y >= self.down_viewbox:
            view_difference = self.down_viewbox - self.rect.y
            self.rect.y = self.down_viewbox
            self.shift_world(0, view_difference)

    # Collision checker
    def collision(self):

        # To check for collision for the player with walls
        for w in walls:

            # If player collided with wall
            if self.rect.colliderect(w.rect):

                if self.change == 2:
                    # Moving right; Hit the left side of the wall
                    self.rect.right = w.rect.left

                if self.change == 1:
                    # Moving left; Hit the right side of the wall
                    self.rect.left = w.rect.right

                if self.change == 3:
                    # Moving up; Hit the bottom side of the wall
                    self.rect.top = w.rect.bottom

                if self.change == 4:
                    self.resting = True
                    # Moving down; Hit the top side of the wall
                    self.rect.bottom = w.rect.top

        # To check for collision for the player with floors
        for f in floors:

            # If player collided with floor
            if self.rect.colliderect(f.rect):

                if self.change == 2:
                    # Moving right; Hit the left side of the floor
                    self.rect.right = f.rect.left

                if self.change == 1:
                    # Moving left; Hit the right side of the floor
                    self.rect.left = f.rect.right

                if self.change == 3:
                    # Moving up; Hit the bottom side of the floor
                    self.rect.top = f.rect.bottom

                if self.change == 4:
                    self.resting = True
                    # Moving down; Hit the top side of the floor
                    self.rect.bottom = f.rect.top

        for e in exits:
            if self.rect.colliderect(e.rect):
                lvl.level = 1

        # To check for collision for the player with coin
        for c in coins:

            # If player collided with the coin
            if self.rect.colliderect(c.rect):
                # Plays sound effect
                Pick.play()

                # Remove coin from the list
                coins.remove(c)
                entities.remove(c)

                # Increment score by 1
                scr.score += 1

        for d in diamonds:

            # If player collided with the coin
            if self.rect.colliderect(d.rect):
                # Plays sound effect
                Pick.play()

                # Remove diamond from the list
                diamonds.remove(d)
                entities.remove(d)

                # Increment score by 5
                scr.score += 5

        # To check for collision for the player with spike
        for s in spikes:

            # If player collided with spike
            if self.rect.colliderect(s.rect):

                # Play Sound effect
                Hurt.play()

                # Decrement score by 10
                scr.score -= 10

                # Move the player back to checkpoint
                for C in checkpoints:
                    self.rect.x = C.rect.x
                    self.rect.y = C.rect.y

        # To check for collision for the player with enenies
        for E in enemies:

            # If player collided with enemies
            if self.rect.colliderect(E.rect):

                # Play Sound effect
                Hurt.play()

                # Decrement score by 10
                scr.score -= 10

                # Move the player back to checkpoint
                for C in checkpoints:
                    self.rect.x = C.rect.x
                    self.rect.y = C.rect.y

    # Creates gravity
    def gravity(self):
        self.rect.y += 2
        self.change = 4
        self.collision()
        self.viewbox()

    # Movement of player
    def move(self):

        # To get key press
        k = pygame.key.get_pressed()

        # To move left
        if k[pygame.K_LEFT]:
            self.rect.x -= self.vel
            self.change = 1
            self.collision()
            self.viewbox()

        # To move right
        if k[pygame.K_RIGHT]:
            self.rect.x += self.vel
            self.change = 2
            self.collision()
            self.viewbox()

        # To jump
        if self.resting and k[pygame.K_UP]:
            jumpsound.play()
            self.resting = False
            self.change = 3
            while self.i < 150:
                self.rect.y -= 1
                self.i += 1
            self.i = 0
            self.collision()
            self.viewbox()

        if k[pygame.K_ESCAPE]:
            pygame.quit()
            quit()

        # Gravity
        self.gravity()
