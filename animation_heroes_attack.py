import pygame


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, animation_sprite, spear1_image, spear2_image, spear3_image, spear1_1_image, spear2_2_image,
                 spear_3_3_image, sword1_image, sword2_image, sword3_image, sword4_image, sword5_image, sword_image6,
                 top_sword1_image, top_sword2_image, top_sword3_image, top_sword4_image, top_sword5_image,
                 down_sword1_image, down_sword2_image, down_sword3_image, down_sword4_image, down_sword5_image):
        super().__init__(animation_sprite)
        self.x, self.y = 45, 45

        self.init_spear(spear1_image, spear2_image, spear3_image, spear1_1_image, spear2_2_image,
                        spear_3_3_image)

        self.init_sword(sword1_image, sword2_image, sword3_image, sword4_image, sword5_image, sword_image6,
                        top_sword1_image, top_sword2_image, top_sword3_image, top_sword4_image, top_sword5_image,
                        down_sword1_image, down_sword2_image, down_sword3_image, down_sword4_image, down_sword5_image)

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

        self.sword_left = False
        self.sword_right = False
        self.sword_top = False
        self.sword_down = False
        self.sword_left_top = False
        self.sword_left_down = False
        self.sword_right_top = False
        self.sword_right_down = False

    def init_spear(self, spear1_image, spear2_image, spear3_image, spear1_1_image, spear2_2_image,
                   spear_3_3_image):
        """инициализация список и картинок, связанная с тычковой анимацией"""

        self.spear1_image_left = pygame.transform.scale(spear1_image, (self.x, self.y))
        self.spear2_image_left = pygame.transform.scale(spear2_image, (self.x, self.y))
        self.spear3_image_left = pygame.transform.scale(spear3_image, (self.x, self.y))
        self.frames_left_spear = [self.spear1_image_left, self.spear1_image_left, self.spear2_image_left,
                                  self.spear3_image_left]

        self.spear1_image_right = pygame.transform.flip(self.spear1_image_left, flip_x=1, flip_y=0)
        self.spear2_image_right = pygame.transform.flip(self.spear2_image_left, flip_x=1, flip_y=0)
        self.spear3_image_right = pygame.transform.flip(self.spear3_image_left, flip_x=1, flip_y=0)
        self.frames_right_spear = [self.spear1_image_right, self.spear1_image_right, self.spear2_image_right,
                                   self.spear3_image_right]

        self.spear1_image_top = pygame.transform.rotate(spear1_image, angle=-90)
        self.spear2_image_top = pygame.transform.rotate(spear2_image, angle=-90)
        self.spear3_image_top = pygame.transform.rotate(spear3_image, angle=-90)
        self.frames_top_spear = [self.spear1_image_top, self.spear1_image_top, self.spear2_image_top,
                                 self.spear3_image_top]

        self.spear1_image_down = pygame.transform.rotate(spear1_image, angle=90)
        self.spear2_image_down = pygame.transform.rotate(spear2_image, angle=90)
        self.spear3_image_down = pygame.transform.rotate(spear3_image, angle=90)
        self.frames_down_spear = [self.spear1_image_down, self.spear1_image_down, self.spear2_image_down,
                                  self.spear3_image_down]

        self.spear1_image_right_down = pygame.transform.rotate(spear1_1_image, angle=180)
        self.spear2_image_right_down = pygame.transform.rotate(spear2_2_image, angle=180)
        self.spear3_image_right_down = pygame.transform.rotate(spear_3_3_image, angle=180)

        self.frames_right_down_spear = [self.spear1_image_right_down, self.spear1_image_right_down,
                                        self.spear2_image_right_down,
                                        self.spear3_image_right_down]

        self.spear1_image_right_up = pygame.transform.rotate(spear1_1_image, angle=-90)
        self.spear2_image_right_up = pygame.transform.rotate(spear2_2_image, angle=-90)
        self.spear3_image_right_up = pygame.transform.rotate(spear_3_3_image, angle=-90)

        self.frames_right_up_spear = [self.spear1_image_right_up, self.spear1_image_right_up,
                                      self.spear2_image_right_up,
                                      self.spear3_image_right_up]

        self.spear1_image_left_down = pygame.transform.rotate(spear1_1_image, angle=90)
        self.spear2_image_left_down = pygame.transform.rotate(spear2_2_image, angle=90)
        self.spear3_image_left_down = pygame.transform.rotate(spear_3_3_image, angle=90)

        self.frames_left_down_spear = [self.spear1_image_left_down, self.spear1_image_left_down,
                                       self.spear2_image_left_down,
                                       self.spear3_image_left_down]

        self.spear1_image_left_up = spear1_1_image
        self.spear2_image_left_up = spear2_2_image
        self.spear3_image_left_up = spear_3_3_image

        self.frames_left_up_spear = [self.spear1_image_left_up, self.spear1_image_left_up,
                                     self.spear2_image_left_up,
                                     self.spear3_image_left_up]

        self.spear_list = [self.frames_left_up_spear, self.frames_left_down_spear, self.frames_right_up_spear,
                           self.frames_right_down_spear,
                           self.frames_left_spear, self.frames_right_spear, self.frames_top_spear,
                           self.frames_down_spear]

    def init_sword(self, sword1_image, sword2_image, sword3_image, sword4_image, sword5_image, sword_image6,
                   top_sword1_image, top_sword2_image, top_sword3_image, top_sword4_image, top_sword5_image,
                   down_sword1_image, down_sword2_image, down_sword3_image, down_sword4_image, down_sword5_image):
        """инициализация список и картинок, связанная с анимацией замаха"""

        self.frames_left_sword = [sword1_image, sword2_image, sword3_image, sword4_image, sword5_image, sword_image6]

        for i in range(len(self.frames_left_sword)):
            self.frames_left_sword[i] = pygame.transform.rotate(self.frames_left_sword[i], angle=39)
            self.frames_left_sword[i] = pygame.transform.scale(self.frames_left_sword[i],
                                                               (self.frames_left_sword[i].get_rect().w + 4,
                                                                self.frames_left_sword[i].get_rect().h + 11))

        self.frames_right_sword = [pygame.transform.flip(sword1_image, flip_x=1, flip_y=0),
                                   pygame.transform.flip(sword2_image, flip_x=1, flip_y=0),
                                   pygame.transform.flip(sword3_image, flip_x=1, flip_y=0),
                                   pygame.transform.flip(sword4_image, flip_x=1, flip_y=0),
                                   pygame.transform.flip(sword5_image, flip_x=1, flip_y=0),
                                   pygame.transform.flip(sword_image6, flip_x=1, flip_y=0)]

        for i in range(len(self.frames_right_sword)):
            self.frames_right_sword[i] = pygame.transform.rotate(self.frames_right_sword[i], angle=-29)
            self.frames_right_sword[i] = pygame.transform.scale(self.frames_right_sword[i],
                                                                (self.frames_right_sword[i].get_rect().w + 4,
                                                                 self.frames_right_sword[i].get_rect().h + 11))

        angle = 13
        self.frames_left_up_sword = [pygame.transform.rotate(sword1_image, angle),
                                     pygame.transform.rotate(sword2_image, angle),
                                     pygame.transform.rotate(sword3_image, angle),
                                     pygame.transform.rotate(sword4_image, angle),
                                     pygame.transform.rotate(sword5_image, angle)]
        angle = 43
        self.frames_left_down_sword = [pygame.transform.rotate(sword1_image, angle),
                                       pygame.transform.rotate(sword2_image, angle),
                                       pygame.transform.rotate(sword3_image, angle),
                                       pygame.transform.rotate(sword4_image, angle),
                                       pygame.transform.rotate(sword5_image, angle)]
        angle = -13
        self.frames_right_up_sword = [
            pygame.transform.flip(pygame.transform.rotate(sword1_image, angle), flip_x=1, flip_y=0),
            pygame.transform.flip(pygame.transform.rotate(sword2_image, angle), flip_x=1, flip_y=0),
            pygame.transform.flip(pygame.transform.rotate(sword3_image, angle), flip_x=1, flip_y=0),
            pygame.transform.flip(pygame.transform.rotate(sword4_image, angle), flip_x=1, flip_y=0),
            pygame.transform.flip(pygame.transform.rotate(sword5_image, angle), flip_x=1, flip_y=0)
        ]
        angle = 43
        self.frames_right_down_sword = [
            pygame.transform.flip(pygame.transform.rotate(sword1_image, angle), flip_x=1, flip_y=0),
            pygame.transform.flip(pygame.transform.rotate(sword2_image, angle), flip_x=1, flip_y=0),
            pygame.transform.flip(pygame.transform.rotate(sword3_image, angle), flip_x=1, flip_y=0),
            pygame.transform.flip(pygame.transform.rotate(sword4_image, angle), flip_x=1, flip_y=0),
            pygame.transform.flip(pygame.transform.rotate(sword5_image, angle), flip_x=1, flip_y=0)]

        self.frames_top_sword_left = [top_sword1_image, top_sword2_image, top_sword3_image, top_sword4_image,
                                      top_sword5_image]
        size = 111
        for i in range(len(self.frames_top_sword_left)):
            self.frames_top_sword_left[i] = pygame.transform.scale(self.frames_top_sword_left[i], (size, size))
            self.frames_top_sword_left[i] = pygame.transform.rotate(self.frames_top_sword_left[i], angle=8.5)

        self.frames_top_sword_right = self.frames_top_sword_left.copy()
        for i in range(len(self.frames_top_sword_right)):
            self.frames_top_sword_right[i] = pygame.transform.flip(self.frames_top_sword_right[i], flip_x=1, flip_y=0)
            self.frames_top_sword_right[i] = pygame.transform.rotate(self.frames_top_sword_right[i], angle=-1)

        size = 111
        self.frames_down_sword_left = [down_sword1_image, down_sword2_image, down_sword3_image, down_sword4_image,
                                       down_sword5_image]

        for i in range(len(self.frames_down_sword_left)):
            self.frames_down_sword_left[i] = pygame.transform.scale(self.frames_down_sword_left[i], (size, size))
            self.frames_down_sword_left[i] = pygame.transform.rotate(self.frames_down_sword_left[i], angle=43)

        self.frames_down_sword_right = self.frames_down_sword_left.copy()
        for i in range(len(self.frames_down_sword_right)):
            self.frames_down_sword_right[i] = pygame.transform.flip(self.frames_down_sword_right[i], flip_x=1, flip_y=0)
            self.frames_down_sword_right[i] = pygame.transform.rotate(self.frames_down_sword_right[i], angle=-1)

        self.sword_list = [self.frames_left_sword, self.frames_right_sword, self.frames_top_sword_left,
                           self.frames_down_sword_left, self.frames_left_up_sword, self.frames_left_down_sword,
                           self.frames_right_up_sword, self.frames_right_down_sword]

    def make_update(self, x, y, frames):
        """
        отображение картинки из списка frames по индексу self.cur_frame
        если картинка последняя, то прекращаем отображение, изменяя ее размеры на 0

        вернет True если надо закончить анимацию
        """

        self.rect.x = x
        self.rect.y = y
        self.image = frames[self.cur_frame]
        if frames in self.spear_list:
            self.image = pygame.transform.scale(self.image, (self.spear1_image_left.get_rect().w,
                                                             self.spear1_image_left.get_rect().h))
        else:
            self.image = pygame.transform.scale(self.image, (frames[0].get_rect().w - 10,
                                                             frames[0].get_rect().h - 10))

        if self.cur_frame == len(frames) - 1:
            self.need = False
            self.image = pygame.transform.scale(self.image, (0, 0))
            self.cur_frame = 0
            return True
        return False

    def update(self, x, y, side):
        """
        принимает координаты героя, сторону, в которую он смотрит
        если необходимо сделать анимацию, выбирает сторону и оружие
        """

        if self.need:
            if self.spear_left:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames_left_spear)
                if self.make_update(x - 25, y + 40, self.frames_left_spear):
                    self.spear_left = False

            elif self.spear_right:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames_left_spear)
                if self.make_update(x + 80, y + 40, self.frames_right_spear):
                    self.spear_right = False

            elif self.spear_top:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames_left_spear)
                if self.make_update(x + 22.5, y - 23, self.frames_top_spear):
                    self.spear_top = False

            elif self.spear_down:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames_left_spear)
                if self.make_update(x + 22.5, y + 23 + 70, self.frames_down_spear):
                    self.spear_down = False

            elif self.spear_right_down:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames_left_spear)
                if self.make_update(x + 22.5 + 55, y + 33 + 60, self.frames_right_down_spear):
                    self.spear_right_down = False

            elif self.spear_right_top:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames_left_spear)
                if self.make_update(x + 22.5 + 55, y + 33 - 52, self.frames_right_up_spear):
                    self.spear_right_top = False

            elif self.spear_left_down:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames_left_spear)
                if self.make_update(x + 22.5 - 45, y + 33 + 55, self.frames_left_down_spear):
                    self.spear_left_down = False

            elif self.spear_left_top:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames_left_spear)
                if self.make_update(x + 22.5 - 45, y + 43 - 55, self.frames_left_up_spear):
                    self.spear_left_top = False

            elif self.sword_left:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames_left_sword)
                if self.make_update(x + 22.5 - 80, y + 43 - 61, self.frames_left_sword):
                    self.sword_left = False

            elif self.sword_right:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames_left_sword)
                if self.make_update(x + 22.5 - 40 + 45, y + 43 - 61, self.frames_right_sword):
                    self.sword_right = False

            elif self.sword_top:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames_left_sword)
                if side == 'left':
                    if self.make_update(x - 9.15, y - 36, self.frames_top_sword_left):
                        self.sword_top = False
                elif side == 'right':
                    if self.make_update(x - 6.2, y - 33, self.frames_top_sword_right):
                        self.sword_top = False

            elif self.sword_down:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames_down_sword_left)
                if side == 'left':
                    if self.make_update(x - 30.456, y + 30, self.frames_down_sword_left):
                        self.sword_down = False
                elif side == 'right':
                    if self.make_update(x - 19.5, y + 30, self.frames_down_sword_right):
                        self.sword_down = False

            elif self.sword_left_top:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames_left_sword)
                if self.make_update(x + 22.5 - 45, y + 43 - 65, self.frames_left_up_sword):
                    self.sword_left_top = False

            elif self.sword_left_down:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames_left_sword)
                if self.make_update(x + 22.5 - 70, y + 3, self.frames_left_down_sword):
                    self.sword_left_down = False

            elif self.sword_right_top:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames_left_sword)
                if self.make_update(x + 22.5, y + 43 - 65, self.frames_right_up_sword):
                    self.sword_right_top = False

            elif self.sword_right_down:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames_left_sword)
                if self.make_update(x + 20.5, y + 3, self.frames_right_down_sword):
                    self.sword_right_down = False
