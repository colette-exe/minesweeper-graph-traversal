from locale import atoi
from tile import Tile
import random

class Board():
    def __init__(self, size):
        self.size = self.set_size(size)
        self.no_of_mines = self.get_no_of_mines()
        self.board_list = self.init_board()

    def init_board(self):
        b = []
        mines = self.generate_mines()
        for y in range(0,self.size[0]):
            temp = []
            for x in range(0,self.size[1]):
                if (y,x) in mines: 
                    temp.append(Tile((y,x),-1))
                else: temp.append(Tile((y,x),0))
            b.append(temp)

        # count mines
        for y in range(0,self.size[0]):
            for x in range(0,self.size[1]):
                if b[y][x].value == -1: continue # ignore mines

                count = 0
                # up
                if y - 1 >= 0:
                    # left
                    if x - 1 >= 0 and b[y-1][x-1].value == -1:
                        count += 1

                    # directly above
                    if b[y-1][x].value == -1:
                        count+=1

                    # right
                    if x + 1 < self.size[1] and b[y-1][x+1].value == -1:
                        count += 1
                
                # same row
                # left
                if x - 1 >= 0 and b[y][x-1].value == -1:
                    count += 1

                # right
                if x + 1 < self.size[1] and b[y][x+1].value == -1:
                    count += 1

                # below
                if y + 1 < self.size[0]:
                    # left
                    if x - 1 >= 0 and b[y+1][x-1].value == -1:
                        count += 1

                    # directly above
                    if b[y+1][x].value == -1:
                        count+=1

                    # right
                    if x + 1 < self.size[1] and b[y+1][x+1].value == -1:
                        count += 1

                b[y][x].value = count
        return b

    def get_no_of_mines(self):
        mines = 60
        if self.size[0] == 9:
            mines = 10
        if self.size[0] == 16 and self.size[1] == 16:
            mines = 32

        return mines

    def generate_mines(self):
        mines = []
        for _ in range(0,self.no_of_mines):
            y = random.randint(0,self.size[0]-1) # y
            x = random.randint(0,self.size[1]-1) # x
            mines.append((y,x))

        return mines

    def set_size(self, size):
        dimensions = size.split('x')
        return (atoi(dimensions[0]), atoi(dimensions[1])) # (y,x)

    def update_board(self, new_state):
        self.board_list = new_state

    def get_tile(self, pos):
        tile = self.board_list[pos[0]][pos[1]]
        return tile