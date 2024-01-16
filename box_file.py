import pygame


def get_boxes(board, all_sprite, box_sprite, box_image, cell_cize, sound):
    boxes = []
    for y in range(len(board.field)):
        for x in range(len(board.field[0])):
            if board.field[y][x] in "KК":
                box = Box(all_sprite, box_sprite, box_image, cell_cize, board, sound)
                box.rect.x = x * cell_cize + board.left_start
                box.rect.y = y * cell_cize + board.top_start
                boxes.append(box)
    return boxes


class Box(pygame.sprite.Sprite):
    def __init__(self, all_sprite, box_sprite, box_image, cell_cize, board, sound):
        super().__init__(all_sprite, box_sprite)
        self.image = box_image
        self.image = pygame.transform.scale(self.image, (cell_cize, cell_cize))
        self.rect = self.image.get_rect()
        self.rect.x = board.left_start
        self.rect.y = board.top_start
        self.sound = sound
