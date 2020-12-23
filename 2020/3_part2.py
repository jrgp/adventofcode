from collections import namedtuple, Counter

Directional = namedtuple('Directional', 'right, down')

def impl(lines, directionals):
    width = len(lines[0])
    numlines = len(lines)
    dirx = Counter()
    diry = Counter()
    dirtrees = Counter()
    remaining = len(directionals)
    dones = []

    while remaining:
        for d_index, d in enumerate(directionals):
            if diry[d_index] > numlines - 1:
                pass
            else:
                pos = dirx[d_index]
                if pos >= width:
                    pos = dirx[d_index] % width
                line_pos = diry[d_index]
                if lines[line_pos][pos] == '#':
                    dirtrees[d_index] += 1
                dirx[d_index] += d.right
                diry[d_index] += d.down
                if diry[d_index] > numlines - 1:
                    remaining -= 1

    result = 1
    for d_index, d in enumerate(directionals):
        r = dirtrees[d_index]
        result *= r
    return result

lines = [line.strip() for line in open('3_input.txt') if line.strip() != '']

directionals = [
    Directional(right=1, down=1),
    Directional(right=3, down=1),
    Directional(right=5, down=1),
    Directional(right=7, down=1),
    Directional(right=1, down=2),
]

result = impl(lines, directionals)

print(f'Result: {result}')

