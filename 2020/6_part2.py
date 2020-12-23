def impl(data):
    count = 0
    for group in data:
        questions = None
        for person in group.split():
            person_questions = set(person)
            if questions is None:
                questions = person_questions
            else:
                questions &= person_questions
        count += len(questions)

    return count

data = open('6_input.txt').read().strip().split('\n\n')

result = impl(data)

print(f'Result: {result}')
