my_file = open("day19/input.txt", "r")
content = my_file.read()

L = [line.strip() for line in content.splitlines()]
R = {}
C = {}


def match_list(line, st, ed, rules):
    if st == ed and not rules:
        return True
    if st == ed:
        return False
    if not rules:
        return False

    ret = False
    for i in range(st + 1, ed + 1):
        if match(line, st, i, rules[0]) and match_list(line, i, ed, rules[1:]):
            ret = True

    return ret


DP = {}


def match(line, st, ed, rule):
    key = (st, ed, rule)
    if key in DP:
        return DP[key]

    ret = False
    if rule in C:
        ret = (line[st:ed] == C[rule])
    else:
        for option in R[rule]:
            if match_list(line, st, ed, option):
                ret = True

    DP[key] = ret
    return ret


def solve():
    ans = 0
    for line in L:
        if ':' in line:
            words = line.split()
            name = words[0][:-1]
            rest = ' '.join(words[1:])
            if "\"" in rest:
                C[name] = rest[1:-1]
            else:
                options = rest.split(' | ')
                R[name] = [x.split(' ') for x in options]
        elif line:
            DP.clear()
            if match(line, 0, len(line), '0'):
                ans += 1
    return ans


print(solve())
