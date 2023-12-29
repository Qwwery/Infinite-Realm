import pygame


def create_pol(boxes, Pol, all_sprite, pol_sprite, pol_image, board, cell_cize):
    """создание объекта пола и удаление объекта коробки"""
    pol = Pol(all_sprite, pol_sprite, pol_image, board, cell_cize)
    pol.rect.x = boxes.rect.x
    pol.rect.y = boxes.rect.y
    boxes.kill()


class Heroes(pygame.sprite.Sprite):
    def __init__(self, all_sprite, heroes_sprite, heroes_image, cell_cize, board, camera, box_sprite, pol, pol_sprite,
                 pol_image):
        super().__init__(all_sprite, heroes_sprite)
        self.image = heroes_image
        self.image = pygame.transform.scale(self.image, (cell_cize * 1.5, cell_cize * 1.5))
        self.mask = pygame.mask.from_surface(self.image)
        self.image_left = pygame.transform.flip(surface=self.image, flip_x=True, flip_y=False)
        self.image_right = self.image

        self.board = board
        self.camera = camera
        self.cell_cize = cell_cize
        self.all_sprite = all_sprite
        self.heroes_sprite = heroes_sprite
        self.box_sprite = box_sprite
        self.pol = pol
        self.pol_sprite = pol_sprite
        self.pol_image = pol_image

        self.sword = "меч"
        self.spear = "копье"
        self.bow = "лук"
        self.weapon = self.spear

        self.rect = self.image.get_rect()
        x_n, y_n = board.return_heroes_cords()
        self.rect.x = x_n * self.cell_cize - 20 + cell_cize
        self.rect.y = y_n * self.cell_cize + cell_cize - 33

    def move(self, event):
        x_her, y_her = self.board.return_heroes_cords()
        speed = self.board.cell_size

        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.rect.x += speed
            self.image = self.image_left
            if self.board.field[y_her][x_her + 1] in "KКСC":  # добавить Д
                self.rect.x -= speed
                return
            self.board.field[y_her][x_her] = '.'
            self.board.field[y_her][x_her + 1] = "@"

            self.camera.update(self, 'x')
            for elem in self.all_sprite:
                self.camera.apply(elem)

        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.rect.x -= speed
            self.image = self.image_right
            if self.board.field[y_her][x_her - 1] in "KКСC":  # добавить Д
                self.rect.x += speed
                return
            self.board.field[y_her][x_her] = '.'
            self.board.field[y_her][x_her - 1] = "@"

            self.camera.update(self, 'x')
            for elem in self.all_sprite:
                self.camera.apply(elem)

        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.rect.y -= speed
            if self.board.field[y_her - 1][x_her] in "KКСC":  # добавить Д
                self.rect.y += speed
                return
            self.board.field[y_her - 1][x_her] = "@"
            self.board.field[y_her][x_her] = "."

            self.camera.update(self, 'y')
            for elem in self.all_sprite:
                self.camera.apply(elem)

        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.rect.y += speed
            if self.board.field[y_her + 1][x_her] in "KКСC":  # добавить Д
                self.rect.y -= speed
                return
            self.board.field[y_her + 1][x_her] = "@"
            self.board.field[y_her][x_her] = "."

            self.camera.update(self, 'y')
            for elem in self.all_sprite:
                self.camera.apply(elem)

    def del_box(self, delta_x, delta_y):
        """
        функция заменяет в поле доски коробки на пустоту путем удаления спрайта коробки и создания спрайта пола
        значения y и x получены путем вычисления разниц координат спрайтов
        """
        x_her, y_her = self.board.return_heroes_cords()
        # print(delta_x, delta_y)
        # print(boxes.rect.x - self.rect.x, boxes.rect.y - self.rect.y)

        if self.weapon == self.spear and delta_x == -45 and delta_y == 33:  # копье лево одна клетка
            if self.board.field[y_her][x_her - 1] in "KК":
                self.board.field[y_her][x_her - 1] = '.'
                for boxes in self.box_sprite:
                    if boxes.rect.x - self.rect.x == -45 and boxes.rect.y - self.rect.y == 33:
                        create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image, self.board,
                                   self.cell_cize)

        elif self.weapon == self.spear and delta_x == 85 and delta_y == 33:  # копье право одна клетка
            if self.board.field[y_her][x_her + 1] in "KК":
                self.board.field[y_her][x_her + 1] = '.'
            for boxes in self.box_sprite:
                if boxes.rect.x - self.rect.x == 85 and boxes.rect.y - self.rect.y == 33:
                    create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image, self.board,
                               self.cell_cize)

        elif self.weapon == self.spear and delta_x == 20 and delta_y == 98:  # копье низ одна клетка
            if self.board.field[y_her + 1][x_her] in "KК":
                self.board.field[y_her + 1][x_her] = '.'
            for boxes in self.box_sprite:
                if boxes.rect.x - self.rect.x == 20 and boxes.rect.y - self.rect.y == 98:
                    create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image, self.board,
                               self.cell_cize)

        elif self.weapon == self.spear and delta_x == 20 and delta_y == -32:  # копье низ одна клетка
            if self.board.field[y_her - 1][x_her] in "KК":
                self.board.field[y_her - 1][x_her] = '.'
                for boxes in self.box_sprite:
                    if boxes.rect.x - self.rect.x == 20 and boxes.rect.y - self.rect.y == -32:
                        create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image, self.board,
                                   self.cell_cize)

        elif delta_x > 20 and delta_y < 0:  # право верх
            if self.weapon == self.sword:
                if self.board.field[y_her - 1][x_her + 1] in "KК":
                    self.board.field[y_her - 1][x_her + 1] = '.'
                if self.board.field[y_her][x_her + 1] in "KК":
                    self.board.field[y_her][x_her + 1] = '.'
                if self.board.field[y_her - 1][x_her] in "KК":
                    self.board.field[y_her - 1][x_her] = '.'
                for boxes in self.box_sprite:
                    if self.rect.x - boxes.rect.x == -85 and self.rect.y - boxes.rect.y == 32 or \
                            self.rect.x - boxes.rect.x == -85 and self.rect.y - boxes.rect.y == -33 or \
                            self.rect.x - boxes.rect.x == -20 and self.rect.y - boxes.rect.y == 32:
                        create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image, self.board,
                                   self.cell_cize)
            elif self.weapon == self.spear:
                if self.board.field[y_her - 1][x_her] != '.' or self.board.field[y_her][x_her + 1] != '.':
                    return
                else:
                    if self.board.field[y_her - 1][x_her + 1] in "КK":
                        self.board.field[y_her - 1][x_her + 1] = '.'
                        for boxes in self.box_sprite:
                            if boxes.rect.x - self.rect.x == 85 and boxes.rect.y - self.rect.y == -32:
                                create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image,
                                           self.board,
                                           self.cell_cize)

        elif delta_x > 0 and delta_y == 33:  # право
            if self.weapon == self.sword:
                if self.board.field[y_her - 1][x_her + 1] in "KК":
                    self.board.field[y_her - 1][x_her + 1] = '.'
                if self.board.field[y_her][x_her + 1] in "KК":
                    self.board.field[y_her][x_her + 1] = '.'
                if self.board.field[y_her + 1][x_her + 1] in "KК":
                    self.board.field[y_her + 1][x_her + 1] = '.'

                for boxes in self.box_sprite:
                    if self.rect.x - boxes.rect.x == -85 and self.rect.y - boxes.rect.y == -33 or \
                            self.rect.x - boxes.rect.x == -85 and self.rect.y - boxes.rect.y == 32 or \
                            self.rect.x - boxes.rect.x == -85 and self.rect.y - boxes.rect.y == -98:
                        create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image, self.board,
                                   self.cell_cize)
            elif self.weapon == self.spear:
                if self.board.field[y_her][x_her + 1] != '.':
                    if self.board.field[y_her][x_her + 1] in "КK":
                        self.board.field[y_her][x_her + 1] = '.'
                        for boxes in self.box_sprite:
                            if boxes.rect.x - self.rect.x == 85 and boxes.rect.y - self.rect.y == 33:
                                create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image,
                                           self.board, self.cell_cize)
                else:
                    if x_her + 2 < len(self.board.field[0]) and self.board.field[y_her][x_her + 2] in "КК":
                        self.board.field[y_her][x_her + 2] = '.'
                        for boxes in self.box_sprite:
                            if boxes.rect.x - self.rect.x == 150 and boxes.rect.y - self.rect.y == 33:
                                create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image,
                                           self.board,
                                           self.cell_cize)

        elif delta_x > 20 and delta_y > 0:  # право низ
            if self.weapon == self.sword:
                if self.board.field[y_her][x_her + 1] in "КK":
                    self.board.field[y_her][x_her + 1] = '.'
                if self.board.field[y_her + 1][x_her + 1] in "КK":
                    self.board.field[y_her + 1][x_her + 1] = '.'
                if self.board.field[y_her + 1][x_her] in "КK":
                    self.board.field[y_her + 1][x_her] = '.'

                for boxes in self.box_sprite:
                    if self.rect.x - boxes.rect.x == -85 and self.rect.y - boxes.rect.y == -98 or \
                            self.rect.x - boxes.rect.x == -85 and self.rect.y - boxes.rect.y == -33 or \
                            self.rect.x - boxes.rect.x == -20 and self.rect.y - boxes.rect.y == -98:
                        create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image, self.board,
                                   self.cell_cize)
            elif self.weapon == self.spear:
                if self.board.field[y_her][x_her + 1] != '.' or self.board.field[y_her + 1][x_her] != '.':
                    return
                else:
                    if self.board.field[y_her + 1][x_her + 1] in "КK":
                        self.board.field[y_her + 1][x_her + 1] = '.'
                        for boxes in self.box_sprite:
                            if boxes.rect.x - self.rect.x == 85 and boxes.rect.y - self.rect.y == 98:
                                create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image,
                                           self.board,
                                           self.cell_cize)

        elif delta_x == 20 and delta_y < 0:  # верх
            if self.weapon == self.sword:
                if self.board.field[y_her - 1][x_her] in "KК":
                    self.board.field[y_her - 1][x_her] = '.'
                if self.board.field[y_her - 1][x_her - 1] in "KК":
                    self.board.field[y_her - 1][x_her - 1] = '.'
                if self.board.field[y_her - 1][x_her + 1] in "KК":
                    self.board.field[y_her - 1][x_her + 1] = '.'

                for boxes in self.box_sprite:
                    if self.rect.x - boxes.rect.x == 45 and self.rect.y - boxes.rect.y == 32 or \
                            self.rect.x - boxes.rect.x == -20 and self.rect.y - boxes.rect.y == 32 or \
                            self.rect.x - boxes.rect.x == -85 and self.rect.y - boxes.rect.y == 32:
                        create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image, self.board,
                                   self.cell_cize)
            elif self.weapon == self.spear:
                if self.board.field[y_her - 1][x_her] != '.':
                    if self.board.field[y_her - 1][x_her] in 'КK':
                        self.board.field[y_her - 1][x_her] = '.'
                        for boxes in self.box_sprite:
                            if boxes.rect.x - self.rect.x == 20 and boxes.rect.y - self.rect.y == -32:
                                create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image,
                                           self.board,
                                           self.cell_cize)
                else:
                    if y_her - 2 >= 0 and self.board.field[y_her - 2][x_her] in 'КK':
                        self.board.field[y_her - 2][x_her] = '.'
                        for boxes in self.box_sprite:
                            if boxes.rect.x - self.rect.x == 20 and boxes.rect.y - self.rect.y == -97:
                                create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image,
                                           self.board,
                                           self.cell_cize)

        elif delta_x == 20 and delta_y > 0:  # низ
            if self.weapon == self.sword:
                if self.board.field[y_her + 1][x_her] in "KК":
                    self.board.field[y_her + 1][x_her] = '.'
                if self.board.field[y_her + 1][x_her - 1] in "KК":
                    self.board.field[y_her + 1][x_her - 1] = '.'
                if self.board.field[y_her + 1][x_her + 1] in "KК":
                    self.board.field[y_her + 1][x_her + 1] = '.'

                for boxes in self.box_sprite:
                    if self.rect.x - boxes.rect.x == 45 and self.rect.y - boxes.rect.y == -98 or \
                            self.rect.x - boxes.rect.x == -20 and self.rect.y - boxes.rect.y == -98 or \
                            self.rect.x - boxes.rect.x == -85 and self.rect.y - boxes.rect.y == -98:
                        create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image, self.board,
                                   self.cell_cize)
            elif self.weapon == self.spear:
                if self.board.field[y_her + 1][x_her] != '.':
                    if self.board.field[y_her + 1][x_her] in 'КK':
                        self.board.field[y_her + 1][x_her] = '.'
                        for boxes in self.box_sprite:
                            if boxes.rect.x - self.rect.x == 20 and boxes.rect.y - self.rect.y == 98:
                                create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image,
                                           self.board,
                                           self.cell_cize)
                else:
                    if y_her + 2 < len(self.board.field) and self.board.field[y_her + 2][x_her] in 'КK':
                        self.board.field[y_her + 2][x_her] = '.'
                        for boxes in self.box_sprite:
                            if boxes.rect.x - self.rect.x == 20 and boxes.rect.y - self.rect.y == 163:
                                create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image,
                                           self.board,
                                           self.cell_cize)

        elif delta_x < 0 and delta_y > 33:  # лево низ
            if self.weapon == self.sword:
                if self.board.field[y_her + 1][x_her - 1] in "KК":
                    self.board.field[y_her + 1][x_her - 1] = '.'
                if self.board.field[y_her][x_her - 1] in "KК":
                    self.board.field[y_her][x_her - 1] = '.'
                if self.board.field[y_her + 1][x_her] in "KК":
                    self.board.field[y_her + 1][x_her] = '.'

                for boxes in self.box_sprite:
                    if self.rect.x - boxes.rect.x == 45 and self.rect.y - boxes.rect.y == -33 or \
                            self.rect.x - boxes.rect.x == 45 and self.rect.y - boxes.rect.y == -98 or \
                            self.rect.x - boxes.rect.x == -20 and self.rect.y - boxes.rect.y == -98:
                        create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image, self.board,
                                   self.cell_cize)
            elif self.weapon == self.spear:
                if self.board.field[y_her][x_her - 1] != '.' or self.board.field[y_her + 1][x_her] != '.':
                    return
                else:
                    if self.board.field[y_her + 1][x_her - 1] in "KК":
                        self.board.field[y_her + 1][x_her - 1] = '.'
                        for boxes in self.box_sprite:
                            if self.rect.x - boxes.rect.x == 45 and self.rect.y - boxes.rect.y == -98:
                                create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image,
                                           self.board,
                                           self.cell_cize)

        elif delta_x < 0 and delta_y == 33:  # лево
            if self.weapon == self.sword:
                if self.board.field[y_her - 1][x_her - 1] in "KК":
                    self.board.field[y_her - 1][x_her - 1] = '.'
                if self.board.field[y_her][x_her - 1] in "KК":
                    self.board.field[y_her][x_her - 1] = '.'
                if self.board.field[y_her + 1][x_her - 1] in "KК":
                    self.board.field[y_her + 1][x_her - 1] = '.'

                for boxes in self.box_sprite:
                    if self.rect.x - boxes.rect.x == 45 and self.rect.y - boxes.rect.y == -33 or \
                            self.rect.x - boxes.rect.x == 45 and self.rect.y - boxes.rect.y == 32 or \
                            self.rect.x - boxes.rect.x == 45 and self.rect.y - boxes.rect.y == -98:
                        create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image, self.board,
                                   self.cell_cize)
            elif self.weapon == self.spear:
                if self.board.field[y_her][x_her - 1] != ".":
                    if self.board.field[y_her][x_her - 1] in "КK":
                        self.board.field[y_her][x_her - 1] = '.'
                        for boxes in self.box_sprite:
                            if self.rect.x - boxes.rect.x == 45 and self.rect.y - boxes.rect.y == -33:
                                create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image,
                                           self.board,
                                           self.cell_cize)
                else:
                    if x_her - 2 >= 0 and self.board.field[y_her][x_her - 2] in "KК":
                        self.board.field[y_her][x_her - 2] = '.'
                        for boxes in self.box_sprite:
                            if self.rect.x - boxes.rect.x == 110 and self.rect.y - boxes.rect.y == -33:
                                create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image,
                                           self.board,
                                           self.cell_cize)

        elif delta_x < 0 and delta_y < 0:  # лево верх
            if self.weapon == self.sword:
                if self.board.field[y_her - 1][x_her] in "KК":
                    self.board.field[y_her - 1][x_her] = '.'
                if self.board.field[y_her][x_her - 1] in "KК":
                    self.board.field[y_her][x_her - 1] = '.'
                if self.board.field[y_her - 1][x_her - 1] in "KК":
                    self.board.field[y_her - 1][x_her - 1] = '.'

                for boxes in self.box_sprite:
                    if self.rect.x - boxes.rect.x == 45 and self.rect.y - boxes.rect.y == 32 or \
                            self.rect.x - boxes.rect.x == -20 and self.rect.y - boxes.rect.y == 32 or \
                            self.rect.x - boxes.rect.x == 45 and self.rect.y - boxes.rect.y == -33:
                        create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image, self.board,
                                   self.cell_cize)
            elif self.weapon == self.spear:
                if self.board.field[y_her][x_her - 1] != '.' or self.board.field[y_her - 1][x_her] != '.':
                    return
                else:
                    if self.board.field[y_her - 1][x_her - 1] in "КK":
                        self.board.field[y_her - 1][x_her - 1] = '.'
                        for boxes in self.box_sprite:
                            if self.rect.x - boxes.rect.x == 45 and self.rect.y - boxes.rect.y == 32:
                                create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image,
                                           self.board,
                                           self.cell_cize)

    def left_box_attack(self, *args):
        """
        проверка корректности атаки коробок, когда герой находится левее коробки
        атака совершается в случае правильности логики
        """
        for elem in self.all_sprite:
            if elem.rect.collidepoint(args[0].pos):
                if self.rect.x - 20 <= elem.rect.x:
                    self.del_box(elem.rect.x - self.rect.x, elem.rect.y - self.rect.y)

    def right_box_attack(self, *args):
        """
        проверка корректности атаки коробок, когда герой находится правее коробки
        атака совершается в случае правильности логики
        """
        for elem in self.all_sprite:
            if elem.rect.collidepoint(args[0].pos):
                if self.rect.x + 20 >= elem.rect.x:
                    self.del_box(elem.rect.x - self.rect.x, elem.rect.y - self.rect.y)

    def attack(self, *args):
        if self.image == self.image_left:  # герой находится слева
            self.left_box_attack(*args)
        else:  # герой находится справа
            self.right_box_attack(*args)
