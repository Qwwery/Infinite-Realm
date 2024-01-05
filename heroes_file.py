import pygame


def create_pol(elem, Pol, all_sprite, pol_sprite, pol_image, board, cell_cize):
    """создание объекта пола и удаление объекта коробки"""
    pol = Pol(all_sprite, pol_sprite, pol_image, board, cell_cize)
    pol.rect.x = elem.rect.x
    pol.rect.y = elem.rect.y
    elem.kill()


def check_spear_one_cells(self, y_her, x_her, delta_x, delta_y):  # возможно потом удалить
    """проверка клеток, если ударить копьем на одну клетку, вернет False, если больше не надо проверять"""
    if self.weapon == self.spear and delta_x == -45 and delta_y == 33:  # копье лево одна клетка
        if self.board.field[y_her][x_her - 1] in "KК.ЛE":
            if self.board.field[y_her][x_her - 1] not in 'ЛE':
                self.board.field[y_her][x_her - 1] = '.'
            for boxes in self.box_sprite:
                if boxes.rect.x - self.rect.x == -45 and boxes.rect.y - self.rect.y == 33:
                    create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image, self.board,
                               self.cell_cize)

            for enemy in self.enemy_sprite:
                if enemy.rect.x - self.rect.x == -40 and enemy.rect.y - self.rect.y == 38:
                    enemy.hp -= 50
                    if enemy.hp <= 0:
                        self.board.field[y_her][x_her - 1] = '.'
                        enemy.kill()

        return False

    elif self.weapon == self.spear and delta_x == 85 and delta_y == 33:  # копье право одна клетка
        if self.board.field[y_her][x_her + 1] in "KК.ЛE":
            if self.board.field[y_her][x_her + 1] not in 'ЛE':
                self.board.field[y_her][x_her + 1] = '.'
        for boxes in self.box_sprite:
            if boxes.rect.x - self.rect.x == 85 and boxes.rect.y - self.rect.y == 33:
                create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image, self.board,
                           self.cell_cize)

        for enemy in self.enemy_sprite:
            if enemy.rect.x - self.rect.x == 90 and enemy.rect.y - self.rect.y == 38:
                enemy.hp -= 50
                if enemy.hp <= 0:
                    self.board.field[y_her][x_her + 1] = '.'
                    enemy.kill()
        return False

    elif self.weapon == self.spear and delta_x == 20 and delta_y == 98:  # копье низ одна клетка
        if self.board.field[y_her + 1][x_her] in "KК.ЛE":
            if self.board.field[y_her + 1][x_her] not in 'ЛE':
                self.board.field[y_her + 1][x_her] = '.'
        for boxes in self.box_sprite:
            if boxes.rect.x - self.rect.x == 20 and boxes.rect.y - self.rect.y == 98:
                create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image, self.board,
                           self.cell_cize)

        for enemy in self.enemy_sprite:
            if enemy.rect.x - self.rect.x == 25 and enemy.rect.y - self.rect.y == 103:
                enemy.hp -= 50
                if enemy.hp <= 0:
                    self.board.field[y_her + 1][x_her] = '.'
                    enemy.kill()
        return False

    elif self.weapon == self.spear and delta_x == 20 and delta_y == -32:  # копье верх одна клетка
        if self.board.field[y_her - 1][x_her] in "KК.ЛE":
            if self.board.field[y_her - 1][x_her] not in 'ЛE':
                self.board.field[y_her - 1][x_her] = '.'
            for boxes in self.box_sprite:
                if boxes.rect.x - self.rect.x == 20 and boxes.rect.y - self.rect.y == -32:
                    create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image, self.board,
                               self.cell_cize)

            for enemy in self.enemy_sprite:
                if enemy.rect.x - self.rect.x == 25 and enemy.rect.y - self.rect.y == -27:
                    enemy.hp -= 50
                    if enemy.hp <= 0:
                        self.board.field[y_her - 1][x_her] = '.'
                        enemy.kill()
        return False
    return True


