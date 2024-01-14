from level_upp import upp_level_hero


def create_pol(elem, Pol, all_sprite, pol_sprite, pol_image, board, cell_cize):
    """создание объекта пола и удаление объекта коробки"""
    pol = Pol(all_sprite, pol_sprite, pol_image, board, cell_cize)
    pol.rect.x = elem.rect.x
    pol.rect.y = elem.rect.y
    elem.sound.play(0)
    elem.kill()


def check_right_top(self, y_her, x_her):  # право верх
    if self.weapon == self.sword:
        if self.board.field[y_her - 1][x_her + 1] in "KК.ЛE":
            if self.board.field[y_her - 1][x_her + 1] not in 'ЛE':
                self.board.field[y_her - 1][x_her + 1] = '.'
        else:
            return
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

        for enemy in self.enemy_sprite:
            if enemy.rect.x - self.rect.x == 90 and enemy.rect.y - self.rect.y == -27:
                enemy.is_stop = True
                enemy.clock_stop.tick()
                enemy.cur_time_stop = 0
                enemy.hp -= self.damage_sword
                if enemy.hp <= 0:
                    self.kill_sound.play(0)
                    enemy.kill()
                    upp_level_hero(self, enemy.level)
                    self.board.field[y_her - 1][x_her + 1] = '.'
                else:
                    self.ydar_sound.play(0)

            elif enemy.rect.x - self.rect.x == 90 and enemy.rect.y - self.rect.y == 38:
                enemy.is_stop = True
                enemy.clock_stop.tick()
                enemy.cur_time_stop = 0
                enemy.hp -= self.damage_sword
                if enemy.hp <= 0:
                    self.kill_sound.play(0)
                    enemy.kill()
                    upp_level_hero(self, enemy.level)
                    self.board.field[y_her][x_her + 1] = '.'
                else:
                    self.ydar_sound.play(0)

            elif enemy.rect.x - self.rect.x == 25 and enemy.rect.y - self.rect.y == -27:
                enemy.is_stop = True
                enemy.clock_stop.tick()
                enemy.cur_time_stop = 0
                enemy.hp -= self.damage_sword
                if enemy.hp <= 0:
                    self.kill_sound.play(0)
                    enemy.kill()
                    upp_level_hero(self, enemy.level)
                    self.board.field[y_her - 1][x_her] = '.'
                else:
                    self.ydar_sound.play(0)

    elif self.weapon == self.spear:
        if self.board.field[y_her - 1][x_her] not in '.ЛВ' or self.board.field[y_her][x_her + 1] not in '.ЛВ':
            return
        else:
            if self.board.field[y_her - 1][x_her + 1] in "КK.ЛEВ":
                if self.board.field[y_her - 1][x_her + 1] not in 'ЛE':
                    self.board.field[y_her - 1][x_her + 1] = '.'

                self.animation.need = True
                self.animation.spear_right_top = True

                for boxes in self.box_sprite:
                    if boxes.rect.x - self.rect.x == 85 and boxes.rect.y - self.rect.y == -32:
                        create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image,
                                   self.board, self.cell_cize)

                for enemy in self.enemy_sprite:
                    if enemy.rect.x - self.rect.x == 90 and enemy.rect.y - self.rect.y == -27:
                        enemy.is_stop = True
                        enemy.clock_stop.tick()
                        enemy.cur_time_stop = 0
                        enemy.hp -= self.damage_spear
                        if enemy.hp <= 0:
                            self.board.field[y_her - 1][x_her + 1] = '.'
                            enemy.kill()
                            upp_level_hero(self, enemy.level)
                            self.kill_sound.play(0)
                        else:
                            self.ydar_sound.play(0)


