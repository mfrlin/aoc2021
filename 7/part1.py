import fileinput

crabs = list(map(int, next(fileinput.input()).strip().split(',')))

def cost(n, target):
    return abs(n - target)


position = sum(crabs) // len(crabs)



start_cost = sum(cost(crab, position) for crab in crabs)
next_cost = sum(cost(crab, position + 1) for crab in crabs)

if start_cost > next_cost:
    direction = 1
else:
    direction = -1


while True:
    if position < 0:
        break
    next_cost = sum(cost(crab, position + direction) for crab in crabs)
    if start_cost < next_cost:
        print(position, start_cost)
        break
    else:
        position += direction
        start_cost = next_cost