import fileinput


class SlidingWindow:
    def __init__(self, size):
        self._size = size
        self._values = []

    def append(self, x):
        self._values.append(x)
        if len(self._values) > self._size:
            self._values.pop(0)

    def sum(self):
        return sum(self._values)

    def __str__(self):
        return f'{self._values} ({self.sum()})'



counter = 0
window_size = 3
prev = SlidingWindow(window_size)
curr = SlidingWindow(window_size)

for i, value in enumerate(map(int, fileinput.input())):
    curr.append(value)
    if i >= window_size:
        increased = curr.sum() > prev.sum()
        print(f'{curr} > {prev} : {increased} ')
        if increased:
            counter += 1
    prev.append(value)


print(counter)