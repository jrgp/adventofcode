def impl(lines):
    prev = None
    larger = 0

    for line in lines:
        if prev is not None:
            if line > prev:
                larger += 1
        prev = line

    return larger


lines = list(map(int, open('1_input.txt')))
print(impl(lines))
