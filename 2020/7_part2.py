import re
from collections import defaultdict

def impl(lines):
    index = defaultdict(list)

    for line in lines:
        if 'contain no other bags' in line:
            continue
        m = re.match('(\S+ \S+) bags contain ', line)
        if m:
            container = m.group(1)
        else:
            continue
        childs = re.findall('(\d+) (\S+ \S+) bags?', line)
        for child in childs:
            index[container].append(child)

    total_count = 0
    stack = index['shiny gold'].copy()
    while stack:
        item = stack.pop()
        count = int(item[0])
        total_count += count
        bag = item[1]
        for x in range(count):
            stack.extend(index[bag])

    return total_count

lines = [line.strip() for line in open('7_input.txt') if line.strip() != '']

result = impl(lines)

print(f'Result: {result}')
