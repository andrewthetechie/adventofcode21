from collections import defaultdict

with open('input', 'r') as fh:
    data = fh.readlines()

intersections = defaultdict(int)
diagonals = defaultdict(int)
for line in data:
    start, stop = line.rstrip().replace(" ", "").split('->')
    x1, y1 = map(int, start.split(','))
    x2, y2 = map(int, stop.split(','))
    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2) + 1):
            intersections[x1, i] += 1
            diagonals[x1, i] += 1
    elif y1 == y2:
        for i in range(min(x1, x2), max(x1, x2) + 1):
            intersections[i, y1] += 1
            diagonals[i, y1] += 1
    else:
        start = range(x1, x2 + 1) if x1 < x2 else range(x1, x2 - 1, -1)
        stop = range(y1, y2 + 1) if y1 < y2 else range(y1, y2 - 1, -1)
        for x, y in zip(start, stop):
            diagonals[x, y] += 1

print(f"Intersections: {sum(x > 1 for x in intersections.values())}")
print(f"Intersections with diagonals: {sum(x > 1 for x in diagonals.values())}")