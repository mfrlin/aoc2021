import fileinput


depth = 0
horizontal = 0


def move(line):
    global depth
    global horizontal

    direction, value = line.strip().split(' ')
    value = int(value)

    if direction == 'up':
        depth -= value
        print(f'moving up -{value} = {depth}')
    elif direction == 'down':
        depth += value
        print(f'moving down +{value} = {depth}')
    else:
        horizontal += value
        print(f'moving forward +{value} = {horizontal}')




for line in fileinput.input():
    move(line)
print(depth * horizontal)