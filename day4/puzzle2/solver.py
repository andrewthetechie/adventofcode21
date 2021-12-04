from typing import List
from copy import deepcopy

bingo_numbers = [63,23,2,65,55,94,38,20,22,39,5,98,9,60,80,45,99,68,12,3,6,34,64,10,70,69,95,96,83,81,32,30,42,73,52,48,92,28,37,35,54,7,50,21,74,36,91,97,13,71,86,53,46,58,76,77,14,88,78,1,33,51,89,26,27,31,82,44,61,62,75,66,11,93,49,43,85,0,87,40,24,29,15,59,16,67,19,72,57,41,8,79,56,4,18,17,84,90,47,25]

with open('input', 'r') as fh:
    data = fh.readlines()

class Board:
    def __init__(self, playboard: List[List[int]]):
        self.playboard = deepcopy(playboard)
        self.positions = self.get_positions(self.playboard)
        self.bingo = {
            "row" : [0,0,0,0,0],
            "col" : [0,0,0,0,0],
            "diagonal" : [0,0]
        }
        self.last_number_found = None

    @staticmethod
    def get_positions(playboard: List[List[int]]):
        positions = dict()
        for x in range(5):
            for y in range(5):
                positions[playboard[x][y]] = (x, y)
        # print(positions)
        return positions

    
    def check_board(self, val: int):
        # print(f"Checking for {val}")
        try:
            x,y = self.positions[str(val)]
            # print("Has value")
            self._update_bingo(x,y)
            self.last_number_found = val
        except KeyError:
            # print("Not found")
            pass

    def _update_bingo(self, x: int, y: int):
        self.bingo["row"][x] += 1
        self.bingo["col"][y] += 1
        if x==y==2:
            self.bingo["diagonal"][0] += 1
            self.bingo["diagonal"][1] += 1
        elif x==y:
            self.bingo["diagonal"][0] += 1
        elif x+y == 4:
            self.bingo["diagonal"][1] += 1
        self.playboard[x][y] = None
    
    def check_bingo(self):
        return 5 in self.bingo["row"] or 5 in self.bingo["col"] or 5 in self.bingo["diagonal"]
    
    @property
    def sum(self):
        if not self.check_bingo():
            return None
        this_sum = 0
        for row in self.playboard:
            for i in row:
                if i is not None:
                    this_sum += int(i)
        return this_sum
    

boards = list()
these_lines = list()
for line in data:
    # print(line)
    if line == "\n":
        boards.append(Board(these_lines))
        these_lines = list()
        continue
    these_lines.append(line.rstrip().split())

print(len(boards))
winning_boards = list()
last_number = None
for number in bingo_numbers:
    if len(boards) == 0:
        break
    for board in boards:
        board.check_board(number)
        if board.sum is not None:
            print("Board won, adding to winners")
            winning_boards.append(board)
            boards.remove(board)
    last_number = number

print(len(winning_boards))
print(last_number)
print(winning_boards[-1].playboard)
print(winning_boards[-1].sum)
print(winning_boards[-1].last_number_found)
print(winning_boards[-1].sum * winning_boards[-1].last_number_found)