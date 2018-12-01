lines = open("input.txt", 'r')
line = lines.readline()
freqs = {}
freq = 0
found = False
while line:
    if line[0] == '+':
        freq += int(line[1:].strip())
    else:
        freq -= int(line[1:].strip())
    
    if freq in freqs:
        print(freq)
        break
    else:
        print(freq)
        freqs[freq] = 1
    
    line = lines.readline()
    if not line:
        lines.seek(0)
        line = lines.readline()
