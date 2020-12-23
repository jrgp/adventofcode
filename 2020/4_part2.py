import re

def impl(passports):
    def validate_height(height):
        num = height[:-2]
        unit = height[-2:]
        if unit == 'cm':
            return 150 <= int(num) <= 193
        elif unit == 'in':
            return 59 <= int(num) <= 76
        else:
            return False
    valid_passports = 0
    required_keys = {
        'byr': lambda x: len(x) == 4 and x.isdigit() and 1920 <= int(x) <= 2002,
        'iyr': lambda x: len(x) == 4 and x.isdigit() and 2010 <= int(x) <= 2020,
        'eyr': lambda x: len(x) == 4 and x.isdigit() and 2020 <= int(x) <= 2030,
        'hgt': validate_height,
        'hcl': lambda x: re.match('#[0-9a-f]{6}', x) is not None,
        'ecl': lambda x: x in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
        'pid': lambda x: len(x) == 9 and x.isdigit(),
    }
    for passport in passports:
        pairs = passport.split()
        passed = set()
        for pair in pairs:
            key, value = pair.split(':')
            validator = required_keys.get(key)
            if validator:
                if validator(value):
                    passed.add(key)
        if passed == required_keys.keys():
            valid_passports += 1
    return valid_passports

passports = open('4_input.txt').read().strip().split('\n\n')

result = impl(passports)

print(f'Result: {result}')

