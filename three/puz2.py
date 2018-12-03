file = open('input.txt', 'r')
line = file.readline().split(' ')

#we store a set of cloth IDs for each coordinate visited in "cuts"
cuts = {}
#we store a boolean value for each cloth ID that says whether it's been overlapped or not
overlapped = {}

while len(line) > 1:
    overlapped[line[0]] = False
    coords = tuple([int(i) for i in line[2][:-1].split(',')])
    dimensions = tuple([int(i) for i in line[3].strip().split('x')])

    for i in range(dimensions[0]):
        for j in range(dimensions[1]):
            if (coords[0]+i, coords[1]+j) not in cuts:
                #this cloth is the first to visit this coordinate
                cuts[(coords[0]+i, coords[1]+j)] = [line[0]]
            else:
                #if we're here we know our current cloth is overlapping
                #we need to keep track of where it's been so it can overlap future cloths
                cuts[(coords[0]+i, coords[1]+j)].append(line[0])
                overlapped[line[0]] = True
                #we only care if a cloth has been overlapped at all, not how much it's been overlapped
                #therefore we only need to update the previous cloth ID that's been here
                #every cloth before the one at cuts[...][-2] has already been updated before
                overlapped[cuts[(coords[0]+i, coords[1]+j)][-2]] = True

    line = file.readline().split(' ')
    
for each in overlapped:
    if not overlapped[each]:
        #there should only be one cloth in the list that hasn't ever been overlapped
        print(each)