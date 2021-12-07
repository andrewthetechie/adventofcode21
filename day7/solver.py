with open('input', 'r') as file:
    raw_data = file.read()

data = list(map(int, raw_data.split(',')))



fuel_used = float('inf')
for i in range(max(data)):
    fuel_used = min(fuel_used, sum(abs(x-i) for x in data))

print(f'Part 1 fuel: {fuel_used}') 


def fuel_cost(x):
    return (x*(x+1))//2

fuel_used = float('inf')
for i in range(max(data)):
    fuel_used = min(fuel_used, sum(fuel_cost(abs(x-i)) for x in data))


print(f'Part 2 fuel: {fuel_used}') 