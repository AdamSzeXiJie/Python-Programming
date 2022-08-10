import pygame
from attributes import *
from levels import *


player = Player(50, 1500)
end = endscreen()
entities.add(player)

# This is the class for the starting screen
class intro():
    # This displays the title of our game
    def Game_Title(self):
        self.INTRO = True
        while self.INTRO:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.bg = pygame.image.load("Image\\background.png")
            self.bgRect = self.bg.get_rect()
            self.bgRect.center = (500 / 2, 500 / 2)
            self.title = pygame.image.load("Image\\Title.png")
            self.titleRect = self.title.get_rect()
            self.titleRect.center = (500 / 2, 500 - 380)
            display.blit(self.bg, self.bgRect)
            display.blit(self.title, self.titleRect)
            self.text_in_button()
            self.button()
            pygame.display.update()

    # Creates buttons
    def button(self):
        # Creates two buttons
        self.button1 = pygame.Surface((100, 50))
        self.button1.fill(green)
        self.button2 = pygame.Surface((100, 50))
        self.button2.fill(red)
        self.button3 = pygame.Surface((200, 50))
        self.button3.fill(blue)

        # Display it on the screen
        display.blit(self.button1, (100, 400))
        display.blit(self.button2, (300, 400))
        display.blit(self.button3, (160, 300))
        self.text_in_button()
        pygame.display.update()

        # This gets the mouse position
        p = pygame.mouse.get_pos()

        # Check if the mouse button is clicked
        click = pygame.mouse.get_pressed()

        # Check if the position of the mouse is within the given range
        if 200 > p[0] > 100 and 450 > p[1] > 400:
            self.button1.fill((0, 139, 0))
            display.blit(self.button1, (100, 400))
            self.text_in_button()
            pygame.display.update()

            # Checks if the left mouse button is pressed
            if click[0] == 1:
                self.INTRO = False

                # Start timer
                t.timer_started = True
                t.start_time = pygame.time.get_ticks()

                # This stops the intro song
                pygame.mixer.music.stop()

                # This loads the level song
                song = pygame.mixer.music.load("Sound\\Level_Song.mp3")

                # This plays the level song
                pygame.mixer.music.play(-1)

                # This is the main loop
                while True:
                    for event in pygame.event.get():
                        # If the user click "X", it will quit the game
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()

                    t.time_count()
                    display.blit(bg, (0, 0))
                    entities.draw(display)
                    player.move()
                    scr.current_score()
                    scr.highscore()
                    t.display_timer()
                    end.display_endscreen()
                    pygame.display.update()

        elif 400 > p[0] > 300 and 450 > p[1] > 400:
            self.button2.fill((139, 0, 0))
            display.blit(self.button2, (300, 400))
            self.text_in_button()
            pygame.display.update()

            # This checks if the left mouse button is pressed
            if click[0] == 1:
                pygame.quit()
                quit()

        elif 360 > p[0] > 160 and 350 > p[1] > 300:
            self.button3.fill((0, 0, 139))
            display.blit(self.button3, (160, 300))
            self.text_in_button()
            self.instructions()
            pygame.display.update()

    # Display text in button
    def text_in_button(self):
        self.font = pygame.font.Font(None, 50)
        self.text = self.font.render("Start", False, black, None)
        self.text1 = self.font.render("Quit", False, black, None)
        self.text2 = self.font.render("Instruction", False, black, None)
        display.blit(self.text, (110, 410))
        display.blit(self.text1, (315, 410))
        display.blit(self.text2, (167, 307))
        
    def instructions(self):
        self.image = instruction
        display.blit(self.image, (50, 200))
