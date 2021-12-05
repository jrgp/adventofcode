def impl(lines):
    x = 0
    y = 0
    aim = 0

    for line in lines:
        command, arg = line.split()
        arg = int(arg)
        if command == 'forward':
            x += arg
            y += (aim * arg)
        elif command == 'down':
            aim += arg
        elif command == 'up':
            aim -= arg
    return x * y

lines = open('2_input.txt').readlines()
print(impl(lines))
