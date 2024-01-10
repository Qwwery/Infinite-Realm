import pygame


def get_enemy(board, all_sprite, enemy_sprite, enemy_image, cell_cize, heroes):
    enemyes = []
    x_her, y_her = board.return_heroes_cords()
    for y in range(len(board.field)):
        for x in range(len(board.field[0])):
            if board.field[y][x] in "X":
                board.field[y][x] = 'E'
                enemy = Enemy(all_sprite, enemy_sprite, enemy_image, cell_cize)
                enemy.rect.x = heroes.rect.x + (x - x_her) * cell_cize - 7 + cell_cize // 2
                enemy.rect.y = heroes.rect.y + (y - y_her) * cell_cize + 6 + cell_cize // 2
                enemyes.append(enemy)
    return enemyes


class Enemy(pygame.sprite.Sprite):
    def __init__(self, all_sprite, enemy_sprite, enemy_image, cell_cize):
        super().__init__(all_sprite, enemy_sprite)
        self.image = enemy_image
        self.image = pygame.transform.scale(self.image, (cell_cize - 10, cell_cize - 10))
        self.rect = self.image.get_rect()
        self.hp = 100
        self.level = 0
