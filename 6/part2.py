import fileinput
from collections import deque
from timeit import default_timer as timer

starting_fishies = list(map(int, next(fileinput.input()).strip().split(',')))

fishies = deque([0] * 9)
for f in starting_fishies:
    fishies[f] += 1

start = timer()
for i in range(256):
    new_gen = fishies.popleft()
    fishies.append(new_gen)
    fishies[6] += new_gen
end = timer()

print(f'{(end - start) * 1_000_000}')
print(sum(fishies)) 
    