def check_right_top(self, y_her, x_her):  # право верх
    if self.weapon == self.sword:
        if self.board.field[y_her - 1][x_her + 1] in "KК.ЛE":
            if self.board.field[y_her - 1][x_her + 1] not in 'ЛE':
                self.board.field[y_her - 1][x_her + 1] = '.'
        if self.board.field[y_her][x_her + 1] in "KК.ЛE":
            if self.board.field[y_her][x_her + 1] not in 'ЛE':
                self.board.field[y_her][x_her + 1] = '.'
        if self.board.field[y_her - 1][x_her] in "KК.ЛE":
            if self.board.field[y_her - 1][x_her] not in 'ЛE':
                self.board.field[y_her - 1][x_her] = '.'

        for boxes in self.box_sprite:
            if self.rect.x - boxes.rect.x == -85 and self.rect.y - boxes.rect.y == 32 or \
                    self.rect.x - boxes.rect.x == -85 and self.rect.y - boxes.rect.y == -33 or \
                    self.rect.x - boxes.rect.x == -20 and self.rect.y - boxes.rect.y == 32:
                create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image, self.board,
                           self.cell_cize)

    elif self.weapon == self.spear:
        if self.board.field[y_her - 1][x_her] not in '.Л' or self.board.field[y_her][x_her + 1] not in '.Л':
            return
        else:
            if self.board.field[y_her - 1][x_her + 1] in "КK.ЛE":
                if self.board.field[y_her - 1][x_her + 1] not in 'ЛE':
                    self.board.field[y_her - 1][x_her + 1] = '.'
                for boxes in self.box_sprite:
                    if boxes.rect.x - self.rect.x == 85 and boxes.rect.y - self.rect.y == -32:
                        create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image,
                                   self.board, self.cell_cize)

                for enemy in self.enemy_sprite:
                    if enemy.rect.x - self.rect.x == 90 and enemy.rect.y - self.rect.y == -27:
                        enemy.hp -= 50
                        if enemy.hp <= 0:
                            self.board.field[y_her - 1][x_her + 1] = '.'
                            enemy.kill()


def check_right(self, y_her, x_her):  # право
    if self.weapon == self.sword:
        if self.board.field[y_her - 1][x_her + 1] in "KК.ЛE":
            if self.board.field[y_her - 1][x_her + 1] not in 'ЛE':
                self.board.field[y_her - 1][x_her + 1] = '.'
        if self.board.field[y_her][x_her + 1] in "KК.ЛE":
            if self.board.field[y_her][x_her + 1] not in 'ЛE':
                self.board.field[y_her][x_her + 1] = '.'
        if self.board.field[y_her + 1][x_her + 1] in "KК.ЛE":
            if self.board.field[y_her + 1][x_her + 1] not in 'ЛE':
                self.board.field[y_her + 1][x_her + 1] = '.'

        for boxes in self.box_sprite:
            if self.rect.x - boxes.rect.x == -85 and self.rect.y - boxes.rect.y == -33 or \
                    self.rect.x - boxes.rect.x == -85 and self.rect.y - boxes.rect.y == 32 or \
                    self.rect.x - boxes.rect.x == -85 and self.rect.y - boxes.rect.y == -98:
                create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image, self.board,
                           self.cell_cize)


    elif self.weapon == self.spear:
        if self.board.field[y_her][x_her + 1] not in '.Л':
            if self.board.field[y_her][x_her + 1] in "КK.ЛE":
                if self.board.field[y_her][x_her + 1] not in 'ЛE':
                    self.board.field[y_her][x_her + 1] = '.'
                for boxes in self.box_sprite:
                    if boxes.rect.x - self.rect.x == 85 and boxes.rect.y - self.rect.y == 33:
                        create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image,
                                   self.board, self.cell_cize)

                for enemy in self.enemy_sprite:
                    if enemy.rect.x - self.rect.x == 90 and enemy.rect.y - self.rect.y == 38:
                        enemy.hp -= 50
                        if enemy.hp <= 0:
                            enemy.kill()
                            self.board.field[y_her][x_her + 1] = '.'
        else:
            if x_her + 2 < len(self.board.field[0]) and self.board.field[y_her][x_her + 2] in "КK.ЛE":
                if self.board.field[y_her][x_her + 2] not in 'ЛE':
                    self.board.field[y_her][x_her + 2] = '.'
                for boxes in self.box_sprite:
                    if boxes.rect.x - self.rect.x == 150 and boxes.rect.y - self.rect.y == 33:
                        create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image,
                                   self.board,
                                   self.cell_cize)

                for enemy in self.enemy_sprite:
                    if enemy.rect.x - self.rect.x == 155 and enemy.rect.y - self.rect.y == 38:
                        enemy.hp -= 50
                        if enemy.hp <= 0:
                            enemy.kill()
                            self.board.field[y_her][x_her + 2] = '.'


