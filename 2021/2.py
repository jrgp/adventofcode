def impl(lines):
    x = 0
    y = 0

    for line in lines:
        command, arg = line.split()
        arg = int(arg)
        if command == 'forward':
            x += arg
        elif command == 'down':
            y += arg
        elif command == 'up':
            y -= arg
    return x * y

lines = open('2_input.txt').readlines()
print(impl(lines))
