import pygame


def get_walls(board, wall_sprite, cell_cize, all_sprite, wall_image):
    walls = []
    for y in range(len(board.field)):
        for x in range(len(board.field[0])):
            if board.field[y][x] in "CС":
                wall = Wall(all_sprite, wall_sprite, wall_image, cell_cize, board, y, x)
                wall.rect.x = x * cell_cize + board.left_start
                wall.rect.y = y * cell_cize + board.top_start
                walls.append(wall)
    return walls


class Wall(pygame.sprite.Sprite):
    def __init__(self, all_sprite, wall_sprite, wall_image, cell_cize, board, y, x):
        super().__init__(all_sprite, wall_sprite)
        self.image = wall_image
        self.image = pygame.transform.scale(self.image, (cell_cize, cell_cize))
        self.rect = self.image.get_rect()
        self.rect.x = board.left_start
        self.rect.y = board.top_start
        self.y = y
        self.x = x
