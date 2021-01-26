import numpy as np
from math import sqrt
import itertools
from pprint import pprint

# there is a numpy thing for this.
# def rotate(matrix):
#     return list(reversed(list(zip(*matrix))))


# Take one, put in, take out next, try it on, match -> take next
# doesn't match -> put it back, try next.
# have an index, the position we are trying to solve.
# somehow increase the location at which the solving is happening.
def solve(image, p, tiles):
    if p[0] >= len(image):
        return True
    for current in tiles:
        if can_fit(image, current, p):
            image[p[0]][p[1]] = current
            new_p = p
            new_p[1] += 1
            if new_p[1] == len(image):
                new_p[0] += 1
                new_p[1] = 0
            # print(f'new point: {new_p}')
            if solve(image, new_p, tiles):
                return True
            else:
                image[p[0]][p[1]] = ()


def can_fit(image, m1, p):
    if p[0]-1 >= 0:
        # match up
        if try_match(image[p[0]-1][p[1]], m1, match_up):
            return True
    if p[0]+1 < len(image):
        # match down
        if try_match(image[p[0]+1][p[1]], m1, match_down):
            return True
    if p[1]+1 < len(image):
        # match right
        if try_match(image[p[0]][p[1]+1], m1, match_right):
            return True
    if p[1]-1 >= 0:
        # match left
        if try_match(image[p[0]][p[1]-1], m1, match_left):
            return True
    return False


def pretty_print(tiles):
    for tile in tiles:
        print(f'Tile: {tile[0]}')
        for y in tile[1]:
            for x in y:
                print(x, end='')
            print()
        print()


def try_match(m1, m2, f) -> bool:
    ## match, rotate, flip, rotate, flip
    return False


def match_up(m1, m2) -> bool:
    for i in range(len(m1[0])):
        if m1[0][i] != m2[-1][i]:
            return False
    return True


def match_down(m1, m2) -> bool:
    for i in range(len(m1[-1])):
        if m1[-1][i] != m2[0][i]:
            return False
    return True


def match_right(m1, m2) -> bool:
    for i in range(len(m1)):
        if m1[i][-1] != m2[i][0]:
            return False
    return True


def match_left(m1, m2) -> bool:
    for i in range(len(m1)):
        if m1[i][0] != m2[i][-1]:
            return False
    return True


my_file = open("day20/test.txt", "r")
content = my_file.read()
tiles = []
tile_id = ''
m = []

for line in content.splitlines():
    if line == '':
        tiles.append((tile_id, m))
        tile_id = ''
        m = []
        continue

    if line.startswith('Tile'):
        tile = line.split(' ')
        tile_id = tile[1].replace(':', '')
        continue

    m.append(list(line))

# add the last tile.
tiles.append((tile_id, m))
pretty_print(tiles)

w = int(sqrt(len(tiles)))
image = [[() for x in range(w)] for y in range(w)]
print(image)

# solve for a location
solve(image, [0, 0], tiles)

# needs to be a square...
# there are only so many combinations the tiles can be arranged in.
# first, arrange all the tiles in all possible combinations on a MxM matrix
# then go through all of the combinations and try to fit them together?
# create the matrix

# start building it up rather than getting all of the permutations.
# keys = list(tiles.keys())
# x = int(sqrt(len(keys)))
# image = np.array(keys).reshape(x, x)
# print(image)
#
# pprint([np.array(i).reshape(image.shape).tolist() for i in set(itertools.permutations(itertools.chain.from_iterable(image)))])
#
# pretty_print(tiles)
