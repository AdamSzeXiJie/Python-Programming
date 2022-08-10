import pygame
from Score import SCORE
from attributes import *

scr = SCORE()


# Creates player
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('/Users/adams/PycharmProjects/Python/Game/nutf2.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel = 2
        self.change = 0
        self.worldshift_x = 0
        self.left_viewbox = 200
        self.right_viewbox = 300
        self.worldshift_y = 0
        self.up_viewbox = 200
        self.down_viewbox = 300
        self.resting = False
        self.gforce = 1
        self.left = False
        self.right = False
        self.pause = False

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

    # Movement of player
    def move(self):

        # To get key press
        k = pygame.key.get_pressed()

        # To move left
        if k[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.vel
            self.change = 1
            # self.left = True
            # self.right = True
            if self.collision():
                pass
            else:
                self.viewbox()

        # To move right
        if k[pygame.K_RIGHT] and self.rect.x < 458:
            self.rect.x += self.vel
            self.change = 2
            # self.left = False
            # self.right = True
            if self.collision():
                pass
            else:
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

        # To climb up
        if k[pygame.K_UP]:
            for v in vines:
                if self.rect.colliderect(v.rect):
                    self.rect.y -= self.vel

        if k[pygame.K_DOWN]:
            self.rect.y += self.vel
            self.change = 4
            if self.collision():
                pass
            else:
                self.viewbox()

        if k[pygame.K_SPACE]:
            if self.left:
                facing = -1
            else:
                facing = 1
            if len(bullets) < 1:
                bullets.append(projectile(self.rect.x, self.rect.y, 6, (0, 0, 0), facing))
