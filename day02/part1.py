from collections import defaultdict

my_file=open("day02/input.txt","r")
content = my_file.read()

valid = 0
for line in content.splitlines():
    words = line.strip().split()
    print(words)
    low, hi = [int(x) for x in words[0].split('-')]
    letter = words[1][0]
    password = words[2]
    counts = defaultdict(int)
    for ch in password:
        counts[ch] += 1
    if low <= counts[letter] <= hi:
        valid += 1

print(valid)
