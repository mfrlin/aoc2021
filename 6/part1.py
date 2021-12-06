import fileinput

fishies = list(map(int, next(fileinput.input()).strip().split(',')))

for i in range(80):
    for i, v in enumerate(fishies[:]):
        v -= 1
        if v < 0:
            v = 6
            fishies.append(8)
        fishies[i] = v

print(len(fishies))