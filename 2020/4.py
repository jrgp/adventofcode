passports = open('4_input.txt').read().strip().split('\n\n')

def impl(passports):
    valid_passports = 0
    required_keys = {
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
    }
    for passport in passports:
        pairs = passport.split()
        keys = {pair[:pair.index(':')] for pair in pairs}
        if keys >= required_keys:
            valid_passports += 1
    return valid_passports

result = impl(passports)

print(f'Result: {result}')
