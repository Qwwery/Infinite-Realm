from random import choice

import pygame


def get_trap(board, all_sprite, trap_sprite, trap_image, cell_cize):
    traps = []
    for y in range(len(board.field)):
        for x in range(len(board.field[0])):
            if board.field[y][x] in "Л":
                trap = Trap(all_sprite, trap_sprite, trap_image, board, cell_cize)
                trap.rect.x = x * cell_cize + board.left_start
                trap.rect.y = y * cell_cize + board.top_start
                traps.append(trap)
    return traps


class Trap(pygame.sprite.Sprite):
    def __init__(self, all_sprite, trap_sprite, trap_image, board, cell_cize):
        super().__init__(all_sprite, trap_sprite)
        self.image = trap_image
        self.image = pygame.transform.scale(self.image, (cell_cize, cell_cize))
        self.cur_image = 0

        self.rect = self.image.get_rect()
        self.rect.x = board.left_start
        self.rect.y = board.top_start

        self.is_attack = 20
        self.need_attack = 20

        self.all_images = self.get_all_images()

    def get_all_images(self):
        all_images = []
        right = choice((0, 1))
        if right == 1:
            images = [self.image, pygame.transform.rotate(self.image, 90), pygame.transform.rotate(self.image, 180),
                      pygame.transform.rotate(self.image, 270)]
        else:
            images = [self.image, pygame.transform.rotate(self.image, 270), pygame.transform.rotate(self.image, 180),
                      pygame.transform.rotate(self.image, 90)]
        for elem in images:
            for i in range(8):
                all_images.append(elem)
        return all_images

    def update(self):
        self.cur_image = (self.cur_image + 1) % len(self.all_images)
        self.image = self.all_images[self.cur_image]
        self.is_attack += 1

    def check_damage(self):
        if self.is_attack > self.need_attack:
            self.is_attack = 0
            return True
        else:
            return False