def check_right(self, y_her, x_her):  # право
    if self.weapon == self.sword:
        if self.board.field[y_her][x_her + 1] in "KК.ЛE":
            if self.board.field[y_her][x_her + 1] not in 'ЛE':
                self.board.field[y_her][x_her + 1] = '.'
        else:
            return
        if self.board.field[y_her - 1][x_her + 1] in "KК.ЛE":
            if self.board.field[y_her - 1][x_her + 1] not in 'ЛE':
                self.board.field[y_her - 1][x_her + 1] = '.'
        if self.board.field[y_her + 1][x_her + 1] in "KК.ЛE":
            if self.board.field[y_her + 1][x_her + 1] not in 'ЛE':
                self.board.field[y_her + 1][x_her + 1] = '.'

        for boxes in self.box_sprite:
            if self.rect.x - boxes.rect.x == -85 and self.rect.y - boxes.rect.y == -33 or \
                    self.rect.x - boxes.rect.x == -85 and self.rect.y - boxes.rect.y == 32 or \
                    self.rect.x - boxes.rect.x == -85 and self.rect.y - boxes.rect.y == -98:
                create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image, self.board,
                           self.cell_cize)

        for enemy in self.enemy_sprite:
            if enemy.rect.x - self.rect.x == 90 and enemy.rect.y - self.rect.y == 38:
                enemy.is_stop = True
                enemy.clock_stop.tick()
                enemy.cur_time_stop = 0
                enemy.hp -= self.damage_sword
                if enemy.hp <= 0:
                    enemy.kill()
                    upp_level_hero(self, enemy.level)
                    self.kill_sound.play(0)
                    self.board.field[y_her][x_her + 1] = '.'
                else:
                    self.ydar_sound.play(0)

            elif enemy.rect.x - self.rect.x == 90 and enemy.rect.y - self.rect.y == 103:
                enemy.is_stop = True
                enemy.clock_stop.tick()
                enemy.cur_time_stop = 0
                enemy.hp -= self.damage_sword
                if enemy.hp <= 0:
                    enemy.kill()
                    upp_level_hero(self, enemy.level)
                    self.kill_sound.play(0)
                    self.board.field[y_her + 1][x_her + 1] = '.'
                else:
                    self.ydar_sound.play(0)

            elif enemy.rect.x - self.rect.x == 90 and enemy.rect.y - self.rect.y == -27:
                enemy.is_stop = True
                enemy.clock_stop.tick()
                enemy.cur_time_stop = 0
                enemy.hp -= self.damage_sword
                if enemy.hp <= 0:
                    enemy.kill()
                    upp_level_hero(self, enemy.level)
                    self.kill_sound.play(0)
                    self.board.field[y_her - 1][x_her + 1] = '.'
                else:
                    self.ydar_sound.play(0)


    elif self.weapon == self.spear:
        if self.board.field[y_her][x_her + 1] not in '.ЛВД':
            if self.board.field[y_her][x_her + 1] in "КK.ЛEВД":
                if self.board.field[y_her][x_her + 1] not in 'ЛE':
                    self.board.field[y_her][x_her + 1] = '.'
                self.animation.need = True
                self.animation.spear_right = True
                for boxes in self.box_sprite:
                    if boxes.rect.x - self.rect.x == 85 and boxes.rect.y - self.rect.y == 33:
                        create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image,
                                   self.board, self.cell_cize)

                for enemy in self.enemy_sprite:
                    if enemy.rect.x - self.rect.x == 90 and enemy.rect.y - self.rect.y == 38:
                        enemy.is_stop = True
                        enemy.clock_stop.tick()
                        enemy.cur_time_stop = 0
                        enemy.hp -= self.damage_spear
                        if enemy.hp <= 0:
                            enemy.kill()
                            upp_level_hero(self, enemy.level)
                            self.kill_sound.play(0)
                            self.board.field[y_her][x_her + 1] = '.'
                        else:
                            self.ydar_sound.play(0)
        else:
            if x_her + 2 < len(self.board.field[0]) and self.board.field[y_her][x_her + 2] in "КK.ЛEВДС":
                if self.board.field[y_her][x_her + 2] not in 'ЛEС':
                    self.board.field[y_her][x_her + 2] = '.'
                self.animation.need = True
                self.animation.spear_right = True
                for boxes in self.box_sprite:
                    if boxes.rect.x - self.rect.x == 150 and boxes.rect.y - self.rect.y == 33:
                        create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image,
                                   self.board,
                                   self.cell_cize)

                for enemy in self.enemy_sprite:
                    if enemy.rect.x - self.rect.x == 155 and enemy.rect.y - self.rect.y == 38:
                        enemy.is_stop = True
                        enemy.clock_stop.tick()
                        enemy.cur_time_stop = 0
                        enemy.hp -= self.damage_spear
                        if enemy.hp <= 0:
                            enemy.kill()
                            upp_level_hero(self, enemy.level)
                            self.kill_sound.play(0)
                            self.board.field[y_her][x_her + 2] = '.'
                        else:
                            self.ydar_sound.play(0)


