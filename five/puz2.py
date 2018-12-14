file = open('input.txt', 'r')

reactants = list(file.readline().strip())
polymers = []
for letter in "abcdefghijklmnopqrstuvwxyz":
    react_copy = reactants.copy()

    i, end = 0, len(react_copy)

    while i+1 < end:
        if react_copy[i].upper() == letter.upper():
            del react_copy[i]
            end -= 1
            i -= 1 if i > 0 else 0
        elif react_copy[i].upper() == react_copy[i+1].upper() and react_copy[i] != react_copy[i+1]:
            del react_copy[i:i+2]
            end -= 2
            i -= 1 if i > 0 else 0
        else:
            i += 1

    polymers.append(end)

print(min(polymers))