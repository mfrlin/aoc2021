import fileinput


depth = 0
horizontal = 0
aim = 0


def move(line):
    global depth
    global horizontal
    global aim

    direction, value = line.strip().split(' ')
    value = int(value)

    if direction == 'up':
        aim -= value
        print(f'aiming up -{value} = {aim}')
    elif direction == 'down':
        aim += value
        print(f'aiming down +{value} = {aim}')
    else:
        horizontal += value
        depth += aim * value
        print(f'moving forward +{value} = {horizontal}, {depth}')




for line in fileinput.input():
    move(line)
print(depth * horizontal)