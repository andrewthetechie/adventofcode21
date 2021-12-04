from typing import List

with open('input', 'r') as fh:
    data = fh.readlines()

split_data = list()
for i, line in enumerate(data):
     split_data.append(list(line.rstrip()))

def get_count_col_bits(list_of_bytes: List[str]):
    """Get the count of 1 and 0 bits in each column of a list of bytes"""
    bits = list(zip(*list_of_bytes))
    return_data = dict()
    for i, bit in enumerate(bits):
        return_data[i] = dict()
        for cnt_bit in ['1', '0']:
            return_data[i][cnt_bit] = bit.count(cnt_bit)
    return return_data

col = 0
valid_bytes = split_data
while len(valid_bytes) > 1:
    counts = get_count_col_bits(valid_bytes)
    if int(counts[col]['0']) > int(counts[col]['1']):
        # more zeroes, keep zeroes
         valid_bytes = [bit for bit in valid_bytes if bit[col] == '0']
    else:
        # more ones or equal, keep ones
        valid_bytes = [bit for bit in valid_bytes if bit[col] == '1']
    col += 1

o2_generator = "".join(valid_bytes.pop())

col = 0
valid_bytes = split_data
while len(valid_bytes) > 1:
    counts = get_count_col_bits(valid_bytes)
    result = int(counts[col]['1']) - int(counts[col]['0'])
    # more 1s or equal
    if result >= 0:
        valid_bytes = [bit for bit in valid_bytes if bit[col] == '0']
    else:
        valid_bytes = [bit for bit in valid_bytes if bit[col] == '1']
    col += 1

co2_scrub = "".join(valid_bytes.pop())

print(f"O2: {o2_generator} -- {int(o2_generator, 2)}")
print(f"CO2: {co2_scrub} -- {int(co2_scrub, 2)}")
print(f"Life Support: {int(o2_generator, 2) * int(co2_scrub, 2)}")
