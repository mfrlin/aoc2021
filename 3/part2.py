import fileinput
import operator


class Node:
    def __init__(self, node_one, node_zero):
        self.count = 0
        self.one = node_one
        self.zero = node_zero


def create_tree(n):
    if n == 12:
        return None, None
    return Node(*create_tree(n+1)), Node(*create_tree(n+1))

tree = Node(*create_tree(1))

for i, line in enumerate(fileinput.input(), 1):
    curr_node = tree
    line = list(map(int, line.strip()))
    for bit in line:
        curr_node.count += bit
        if bit:
            curr_node = curr_node.one
        else:
            curr_node = curr_node.zero


oxygen_rating = []
co2_rating = []
for var, comparator in [(oxygen_rating, operator.ge), (co2_rating, operator.lt)]:
    curr_node = tree
    curr_count = i
    while curr_node is not None:
        one_left = curr_count <= 1
        if (one_left and curr_node.count == 1) or (not one_left and comparator(curr_node.count, curr_count / 2)):
            curr_count = curr_node.count
            var.append('1')
            curr_node = curr_node.one
        else:
            curr_count = curr_count - curr_node.count
            var.append('0')
            curr_node = curr_node.zero

oxygen_rating = int(''.join(oxygen_rating), 2)
co2_rating = int(''.join(co2_rating), 2)
print('oxygen rating:', oxygen_rating)
print('co2 rating:', co2_rating)
print(oxygen_rating * co2_rating)
