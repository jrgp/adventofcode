from collections import defaultdict, Counter

def impl_simple(lines):
    positions = 12
    bit_counter = defaultdict(Counter)
    for line in lines:
        number = int(line, 2)
        for position in range(positions):
            value = 1 if (number & (1 << position)) != 0 else 0
            bit_counter[position][value] += 1

    gamma = 0
    epsilon = 0

    for position, counts in bit_counter.items():
        if counts[1] > counts[0]:
            gamma |= (1 << position)
        else:
            epsilon |= (1 << position)

    return gamma * epsilon

def impl_clever(lines):
    positions = 12
    bit_counter = defaultdict(Counter)
    for line in lines:
        number = int(line, 2)
        for position in range(positions):
            value = 1 if (number & (1 << position)) != 0 else 0
            bit_counter[position][value] += 1

    gamma = 0

    for position, counts in bit_counter.items():
        if counts[1] > counts[0]:
            gamma |= (1 << position)

    # We can also determine epsilon by "simply" inverting all
    # bits within gamma
    epsilon = (~gamma & (1 << positions) - 1)

    return gamma * epsilon

lines = open('3_input.txt').readlines()
assert impl_simple(lines) == impl_clever(lines)
print(impl_simple(lines))