def check_right_down(self, y_her, x_her):  # право низ
    if self.weapon == self.sword:
        if self.board.field[y_her][x_her + 1] in "КK.ЛE":
            if self.board.field[y_her][x_her + 1] not in 'ЛE':
                self.board.field[y_her][x_her + 1] = '.'
        if self.board.field[y_her + 1][x_her + 1] in "КK.ЛE":
            if self.board.field[y_her + 1][x_her + 1] not in 'ЛE':
                self.board.field[y_her + 1][x_her + 1] = '.'
        if self.board.field[y_her + 1][x_her] in "КK.ЛE":
            if self.board.field[y_her + 1][x_her] not in 'ЛE':
                self.board.field[y_her + 1][x_her] = '.'

        for boxes in self.box_sprite:
            if self.rect.x - boxes.rect.x == -85 and self.rect.y - boxes.rect.y == -98 or \
                    self.rect.x - boxes.rect.x == -85 and self.rect.y - boxes.rect.y == -33 or \
                    self.rect.x - boxes.rect.x == -20 and self.rect.y - boxes.rect.y == -98:
                create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image, self.board,
                           self.cell_cize)
    elif self.weapon == self.spear:
        if self.board.field[y_her][x_her + 1] not in '.Л' or self.board.field[y_her + 1][x_her] not in '.Л':
            return
        else:
            if self.board.field[y_her + 1][x_her + 1] in "КK.ЛE":
                if self.board.field[y_her + 1][x_her + 1] not in 'ЛE':
                    self.board.field[y_her + 1][x_her + 1] = '.'
                for boxes in self.box_sprite:
                    if boxes.rect.x - self.rect.x == 85 and boxes.rect.y - self.rect.y == 98:
                        create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image, self.board,
                                   self.cell_cize)

                for enemy in self.enemy_sprite:
                    if enemy.rect.x - self.rect.x == 90 and enemy.rect.y - self.rect.y == 103:
                        enemy.hp -= 50
                        if enemy.hp <= 0:
                            self.board.field[y_her + 1][x_her + 1] = '.'
                            enemy.kill()


