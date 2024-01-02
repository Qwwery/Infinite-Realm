import pygame


def get_trap(board, all_sprite, trap_sprite, trap_image1, trap_image2, trap_image3, cell_cize):
    traps = []
    for y in range(len(board.field)):
        for x in range(len(board.field[0])):
            if board.field[y][x] in "Л":
                trap = Trap(all_sprite, trap_sprite, trap_image1, trap_image2, trap_image3, board, cell_cize)
                trap.rect.x = x * cell_cize + board.left_start
                trap.rect.y = y * cell_cize + board.top_start
                traps.append(trap)
    return traps


class Trap(pygame.sprite.Sprite):
    def __init__(self, all_sprite, trap_sprite, trap_image1, trap_image2, trap_image3, board, cell_cize):
        super().__init__(all_sprite, trap_sprite)
        self.image = trap_image1
        self.image_trap2 = trap_image2
        self.image_trap3 = trap_image3
        self.image = pygame.transform.scale(self.image, (cell_cize, cell_cize))
        self.image_trap2 = pygame.transform.scale(self.image_trap2, (cell_cize, cell_cize))
        self.image_trap3 = pygame.transform.scale(self.image_trap3, (cell_cize, cell_cize))
        self.cur_image = 0

        self.rect = self.image.get_rect()
        self.rect.x = board.left_start
        self.rect.y = board.top_start

        self.all_images = self.get_all_images()

    def get_all_images(self):
        all_images = []
        images = [self.image, self.image_trap2, self.image_trap3]
        for elem in images:
            for i in range(10):
                all_images.append(elem)
        return all_images

    def update(self):
        self.cur_image = (self.cur_image + 1) % len(self.all_images)
        self.image = self.all_images[self.cur_image]

    def make_standart_image(self):
        self.image = self.all_images[0]
