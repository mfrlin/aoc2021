import fileinput


counter = None

for i, line in enumerate(fileinput.input()):
    line = list(map(int, line.strip()))
    if counter is None:
        counter = line
    else:
        counter = [c + l for c, l in zip(counter, line)]

gama = int(''.join(str(int(c > i / 2)) for c in counter), 2)
epsilon = int(''.join(str(int(c < i / 2)) for c in counter), 2)

print(gama * epsilon)
