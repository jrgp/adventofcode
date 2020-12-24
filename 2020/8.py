def impl(lines):
    a = 0
    pc = 0
    seen_lines = set()
    while True:
        line = lines[pc]
        op, arg = line.split()
        if op == 'nop':
            pc += 1
        elif op == 'acc':
            a += int(arg)
            pc += 1
        elif op == 'jmp':
            pc += int(arg)
        else:
            raise Exception(f'unknown op {op}')
        if pc in seen_lines:
            return a
        else:
            seen_lines.add(pc)

lines = [line.strip() for line in open('8_input.txt') if line.strip() != '']

result = impl(lines)

print(f'Result: {result}')
