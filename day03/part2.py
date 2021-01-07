my_file=open("day03/input.txt","r")
content = my_file.read()

area = []
for l in content.splitlines():
    area.append(l)

slops = [(1,1), (3,1), (5,1), (7,1), (1,2)]
s = 1
for slop in slops:
    right = slop[0]
    down = slop[1]
    trees = 0
    i = 0
    j = 0
    while i < len(area):
        if area[i][j] == '#':
            trees += 1
        
        j = (j + right) % len(area[i])
        i += down
    s *= trees

print(s)