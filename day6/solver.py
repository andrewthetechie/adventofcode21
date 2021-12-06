from collections import defaultdict

with open('input', 'r') as fh:
    data = fh.readlines()


fish_ages = list(map(int, data[0].strip().split(",")))
# get a dict that is a count of all of our current fish agets
fish = [fish_ages.count(i) for i in range(9)]
for i in range(256):
    # grab off our fishes that are at 0 age 
    num = fish.pop(0)
    # Add those fish back in in the 6 day spot
    fish[6] += num
    # Add the new fish to the end of the list
    fish.append(num)
    # problem 1 solution
    if i==80:
        print(f"Fish at 80 days: {sum(fish)}")
# problem 2 solution
print(f"Fish at 256 days {sum(fish)}")

