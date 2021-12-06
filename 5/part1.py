import fileinput


sparse_matrix = dict()

for line in fileinput.input():
    print(line)
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
        

print(len([True for v in sparse_matrix.values() if v >= 2]))