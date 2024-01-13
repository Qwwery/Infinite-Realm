import pygame


def get_pols(board, pol_sprite, cell_cize, pol_image, all_sprite):
    pols = []
    for y in range(len(board.field)):
        for x in range(len(board.field[0])):
            if board.field[y][x] in ".@ВBE":
                pol = Pol(all_sprite, pol_sprite, pol_image, board, cell_cize)
                pol.rect.x = x * cell_cize + board.left_start
                pol.rect.y = y * cell_cize + board.top_start
                pols.append(pol)
    return pols


class Pol(pygame.sprite.Sprite):
    def __init__(self, all_sprite, pol_sprite, pol_image, board, cell_cize):
        super().__init__(all_sprite, pol_sprite)
        self.image = pol_image
        self.image = pygame.transform.scale(self.image, (cell_cize, cell_cize))
        self.rect = self.image.get_rect()
        self.rect.x = board.left_start
        self.rect.y = board.top_start