import pprint
from random import randint


def generation_map():
    count_stage = randint(4, 7)
    print(count_stage)
    difficulty_level = int()  # Придумать алгоритм генерации сложности в зависимости от кол-ва. стадий на уровне в обраной пропорции
    map_level = [[0 for _ in range(14)] for _ in range(14)]
    x, y = 7, 7 # 3 3 - точка старта
    map_level[x][y] = 1
    direction = -1
    last_direction = -1
    for i in range(count_stage - 1):
        while True:
            direction = randint(0, 3) # 0 - лево, 1 - право, 2 - верх, 3 - низ
            if direction == 0:
                y -= 1
            elif direction == 1:
                y += 1
            elif direction == 2:
                x -= 1
            elif direction == 3:
                x += 1
            if map_level[x][y] == 1:
                if direction == 0:
                    y += 1
                elif direction == 1:
                    y -= 1
                elif direction == 2:
                    x += 1
                elif direction == 3:
                    x -= 1
            else:
                break
        map_level[x][y] = 1
        last_direction = direction
    pprint.pprint(map_level)


generation_map()