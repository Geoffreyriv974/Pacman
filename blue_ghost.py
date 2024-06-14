import pygame
import random

from sprites import *
from run import *
from map import *


class Blue_Ghost:
    def __init__(self, x, y, target_x, target_y):
        self.x = x
        self.y = y
        self.target_x = target_x
        self.target_y = target_y
        self.speed = 1
        self.moving = False
        self.image = blue_shadow_right_1
        self.direction = "UP"
        self.last_image_change_time = pygame.time.get_ticks()
        self.size = 20
        self.time_move = pygame.time.get_ticks()
        self.valid_start_position = False
        self.time_vulnerable = pygame.time.get_ticks()
        self.vulnerable = False
        self.eat = False
        self.ghost_heye = False

    def get_cube(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

    def ghost_vulnerable(self):
        self.vulnerable = True
        self.time_vulnerable = pygame.time.get_ticks() + 13000

    def reset_vulnerability(self):
        self.vulnerable = False

    def reset_position(self):
        self.x = 320
        self.y = 300
        self.direction = "UP"
        self.eat = False
        self.vulnerable = False
        self.valid_start_position = False

    def ghost_heye(self):
        self.ghost_heye = True

    def position_target(self):
        if self.x < self.target_x:
            self.x += self.speed
            self.direction = "RIGHT"
        elif self.x > self.target_x:
            self.x -= self.speed
            self.direction = "LEFT"
        elif self.y < self.target_y:
            self.y += self.speed
            self.direction = "DOWN"
        elif self.y > self.target_y:
            self.y -= self.speed
            self.direction = "UP"

        if self.x == self.target_x and self.y == self.target_y:
            self.valid_start_position = True

    def move(self):
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - self.time_move

        if elapsed_time > 26000:

            if not self.valid_start_position:
                self.position_target()

            if self.valid_start_position:
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
        else:
            if self.direction == "UP":
                next_position = list_tableau_number[
                    (self.y - self.speed) // self.size * (560 // self.size) + self.x // self.size]
                if next_position != -1:
                    self.y -= self.speed
                else:
                    self.direction = "DOWN"
            elif self.direction == "DOWN":
                next_position = list_tableau_number[
                    (self.y + self.speed + self.size - 2) // self.size * (560 // self.size) + self.x // self.size]
                if next_position != -1:
                    self.y += self.speed
                else:
                    self.direction = "UP"


        def move(self):
            if self.direction == "UP":
                next_position = list_tableau_number[
                    (self.y - self.speed) // self.size * (560 // self.size) + self.x // self.size]
                if next_position != -1:
                    self.y -= self.speed
                else:
                    self.direction = "DOWN"
            elif self.direction == "DOWN":
                next_position = list_tableau_number[
                    (self.y + self.speed + self.size - 2) // self.size * (560 // self.size) + self.x // self.size]
                if next_position != -1:
                    self.y += self.speed
                else:
                    self.direction = "UP"

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
        else:
            if elapsed_time > 100:
                if self.direction == "RIGHT":
                    if self.image == blue_shadow_right_1:
                        self.image = blue_shadow_right_2
                    else:
                        self.image = blue_shadow_right_1
                    self.last_image_change_time = current_time
                if self.direction == "LEFT":
                    if self.image == blue_shadow_left_1:
                        self.image = blue_shadow_left_2
                    else:
                        self.image = blue_shadow_left_1
                    self.last_image_change_time = current_time
                if self.direction == "UP":
                    if self.image == blue_shadow_up_1:
                        self.image = blue_shadow_up_2
                    else:
                        self.image = blue_shadow_up_1
                    self.last_image_change_time = current_time
                if self.direction == "DOWN":
                    if self.image == blue_shadow_down_1:
                        self.image = blue_shadow_down_2
                    else:
                        self.image = blue_shadow_down_1
                    self.last_image_change_time = current_time
        screen.blit(self.image, (self.x + (self.size - self.image.get_width()) // 2, self.y + (self.size - self.image.get_height()) // 2))
