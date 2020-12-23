def impl(data):
    count = 0

    for line in data:
        parts = line.split()
        min, max = map(int, parts[0].split('-'))
        char = parts[1][0]
        s = parts[2]

        if min <= s.count(char) <= max:
            count += 1

    return count

data = [line.strip() for line in open('2_input.txt') if line.strip() != '']

result = impl(data)

print(f'Result: {result}')
