my_file=open("day03/input.txt","r")
content = my_file.read()

area = []
for l in content.splitlines():
    area.append(l)

right = 3
down = 1
side = 0
bottom = 0
trees = 0

while bottom < len(area)-1:
    if area[bottom][side] == '#':
        trees += 1
    
    side = (side+right) % len(area[bottom])
    bottom += down

print(trees)