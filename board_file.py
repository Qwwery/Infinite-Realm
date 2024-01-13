from maps import generation_map


class Board:
    def __init__(self, width, height, cell_cize):
        self.this_level = 1
        self.width = width
        self.height = height

        self.left_start = 65
        self.top_start = 65
        self.cell_size = cell_cize

        self.field = generation_map()
        self.add_wall(self.field)

        self.new_level = False

    def add_wall(self, field):
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

    def return_heroes_cords(self):
        for y_n in range(len(self.field)):
            for x_n in range(len(self.field[y_n])):
                if self.field[y_n][x_n] == "@":
                    return x_n, y_n
