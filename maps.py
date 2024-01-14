from random import randint, shuffle

from rooms import rooms, RIGHT, DOWN, NEXT_ROOM

count = 0
result_map = [['']]


def add_wall(field):
    max_len = max(map(lambda x: len(x), field)) + 2
    for i in range(len(field)):
        field[i] = [' '] + field[i] + [' ']
        while len(field[i]) != max_len:
            field[i].append(' ')

    spaces = [" " for _ in range(len(field[0]))]
    field.insert(0, spaces.copy())
    field.extend([spaces.copy()])

    for y in range(1, len(field) - 1):
        for x in range(1, len(field[0]) - 1):
            if field[y][x] != ' ' and field[y][x] != "С":
                if x - 1 >= 0 and field[y][x - 1] == ' ':
                    field[y][x - 1] = 'С'
                if x - 1 >= 0 and y - 1 >= 0 and field[y - 1][x - 1] == ' ':
                    field[y - 1][x - 1] = 'С'
                if y - 1 >= 0 and field[y - 1][x] == ' ':
                    field[y - 1][x] = 'С'
                if y - 1 >= 0 and x + 1 < len(field[0]) and field[y - 1][x + 1] == ' ':
                    field[y - 1][x + 1] = 'С'
                if x + 1 < len(field[0]) and field[y][x + 1] == ' ':
                    field[y][x + 1] = 'С'
                if y + 1 < len(field) and field[y + 1][x] == ' ':
                    field[y + 1][x] = 'С'
                if y + 1 < len(field) and x - 1 >= 0 and field[y + 1][x - 1] == ' ':
                    field[y + 1][x - 1] = 'С'
                if y + 1 < len(field) and x + 1 < len(field[0]) and field[y + 1][x + 1] == ' ':
                    field[y + 1][x + 1] = 'С'
    return field


def generation_chance(count_tocheck):
    count_enemy = randint(5, 7)
    chance = count_enemy / count_tocheck

    return chance


def preparing_map(map):
    map_copy = map.copy()
    for i in range(len(map_copy)):
        map_copy[i] = list(''.join(map[i]))
    return map_copy


def generation_map(lvl_hero=1, lvl=1):
    global result_map
    count_stage = randint(5, 7)
    map_level = [[0 for _ in range(14)] for _ in range(14)]

    x, y = 7, 7  # 3 3 - точка старта
    map_level[x][y] = 1
    direction = -1
    cords = (0, 0)
    stages = [1]
    max_x = 0
    maps = list(rooms.keys())
    result_map = []

    for i in range(count_stage - 1):
        direction = randint(0, 1)
        if direction == 0:
            stages.append('>')
        else:
            stages.append('v')
        shuffle(maps)
        stages.append(maps[0])
    # print(stages)

    for i in stages:
        if i == '>':
            for i_lvl in RIGHT:
                try:
                    result_map[cords[1]].append(''.join(i_lvl))
                except IndexError:
                    result_map.append(''.join(i_lvl).split(' sdfsdsd'))
                cords = cords[0], cords[1] + 1
            cords = cords[0] + 10, cords[1] - 10

            cords = cords[0] + 20, cords[1]
        elif i == 'v':
            cords = cords[0], cords[1] + 10
            try:
                max_x = max(list(map(lambda x: len(x), result_map)))
            except ValueError:
                max_x = 0
            for i_lvl in range(max_x - 1):
                for ii_lvl in range(10):
                    try:
                        result_map[cords[1]].append('          ')
                    except IndexError:
                        result_map.append(['          '])
                    cords = cords[0], cords[1] + 1
                cords = cords[0] + 10, cords[1] - 10

            for i_lvl in DOWN:
                try:
                    result_map[cords[1]].append(''.join(i_lvl))
                except IndexError:
                    result_map.append(''.join(i_lvl).split('qweasdwe121213233tr21'))
                cords = cords[0], cords[1] + 1
            cords = cords[0] + 10, cords[1] - 10

            cords = cords[0], cords[1] + 10

        else:
            try:
                max_x = len(result_map[-1])
            except IndexError:
                max_x = 0

            for i_lvl in rooms[i]:
                try:
                    result_map[cords[1]].append(''.join(i_lvl))
                except IndexError:
                    for ii_lvl in range(max_x - 1):
                        for iii_lvl in range(10):
                            try:
                                result_map[cords[1]].append('          ')
                            except IndexError:
                                result_map.append(['          '])
                            cords = cords[0], cords[1] + 1
                        cords = cords[0] + 10, cords[1] - 10
                    try:
                        result_map[cords[1]].append(''.join(i_lvl))
                    except IndexError:
                        result_map.append([''.join(i_lvl)])
                cords = cords[0], cords[1] + 1
            cords = cords[0] + 10, cords[1] - 10

    for i_lvl in RIGHT:
        try:
            result_map[cords[1]].append(''.join(i_lvl))
        except IndexError:
            result_map.append(''.join(i_lvl).split())
        cords = cords[0], cords[1] + 1
    cords = cords[0] + 10, cords[1] - 10

    cords = cords[0] + 20, cords[1]

    for i_lvl in NEXT_ROOM:
        try:
            result_map[cords[1]].append(''.join(i_lvl))
        except IndexError:
            result_map.append([''.join(i_lvl)])
        cords = cords[0], cords[1] + 1
    cords = cords[0] + 10, cords[1] - 10

    result_map_copy = preparing_map(result_map)

    result_map_copy[-6][-6] = '1'
    result_map_copy[-5][-6] = '2'
    result_map_copy[-6][-5] = '3'
    result_map_copy[-5][-5] = '4'
    result_map_copy[5][5] = '@'

    return result_map_copy


