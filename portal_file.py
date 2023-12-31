import pygame


def get_partals(board, all_sprite, portal_sprite, portal_image, cell_cize):
    portals = []
    for y in range(len(board.field)):
        for x in range(len(board.field[0])):
            if board.field[y][x] == 'П1':
                portal = Portal(all_sprite, portal_sprite, portal_image, cell_cize * 2.3)
                portal.rect.x = x * cell_cize + board.left_start - 10
                portal.rect.y = y * cell_cize + board.top_start - 12
                portals.append(portal)
    return portals


class Portal(pygame.sprite.Sprite):
    def __init__(self, all_sprite, portal_sprite, portal_image, cell_cize):
        super().__init__(all_sprite, portal_sprite)
        self.image = portal_image
        self.image = pygame.transform.scale(self.image, (cell_cize, cell_cize))
        self.rect = self.image.get_rect()
