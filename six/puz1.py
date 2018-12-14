file = open('input.txt', 'r')

line = file.readline().strip()
coords = []
while line:
    coords.append(tuple([int(i) for i in line.split(', ')]))
    line = file.readline().strip()

i_sort = sorted(coords, key=lambda x: x[0])
j_sort = sorted(coords, key=lambda x: x[1])

i_range = (i_sort[0][0], i_sort[-1][0])
j_range = (j_sort[0][1], j_sort[-1][1])

