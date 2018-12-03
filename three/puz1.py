file = open('input.txt', 'r')
line = file.readline().split(' ')

cuts = [[0 for i in range(1000)] for i in range(1000)]

overlaps = 0
while len(line) > 1:
    coords = line[2][:-1].split(',')
    dimensions = line[3].strip().split('x')
    for i in range(int(dimensions[0])):
        for j in range(int(dimensions[1])):
            cuts[i+int(coords[0])][j+int(coords[1])] += 1
            if cuts[i+int(coords[0])][j+int(coords[1])] == 2:
                overlaps += 1

    line = file.readline().split(' ')
    

print(overlaps)