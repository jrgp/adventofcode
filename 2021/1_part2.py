def impl(lines):
    larger = 0

    for i in range(len(lines)):
        if i == 0:
            continue

        try:
            prev_window = sum([lines[i-1], lines[i], lines[i+1]])
            this_window = sum([lines[i], lines[i+1], lines[i+2]])
        except IndexError:
            break

        if this_window > prev_window:
            larger += 1
    return larger


lines = list(map(int, open('1_input.txt')))
print(impl(lines))
