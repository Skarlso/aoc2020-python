import re

class Validator:
    """
    Validator validates a passport.
    """
    def __init__(self, passport):
        self.passport = passport

    def is_valid(self) -> bool:
        return self.byr() and self.iyr() and self.eyr() and self.hgt() and self.hcl() and self.ecl() and self.pid()

    def byr(self) -> bool:
        if 'byr' not in self.passport:
            return False
        return int(self.passport['byr']) >= 1920 and int(self.passport['byr']) <= 2002

    def iyr(self) -> bool:
        if 'iyr' not in self.passport:
            return False        
        return int(self.passport['iyr']) >= 2010 and int(self.passport['iyr']) <= 2020

    def eyr(self) -> bool:
        if 'eyr' not in self.passport:
            return False        
        return int(self.passport['eyr']) >= 2020 and int(self.passport['eyr']) <= 2030

    def hgt(self) -> bool:
        if 'hgt' not in self.passport:
            return False        
        if self.passport['hgt'].endswith('cm'):
            i = self.passport['hgt'][:-2]
            return int(i) >= 150 and int(i) <= 193
        elif self.passport['hgt'].endswith('in'):
            i = self.passport['hgt'][:-2]
            return int(i) >= 59 and int(i) <= 76
        return False

    def hcl(self) -> bool:
        if 'hcl' not in self.passport:
            return False        
        if self.passport['hcl'][0] != '#':
            return False

        r = re.compile(r'^[a-f|0-9]+$')
        if r.match(self.passport['hcl'][1:]):
            return True

        return False

    def ecl(self) -> bool:
        if 'ecl' not in self.passport:
            return False        
        allowed = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        return self.passport['ecl'] in allowed


    def pid(self) -> bool:
        if 'pid' not in self.passport:
            return False        
        return len(self.passport['pid']) == 9

    

my_file=open("day04/input.txt","r")
content = my_file.read()

valids = 0
passport = {}
for line in content.splitlines():
    line = line.strip()
    if not line:
        validator = Validator(passport)
        if validator.is_valid():
            valids += 1
        passport = {}
    else:
        words = line.split()
        for w in words:
            k, v = w.split(':')
            passport[k] = v

print(valids)