def check_top(self, y_her, x_her):  # верх
    if self.weapon == self.sword:
        if self.board.field[y_her - 1][x_her] in "KК.ЛE":
            if self.board.field[y_her - 1][x_her] not in 'ЛE':
                self.board.field[y_her - 1][x_her] = '.'
        if self.board.field[y_her - 1][x_her - 1] in "KК.ЛE":
            if self.board.field[y_her - 1][x_her - 1] not in 'ЛE':
                self.board.field[y_her - 1][x_her - 1] = '.'
        if self.board.field[y_her - 1][x_her + 1] in "KК.ЛE":
            if self.board.field[y_her - 1][x_her + 1] not in 'ЛE':
                self.board.field[y_her - 1][x_her + 1] = '.'

        for boxes in self.box_sprite:
            if self.rect.x - boxes.rect.x == 45 and self.rect.y - boxes.rect.y == 32 or \
                    self.rect.x - boxes.rect.x == -20 and self.rect.y - boxes.rect.y == 32 or \
                    self.rect.x - boxes.rect.x == -85 and self.rect.y - boxes.rect.y == 32:
                create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image, self.board,
                           self.cell_cize)

    elif self.weapon == self.spear:
        if self.board.field[y_her - 1][x_her] not in '.Л':
            if self.board.field[y_her - 1][x_her] in 'КK.ЛE':
                if self.board.field[y_her - 1][x_her] not in 'ЛE':
                    self.board.field[y_her - 1][x_her] = '.'
                for boxes in self.box_sprite:
                    if boxes.rect.x - self.rect.x == 20 and boxes.rect.y - self.rect.y == -32:
                        create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image,
                                   self.board,
                                   self.cell_cize)

                for enemy in self.enemy_sprite:
                    if enemy.rect.x - self.rect.x == 25 and enemy.rect.y - self.rect.y == - 27:
                        enemy.hp -= 50
                        if enemy.hp <= 0:
                            enemy.kill()
                            self.board.field[y_her - 1][x_her] = '.'
        else:
            if y_her - 2 >= 0 and self.board.field[y_her - 2][x_her] in 'КK.ЛE':
                if self.board.field[y_her - 2][x_her] not in 'ЛE':
                    self.board.field[y_her - 2][x_her] = '.'
                for boxes in self.box_sprite:
                    if boxes.rect.x - self.rect.x == 20 and boxes.rect.y - self.rect.y == -97:
                        create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image,
                                   self.board, self.cell_cize)

                for enemy in self.enemy_sprite:
                    if enemy.rect.x - self.rect.x == 25 and enemy.rect.y - self.rect.y == - 92:
                        enemy.hp -= 50
                        if enemy.hp <= 0:
                            enemy.kill()
                            self.board.field[y_her - 2][x_her] = '.'


def check_down(self, y_her, x_her):  # низ
    if self.weapon == self.sword:
        if self.board.field[y_her + 1][x_her] in "KК.ЛE":
            if self.board.field[y_her + 1][x_her] not in 'ЛE':
                self.board.field[y_her + 1][x_her] = '.'
        if self.board.field[y_her + 1][x_her - 1] in "KК.ЛE":
            if self.board.field[y_her + 1][x_her - 1] not in 'ЛE':
                self.board.field[y_her + 1][x_her - 1] = '.'
        if self.board.field[y_her + 1][x_her + 1] in "KК.ЛE":
            if self.board.field[y_her + 1][x_her + 1] not in 'ЛE':
                self.board.field[y_her + 1][x_her + 1] = '.'

        for boxes in self.box_sprite:
            if self.rect.x - boxes.rect.x == 45 and self.rect.y - boxes.rect.y == -98 or \
                    self.rect.x - boxes.rect.x == -20 and self.rect.y - boxes.rect.y == -98 or \
                    self.rect.x - boxes.rect.x == -85 and self.rect.y - boxes.rect.y == -98:
                create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image, self.board,
                           self.cell_cize)
    elif self.weapon == self.spear:
        if self.board.field[y_her + 1][x_her] not in '.Л':
            if self.board.field[y_her + 1][x_her] in 'КK.ЛE':
                if self.board.field[y_her + 1][x_her] not in 'ЛE':
                    self.board.field[y_her + 1][x_her] = '.'
                for boxes in self.box_sprite:
                    if boxes.rect.x - self.rect.x == 20 and boxes.rect.y - self.rect.y == 98:
                        create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image,
                                   self.board,
                                   self.cell_cize)

            for enemy in self.enemy_sprite:
                if enemy.rect.x - self.rect.x == 25 and enemy.rect.y - self.rect.y == 103:
                    enemy.hp -= 50
                    if enemy.hp <= 0:
                        enemy.kill()
                        self.board.field[y_her + 1][x_her] = '.'
        else:
            if y_her + 2 < len(self.board.field) and self.board.field[y_her + 2][x_her] in 'КK.ЛE':
                if self.board.field[y_her + 2][x_her] not in 'ЛE':
                    self.board.field[y_her + 2][x_her] = '.'
                for boxes in self.box_sprite:
                    if boxes.rect.x - self.rect.x == 20 and boxes.rect.y - self.rect.y == 163:
                        create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image,
                                   self.board,
                                   self.cell_cize)

                for enemy in self.enemy_sprite:
                    if enemy.rect.x - self.rect.x == 25 and enemy.rect.y - self.rect.y == 168:
                        enemy.hp -= 50
                        if enemy.hp <= 0:
                            enemy.kill()
                            self.board.field[y_her + 2][x_her] = '.'


