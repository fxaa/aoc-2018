file = open('input.txt', 'r')

reactants = list(file.readline().strip())
i, end = 0, len(reactants)

while i+1 < end and i >= 0:
    if reactants[i].upper() == reactants[i+1].upper() and reactants[i] != reactants[i+1]:
        del reactants[i:i+2]
        end -= 2
        i -= 1 if i > 0 else 0
    else:
        i += 1

print(len(reactants))
