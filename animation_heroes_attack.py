import pygame


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, animation_sprite, spear1_image, spear2_image, spear3_image, spear1_1_image, spear2_2_image,
                 spear_3_3_image):
        super().__init__(animation_sprite)
        self.x, self.y = 45, 45

        self.spear1_image_left = pygame.transform.scale(spear1_image, (self.x, self.y))
        self.spear2_image_left = pygame.transform.scale(spear2_image, (self.x, self.y))
        self.spear3_image_left = pygame.transform.scale(spear3_image, (self.x, self.y))
        self.frames_left = [self.spear1_image_left, self.spear1_image_left, self.spear2_image_left,
                            self.spear3_image_left]

        self.spear1_image_right = pygame.transform.flip(self.spear1_image_left, flip_x=1, flip_y=0)
        self.spear2_image_right = pygame.transform.flip(self.spear2_image_left, flip_x=1, flip_y=0)
        self.spear3_image_right = pygame.transform.flip(self.spear3_image_left, flip_x=1, flip_y=0)
        self.frames_right = [self.spear1_image_right, self.spear1_image_right, self.spear2_image_right,
                             self.spear3_image_right]

        self.spear1_image_top = pygame.transform.rotate(spear1_image, angle=-90)
        self.spear2_image_top = pygame.transform.rotate(spear2_image, angle=-90)
        self.spear3_image_top = pygame.transform.rotate(spear3_image, angle=-90)
        self.frames_top = [self.spear1_image_top, self.spear1_image_top, self.spear2_image_top,
                           self.spear3_image_top]

        self.spear1_image_down = pygame.transform.rotate(spear1_image, angle=90)
        self.spear2_image_down = pygame.transform.rotate(spear2_image, angle=90)
        self.spear3_image_down = pygame.transform.rotate(spear3_image, angle=90)
        self.frames_down = [self.spear1_image_down, self.spear1_image_down, self.spear2_image_down,
                            self.spear3_image_down]

        self.spear1_image_right_down = pygame.transform.rotate(spear1_1_image, angle=180)
        self.spear2_image_right_down = pygame.transform.rotate(spear2_2_image, angle=180)
        self.spear3_image_right_down = pygame.transform.rotate(spear_3_3_image, angle=180)

        self.frames_right_down = [self.spear1_image_right_down, self.spear1_image_right_down,
                                  self.spear2_image_right_down,
                                  self.spear3_image_right_down]

        self.spear1_image_right_up = pygame.transform.rotate(spear1_1_image, angle=-90)
        self.spear2_image_right_up = pygame.transform.rotate(spear2_2_image, angle=-90)
        self.spear3_image_right_up = pygame.transform.rotate(spear_3_3_image, angle=-90)

        self.frames_right_up = [self.spear1_image_right_up, self.spear1_image_right_up,
                                self.spear2_image_right_up,
                                self.spear3_image_right_up]

        self.spear1_image_left_down = pygame.transform.rotate(spear1_1_image, angle=90)
        self.spear2_image_left_down = pygame.transform.rotate(spear2_2_image, angle=90)
        self.spear3_image_left_down = pygame.transform.rotate(spear_3_3_image, angle=90)

        self.frames_left_down = [self.spear1_image_left_down, self.spear1_image_left_down,
                                  self.spear2_image_left_down,
                                  self.spear3_image_left_down]

        self.image = self.spear1_image_left
        self.rect = self.image.get_rect()
        self.cur_frame = 0
        self.need = False
        self.spear_left = False
        self.spear_right = False
        self.spear_top = False
        self.spear_down = False
        self.spear_right_down = False
        self.spear_right_top = False
        self.spear_left_down = False
        self.spear_left_top = False

    def make_update(self, x, y, frames):
        """вернет True если надо закончить анимацию"""
        self.rect.x = x
        self.rect.y = y
        self.image = frames[self.cur_frame]
        self.image = pygame.transform.scale(self.image, (self.spear1_image_left.get_rect().w,
                                                         self.spear1_image_left.get_rect().h))
        if self.cur_frame == len(self.frames_left) - 1:
            self.need = False
            self.image = pygame.transform.scale(self.image, (0, 0))
            self.cur_frame = 0
            return True
        return False

    def update(self, x, y):
        self.image = pygame.transform.scale(self.image, (0, 0))
        if self.need:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames_left)

            if self.spear_left:
                if self.make_update(x - 25, y + 40, self.frames_left):
                    self.spear_left = False

            if self.spear_right:
                if self.make_update(x + 80, y + 40, self.frames_right):
                    self.spear_right = False

            if self.spear_top:
                if self.make_update(x + 22.5, y - 23, self.frames_top):
                    self.spear_top = False

            if self.spear_down:
                if self.make_update(x + 22.5, y + 23 + 70, self.frames_down):
                    self.spear_down = False

            if self.spear_right_down:
                if self.make_update(x + 22.5 + 55, y + 33 + 60, self.frames_right_down):
                    self.spear_right_down = False

            if self.spear_right_top:
                if self.make_update(x + 22.5 + 55, y + 33 - 52, self.frames_right_up):
                    self.spear_right_top = False

            if self.spear_left_down:
                if self.make_update(x + 22.5 - 45, y + 33 + 55, self.frames_left_down):
                    self.spear_left_down = False