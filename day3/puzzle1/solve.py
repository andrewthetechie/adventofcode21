with open('input', 'r') as fh:
    data = fh.readlines()

for i, line in enumerate(data):
    data[i] = list(line.rstrip())

bits = list(zip(*data))

gamma_bits = list()
eps_bits = list()

for bit in bits:
    if bit.count('1') > bit.count('0'):
        gamma_bits.append('1')
        eps_bits.append('0')
    else:
        gamma_bits.append('0')
        eps_bits.append('1')

gamma_str = ("".join(gamma_bits))
eps_str = ("".join(eps_bits))

print(f"Gamma: {gamma_str}")
print(f"Epsilon: {eps_str}")
print(f"Power usage: {int(gamma_str, 2) * int(eps_str, 2)}" )