def check_right_down(self, y_her, x_her):  # право низ
    if self.weapon == self.sword:
        if self.board.field[y_her + 1][x_her + 1] in "КK.ЛE":
            if self.board.field[y_her + 1][x_her + 1] not in 'ЛE':
                self.board.field[y_her + 1][x_her + 1] = '.'
        else:
            return
        if self.board.field[y_her][x_her + 1] in "КK.ЛE":
            if self.board.field[y_her][x_her + 1] not in 'ЛE':
                self.board.field[y_her][x_her + 1] = '.'
        if self.board.field[y_her + 1][x_her] in "КK.ЛE":
            if self.board.field[y_her + 1][x_her] not in 'ЛE':
                self.board.field[y_her + 1][x_her] = '.'

        for boxes in self.box_sprite:
            if self.rect.x - boxes.rect.x == -85 and self.rect.y - boxes.rect.y == -98 or \
                    self.rect.x - boxes.rect.x == -85 and self.rect.y - boxes.rect.y == -33 or \
                    self.rect.x - boxes.rect.x == -20 and self.rect.y - boxes.rect.y == -98:
                create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image, self.board,
                           self.cell_cize)

        for enemy in self.enemy_sprite:
            if enemy.rect.x - self.rect.x == 90 and enemy.rect.y - self.rect.y == 103:
                enemy.hp -= self.damage_sword
                enemy.is_stop = True
                enemy.clock_stop.tick()
                enemy.cur_time_stop = 0
                if enemy.hp <= 0:
                    enemy.kill()
                    upp_level_hero(self, enemy.level)
                    self.kill_sound.play(0)
                    self.board.field[y_her + 1][x_her + 1] = '.'
                else:
                    self.ydar_sound.play(0)

            elif enemy.rect.x - self.rect.x == 25 and enemy.rect.y - self.rect.y == 103:
                enemy.hp -= self.damage_sword
                enemy.is_stop = True
                enemy.clock_stop.tick()
                enemy.cur_time_stop = 0
                if enemy.hp <= 0:
                    enemy.kill()
                    upp_level_hero(self, enemy.level)
                    self.kill_sound.play(0)
                    self.board.field[y_her + 1][x_her] = '.'
                else:
                    self.ydar_sound.play(0)

            elif enemy.rect.x - self.rect.x == 90 and enemy.rect.y - self.rect.y == 38:
                enemy.hp -= self.damage_sword
                enemy.is_stop = True
                enemy.clock_stop.tick()
                enemy.cur_time_stop = 0
                if enemy.hp <= 0:
                    enemy.kill()
                    upp_level_hero(self, enemy.level)
                    self.kill_sound.play(0)
                    self.board.field[y_her][x_her + 1] = '.'
                else:
                    self.ydar_sound.play(0)

    elif self.weapon == self.spear:
        if self.board.field[y_her][x_her + 1] not in '.ЛВ' or self.board.field[y_her + 1][x_her] not in '.ЛВ':
            return
        else:
            if self.board.field[y_her + 1][x_her + 1] in "КK.ЛEВ":
                if self.board.field[y_her + 1][x_her + 1] not in 'ЛE':
                    self.board.field[y_her + 1][x_her + 1] = '.'

                self.animation.need = True
                self.animation.spear_right_down = True

                for boxes in self.box_sprite:
                    if boxes.rect.x - self.rect.x == 85 and boxes.rect.y - self.rect.y == 98:
                        create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image, self.board,
                                   self.cell_cize)

                for enemy in self.enemy_sprite:
                    if enemy.rect.x - self.rect.x == 90 and enemy.rect.y - self.rect.y == 103:
                        enemy.is_stop = True
                        enemy.clock_stop.tick()
                        enemy.cur_time_stop = 0
                        enemy.hp -= self.damage_spear
                        if enemy.hp <= 0:
                            self.board.field[y_her + 1][x_her + 1] = '.'
                            enemy.kill()
                            upp_level_hero(self, enemy.level)
                            self.kill_sound.play(0)
                        else:
                            self.ydar_sound.play(0)