def spawn_enemy(self, x_her, y_her, lvl_hero, lvl):
    global result_map, count
    passage = False

    x_comnati = (x_her - 1) // 10
    y_comnati = (y_her - 1) // 10

    result = False
    this_etaps = [list(result_map[y][x_comnati]) for y in range(y_comnati * 10, y_comnati * 10 + 10)]
    for i in range(len(this_etaps)):
        for ii in range(len(this_etaps[i])):
            this_etaps[i][ii] = self.board.field[y_comnati * 10 + i + 1][x_comnati * 10 + ii + 1]

    def map_enemy():
        global passage, count
        with open('passage.txt', 'r') as passage_read:
            passage = passage_read.read()
        if passage == 'False' and sum(list(map(lambda x: sum([x.count('E')]), this_etaps))) == 0:
            count += 1
            passage = 'True'
        if passage != 'True':
            return None
        chance = generation_chance(sum(list(map(lambda x: x.count('.'), this_etaps))))
        if sum(list(map(lambda x: sum([x.count('X')]), this_etaps))) != 0 and sum(
                list(map(lambda x: sum([x.count('E')]), this_etaps))) != 0:
            return None
        else:
            for i in range(10):
                for j in range(10):
                    if this_etaps[i][j] == '.' and randint(1, 100) <= chance * 100:
                        this_etaps[i][j] = 'X'
            while sum(list(map(lambda x: sum([x.count('X')]), this_etaps))) + sum(
                    list(map(lambda x: sum([x.count('E')]), this_etaps))) > 10 :
                for i in range(10):
                    for j in range(10):
                        if this_etaps[i][j] == '.' and randint(1, 100) <= chance * 100:
                            this_etaps[i][j] = 'X'
            with open('passage.txt', 'w') as passage_write:
                passage_write.write('False')

    if (x_comnati != 0 or y_comnati != 0) and x_comnati % 2 != 1 and y_comnati % 2 != 1 and x_comnati != len(
            result_map[-1]) - 1 and count < 3:
        result = True
        map_enemy()
    elif count >= 3 and x_comnati % 2 != 0 or y_comnati % 2 != 0 or (x_comnati == 0 and y_comnati == 0):
        count = 0

    with open('count.txt', 'w') as count_write:
        count_write.write(str(count))

    # with open('count.txt', 'r') as count_write:
    #     print(count_write.read())
    for i in range(len(this_etaps)):
        for ii in range(len(this_etaps[i])):
            if this_etaps[i][ii] == '@':
                this_etaps[i][ii] = '.'

    for i in range(len(result_map)):
        for ii in range(len(result_map[i])):
            if result_map[i][ii].count('@') >= 1:
                result_map[i][ii] = result_map[i][ii].replace('@', '.')
    this_etaps[(y_her - 1) % 10][(x_her - 1) % 10] = '@'

    for i in range(len(this_etaps)):
        this_etaps[i] = ''.join(this_etaps[i])

    for y in range(y_comnati * 10, y_comnati * 10 + 10):
        result_map[y][x_comnati] = this_etaps[y % 10]

    result_map_copy = add_wall(preparing_map(result_map))
    self.board.field = result_map_copy
    with open('passage.txt', 'w') as passage_write:
        passage_write.write(str(passage))

    result_map_copy[-7][-7] = 'П'
    result_map_copy[-6][-7] = 'П'
    result_map_copy[-7][-6] = 'П'
    result_map_copy[-6][-6] = 'П'

    return result
