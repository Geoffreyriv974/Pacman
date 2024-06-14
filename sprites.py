from pygame import *

#map
pacman_mur = image.load("sprites/map/mur.jpg")
porte_shadow = image.load("sprites/map/porte.png")

# pacman
pac_right_open = image.load("sprites/pacman/pac_right_open.png")
pac_right_closed = image.load("sprites/pacman/pac_right_closed.png")
pac_left_open = image.load("sprites/pacman/pac_left_open.png")
pac_left_closed = image.load("sprites/pacman/pac_left_closed.png")
pac_down_open = image.load("sprites/pacman/pac_down_open.png")
pac_down_closed = image.load("sprites/pacman/pac_down_closed.png")
pac_up_open = image.load("sprites/pacman/pac_up_open.png")
pac_up_closed = image.load("sprites/pacman/pac_up_closed.png")

# pacman-life
pac_life = image.load("sprites/pacman/pacman_life.png")

# pacman-dead
pac_dead_1 = image.load("sprites/pacman/pac_dead_1.png")
pac_dead_2 = image.load("sprites/pacman/pac_dead_2.png")
pac_dead_3 = image.load("sprites/pacman/pac_dead_3.png")
pac_dead_4 = image.load("sprites/pacman/pac_dead_4.png")
pac_dead_5 = image.load("sprites/pacman/pac_dead_5.png")
pac_dead_6 = image.load("sprites/pacman/pac_dead_6.png")
pac_dead_7 = image.load("sprites/pacman/pac_dead_7.png")
pac_dead_8 = image.load("sprites/pacman/pac_dead_8.png")
pac_dead_9 = image.load("sprites/pacman/pac_dead_9.png")
pac_dead_10 = image.load("sprites/pacman/pac_dead_10.png")
pac_dead_11 = image.load("sprites/pacman/pac_dead_11.png")
pac_dead_12 = image.load("sprites/pacman/pac_dead_12.png")

# red shadow
red_shadow_up_1 = image.load("sprites/fantome/Blinky/red_shadow_up_1.png")
red_shadow_up_2 = image.load("sprites/fantome/Blinky/red_shadow_up_2.png")
red_shadow_down_1 = image.load("sprites/fantome/Blinky/red_shadow_down_1.png")
red_shadow_down_2 = image.load("sprites/fantome/Blinky/red_shadow_down_2.png")
red_shadow_left_1 = image.load("sprites/fantome/Blinky/red_shadow_left_1.png")
red_shadow_left_2 = image.load("sprites/fantome/Blinky/red_shadow_left_2.png")
red_shadow_right_1 = image.load("sprites/fantome/Blinky/red_shadow_right_1.png")
red_shadow_right_2 = image.load("sprites/fantome/Blinky/red_shadow_right_2.png")

# yellow shadow
yellow_shadow_up_1 = image.load("sprites/fantome/Bashful/yellow_shadow_up_1.png")
yellow_shadow_up_2 = image.load("sprites/fantome/Bashful/yellow_shadow_up_2.png")
yellow_shadow_down_1 = image.load("sprites/fantome/Bashful/yellow_shadow_down_1.png")
yellow_shadow_down_2 = image.load("sprites/fantome/Bashful/yellow_shadow_down_2.png")
yellow_shadow_left_1 = image.load("sprites/fantome/Bashful/yellow_shadow_left_1.png")
yellow_shadow_left_2 = image.load("sprites/fantome/Bashful/yellow_shadow_left_2.png")
yellow_shadow_right_1 = image.load("sprites/fantome/Bashful/yellow_shadow_right_1.png")
yellow_shadow_right_2 = image.load("sprites/fantome/Bashful/yellow_shadow_right_2.png")

# blue shadow
blue_shadow_up_1 = image.load("sprites/fantome/Inky/blue_shadow_up_1.png")
blue_shadow_up_2 = image.load("sprites/fantome/Inky/blue_shadow_up_2.png")
blue_shadow_down_1 = image.load("sprites/fantome/Inky/blue_shadow_down_1.png")
blue_shadow_down_2 = image.load("sprites/fantome/Inky/blue_shadow_down_2.png")
blue_shadow_left_1 = image.load("sprites/fantome/Inky/blue_shadow_left_1.png")
blue_shadow_left_2 = image.load("sprites/fantome/Inky/blue_shadow_left_2.png")
blue_shadow_right_1 = image.load("sprites/fantome/Inky/blue_shadow_right_1.png")
blue_shadow_right_2 = image.load("sprites/fantome/Inky/blue_shadow_right_2.png")

# pink shadow
pink_shadow_up_1 = image.load("sprites/fantome/Pinky/pink_shadow_up_1.png")
pink_shadow_up_2 = image.load("sprites/fantome/Pinky/pink_shadow_up_2.png")
pink_shadow_down_1 = image.load("sprites/fantome/Pinky/pink_shadow_down_1.png")
pink_shadow_down_2 = image.load("sprites/fantome/Pinky/pink_shadow_down_2.png")
pink_shadow_left_1 = image.load("sprites/fantome/Pinky/pink_shadow_left_1.png")
pink_shadow_left_2 = image.load("sprites/fantome/Pinky/pink_shadow_left_2.png")
pink_shadow_right_1 = image.load("sprites/fantome/Pinky/pink_shadow_right_1.png")
pink_shadow_right_2 = image.load("sprites/fantome/Pinky/pink_shadow_right_2.png")

# eyes
heye_right = image.load("sprites/fantome/yeux/heye_right.png")
heye_left = image.load("sprites/fantome/yeux/heye_left.png")
heye_up = image.load("sprites/fantome/yeux/heye_up.png")
heye_down = image.load("sprites/fantome/yeux/heye_down.png")

# dead shadow
dead_shadow_1 = image.load("sprites/fantome/vulnerable/dead_shadow_1.png")
dead_shadow_2 = image.load("sprites/fantome/vulnerable/dead_shadow_2.png")
dead_shadow_3 = image.load("sprites/fantome/vulnerable/dead_shadow_3.png")
dead_shadow_4 = image.load("sprites/fantome/vulnerable/dead_shadow_4.png")

# display
pac_ready = image.load("sprites/display/ready.jpg")
pac_game_over = image.load("sprites/display/game_over.jpg")
