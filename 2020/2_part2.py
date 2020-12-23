def impl(data):
    count = 0

    for line in data:
        parts = line.split()
        pos1, pos2 = map(lambda x: int(x) - 1, parts[0].split('-'))
        char = parts[1][0]
        s = parts[2]

        pos1_correct = s[pos1] == char
        pos2_correct = s[pos2] == char

        if (pos1_correct or pos2_correct) and (pos1_correct ^ pos2_correct):
            count += 1

    return count

data = [line.strip() for line in open('2_input.txt') if line.strip() != '']

result = impl(data)

print(f'Result: {result}')

