import fileinput


sparse_matrix = dict()

def produce_diagonal(x1, y1, x2, y2):
    x_mod = -1
    y_mod = -1
    if x1 <= x2:
        x_mod = 1
    if y1 <= y2:
        y_mod = 1
    return list(zip(range(x1, x2 + x_mod, x_mod),range(y1, y2 + y_mod, y_mod)))

for line in fileinput.input():
    point1, point2 = line.strip().split('->')
    point1 = tuple(map(int, point1.strip().split(',')))
    point2 = tuple(map(int, point2.strip().split(',')))
    if point1[0] == point2[0]:
        for i in range(min(point1[1], point2[1]), max(point1[1], point2[1])+1):
            point = (point1[0], i)
            if point in sparse_matrix:
                sparse_matrix[point] += 1
            else:
                sparse_matrix[point] = 1
    elif point1[1] == point2[1]:
        for i in range(min(point1[0], point2[0]), max(point1[0], point2[0])+1):
            point = (i, point1[1])
            if point in sparse_matrix:
                sparse_matrix[point] += 1
            else:
                sparse_matrix[point] = 1
    else:
        for p in produce_diagonal(*point1, *point2):
            if p in sparse_matrix:
                sparse_matrix[p] += 1
            else:
                sparse_matrix[p] = 1
        

print(len([True for v in sparse_matrix.values() if v >= 2]))