def check_left_down(self, y_her, x_her):  # лево низ
    if self.weapon == self.sword:
        if self.board.field[y_her + 1][x_her - 1] in "KК.ЛE":
            if self.board.field[y_her + 1][x_her - 1] not in 'ЛE':
                self.board.field[y_her + 1][x_her - 1] = '.'
        if self.board.field[y_her][x_her - 1] in "KК.ЛE":
            if self.board.field[y_her][x_her - 1] not in 'ЛE':
                self.board.field[y_her][x_her - 1] = '.'
        if self.board.field[y_her + 1][x_her] in "KК.ЛE":
            if self.board.field[y_her + 1][x_her] not in 'ЛE':
                self.board.field[y_her + 1][x_her] = '.'

        for boxes in self.box_sprite:
            if self.rect.x - boxes.rect.x == 45 and self.rect.y - boxes.rect.y == -33 or \
                    self.rect.x - boxes.rect.x == 45 and self.rect.y - boxes.rect.y == -98 or \
                    self.rect.x - boxes.rect.x == -20 and self.rect.y - boxes.rect.y == -98:
                create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image, self.board,
                           self.cell_cize)

    elif self.weapon == self.spear:
        if self.board.field[y_her][x_her - 1] not in '.Л' or self.board.field[y_her + 1][x_her] not in '.Л':
            return
        else:
            if self.board.field[y_her + 1][x_her - 1] in "KК.ЛE":
                if self.board.field[y_her + 1][x_her - 1] not in 'ЛE':
                    self.board.field[y_her + 1][x_her - 1] = '.'
                for boxes in self.box_sprite:
                    if self.rect.x - boxes.rect.x == 45 and self.rect.y - boxes.rect.y == -98:
                        create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image,
                                   self.board,
                                   self.cell_cize)

                for enemy in self.enemy_sprite:
                    if enemy.rect.x - self.rect.x == -40 and enemy.rect.y - self.rect.y == 103:
                        enemy.hp -= 50
                        if enemy.hp <= 0:
                            self.board.field[y_her + 1][x_her - 1] = '.'
                            enemy.kill()


def check_left(self, y_her, x_her):  # лево
    if self.weapon == self.sword:
        if self.board.field[y_her - 1][x_her - 1] in "KК.ЛE":
            if self.board.field[y_her - 1][x_her - 1] not in 'ЛE':
                self.board.field[y_her - 1][x_her - 1] = '.'
        if self.board.field[y_her][x_her - 1] in "KК.ЛE":
            if self.board.field[y_her][x_her - 1] not in 'ЛE':
                self.board.field[y_her][x_her - 1] = '.'
        if self.board.field[y_her + 1][x_her - 1] in "KК.ЛE":
            if self.board.field[y_her + 1][x_her - 1] not in 'ЛE':
                self.board.field[y_her + 1][x_her - 1] = '.'

        for boxes in self.box_sprite:
            if self.rect.x - boxes.rect.x == 45 and self.rect.y - boxes.rect.y == -33 or \
                    self.rect.x - boxes.rect.x == 45 and self.rect.y - boxes.rect.y == 32 or \
                    self.rect.x - boxes.rect.x == 45 and self.rect.y - boxes.rect.y == -98:
                create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image, self.board,
                           self.cell_cize)
    elif self.weapon == self.spear:
        if self.board.field[y_her][x_her - 1] not in ".Л":
            if self.board.field[y_her][x_her - 1] in "КK.ЛE":
                if self.board.field[y_her][x_her - 1] not in 'ЛE':
                    self.board.field[y_her][x_her - 1] = '.'
                for boxes in self.box_sprite:
                    if self.rect.x - boxes.rect.x == 45 and self.rect.y - boxes.rect.y == -33:
                        create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image,
                                   self.board, self.cell_cize)
                for enemy in self.enemy_sprite:
                    if enemy.rect.x - self.rect.x == -40 and enemy.rect.y - self.rect.y == 38:
                        enemy.hp -= 50
                        if enemy.hp <= 0:
                            enemy.kill()
                            self.board.field[y_her][x_her - 1] = '.'

        else:
            if x_her - 2 >= 0 and self.board.field[y_her][x_her - 2] in "KК.ЛE":
                if self.board.field[y_her][x_her - 2] not in 'ЛE':
                    self.board.field[y_her][x_her - 2] = '.'
                for boxes in self.box_sprite:
                    if self.rect.x - boxes.rect.x == 110 and self.rect.y - boxes.rect.y == -33:
                        create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image,
                                   self.board, self.cell_cize)

                for enemy in self.enemy_sprite:
                    if enemy.rect.x - self.rect.x == -105 and enemy.rect.y - self.rect.y == 38:
                        enemy.hp -= 50
                        if enemy.hp <= 0:
                            enemy.kill()
                            self.board.field[y_her][x_her - 2] = '.'


