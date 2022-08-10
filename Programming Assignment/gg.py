import time

import pygame

pygame.init()
pygame.time.get_ticks()

Clock = pygame.time.Clock()
display_height = 500
display_width = 500
display = pygame.display.set_mode((display_width, display_height))

bg = pygame.image.load("bg1.jpeg").convert()
jumpsound = pygame.mixer.Sound('jump.wav')
Pick = pygame.mixer.Sound('coin.wav')
Hurt = pygame.mixer.Sound('Hurt.wav')


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('nutf2.png')
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
        self.gforce = 2
        self.left = False
        self.right = False

    def shift_world(self, shift_x, shift_y):
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

    def viewbox(self):
        if player.rect.x <= self.left_viewbox:
            view_difference = self.left_viewbox - player.rect.x
            player.rect.x = self.left_viewbox
            self.shift_world(view_difference, 0)

        if player.rect.x >= self.right_viewbox:
            view_difference = self.right_viewbox - player.rect.x
            player.rect.x = self.right_viewbox
            self.shift_world(view_difference, 0)

        if player.rect.y <= self.up_viewbox:
            view_difference = self.up_viewbox - player.rect.y
            player.rect.y = self.up_viewbox
            self.shift_world(0, view_difference)

        if player.rect.y >= self.down_viewbox:
            view_difference = self.down_viewbox - player.rect.y
            player.rect.y = self.down_viewbox
            self.shift_world(0, view_difference)

    def collision(self):
        # To check for collision for the player with walls
        for w in walls:
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

        for c in coins:
            if self.rect.colliderect(c.rect):
                Pick.play()
                coins.remove(c)
                entities.remove(c)
                scr.score += 1

        for d in diamonds:
            if self.rect.colliderect(d.rect):
                Pick.play()
                diamonds.remove(d)
                entities.remove(d)
                scr.score += 5

        for s in spikes:
            if self.rect.colliderect(s.rect):
                Hurt.play()
                scr.score -= 10
                for C in checkpoints:
                    self.rect.x = C.rect.x
                    self.rect.y = C.rect.y

        for E in enemies:
            if self.rect.colliderect(E.rect):
                Hurt.play()
                scr.score -= 10
                for C in checkpoints:
                    self.rect.x = C.rect.x
                    self.rect.y = C.rect.y + 55

    def move(self):
        k = pygame.key.get_pressed()
        # To move left
        if k[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.vel
            self.change = 1
            # self.left = True
            # self.right = True
            self.collision()
            self.viewbox()

        # To move right
        if k[pygame.K_RIGHT] and self.rect.x < 458:
            self.rect.x += self.vel
            self.change = 2
            # self.left = False
            # self.right = True
            self.collision()
            self.viewbox()

        # To jump
        if self.resting and k[pygame.K_UP]:
            jumpsound.play()
            self.rect.y -= 100
            self.resting = False
            self.change = 3
            self.collision()
            self.viewbox()

        # Gravity
        self.rect.y += 2
        self.change = 4
        self.collision()
        self.viewbox()


        if k[pygame.K_DOWN]:
            self.rect.y += self.vel
            self.change = 4
            self.collision()
            self.viewbox()

        if k[pygame.K_p]:
            P.pause = True
            P.paused()


class projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 2 * facing

    def draw_bullet(self):
        pygame.draw.circle(display, self.color, (self.x, self.y), self.radius, 0)

    def bullet(self):
        for bullet in bullets:
            if self.x < 500 and self.x > 0:
                self.x += self.vel

            else:
                bullets.pop(bullet)

    def bullet_collision(self):
        for w in walls:
            if self.rect.colliderect(w.rect):
                bullets.pop(self)

        for f in floors:
            if self.rect.colliderect(f.rect):
                bullets.pop(self)


class LEVEL():
    def __init__(self):
        # Creates the level
        self.level = 1
        if self.level == 0:
            level = [
                "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
                "wC       wwwwwww ccc       E     swwwwwww   ccccc   wwwwwwwwwwwwwws   sddddwwwwwwwwwwwwwwwdddd    sw",
                "w        wwwwwww     E ccc        wwwwwww  wwwwwww  wwwwwwwwwwwwww     ddddwwwwwwwwwwwwwwwdddds    w",
                "wwwwwww  wwwwwww  wwwwwwwwwwwwww  cc   ss  wwwwwww  wwwwwwwwwwwwww  wwwwwwwwwwwwwwwwwwwwwwwwwwwww  w",
                "wwwwwww  wwwwwww  wwwwwwwwwwwwww  ss   cc  wwwwwww     dccdwwwwwww Ewwwwwwwwwwwwwwwwwwwwwwwwwwwww  w",
                "wwwwwww  wwwwwww  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww     dccdwwwwwww  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwE w",
                "wwwwwww  wwwwwww  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww  wwwwwwwwwwwwwwwwwwwwwwwwwwwww  w",
                "w   cc      E   c    E               c     s dwwwwwwwwwwcccc   E     c       c       E     c       w",
                "w    c   cc              c   E          E    dwwwwwwwwwwcccc          E  c      E    c       E     w",
                "wwwwwwwwwwwwwwwwwwwwww wwwwwwwwwwwwww  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwws wwwwwwwwwwww Ewwwwwwwwww",
                "wwwwwwwwwwwwwwwwwwwwww wwwwwwwwwwwwww  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww  wwwwwwwwwwww  wwwwwwwwww",
                "wwwwwwwwwwwwwwwwwwwwww cccccccwwwwwww  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww  wwwwwwwwwwww  wwwwwwwwww",
                "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww swwwwwwwwwwwwE wwwwwwwwww",
                "w   E    c      c  E                    c             c        wwwwwwwwwww      c          wwwwwwwwww",
                "w   c     E      c       E    c  c                c            wwwwwwwwwww    E    c  E    wwwwwwwwww",
                "ws wwwwwwwwwwwwww Ewwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww  E       wwwwwwwwwwwwwwwww    wwwwwwwwwwwwwwww",
                "w  wwwwwwwwwwwwww  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww          wwwwww   c    w      c  c    c      w",
                "w  wwwwwwwwwwwwww  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww         Ewwwwww    w c    c     wwwwwwww     w",
                "w swwwwwwwwwwwwwwE wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww     s        c          w       wwwww    c   w",
                "w   cccccc  sssss  sssss   cccccwwwwwwwccccccccwwwwww            c     c     w        wwwww c      w",
                "w   ssssss  ccccc  ccccc   ssssswwwwwwwccEddEccwwwwww   E      wwwwwwwwwwwwwwwwww  c  wwwwwwww   www",
                "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwccccccccwwwwww          wwwwwwwwwwwwwwwwwwww   wwwwww       w",
                "wwddddddddwwwwwwwww c     E        E         c      E        c   c   wwwwwwwwww   c   wwwwwwww  c  w",
                "wwwwww wwwwwwwwwwww  E   c     E      c        E        c   E        wwwwwwwwwwwwwww  wwwwwwwww    w",
                "wwwwww wwwwwwwwwwww  wwwwwwwwwwwwwwwwwwccccccwwwwwwwwwwwwwwwwww   c   wwwwwwwwwwww    c     ww   c w",
                "wccc           s     wwwwwwwwwwwwwwwwwwccccccwwwwwwwwwwwwwwwwww   c   wwwwwwwwwwww    ww   ww    www",
                "wccc s              c      c swwwwwwwwwwwwwwwwwwwwwwwws                 w        c    ww cc   c    w",
                "wwwwwwwwwwwww  wwwwwwwwwwww   wwwwwwwwwwwwwwwwwwwwwwww    wwwwwwwwwww   w   w dd wwwwwwwwwwwwwwwwwww",
                "wwwwwwwwwwwwwddwwwwwwwwwwww   cccccccccccccccccccccccc    wwwwwwwwwwwcccccccw dd wwwwwwwwwwwwwwwwwww",
                "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww", ]

        elif self.level == 1:
            level = [
                "w                                                     w",
                "w                                                     w",
                "w                                                     w",
                "w                                                     w",
                "w                                        ww           w",
                "w                                                     w",
                "w                                               ww    w",
                "w               w                        ww           w",
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


class Floor(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Loads the image of the floor on the display
        self.image = pygame.image.load("floor1.png").convert()
        # Set the width, length and position of the floor
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Add the floor to the list
        floors.append(self)
        entities.add(self)


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Loads the image of the wall on the display
        self.image = pygame.image.load("WALL.png").convert()
        # Set the width, length and position of the wall
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Add the wall to the list
        walls.append(self)
        entities.add(self)


class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Loads the image of the wall on the display
        self.image = pygame.image.load("Door.png")
        # Set the width, length and position of the wall
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Add the wall to the list
        exits.append(self)
        entities.add(self)


class Vine(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Loads the image of the wall on the display
        self.image = pygame.image.load("Vine.png")
        # Set the width, length and position of the wall
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Add the wall to the list
        vines.append(self)
        entities.add(self)


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Loads the image of the wall on the display
        self.image = pygame.image.load("coin.png")
        # Set the width, length and position of the wall
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Add the coin to the list
        coins.append(self)
        entities.add(self)


class Diamond(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Loads the image of the diamond on the display
        self.image = pygame.image.load("DIAMOND.png")
        # Set the width, length and position of the diamond
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Add the diamond to the list
        diamonds.append(self)
        entities.add(self)


class Spike(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Loads the image of the wall on the display
        self.image = pygame.image.load("SPIKE.png")
        # Set the width, length and position of the wall
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Add the coin to the list
        spikes.append(self)
        entities.add(self)


class Checkpoint(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Loads the image of the wall on the display
        self.image = pygame.image.load("checkpoint.png")
        # Set the width, length and position of the wall
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Add the coin to the list
        checkpoints.append(self)
        entities.add(self)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Loads the image of the wall on the display
        self.image = pygame.image.load("enemy.png")
        # Set the width, length and position of the wall
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Add the coin to the list
        enemies.append(self)
        entities.add(self)


class Score():
    def __init__(self):
        self.font = pygame.font.Font(None, 30)
        self.score = 0
        self.Highscore = 0

    def current_score(self):
        self.text = self.font.render("Score: " + str(self.score), False, (0, 0, 0), None)
        display.blit(self.text, (380, 10))

    def highscore(self):
        self.text1 = self.font.render("High score: " + str(self.set_highscore()), False, (0, 0, 0), None)
        display.blit(self.text1, (332, 30))

    def set_highscore(self):
        f = open("score.txt", "r")
        file = f.readlines()
        self.Highscore = int(file[0])

        if self.Highscore < int(self.score):
            f.close()
            file = open("score.txt", "w")
            file.write(str(self.score))
            file.close()

            return self.score
        return self.Highscore


class PAUSE():
    def __init__(self):
        self.pause = True

    def p_button(self):
        self.font = pygame.font.Font(None, 100)
        self.text = self.font.render("Paused", False, (0, 0, 0), None)
        self.p_screen = pygame.Surface((500, 500))
        self.p_screen.fill((255, 255, 255))
        display.blit(self.p_screen, (0, 0))
        display.blit(self.text, (130, 200))

    def paused(self):
        while self.pause:
            k = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if k[pygame.K_p]:
                    self.pause = False

            self.p_button()


class timer():
    def __init__(self):
        self.timer_started = True
        self.passed_time = 0
        self.start_time = pygame.time.get_ticks()

    def display_timer(self):
        self.font = pygame.font.Font(None, 30)
        self.text = self.font.render("Time: " + str(self.passed_time), False, (0, 0, 0), None)
        self.textRect = self.text.get_rect()
        display.blit(self.text, (20, 20))

    def time_count(self):
        if self.timer_started:
            self.passed_time = ((60000 - (pygame.time.get_ticks() - self.start_time)) // 1000)


# Creates endscreen
class endscreen():
    def Surface(self):
        self.surface = pygame.Surface((500, 500))
        self.surface.fill((255, 255, 255))
        display.blit(self.surface, (0, 0))

    # Creates end text
    def end_text(self):
        # Displays "TIMES OUT"
        self.font = pygame.font.Font(None, 50)
        self.text = self.font.render("TIMES OUT", False, (0, 0, 0), None)
        display.blit(self.text, (155, 70))

        # Creates score and highscore
        self.font1 = pygame.font.Font(None, 50)
        self.text1 = self.font1.render("Score: " + str(scr.score), False, (0, 0, 0), None)
        self.text2 = self.font1.render("High score: " + str(scr.set_highscore()), False, (0, 0, 0), None)
        display.blit(self.text1, (155, 150))
        display.blit(self.text2, (155, 200))

    # Creates button
    def END_BUTTON(self):
        # Creates "Play" button
        self.end_button = pygame.Surface((100, 50))
        self.end_button.fill((0, 255, 0))

        # Creates "Quit" button
        self.end_button1 = pygame.Surface((100, 50))
        self.end_button1.fill((255, 0, 0))

        # Display on the screen
        display.blit(self.end_button, (100, 400))
        display.blit(self.end_button1, (300, 400))

        # Gets the mouse position
        p = pygame.mouse.get_pos()

        # Check if the mouse button is clicked
        click = pygame.mouse.get_pressed()

        # Check if the position of the mouse is within the given range
        if 200 > p[0] > 100 and 450 > p[1] > 400:
            self.end_button.fill((0, 139, 0))
            display.blit(self.end_button, (100, 400))
            self.text_in_end_button()
            pygame.display.update()

            # Checks if the left mouse button is pressed
            if click[0] == 1:
                self.INTRO = False


        elif 400 > p[0] > 300 and 450 > p[1] > 400:
            self.end_button1.fill((139, 0, 0))
            display.blit(self.end_button1, (300, 400))
            self.text_in_end_button()
            pygame.display.update()

            # This checks if the left mouse button is pressed
            if click[0] == 1:
                pygame.quit()
                quit()

    def text_in_end_button(self):
        # Set the font size
        self.font = pygame.font.Font(None, 50)

        # Create "Play" text
        self.text = self.font.render("Play", False, (0, 0, 0), None)

        # Create "Quit" text
        self.text1 = self.font.render("Quit", False, (0, 0, 0), None)

        # Display it on the screen
        display.blit(self.text, (110, 410))
        display.blit(self.text1, (315, 410))

    def display(self):
        # Check if timer is less than 0
        if time.passed_time < 0:
            self.Surface()
            self.end_text()
            self.END_BUTTON()
            self.text_in_end_button()


entities = pygame.sprite.Group()
player = Player(50, 100)
entities.add(player)
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

lvl = LEVEL()
scr = Score()
P = PAUSE()
time = timer()
end = endscreen()

while True:
    k = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    time.time_count()
    display.blit(bg, (0, 0))
    entities.draw(display)
    player.move()
    scr.current_score()
    scr.highscore()
    time.display_timer()
    end.display()
    pygame.display.update()
