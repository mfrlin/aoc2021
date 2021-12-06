import fileinput

puzzle_input = fileinput.input()

numbers = list(map(int, next(puzzle_input).strip().split(',')))
print(numbers)

class Board:
    def __init__(self, numbers):
        self.numbers = numbers
        self.filled = [False] * len(numbers)

    def fill_number(self, n):
        try:
            position = self.numbers.index(n)
        except:
            pass
        else:
            return n * self._mark_hit(position)

    def _mark_hit(self, position):
        self.filled[position] = True
        row = position // 5
        column = position % 5

        if all(self.filled[column::5]) or all(self.filled[row*5:row*5+5]):
            return self._sum_unmarked()
        return 0

    def _sum_unmarked(self):
        return sum(n for n, f in zip(self.numbers, self.filled) if not f)



boards = []
current_board = []
for line in puzzle_input:
    line = line.strip()
    if line == '':
        continue
    current_board += list(map(int, line.split()))
    if len(current_board) == 25:
        boards.append(Board(current_board))
        current_board = []


def run():
    for n in numbers:
        print('processing', n)
        for b in boards:
            res = b.fill_number(n)
            if res:
                print('result:', res)
                return

run()