def check_left_top(self, y_her, x_her):  # лево верх
    if self.weapon == self.sword:
        if self.board.field[y_her - 1][x_her] in "KК.ЛE":
            if self.board.field[y_her - 1][x_her] not in 'ЛE':
                self.board.field[y_her - 1][x_her] = '.'
        if self.board.field[y_her][x_her - 1] in "KК.ЛE":
            if self.board.field[y_her][x_her - 1] not in 'ЛE':
                self.board.field[y_her][x_her - 1] = '.'
        if self.board.field[y_her - 1][x_her - 1] in "KК.ЛE":
            if self.board.field[y_her - 1][x_her - 1] not in 'ЛE':
                self.board.field[y_her - 1][x_her - 1] = '.'

        for boxes in self.box_sprite:
            if self.rect.x - boxes.rect.x == 45 and self.rect.y - boxes.rect.y == 32 or \
                    self.rect.x - boxes.rect.x == -20 and self.rect.y - boxes.rect.y == 32 or \
                    self.rect.x - boxes.rect.x == 45 and self.rect.y - boxes.rect.y == -33:
                create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image, self.board,
                           self.cell_cize)
    elif self.weapon == self.spear:
        if self.board.field[y_her][x_her - 1] not in '.Л' or self.board.field[y_her - 1][x_her] not in '.Л':
            return
        else:
            if self.board.field[y_her - 1][x_her - 1] in "КK.ЛE":
                if self.board.field[y_her - 1][x_her - 1] not in 'ЛE':
                    self.board.field[y_her - 1][x_her - 1] = '.'
                for boxes in self.box_sprite:
                    if self.rect.x - boxes.rect.x == 45 and self.rect.y - boxes.rect.y == 32:
                        create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image,
                                   self.board,
                                   self.cell_cize)

                for enemy in self.enemy_sprite:
                    if enemy.rect.x - self.rect.x == -40 and enemy.rect.y - self.rect.y == -27:
                        enemy.hp -= 50
                        if enemy.hp <= 0:
                            self.board.field[y_her - 1][x_her - 1] = '.'
                            enemy.kill()


