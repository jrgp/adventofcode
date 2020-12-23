def impl(lines):
    width = len(lines[0])
    x = 0
    trees = 0
    for line in lines:
        pos = x
        if pos > width:
            pos = x % width
        if line[pos] == '#':
            trees += 1
        x += 3
    return trees

lines = [line.strip() for line in open('3_input.txt') if line.strip() != '']

result = impl(lines)

print(f'Result: {result}')
