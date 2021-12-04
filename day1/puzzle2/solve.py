from itertools import islice

with open('input', 'r') as fh:
    data = fh.readlines()

for i, line in enumerate(data):
    data[i] = int(line)

increased = 0

for i, _ in enumerate(data):
    this_window = sum(data[i:i+3])
    next_window = sum(data[i+1:i+4])
    if next_window > this_window:
        increased += 1

print(increased)
