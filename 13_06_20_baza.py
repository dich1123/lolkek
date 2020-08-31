import random

pole = [['_', '_', '_', '_'],
        ['_', '_', '_', '_'],
        ['_', '_', '_', '_'],
        ['_', '_', '_', '_']]


def pprint(pole):
    max_length = []
    for i in range(len(pole)):
        max_length.append(0)

    for i in range(len(pole)):
        for j in range(len(pole)):
            elem = str(pole[i][j])
            if max_length[j] < len(elem):
                max_length[j] = len(elem)

    for i in pole:
        row = '|'
        for j in range(len(i)):
            elem = str(i[j])
            row += '_' * (max_length[j] - len(elem)) + elem + '|'
        print(row)


def is_full(pole):
    for i in pole:
        for j in i:
            if j == '_':
                return False
    return True


def rand_hod(pole):
    if is_full(pole):
        return pole
    num = [2, 2, 2, 4]
    while True:
        x = random.randint(0, len(pole)-1)
        y = random.randint(0, len(pole)-1)
        random_num = random.choice(num)
        if pole[x][y] == '_':
            pole[y][x] = random_num
            return pole


pprint(pole)
pole = rand_hod(pole)
print('_______________')
pprint(pole)