def check_top(self, y_her, x_her):  # верх
    if self.weapon == self.sword:
        if self.board.field[y_her - 1][x_her] in "KК.ЛE":
            if self.board.field[y_her - 1][x_her] not in 'ЛE':
                self.board.field[y_her - 1][x_her] = '.'
        else:
            return
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
        for enemy in self.enemy_sprite:
            if enemy.rect.x - self.rect.x == 25 and enemy.rect.y - self.rect.y == - 27:
                enemy.is_stop = True
                enemy.clock_stop.tick()
                enemy.cur_time_stop = 0
                enemy.hp -= self.damage_sword
                if enemy.hp <= 0:
                    enemy.kill()
                    upp_level_hero(self, enemy.level)
                    self.kill_sound.play(0)
                    self.board.field[y_her - 1][x_her] = '.'
                else:
                    self.ydar_sound.play(0)

            elif enemy.rect.x - self.rect.x == 90 and enemy.rect.y - self.rect.y == -27:
                enemy.is_stop = True
                enemy.clock_stop.tick()
                enemy.cur_time_stop = 0
                enemy.hp -= self.damage_sword
                if enemy.hp <= 0:
                    enemy.kill()
                    upp_level_hero(self, enemy.level)
                    self.kill_sound.play(0)
                    self.board.field[y_her - 1][x_her + 1] = '.'
                else:
                    self.ydar_sound.play(0)

            elif enemy.rect.x - self.rect.x == -40 and enemy.rect.y - self.rect.y == -27:
                enemy.is_stop = True
                enemy.clock_stop.tick()
                enemy.cur_time_stop = 0
                enemy.hp -= self.damage_sword
                if enemy.hp <= 0:
                    enemy.kill()
                    upp_level_hero(self, enemy.level)
                    self.kill_sound.play(0)
                    self.board.field[y_her - 1][x_her - 1] = '.'
                else:
                    self.ydar_sound.play(0)

    elif self.weapon == self.spear:
        if self.board.field[y_her - 1][x_her] not in '.ЛВ':
            if self.board.field[y_her - 1][x_her] in 'КK.ЛEВ':
                if self.board.field[y_her - 1][x_her] not in 'ЛE':
                    self.board.field[y_her - 1][x_her] = '.'

                self.animation.need = True
                self.animation.spear_top = True

                for boxes in self.box_sprite:
                    if boxes.rect.x - self.rect.x == 20 and boxes.rect.y - self.rect.y == -32:
                        create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image,
                                   self.board,
                                   self.cell_cize)

                for enemy in self.enemy_sprite:
                    if enemy.rect.x - self.rect.x == 25 and enemy.rect.y - self.rect.y == - 27:
                        enemy.is_stop = True
                        enemy.clock_stop.tick()
                        enemy.cur_time_stop = 0
                        enemy.hp -= self.damage_spear
                        if enemy.hp <= 0:
                            enemy.kill()
                            upp_level_hero(self, enemy.level)
                            self.kill_sound.play(0)
                            self.board.field[y_her - 1][x_her] = '.'
                        else:
                            self.ydar_sound.play(0)
        else:
            if y_her - 2 >= 0 and self.board.field[y_her - 2][x_her] in 'КK.ЛEВДС':
                if self.board.field[y_her - 2][x_her] not in 'ЛEС':
                    self.board.field[y_her - 2][x_her] = '.'

                self.animation.need = True
                self.animation.spear_top = True

                for boxes in self.box_sprite:
                    if boxes.rect.x - self.rect.x == 20 and boxes.rect.y - self.rect.y == -97:
                        create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image,
                                   self.board, self.cell_cize)

                for enemy in self.enemy_sprite:
                    enemy.is_stop = True
                    enemy.clock_stop.tick()
                    enemy.cur_time_stop = 0
                    if enemy.rect.x - self.rect.x == 25 and enemy.rect.y - self.rect.y == - 92:
                        enemy.hp -= self.damage_spear
                        if enemy.hp <= 0:
                            enemy.kill()
                            upp_level_hero(self, enemy.level)
                            self.kill_sound.play(0)
                            self.board.field[y_her - 2][x_her] = '.'
                        else:
                            self.ydar_sound.play(0)


