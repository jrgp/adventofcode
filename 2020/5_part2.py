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
    all_ids = sorted(parse_bsp(line) for line in lines)
    for myid in range(all_ids[0], all_ids[-1]+1):
        if myid not in all_ids and myid + 1 in all_ids and myid - 1 in all_ids:
            return myid

data = [line.strip() for line in open('5_input.txt') if line.strip() != '']

result = impl(data)

print(f'Result: {result}')
