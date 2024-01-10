import pygame


def get_enemy(board, all_sprite, enemy_sprite, enemy_image, cell_cize):
    enemyes = []
    for y in range(len(board.field)):
        for x in range(len(board.field[0])):
            if board.field[y][x] in "E":
                enemy = Enemy(all_sprite, enemy_sprite, enemy_image, cell_cize, board)
                enemy.rect.x = x * cell_cize + board.left_start + 5
                enemy.rect.y = y * cell_cize + board.top_start + 5
                enemyes.append(enemy)
    return enemyes


class Enemy(pygame.sprite.Sprite):
    def __init__(self, all_sprite, enemy_sprite, enemy_image, cell_cize, board):
        super().__init__(all_sprite, enemy_sprite)
        self.image = enemy_image
        self.image = pygame.transform.scale(self.image, (cell_cize - 10, cell_cize - 10))
        self.rect = self.image.get_rect()
        self.rect.x = board.left_start
        self.rect.y = board.top_start

        self.hp = 100
        self.level = 0