def check_down(self, y_her, x_her):  # низ
    if self.weapon == self.sword:
        if self.board.field[y_her + 1][x_her] in "KК.ЛE":
            if self.board.field[y_her + 1][x_her] not in 'ЛE':
                self.board.field[y_her + 1][x_her] = '.'
        else:
            return
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

        for enemy in self.enemy_sprite:
            if enemy.rect.x - self.rect.x == 90 and enemy.rect.y - self.rect.y == 103:
                enemy.is_stop = True
                enemy.clock_stop.tick()
                enemy.cur_time_stop = 0
                enemy.hp -= self.damage_sword
                if enemy.hp <= 0:
                    enemy.kill()
                    upp_level_hero(self, enemy.level)
                    self.kill_sound.play(0)
                    self.board.field[y_her + 1][x_her + 1] = '.'
                else:
                    self.ydar_sound.play(0)

            elif enemy.rect.x - self.rect.x == 25 and enemy.rect.y - self.rect.y == 103:
                enemy.is_stop = True
                enemy.clock_stop.tick()
                enemy.cur_time_stop = 0
                enemy.hp -= self.damage_sword
                if enemy.hp <= 0:
                    enemy.kill()
                    upp_level_hero(self, enemy.level)
                    self.kill_sound.play(0)
                    self.board.field[y_her + 1][x_her] = '.'
                else:
                    self.ydar_sound.play(0)

            elif enemy.rect.x - self.rect.x == -40 and enemy.rect.y - self.rect.y == 103:
                enemy.is_stop = True
                enemy.clock_stop.tick()
                enemy.cur_time_stop = 0
                enemy.hp -= self.damage_sword
                if enemy.hp <= 0:
                    enemy.kill()
                    upp_level_hero(self, enemy.level)
                    self.kill_sound.play(0)
                    self.board.field[y_her + 1][x_her - 1] = '.'
                else:
                    self.ydar_sound.play(0)

    elif self.weapon == self.spear:
        if self.board.field[y_her + 1][x_her] not in '.ЛВ':
            if self.board.field[y_her + 1][x_her] in 'КK.ЛEВ':
                if self.board.field[y_her + 1][x_her] not in 'ЛE':
                    self.board.field[y_her + 1][x_her] = '.'

                self.animation.need = True
                self.animation.spear_down = True

                for boxes in self.box_sprite:
                    if boxes.rect.x - self.rect.x == 20 and boxes.rect.y - self.rect.y == 98:
                        create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image,
                                   self.board,
                                   self.cell_cize)

            for enemy in self.enemy_sprite:
                if enemy.rect.x - self.rect.x == 25 and enemy.rect.y - self.rect.y == 103:
                    enemy.is_stop = True
                    enemy.clock_stop.tick()
                    enemy.cur_time_stop = 0
                    enemy.hp -= self.damage_spear
                    if enemy.hp <= 0:
                        enemy.kill()
                        upp_level_hero(self, enemy.level)
                        self.kill_sound.play(0)
                        self.board.field[y_her + 1][x_her] = '.'
                    else:
                        self.ydar_sound.play(0)
        else:
            if y_her + 2 < len(self.board.field) and self.board.field[y_her + 2][x_her] in 'КK.ЛEВДС':
                if self.board.field[y_her + 2][x_her] not in 'ЛEС':
                    self.board.field[y_her + 2][x_her] = '.'

                self.animation.need = True
                self.animation.spear_down = True

                for boxes in self.box_sprite:
                    if boxes.rect.x - self.rect.x == 20 and boxes.rect.y - self.rect.y == 163:
                        create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image,
                                   self.board,
                                   self.cell_cize)

                for enemy in self.enemy_sprite:
                    if enemy.rect.x - self.rect.x == 25 and enemy.rect.y - self.rect.y == 168:
                        enemy.is_stop = True
                        enemy.clock_stop.tick()
                        enemy.cur_time_stop = 0
                        enemy.hp -= self.damage_spear
                        if enemy.hp <= 0:
                            enemy.kill()
                            upp_level_hero(self, enemy.level)
                            self.kill_sound.play(0)
                            self.board.field[y_her + 2][x_her] = '.'
                        else:
                            self.ydar_sound.play(0)