class Heroes(pygame.sprite.Sprite):
    def __init__(self, all_sprite, heroes_sprite, heroes_image, cell_cize, board, camera, box_sprite, pol, pol_sprite,
                 pol_image, trap_sprite, enemy_sprite):
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
        self.trap_sprite = trap_sprite
        self.enemy_sprite = enemy_sprite

        self.sword = "меч"
        self.spear = "копье"
        self.bow = "лук"
        self.weapon = self.spear

        self.rect = self.image.get_rect()
        x_n, y_n = board.return_heroes_cords()
        self.rect.x = x_n * self.cell_cize - 20 + cell_cize
        self.rect.y = y_n * self.cell_cize + cell_cize - 33

        self.full_hp = 100
        self.hp = self.full_hp

    def move(self, event):
        x_her, y_her = self.board.return_heroes_cords()
        speed = self.board.cell_size

        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.rect.x += speed
            self.image = self.image_left
            if self.board.field[y_her][x_her + 1] in "KКСCE":  # добавить Д
                self.rect.x -= speed
                return
            self.board.field[y_her][x_her] = '.'
            if 'П' in self.board.field[y_her][x_her + 1]:
                self.board.new_level = True
            self.board.field[y_her][x_her + 1] = "@"

            self.camera.update(self, 'x')
            for elem in self.all_sprite:
                self.camera.apply(elem)
            return

        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.rect.x -= speed
            self.image = self.image_right
            if self.board.field[y_her][x_her - 1] in "KКСCE":  # добавить Д
                self.rect.x += speed
                return
            self.board.field[y_her][x_her] = '.'
            if 'П' in self.board.field[y_her][x_her - 1]:
                self.board.new_level = True
            self.board.field[y_her][x_her - 1] = "@"

            self.camera.update(self, 'x')
            for elem in self.all_sprite:
                self.camera.apply(elem)

        elif sum(list(pygame.key.get_pressed())) > 1:  # нельзя двигать по диагонали
            return

        elif event.key == pygame.K_UP or event.key == pygame.K_w:
            self.rect.y -= speed
            if self.board.field[y_her - 1][x_her] in "KКСEC":  # добавить Д
                self.rect.y += speed
                return
            if 'П' in self.board.field[y_her - 1][x_her]:
                self.board.new_level = True
            self.board.field[y_her - 1][x_her] = "@"
            self.board.field[y_her][x_her] = "."

            self.camera.update(self, 'y')
            for elem in self.all_sprite:
                self.camera.apply(elem)

        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.rect.y += speed
            if self.board.field[y_her + 1][x_her] in "KКСEC":  # добавить Д
                self.rect.y -= speed
                return
            if 'П' in self.board.field[y_her + 1][x_her]:
                self.board.new_level = True
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
        # if check_spear_one_cells(self, y_her, x_her, delta_x, delta_y):

        if delta_x > 20 and delta_y < 0:  # право верх
            check_right_top(self, y_her, x_her)

        elif delta_x > 0 and delta_y == 33:  # право
            check_right(self, y_her, x_her)

        elif delta_x > 20 and delta_y > 0:  # право низ
            check_right_down(self, y_her, x_her)

        elif delta_x == 20 and delta_y < 0:  # верх
            check_top(self, y_her, x_her)

        elif delta_x == 20 and delta_y > 0:  # низ
            check_down(self, y_her, x_her)

        elif delta_x < 0 and delta_y > 33:  # лево низ
            check_left_down(self, y_her, x_her)

        elif delta_x < 0 and delta_y == 33:  # лево
            check_left(self, y_her, x_her)

        elif delta_x < 0 and delta_y < 0:  # лево верх
            check_left_top(self, y_her, x_her)

    def left_box_attack(self, *args):
        """
        проверка корректности атаки коробок, когда герой находится левее коробки
        атака совершается в случае правильности логики
        """
        for elem in self.all_sprite:
            if elem.rect.collidepoint(args[0].pos):
                if elem == self or str(elem)[1:6] == 'Enemy':
                    return
                if self.rect.x - 20 <= elem.rect.x:
                    self.del_box(elem.rect.x - self.rect.x, elem.rect.y - self.rect.y)

    def right_box_attack(self, *args):
        """
        проверка корректности атаки коробок, когда герой находится правее коробки
        атака совершается в случае правильности логики
        """
        for elem in self.all_sprite:
            if elem.rect.collidepoint(args[0].pos):
                if elem == self or str(elem)[1:6] == 'Enemy':
                    return

                if self.rect.x + 20 >= elem.rect.x:
                    self.del_box(elem.rect.x - self.rect.x, elem.rect.y - self.rect.y)

    def attack(self, *args):
        if self.image == self.image_left:  # герой находится слева
            self.left_box_attack(*args)
        else:  # герой находится справа
            self.right_box_attack(*args)

    def check_intersection_trap(self, trap_sprite):
        for trap in trap_sprite:
            center = trap.rect.center[0], trap.rect.center[1] - 15
            if self.rect.collidepoint(center):
                return trap
        return False
