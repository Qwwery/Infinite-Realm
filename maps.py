import random
from random import randint, shuffle

from rooms import rooms, RIGHT, DOWN


def generation_map():
    count_stage = random.randint(12, 18)
    difficulty_level = int()  # Придумать алгоритм генерации сложности в зависимости от кол-ва. стадий на уровне в
    # обратной пропорции
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
    print(stages)

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

    for i_lvl in rooms[1]:
        try:
            result_map[cords[1]].append(''.join(i_lvl))
        except IndexError:
            result_map.append([''.join(i_lvl)])
        cords = cords[0], cords[1] + 1
    cords = cords[0] + 10, cords[1] - 10

    # for i in range(len(result_map)):
    #     result_map[i] = list(''.join(result_map[i]))
    #
    # result_map[5][5] = '@'

    return result_map
for i in generation_map():
    print(i)