def check_left_down(self, y_her, x_her):  # лево низ
    if self.weapon == self.sword:
        if self.board.field[y_her + 1][x_her - 1] in "KК.ЛE":
            if self.board.field[y_her + 1][x_her - 1] not in 'ЛE':
                self.board.field[y_her + 1][x_her - 1] = '.'
        else:
            return
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

        for enemy in self.enemy_sprite:
            if enemy.rect.x - self.rect.x == -40 and enemy.rect.y - self.rect.y == 38:
                enemy.is_stop = True
                enemy.clock_stop.tick()
                enemy.cur_time_stop = 0
                enemy.hp -= self.damage_sword
                if enemy.hp <= 0:
                    enemy.kill()
                    upp_level_hero(self, enemy.level)
                    self.kill_sound.play(0)
                    self.board.field[y_her][x_her - 1] = '.'
                else:
                    self.ydar_sound.play(0)

            elif enemy.rect.x - self.rect.x == -40 and enemy.rect.y - self.rect.y == 103:
                enemy.is_stop = True
                enemy.clock_stop.tick()
                enemy.cur_time_stop = 0
                enemy.hp -= self.damage_sword
                if enemy.hp <= 0:
                    enemy.kill()
                    upp_level_hero(self, enemy.level)
                    self.kill_sound.play(0)
                    self.board.field[y_her + 1][x_her - 1] = '.'
                else:
                    self.ydar_sound.play(0)

            elif enemy.rect.x - self.rect.x == 25 and enemy.rect.y - self.rect.y == 103:
                enemy.is_stop = True
                enemy.clock_stop.tick()
                enemy.cur_time_stop = 0
                enemy.hp -= self.damage_sword
                if enemy.hp <= 0:
                    enemy.kill()
                    upp_level_hero(self, enemy.level)
                    self.kill_sound.play(0)
                    self.board.field[y_her + 1][x_her] = '.'
                else:
                    self.ydar_sound.play(0)

    elif self.weapon == self.spear:
        if self.board.field[y_her][x_her - 1] not in '.ЛВ' or self.board.field[y_her + 1][x_her] not in '.ЛВ':
            return
        else:
            if self.board.field[y_her + 1][x_her - 1] in "KК.ЛEВ":
                if self.board.field[y_her + 1][x_her - 1] not in 'ЛE':
                    self.board.field[y_her + 1][x_her - 1] = '.'

                self.animation.need = True
                self.animation.spear_left_down = True

                for boxes in self.box_sprite:
                    if self.rect.x - boxes.rect.x == 45 and self.rect.y - boxes.rect.y == -98:
                        create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image,
                                   self.board,
                                   self.cell_cize)

                for enemy in self.enemy_sprite:
                    if enemy.rect.x - self.rect.x == -40 and enemy.rect.y - self.rect.y == 103:
                        enemy.is_stop = True
                        enemy.clock_stop.tick()
                        enemy.cur_time_stop = 0
                        enemy.hp -= self.damage_spear
                        if enemy.hp <= 0:
                            self.board.field[y_her + 1][x_her - 1] = '.'
                            enemy.kill()
                            upp_level_hero(self, enemy.level)
                            self.kill_sound.play(0)
                        else:
                            self.ydar_sound.play(0)


