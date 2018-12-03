file = open('input.txt', 'r')
line = file.readline().split(' ')

cuts = {}
overlapped = {}

while len(line) > 1:
    overlapped[line[0]] = False
    coords = tuple([int(i) for i in line[2][:-1].split(',')])
    dimensions = tuple([int(i) for i in line[3].strip().split('x')])

    for i in range(dimensions[0]):
        for j in range(dimensions[1]):
            if (coords[0]+i, coords[1]+j) not in cuts:
                cuts[(coords[0]+i, coords[1]+j)] = [line[0]]
            else:
                cuts[(coords[0]+i, coords[1]+j)].append(line[0])
                overlapped[line[0]] = True
                for each in cuts[(coords[0]+i, coords[1]+j)]:
                    overlapped[each] = True

    line = file.readline().split(' ')
    
for each in overlapped:
    if not overlapped[each]:
        print(each)