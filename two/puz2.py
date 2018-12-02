scores  = {}
letters = "abcdefghijklmnopqrstuvwxyz"

for i in range(len(letters)):
    scores[letters[i]] = i+1

totals  = []
lines   = []
file    = open('input.txt', 'r')
line    = file.readline()

#returns whether a and b differ by one character (location sensitive)
def one_char_diff(a, b):
    if len(a) != len(b):
        return False

    else:
        idx = 0
        diff_found = False
        for i in range(len(a)):
            if a[i] != b[i]:
                if not diff_found:
                    diff_found, idx = True, i
                else: 
                    return (False, 0)
    
    #return whether exactly 1 difference was found and where that difference is
    #if no diff was found just return 0 as the index
    return (diff_found, idx)


#setting up positional scores
while line:
    totals.append(0)
    lines.append(line.strip())
    line = file.readline()

for i in range(len(lines)):
    for letter in lines[i]:
        totals[i] += scores[letter]

for i in range(len(lines)):
    for j in range(len(lines)):
        #don't even consider the pair if the score difference is too big to be crossed by one character
        if abs(totals[i] - totals[j]) < 26:
            diff = one_char_diff(lines[i], lines[j])
            if diff[0]:
                print(lines[i][0:diff[1]] + lines[i][diff[1]+1:])
                quit()
