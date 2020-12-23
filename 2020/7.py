import re
from collections import defaultdict

def impl(lines):
    reverse_index = defaultdict(set)

    for line in lines:
        if 'contain no other bags' in line:
            continue
        m = re.match('(\S+ \S+) bags contain ', line)
        if m:
            container = m.group(1)
        else:
            continue
        childs = re.findall('\d+ (\S+ \S+) bags?', line)
        for child in childs:
            reverse_index[child].add(container)

    root = reverse_index['shiny gold']
    stack = list(root)
    possible = set()
    while stack:
        item = stack.pop()
        possible.add(item)
        if len(reverse_index[item]):
            stack.extend(list(reverse_index[item]))
    return len(possible)


lines = [line.strip() for line in open('7_input.txt') if line.strip() != '']

result = impl(lines)

print(f'Result: {result}')