def check_left(self, y_her, x_her):  # лево
    if self.weapon == self.sword:
        if self.board.field[y_her][x_her - 1] in "KК.ЛE":
            if self.board.field[y_her][x_her - 1] not in 'ЛE':
                self.board.field[y_her][x_her - 1] = '.'
        else:
            return
        if self.board.field[y_her - 1][x_her - 1] in "KК.ЛE":
            if self.board.field[y_her - 1][x_her - 1] not in 'ЛE':
                self.board.field[y_her - 1][x_her - 1] = '.'
        if self.board.field[y_her + 1][x_her - 1] in "KК.ЛE":
            if self.board.field[y_her + 1][x_her - 1] not in 'ЛE':
                self.board.field[y_her + 1][x_her - 1] = '.'

        self.animation.need = True
        self.animation.sword_left = True

        for boxes in self.box_sprite:
            if self.rect.x - boxes.rect.x == 45 and self.rect.y - boxes.rect.y == -33 or \
                    self.rect.x - boxes.rect.x == 45 and self.rect.y - boxes.rect.y == 32 or \
                    self.rect.x - boxes.rect.x == 45 and self.rect.y - boxes.rect.y == -98:
                create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image, self.board,
                           self.cell_cize)

        for enemy in self.enemy_sprite:
            if enemy.rect.x - self.rect.x == -40 and enemy.rect.y - self.rect.y == 38:
                enemy.is_stop = True
                enemy.clock_stop.tick()
                enemy.cur_time_stop = 0
                enemy.hp -= self.damage_sword
                if enemy.hp <= 0:
                    enemy.kill()
                    upp_level_hero(self, enemy.level)
                    self.kill_sound.play(0)
                    self.board.field[y_her][x_her - 1] = '.'
                else:
                    self.ydar_sound.play(0)

            elif enemy.rect.x - self.rect.x == -40 and enemy.rect.y - self.rect.y == 103:
                enemy.is_stop = True
                enemy.clock_stop.tick()
                enemy.cur_time_stop = 0
                enemy.hp -= self.damage_sword
                if enemy.hp <= 0:
                    enemy.kill()
                    upp_level_hero(self, enemy.level)
                    self.kill_sound.play(0)
                    self.board.field[y_her + 1][x_her - 1] = '.'
                else:
                    self.ydar_sound.play(0)

            elif enemy.rect.x - self.rect.x == -40 and enemy.rect.y - self.rect.y == -27:
                enemy.is_stop = True
                enemy.clock_stop.tick()
                enemy.cur_time_stop = 0
                enemy.hp -= self.damage_sword
                if enemy.hp <= 0:
                    enemy.kill()
                    upp_level_hero(self, enemy.level)
                    self.kill_sound.play(0)
                    self.board.field[y_her - 1][x_her - 1] = '.'
                else:
                    self.ydar_sound.play(0)

    elif self.weapon == self.spear:
        if self.board.field[y_her][x_her - 1] not in ".ЛВД":
            if self.board.field[y_her][x_her - 1] in "КK.ЛEВД":
                if self.board.field[y_her][x_her - 1] not in 'ЛE':
                    self.board.field[y_her][x_her - 1] = '.'

                self.animation.need = True
                self.animation.spear_left = True

                for boxes in self.box_sprite:
                    if self.rect.x - boxes.rect.x == 45 and self.rect.y - boxes.rect.y == -33:
                        create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image,
                                   self.board, self.cell_cize)
                for enemy in self.enemy_sprite:
                    if enemy.rect.x - self.rect.x == -40 and enemy.rect.y - self.rect.y == 38:
                        enemy.is_stop = True
                        enemy.clock_stop.tick()
                        enemy.cur_time_stop = 0
                        enemy.hp -= self.damage_spear
                        if enemy.hp <= 0:
                            enemy.kill()
                            upp_level_hero(self, enemy.level)
                            self.kill_sound.play(0)
                            self.board.field[y_her][x_her - 1] = '.'
                        else:
                            self.ydar_sound.play(0)

        else:
            if x_her - 2 >= 0 and self.board.field[y_her][x_her - 2] in "KК.ЛEВДС":
                if self.board.field[y_her][x_her - 2] not in 'ЛEС':
                    self.board.field[y_her][x_her - 2] = '.'

                self.animation.need = True
                self.animation.spear_left = True

                for boxes in self.box_sprite:
                    if self.rect.x - boxes.rect.x == 110 and self.rect.y - boxes.rect.y == -33:
                        create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image,
                                   self.board, self.cell_cize)

                for enemy in self.enemy_sprite:
                    if enemy.rect.x - self.rect.x == -105 and enemy.rect.y - self.rect.y == 38:
                        enemy.is_stop = True
                        enemy.clock_stop.tick()
                        enemy.cur_time_stop = 0
                        enemy.hp -= self.damage_spear
                        if enemy.hp <= 0:
                            enemy.kill()
                            self.kill_sound.play(0)
                            upp_level_hero(self, enemy.level)
                            self.board.field[y_her][x_her - 2] = '.'
                        else:
                            self.ydar_sound.play(0)


