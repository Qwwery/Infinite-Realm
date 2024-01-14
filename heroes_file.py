import pygame
from maps import spawn_enemy
from enemy_file import get_enemy
from heroes_attack import *


class Heroes(pygame.sprite.Sprite):
    def __init__(self, all_sprite, heroes_sprite, heroes_image, cell_cize, board, camera, box_sprite, pol, pol_sprite,
                 pol_image, trap_sprite, enemy_sprite, enemy_image, door_sprite, kill, ydar_sound, ydar_sound2):
        super().__init__(all_sprite, heroes_sprite)
        self.image = heroes_image
        self.image = pygame.transform.scale(self.image, (cell_cize * 1.5, cell_cize * 1.5))
        self.mask = pygame.mask.from_surface(self.image)
        self.image_left = pygame.transform.flip(surface=self.image, flip_x=True, flip_y=False)
        self.image_right = self.image
        self.enemy_image = enemy_image

        self.board = board
        self.camera = camera
        self.cell_cize = cell_cize
        self.all_sprite = all_sprite
        self.heroes_sprite = heroes_sprite
        self.box_sprite = box_sprite
        self.pol = pol
        self.pol_sprite = pol_sprite
        self.pol_image = pol_image
        self.trap_sprite = trap_sprite
        self.enemy_sprite = enemy_sprite
        self.door_sprite = door_sprite

        self.kill_sound = kill
        self.ydar_sound = ydar_sound
        self.ydar_sound_enemy = ydar_sound2

        self.sword = "меч"
        self.spear = "копье"
        self.weapon = self.spear

        self.rect = self.image.get_rect()
        x_n, y_n = board.return_heroes_cords()
        self.rect.x = x_n * self.cell_cize - 20 + cell_cize
        self.rect.y = y_n * self.cell_cize + cell_cize - 33

        self.full_hp = 100
        self.hp = self.full_hp
        self.max_hp = 100

        self.xp = 0
        self.level = 1

        self.clock_cool_down = pygame.time.Clock()
        self.cur_time_cool_down = 0
        self.limit_time_cool_down = 0.4

        self.damage_spear = self.damage_sword = 20

    def get_level_hero(self):
        return self.level

    def move(self, event):
        f = open('count.txt')
        cur_waves = int(f.readline())
        f.close()

        x_her, y_her = self.board.return_heroes_cords()
        speed = self.board.cell_size

        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.rect.x += speed
            self.image = self.image_left
            if self.board.field[y_her][x_her + 1] in "KКСCE":  # добавить Д
                self.rect.x -= speed
                return

            if cur_waves != 0:
                for door in self.door_sprite:
                    center = door.rect.center
                    x, y = center
                    if self.rect.collidepoint(x, y - 15):
                        if cur_waves != 3:
                            self.rect.x -= speed
                            return
                        else:
                            if len(self.enemy_sprite) > 0:
                                self.rect.x -= speed
                                return

            self.board.field[y_her][x_her] = '.'
            if 'П' in self.board.field[y_her][x_her + 1]:
                self.board.new_level = True
            self.board.field[y_her][x_her + 1] = "@"
            if spawn_enemy(self, x_her + 1, y_her, self.level, self.board.this_level):
                get_enemy(self.board, self.all_sprite, self.enemy_sprite, self.enemy_image, self.cell_cize, self,
                          self.door_sprite, self.ydar_sound_enemy)

            self.camera.update(self, 'x')
            for elem in self.all_sprite:
                self.camera.apply(elem)
            return

        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.rect.x -= speed
            self.image = self.image_right
            if self.board.field[y_her][x_her - 1] in "KКСCE":  # добавить Д
                self.rect.x += speed
                return

            if cur_waves != 0:
                for door in self.door_sprite:
                    center = door.rect.center
                    x, y = center
                    if self.rect.collidepoint(x, y - 15):
                        if cur_waves != 3:
                            self.rect.x += speed
                            return
                        else:
                            if len(self.enemy_sprite) > 0:
                                self.rect.x += speed
                                return

            self.board.field[y_her][x_her] = '.'
            if 'П' in self.board.field[y_her][x_her - 1]:
                self.board.new_level = True
            if spawn_enemy(self, x_her - 1, y_her, self.level, self.board.this_level):
                get_enemy(self.board, self.all_sprite, self.enemy_sprite, self.enemy_image, self.cell_cize, self,
                          self.door_sprite, self.ydar_sound_enemy)
            self.board.field[y_her][x_her - 1] = "@"

            self.camera.update(self, 'x')
            for elem in self.all_sprite:
                self.camera.apply(elem)

        elif sum(list(pygame.key.get_pressed())) > 1:  # нельзя двигать по диагонали
            return

        elif event.key == pygame.K_UP or event.key == pygame.K_w:
            self.rect.y -= speed
            if self.board.field[y_her - 1][x_her] in "KКСEC":  # добавить Д
                self.rect.y += speed
                return
            if cur_waves != 0:

                for door in self.door_sprite:
                    center = door.rect.center
                    x, y = center
                    if self.rect.collidepoint(x, y - 15):
                        if cur_waves != 3:
                            self.rect.y += speed
                            return
                        else:
                            if len(self.enemy_sprite) > 0:
                                self.rect.y += speed
                                return

            if 'П' in self.board.field[y_her - 1][x_her]:
                self.board.new_level = True
            if spawn_enemy(self, x_her, y_her - 1, self.level, self.board.this_level):
                get_enemy(self.board, self.all_sprite, self.enemy_sprite, self.enemy_image, self.cell_cize, self,
                          self.door_sprite, self.ydar_sound_enemy)
            self.board.field[y_her - 1][x_her] = "@"
            self.board.field[y_her][x_her] = "."

            self.camera.update(self, 'y')
            for elem in self.all_sprite:
                self.camera.apply(elem)

        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.rect.y += speed
            if self.board.field[y_her + 1][x_her] in "СEKКC":  # добавить Д
                self.rect.y -= speed
                return
            if cur_waves != 0:
                for door in self.door_sprite:
                    if len(self.enemy_sprite) > 0 and self.rect.collidepoint(door.rect.center):
                        self.rect.y -= speed
                        return

            if cur_waves != 0:
                for door in self.door_sprite:
                    if self.rect.collidepoint(door.rect.center):
                        if cur_waves != 3:
                            self.rect.y -= speed
                            return
                        else:
                            if len(self.enemy_sprite) > 0:
                                self.rect.y -= speed
                                return

            if 'П' in self.board.field[y_her + 1][x_her]:
                self.board.new_level = True
            if spawn_enemy(self, x_her, y_her + 1, self.level, self.board.this_level):
                get_enemy(self.board, self.all_sprite, self.enemy_sprite, self.enemy_image, self.cell_cize, self,
                          self.door_sprite, self.ydar_sound_enemy)
            self.board.field[y_her + 1][x_her] = "@"
            self.board.field[y_her][x_her] = "."

            self.camera.update(self, 'y')
            for elem in self.all_sprite:
                self.camera.apply(elem)

    def make_attack(self, delta_x, delta_y):
        """
        Функция вызывает функции в зависимости от координат. В других функциях происходит действие атаки, при которой
        удаляются спрайты коробок и создается пол при атаки коробок. При атаке врагов происходит действие урона. При
        убийстве врага его спрайт удаляется и позиция в доске заменяется на пустоту.
        """
        x_her, y_her = self.board.return_heroes_cords()

        if delta_x > 20 and delta_y < 0:  # право верх
            check_right_top(self, y_her, x_her)

        elif delta_x > 0 and delta_y == 33:  # право
            check_right(self, y_her, x_her)

        elif delta_x > 20 and delta_y > 0:  # право низ
            check_right_down(self, y_her, x_her)

        elif delta_x == 20 and delta_y < 0:  # верх
            check_top(self, y_her, x_her)

        elif delta_x == 20 and delta_y > 0:  # низ
            check_down(self, y_her, x_her)

        elif delta_x < 0 and delta_y > 33:  # лево низ
            check_left_down(self, y_her, x_her)

        elif delta_x < 0 and delta_y == 33:  # лево
            check_left(self, y_her, x_her)

        elif delta_x < 0 and delta_y < 0:  # лево верх
            check_left_top(self, y_her, x_her)

    def left_attack(self, *args):
        """
        проверка корректности атаки объекта, когда герой находится левее объекта или ниже/выше
        атака совершается в случае правильности логики
        """
        for elem in self.all_sprite:
            if elem.rect.collidepoint(args[0].pos):
                if self.rect.x - 20 <= elem.rect.x:
                    self.make_attack(elem.rect.x - self.rect.x, elem.rect.y - self.rect.y)

    def right_attack(self, *args):
        """
        проверка корректности атаки объекта, когда герой находится правее объекта  или ниже/выше
        атака совершается в случае правильности логики
        """
        for elem in self.all_sprite:
            if elem.rect.collidepoint(args[0].pos):
                if self.rect.x + 20 >= elem.rect.x:
                    self.make_attack(elem.rect.x - self.rect.x, elem.rect.y - self.rect.y)

    def check_attack(self, *args):
        if self.check_cooldown():
            if self.image == self.image_left:  # герой находится слева
                self.left_attack(*args)
            else:  # герой находится справа
                self.right_attack(*args)

    def check_intersection_trap(self, trap_sprite):
        for trap in trap_sprite:
            center = trap.rect.center[0], trap.rect.center[1] - 15
            if self.rect.collidepoint(center):
                return trap
        return False

    def check_cooldown(self):
        self.clock_cool_down.tick()
        self.cur_time_cool_down += self.clock_cool_down.get_time() / 1000
        if self.cur_time_cool_down > self.limit_time_cool_down:
            self.cur_time_cool_down = 0
            return True
        return False