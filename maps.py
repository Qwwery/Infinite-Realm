import pprint
from random import randint, shuffle
from rooms import rooms, passage


def generation_map():
    count_stage = randint(4, 7)
    difficulty_level = int()  # Придумать алгоритм генерации сложности в зависимости от кол-ва. стадий на уровне в обратной пропорции
    map_level = [[0 for _ in range(14)] for _ in range(14)]
    x, y = 7, 7 # 3 3 - точка старта
    map_level[x][y] = 1
    direction = -1
    cords = (0, 0)
    stages = [1]
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
            count = 0
            for i_lvl in range(len(result_map)):
                result_map[cords[1]].append(' ' * 10 if y != cords[1] + 4 and y != cords[1] + 5 else '.' * 10)
                cords = cords[0], cords[1] + 1
                count += 1
            cords = cords[0] + 10, cords[1] - 10
        elif i == 'v':
            for i in range(len(result_map[0]) * 10):
                pass

        else:
            for i_lvl in rooms[i]:
                try:
                    result_map[cords[1]].append(''.join(i_lvl))
                except IndexError:
                    result_map.append(''.join(i_lvl).split())
                cords = cords[0], cords[1] + 1
            cords = cords[0] + 10, cords[1] - 10

        for j in result_map:
            print(j)
        print('-' * 10)

    print()

    # for i in range(count_stage - 1):
    #     while True:
    #         direction = randint(0, 3) # 0 - лево, 1 - право, 2 - верх, 3 - низ
    #         if direction == 0:
    #             x -= 1
    #             direction_to_the_level = '<'
    #         elif direction == 1:
    #             x += 1
    #             direction_to_the_level = '>'
    #         elif direction == 2:
    #             y -= 1
    #             direction_to_the_level = '^'
    #         elif direction == 3:
    #             y += 1
    #             direction_to_the_level = 'v'
    #         if map_level[x][y] == 1:
    #             if direction == 0:
    #                 x += 1
    #             elif direction == 1:
    #                 x -= 1
    #             elif direction == 2:
    #                 y += 1
    #             elif direction == 3:
    #                 y -= 1
    #         else:
    #             maps = list(rooms.keys())
    #             shuffle(maps)
    #             this_map = maps[0]
    #             stages.append(this_map)
    #             stages.append(direction_to_the_level)
    #             break
    #     map_level[x][y] = 1
    # print(stages)
    # print(cords)
    # stages = ['1g', '<', '3g', '<', '3g', '<',  1, '<', '1_v', 'v', '2g', 'v']
    # for i in stages:
    #     new_x, new_y = 0, 0
    #     if i == '>': #x. y
    #         cords = (cords[0] + 18, cords[1])
    #         new_y = cords[1] + 10
    #         print(new_y)
    #         for y in range(new_y):
    #             result_map[y] = result_map[y] + (' ' if y != cords[1] + 4 and y != cords[1] + 5 else '.') * 8
    #     elif i == '<':
    #         cords = (cords[0] - 18, cords[1]) if cords[0] - 18 >= 0 else (cords[0], cords[1])
    #         new_y = cords[1] + 10
    #         for y in range(new_y):
    #             result_map[y] = (' ' if y != cords[1] + 4 and y != cords[1] + 5 else '.') * 8 + result_map[y]
    #     elif i == '^':
    #         cords = (cords[0], cords[1] - 18) if cords[1] - 18 >= 0 else (cords[0], cords[1])
    #         for x in range(8):
    #             result_map.insert(0, ' ' * 4 + '..' + ' ' * 4)
    #     elif i == 'v':
    #         cords = (cords[0], cords[1] + 18)
    #         new_x = cords[0] + 8
    #         for x in range(new_x):
    #             result_map.append(' ' * 4 + '..' + ' ' * 4)
    #
    #     else:
    #         for y in rooms[i]:
    #             try:
    #                 result_map[cords[1]] += ''.join(y)
    #             except IndexError:
    #                 result_map.append(''.join(y))
    #             cords = (cords[0], cords[1] + 1)
    #         cords = (cords[0], cords[1] - 10)
    #     print('[' + ']\n['.join(result_map) + ']')
    #     print(cords)
    #     print(stages)
    #     # count = 0
    #     #
    #     # if i == '>':
    #     #     for width in range(cords[1]):
    #     #         result_map[width] = result_map[width] + (' ' if width != cords[1] + 4 and width != cords[1] + 5 else '.') * 8
    #     #         cords = (cords[0], cords[1] + 1)
    #     #         print(cords)
    #     #     cords = (cords[0] + 8, cords[1] - 10)
    #     #
    #     # elif i == '<':
    #     #     for width in range(10):
    #     #         result_map[cords[1]] = (' ' if count != 4 and count != 5 else '.') * 8 + result_map[cords[1]]
    #     #         count += 1
    #     #         cords = (cords[0], cords[1] + 1)
    #     #     if cords[0] - 8 >= 0:
    #     #         cords = (cords[0] - 8, cords[1] - 10)
    #     #
    #     # elif i == '^':
    #     #     cords = (cords[0], cords[1] + 10)
    #     #     for width in range(8):
    #     #         result_map.insert(0, '    ..    ')
    #     #     cords = (cords[0], cords[1] + 8)
    #     #     # cords = (cords[0], len(result_map))
    #     #
    #     # elif i == 'v':
    #     #     cords = (cords[0], cords[1] + 10)
    #     #     for width in range(8):
    #     #         result_map.append('    ..    ')
    #     #     cords = (cords[0], cords[1] + 8)
    #     #
    #     #     # for width in range(10):
    #     #     #     result_map.append('')
    #     #     #     result_map[width + cords[1]] = (' ' if count != 4 and count != 5 else '.') * 8 + result_map[cords[1]]
    #     #     #     count += 1
    #     #     #     cords = (cords[0], cords[1] + 1)
    #     #     # cords = (cords[0], cords[1] - 10)
    #     #
    #     # else:
    #     #     for width in rooms[i]:
    #     #         try:
    #     #             result_map[cords[1]] += ''.join(width)
    #     #         except IndexError:
    #     #             result_map.append(''.join(width))
    #     #         cords = (cords[0], cords[1] + 1)
    #     #     cords = (cords[0], cords[1] )
    #     # print('[' + ']\n['.join(result_map) + ']')
    #     # print(cords)

    return
generation_map()
