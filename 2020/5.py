def parse_bsp(line):
    rows = list(range(128))
    for c in line[:7]:
        if c == 'F':
            rows = rows[:(len(rows)//2)]
        elif c == 'B':
            rows = rows[(len(rows)//2):]
        else:
            raise Exception(f'Unknown {c}')
    row = rows.pop()

    columns = list(range(8))
    for c in line[-3:]:
        if c == 'L':
            columns = columns[:(len(columns)//2)]
        elif c == 'R':
            columns = columns[(len(columns)//2):]
        else:
            raise Exception(f'Unknown {c}')
    column = columns.pop()

    return (row * 8) + column

def impl(lines):
    highest = 0
    for line in lines:
        seat = parse_bsp(line)
        if seat > highest:
            highest = seat
    return highest

data = [line.strip() for line in open('5_input.txt') if line.strip() != '']

result = impl(data)

print(f'Result: {result}')
