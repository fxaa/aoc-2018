freqs = open("input.txt", 'r')
line = freqs.readline()
freq = 0
while line:
    if line[0] == '+':
        freq += int(line[1:].strip())
    else:
        freq -= int(line[1:].strip())
    
    line = freqs.readline()

print(freq)