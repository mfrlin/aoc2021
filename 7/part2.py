import fileinput

crabs = list(map(int, next(fileinput.input()).strip().split(',')))

def cost(n, target):
    return sum(range(abs(n - target)+1))


position = sum(crabs) // len(crabs)

# costs = []
# for i in range(max(crabs)+1):
#     costs.append(sum(cost(crab, i) for crab in crabs))

# print(costs)



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