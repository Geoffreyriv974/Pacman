import sys

from blue_ghost import *
from pacman import *
from pink_ghost import *
from red_ghost import *
from yellow_ghost import *

plateau_width = 560
plateau_height = 620
size = 20
color_white = (255, 255, 255)
list_mur_position = []
time_super_pac_gom = 0


def reset_speed():
    pacman.change_speed(1)
    for ghost in all_ghosts:
        ghost.reset_vulnerability()


def play_super_pac_gom():
    global time_super_pac_gom, music_gobe_pac_gom

    music_gobe_pac_gom = pygame.mixer.Sound('musique/super-pac-gom.mp3')
    music_gobe_pac_gom.set_volume(0.2)

    if pygame.mixer.get_busy():
        pygame.mixer.stop()

    pacman.change_speed(2)
    music_gobe_pac_gom.play()

    for ghost in all_ghosts:
        ghost.ghost_vulnerable()

    time_super_pac_gom = pygame.time.get_ticks() + int(music_gobe_pac_gom.get_length() * 1000)


def music_dead():
    global music_dead_pacman
    music_dead_pacman.play()


def win_game(liste_position):
    for x, y, value in liste_position:
        if value == 1 or value == 2:
            return True
    return False


def display(surface, liste_position):
    color_point = (color_white)

    for position in liste_position:
        x, y, value = position
        if value == 1:
            pygame.draw.circle(surface, color_point, (x + size // 2, y + size // 2), 3)
        elif value == 2:
            pygame.draw.circle(surface, color_point, (x + size // 2, y + size // 2), 7)
        elif value == -1:
            surface.blit(pacman_mur, (x, y))
            list_mur_position.append((x, y))
        elif value == "":
            surface.blit(porte_shadow, (x, y))
        elif value == 0:
            pass


def Run():
    global ghost_vulnerable, pacman, time_super_pac_gom, all_ghosts, ghost, music_dead_pacman

    pygame.init()

    pygame.mixer.music.load('musique/start.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play()

    music_dead_pacman = pygame.mixer.Sound('musique/dead.wav')
    music_dead_pacman.set_volume(0.2)

    window = pygame.display.set_mode((560, 680))
    pygame.display.set_caption("Pacman")

    liste_position = []
    for y in range(0, plateau_height, size):
        for x in range(0, plateau_width, size):
            value = list_tableau_number[y // size * (plateau_width // size) + x // size]
            liste_position.append((x, y, value))

    pacman = Player(280, 460)

    red_ghost = Red_Ghost(280, 220)
    yellow_ghost = Yellow_Ghost(240, 300, 280, 220)
    pink_ghost = Pink_Ghost(280, 260, 280, 220)
    blue_ghost = Blue_Ghost(320, 300, 280, 220)

    all_ghosts = [red_ghost, yellow_ghost, pink_ghost, blue_ghost]

    refresh = pygame.time.Clock()

    score_font = pygame.font.SysFont('Arial', 30)
    winner_font = pygame.font.SysFont('Arial', 15, True)

    running = True
    pause = False
    pause_time = 0
    change_position = False

    while running:
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if pause:

            if current_time - pause_time > music_dead_pacman.get_length() * 1000:
                pause = False
                pygame.mixer.music.unpause()

                if change_position:
                    change_position = False
                    if pacman.lives > 0:
                        pacman.reset_position()

                        for ghost in all_ghosts:
                            ghost.reset_position()

        else:
            if not pygame.mixer.music.get_busy():
                window.fill((0, 0, 0))

                if current_time > time_super_pac_gom:
                    time_super_pac_gom = 0
                    reset_speed()

                pos_actuelle = list_tableau_number[pacman.y // size * (plateau_width // size) + pacman.x // size]

                if pos_actuelle == 1:
                    pacman.score += 10
                    list_tableau_number[pacman.y // size * (plateau_width // size) + pacman.x // size] = 0
                    liste_position[pacman.y // size * (plateau_width // size) + pacman.x // size] = (
                        pacman.x, pacman.y, 0)

                    music_move = pygame.mixer.Sound('musique/move.wav')
                    music_move.set_volume(0.2)
                    music_move.play()
                elif pos_actuelle == 2:
                    pacman.score += 50
                    list_tableau_number[pacman.y // size * (plateau_width // size) + pacman.x // size] = 0
                    liste_position[pacman.y // size * (plateau_width // size) + pacman.x // size] = (
                        pacman.x, pacman.y, 0)

                    play_super_pac_gom()

                if not win_game(liste_position):
                    winner_label = winner_font.render("WINNER !", True, (0, 255, 0))
                    window.blit(winner_label, (250, 340))

                pacman.move()
                pacman.draw(window)

                display(window, liste_position)

                label_score = score_font.render(f"{pacman.score}", True, color_white)
                window.blit(label_score, (200, 630))

                for ghost in all_ghosts:
                    ghost.move()
                    ghost.draw(window)

                if pacman.ghost_collision(all_ghosts):

                    pause = True
                    pause_time = pygame.time.get_ticks()

                    change_position = True

                    pygame.mixer.music.pause()

                    if pacman.lives <= 0:
                        window.blit(pac_game_over, (220, 340))

                        if not pygame.mixer.music.get_busy():
                            running = False

                for i in range(pacman.lives):
                    window.blit(pac_life, (20 + i * 35, 630))

                refresh.tick(50)
            else:
                window.blit(pac_ready, (250, 340))

                window.blit(pac_dead_1, (
                    pacman.x + (size - pacman.image.get_width()) // 2,
                    pacman.y + (size - pacman.image.get_height()) // 2))
                window.blit(red_shadow_right_1, (red_ghost.x + (size - red_ghost.image.get_width()) // 2,
                                                 red_ghost.y + (size - red_ghost.image.get_height()) // 2))
                window.blit(yellow_shadow_right_1, (yellow_ghost.x + (size - yellow_ghost.image.get_width()) // 2,
                                                    yellow_ghost.y + (size - yellow_ghost.image.get_height()) // 2))
                window.blit(pink_shadow_right_1, (pink_ghost.x + (size - pink_ghost.image.get_width()) // 2,
                                                  pink_ghost.y + (size - pink_ghost.image.get_height()) // 2))
                window.blit(blue_shadow_right_1, (blue_ghost.x + (size - blue_ghost.image.get_width()) // 2,
                                                  blue_ghost.y + (size - blue_ghost.image.get_height()) // 2))

        display(window, liste_position)

        pacman.change_direction()

        pygame.display.flip()

    pygame.quit()
    sys.exit()
