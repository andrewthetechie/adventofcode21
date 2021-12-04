from itertools import islice

with open('input', 'r') as fh:
    data = fh.readlines()

print(sum(n1 < n2 for n1, n2 in zip(data, islice(data, 1, None))))