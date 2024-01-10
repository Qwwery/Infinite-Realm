import pygame


def get_doors(board, all_sprite, door_sprite, door_image, cell_cize):
    doors = []
    for y in range(len(board.field)):
        for x in range(len(board.field[0])):
            if board.field[y][x] in "Д":
                door = Door(all_sprite, door_sprite, door_image, cell_cize, board)
                door.rect.x = x * cell_cize + board.left_start
                door.rect.y = y * cell_cize + board.top_start
                doors.append(door)
    return doors


class Door(pygame.sprite.Sprite):
    def __init__(self, all_sprite, door_sprite, door_image, cell_cize, board):
        super().__init__(all_sprite, door_sprite)
        self.image = door_image
        self.image = pygame.transform.scale(self.image, (cell_cize, cell_cize))
        self.rect = self.image.get_rect()
        self.rect.x = board.left_start
        self.rect.y = board.top_start
