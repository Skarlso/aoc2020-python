my_file=open("day04/input.txt","r")
content = my_file.read()

valids = 0
passport = {}
for line in content.splitlines():
    line = line.strip()
    if not line:
        valid = True
        for field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
            if field not in passport:
                valid = False
        if valid:
            valids += 1
        passport = {}
    else:
        words = line.split()
        for w in words:
            k, v = w.split(':')
            passport[k] = v

print(valids)