def impl(data, target):
  s = set(data)
  for n1 in s:
      n2 = target - n1
      if n2 in s:
          print(f'{n1} {n2}')
          return n1 * n2

data = [int(line) for line in open('1_input.txt') if line.strip() != '']

target = 2020

result = impl(data, target)

print(f'Result: {result}')
