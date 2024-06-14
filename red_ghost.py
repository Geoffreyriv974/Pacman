import random

import pygame

import pacman
from map import *
from run import *
from sprites import *


class Red_Ghost:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dead_ghost_replace_x = 280
        self.dead_ghost_replace_y = 260
        self.speed = 1
        self.moving = False
        self.image = red_shadow_right_1
        self.direction = "RIGHT"
        self.last_image_change_time = pygame.time.get_ticks()
        self.size = 20
        self.vulnerable = False
        self.time_vulnerable = pygame.time.get_ticks()
        self.eat = False
        self.ghost_heye = False

    def ghost_vulnerable(self):
        self.vulnerable = True
        self.time_vulnerable = pygame.time.get_ticks() + 13000

    def reset_vulnerability(self):
        self.vulnerable = False

    def ghost_heye(self):
        self.ghost_heye = True

    def vulnerability(self):
        return self.vulnerable

    def get_cube(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

    def reset_position(self):
        self.x = 280
        self.y = 220
        self.direction = "RIGHT"
        self.eat = False
        self.vulnerable = False

    def move(self):
        if self.direction == "RIGHT":
            next_position = list_tableau_number[
                self.y // self.size * (560 // self.size) + (self.x + self.speed + self.size - 2) // self.size]
            if next_position != -1:
                self.x += self.speed
            else:
                self.direction = random.choice(["UP", "DOWN"])

            if self.x == 540 and self.y == 280:
                self.x = 0
                self.y = 280

        elif self.direction == "LEFT":
            next_position = list_tableau_number[
                self.y // self.size * (560 // self.size) + (self.x - self.speed) // self.size]
            if next_position != -1:
                self.x -= self.speed
            else:
                self.direction = random.choice(["UP", "DOWN"])

            if self.x == 0 and self.y == 280:
                self.x = 540
                self.y = 280

        elif self.direction == "UP":
            next_position = list_tableau_number[
                (self.y - self.speed) // self.size * (560 // self.size) + self.x // self.size]
            if next_position != -1:
                self.y -= self.speed
            else:
                self.direction = random.choice(["RIGHT", "LEFT"])

        elif self.direction == "DOWN":
            next_position = list_tableau_number[
                (self.y + self.speed + self.size - 2) // self.size * (560 // self.size) + self.x // self.size]
            if next_position != -1:
                self.y += self.speed
            else:
                self.direction = random.choice(["RIGHT", "LEFT"])

    def draw(self, screen):

        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - self.last_image_change_time

        if self.vulnerable:
            self.image = dead_shadow_1

            time_left = self.time_vulnerable - current_time

            if time_left < 4000:
                if elapsed_time > 500:
                    if self.image == dead_shadow_1:
                        self.image = dead_shadow_3
                    elif self.image == dead_shadow_2:
                        self.image = dead_shadow_4
                    elif self.image == dead_shadow_3:
                        self.image = dead_shadow_1
                    elif self.image == dead_shadow_4:
                        self.image = dead_shadow_2
                    self.last_image_change_time = current_time
            else:
                if elapsed_time > 500:
                    if self.image == dead_shadow_1:
                        self.image = dead_shadow_2
                    else:
                        self.image = dead_shadow_1
                    self.last_image_change_time = current_time
        elif self.eat:
            self.image = heye_left
        else:
            if elapsed_time > 100:
                if self.direction == "RIGHT":
                    if self.image == red_shadow_right_1:
                        self.image = red_shadow_right_2
                    else:
                        self.image = red_shadow_right_1
                    self.last_image_change_time = current_time
                if self.direction == "LEFT":
                    if self.image == red_shadow_left_1:
                        self.image = red_shadow_left_2
                    else:
                        self.image = red_shadow_left_1
                    self.last_image_change_time = current_time
                if self.direction == "UP":
                    if self.image == red_shadow_up_1:
                        self.image = red_shadow_up_2
                    else:
                        self.image = red_shadow_up_1
                    self.last_image_change_time = current_time
                if self.direction == "DOWN":
                    if self.image == red_shadow_down_1:
                        self.image = red_shadow_down_2
                    else:
                        self.image = red_shadow_down_1
                    self.last_image_change_time = current_time
        screen.blit(self.image, (
            self.x + (self.size - self.image.get_width()) // 2, self.y + (self.size - self.image.get_height()) // 2))