def check_left_top(self, y_her, x_her):  # лево верх
    if self.weapon == self.sword:
        if self.board.field[y_her - 1][x_her - 1] in "KК.ЛE":
            if self.board.field[y_her - 1][x_her - 1] not in 'ЛE':
                self.board.field[y_her - 1][x_her - 1] = '.'
        else:
            return
        if self.board.field[y_her - 1][x_her] in "KК.ЛE":
            if self.board.field[y_her - 1][x_her] not in 'ЛE':
                self.board.field[y_her - 1][x_her] = '.'
        if self.board.field[y_her][x_her - 1] in "KК.ЛE":
            if self.board.field[y_her][x_her - 1] not in 'ЛE':
                self.board.field[y_her][x_her - 1] = '.'

        for boxes in self.box_sprite:
            if self.rect.x - boxes.rect.x == 45 and self.rect.y - boxes.rect.y == 32 or \
                    self.rect.x - boxes.rect.x == -20 and self.rect.y - boxes.rect.y == 32 or \
                    self.rect.x - boxes.rect.x == 45 and self.rect.y - boxes.rect.y == -33:
                create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image, self.board,
                           self.cell_cize)

        for enemy in self.enemy_sprite:
            if enemy.rect.x - self.rect.x == -40 and enemy.rect.y - self.rect.y == -27:
                enemy.is_stop = True
                enemy.clock_stop.tick()
                enemy.cur_time_stop = 0
                enemy.hp -= self.damage_sword
                if enemy.hp <= 0:
                    enemy.kill()
                    upp_level_hero(self, enemy.level)
                    self.kill_sound.play(0)
                    self.board.field[y_her - 1][x_her - 1] = '.'
                else:
                    self.ydar_sound.play(0)

            elif enemy.rect.x - self.rect.x == -40 and enemy.rect.y - self.rect.y == 38:
                enemy.is_stop = True
                enemy.clock_stop.tick()
                enemy.cur_time_stop = 0
                enemy.hp -= self.damage_sword
                if enemy.hp <= 0:
                    enemy.kill()
                    upp_level_hero(self, enemy.level)
                    self.kill_sound.play(0)
                    self.board.field[y_her][x_her - 1] = '.'
                else:
                    self.ydar_sound.play(0)

            elif enemy.rect.x - self.rect.x == 25 and enemy.rect.y - self.rect.y == -27:
                enemy.is_stop = True
                enemy.clock_stop.tick()
                enemy.cur_time_stop = 0
                enemy.hp -= self.damage_sword
                if enemy.hp <= 0:
                    enemy.kill()
                    self.kill_sound.play(0)
                    upp_level_hero(self, enemy.level)
                    self.board.field[y_her - 1][x_her] = '.'
                else:
                    self.ydar_sound.play(0)

    elif self.weapon == self.spear:
        if self.board.field[y_her][x_her - 1] not in '.ЛВ' or self.board.field[y_her - 1][x_her] not in '.ЛВ':
            return
        else:
            if self.board.field[y_her - 1][x_her - 1] in "КK.ЛEВ":
                if self.board.field[y_her - 1][x_her - 1] not in 'ЛE':
                    self.board.field[y_her - 1][x_her - 1] = '.'

                self.animation.need = True
                self.animation.spear_left_top = True

                for boxes in self.box_sprite:
                    if self.rect.x - boxes.rect.x == 45 and self.rect.y - boxes.rect.y == 32:
                        create_pol(boxes, self.pol, self.all_sprite, self.pol_sprite, self.pol_image,
                                   self.board,
                                   self.cell_cize)

                for enemy in self.enemy_sprite:
                    if enemy.rect.x - self.rect.x == -40 and enemy.rect.y - self.rect.y == -27:
                        enemy.is_stop = True
                        enemy.clock_stop.tick()
                        enemy.cur_time_stop = 0
                        enemy.hp -= self.damage_spear
                        if enemy.hp <= 0:
                            self.board.field[y_her - 1][x_her - 1] = '.'
                            enemy.kill()
                            self.kill_sound.play(0)
                            upp_level_hero(self, enemy.level)
                        else:
                            self.ydar_sound.play(0)
