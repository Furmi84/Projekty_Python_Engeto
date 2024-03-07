sequence = [1, 21, 5, 3, 5, 8, 321, 1, 2, 2, 32, 6, 9, 1, 4, 6, 3, 1, 2]
print(sequence)
counts = {}

sequence.sort()
#print(sequence)

for item in sequence:
    print(item)
    if counts.get(item) != None:
        counts[item] = counts.get(item) + 1
        #print(counts.get(item))
    else:
        counts[item] = 1

for key, value in sorted(counts.items()):
    print("key:", key, "value:", value)
