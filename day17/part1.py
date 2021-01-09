my_file = open("day17/input.txt", "r")
content = my_file.read()

field = set()
lines = [line.strip() for line in content.splitlines()]

for i, line in enumerate(lines):
    for j, ch in enumerate(line):
        if ch == '#':
            field.add((i, j, 0))

for _ in range(6):
    new_field = set()
    for x in range(-15, 15):
        for y in range(-15, 15):
            for z in range(-15, 15):
                nbr = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        for dz in [-1, 0, 1]:
                            if dx != 0 or dy != 0 or dz != 0:
                                if (x + dx, y + dy, z + dz) in field:
                                    nbr += 1
                if (x, y, z) not in field and nbr == 3:
                    new_field.add((x, y, z))
                if (x, y, z) in field and nbr in [2, 3]:
                    new_field.add((x, y, z))
    field = new_field

print(len(field))
