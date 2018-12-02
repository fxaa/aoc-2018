file = open('input.txt', 'r')
line = file.readline()
twos, threes = 0, 0
while line:
    counts = {}
    two, three = False, False
    for letter in line.strip():
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    
    for letter in counts:
        if counts[letter] == 2 and not two:
            twos += 1
            two = True
        if counts[letter] == 3 and not three:
            threes += 1
            three = False
    
    line = file.readline()

print(twos*threes)

