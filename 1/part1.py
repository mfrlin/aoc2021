import fileinput

counter = 0
prev = None

for i in map(int, fileinput.input()):
    if prev is None:
        prev = i

    print(f'comparing {i} to {prev}: {i > prev} {counter}')
    if i > prev:
        counter += 1
    prev = i

print(counter)