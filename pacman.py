import pygame

import run
from GAME import red_ghost, yellow_ghost, pink_ghost, blue_ghost
from sprites import *
from run import *
from map import *

from red_ghost import *
from yellow_ghost import *
from pink_ghost import *
from blue_ghost import *


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 1
        self.image = pac_right_open
        self.direction = None
        self.last_image_change_time = pygame.time.get_ticks()
        self.size = 20
        self.image_dead = pac_dead_1
        self.lives = 3
        self.score = 0

    def get_cube(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

    def change_speed(self, speed):
        self.speed = speed

    def reset_position(self):
        self.x = 280
        self.y = 460
        self.direction = None
        self.image = pac_right_open

    def ghost_collision(self, ghosts):
        player_cube = self.get_cube().inflate(-10, -10)

        for ghost in ghosts:
            ghost_cube = ghost.get_cube().inflate(-10, -10)
            if player_cube.colliderect(ghost_cube):
                if ghost.vulnerable:
                    ghost.reset_position()

                    for ghost in ghosts:
                        if red_ghost:
                            self.score += 200
                        elif yellow_ghost:
                            self.score += 400
                        elif pink_ghost:
                            self.score += 600
                        elif blue_ghost:
                            self.score += 800
                    ghost.reset_vulnerability()

                else:
                    self.speed = 1
                    self.lives -= 1
                    pygame.mixer.stop()
                    run.music_dead()
                    return True
        return False

    def change_direction(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.direction = "LEFT"
                elif event.key == pygame.K_RIGHT:
                    self.direction = "RIGHT"
                elif event.key == pygame.K_UP:
                    self.direction = "UP"
                elif event.key == pygame.K_DOWN:
                    self.direction = "DOWN"

    def move(self):
        if self.direction == "RIGHT":
            next_position = list_tableau_number[self.y // self.size * (560 // self.size) + (self.x + self.speed + self.size - 2) // self.size]
            if next_position != -1 and next_position != "":
                self.x += self.speed

            if self.x == 540 and self.y == 280:
                self.x = 0
                self.y = 280

        elif self.direction == "LEFT":
            next_position = list_tableau_number[self.y // self.size * (560 // self.size) + (self.x - self.speed) // self.size]
            if next_position != -1 and next_position != "":
                self.x -= self.speed

            if self.x == 0 and self.y == 280:
                self.x = 540
                self.y = 280

        elif self.direction == "UP":
            next_position = list_tableau_number[(self.y - self.speed) // self.size * (560 // self.size) + self.x // self.size]
            if next_position != -1 and next_position != "":
                self.y -= self.speed

        elif self.direction == "DOWN":
            next_position = list_tableau_number[(self.y + self.speed + self.size - 2) // self.size * (560 // self.size) + self.x // self.size]
            if next_position != -1 and next_position != "":
                self.y += self.speed

    def draw(self, screen):
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - self.last_image_change_time

        if elapsed_time > 100:

            if self.direction == "RIGHT":
                if self.image == pac_right_open:
                    self.image = pac_right_closed
                else:
                    self.image = pac_right_open
                self.last_image_change_time = current_time
            elif self.direction == "LEFT":
                if self.image == pac_left_open:
                    self.image = pac_left_closed
                else:
                    self.image = pac_left_open
                self.last_image_change_time = current_time
            elif self.direction == "UP":
                if self.image == pac_up_open:
                    self.image = pac_up_closed
                else:
                    self.image = pac_up_open
                self.last_image_change_time = current_time
            elif self.direction == "DOWN":
                if self.image == pac_down_open:
                    self.image = pac_down_closed
                else:
                    self.image = pac_down_open
                self.last_image_change_time = current_time

        screen.blit(self.image, (self.x + (self.size - self.image.get_width()) // 2, self.y + (self.size - self.image.get_height()) // 2))
