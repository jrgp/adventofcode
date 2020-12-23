def impl(data):
    count = 0
    for group in data:
        questions = set()
        for person in group.split():
            questions.update(set(person))
        count += len(questions)
    return count

data = open('6_input.txt').read().strip().split('\n\n')

result = impl(data)

print(f'Result: {result}')
