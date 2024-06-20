# get tile coordinates (pos)
# T R B L
# size - string (9x9, 16x16, 16x30)

from locale import atoi


class Explore():
    def __init__(self, size):
        self.size = self.set_size(size)
    
    def set_board(self, board):
        self.board = board # Board object

    def set_size(self, size):
        dimensions = size.split('x')
        return (atoi(dimensions[0]), atoi(dimensions[1])) # (y,x)
    
    # Tile object, the one the user chose
    def bfs(self, tile):
        # tile chosen was a mine
        if tile.value == -1:
            return -1

        tile.set_parent(None)
        frontier = [tile]
        explored = []

        while (len(frontier) > 0):
            curr_tile = frontier.pop(0)
            explored.append(curr_tile)

            if curr_tile.value > 0:
                if curr_tile.parent == None:
                    curr_tile.reveal()
                    break
                if curr_tile.parent.value != 0:
                    continue

            # reveal tile
            curr_tile.reveal() # set hidden = false

            # get tiles surrounding the current tile
            tiles = self.get_tiles(curr_tile)
            for each in tiles:
                if each not in explored:
                    frontier.append(each)

        return explored

    def get_tiles(self, curr_tile):
        MINE = -1
        y = curr_tile.pos[0]
        x = curr_tile.pos[1]
        tiles = []

        # up
        if y - 1 >= 0:
            # left
            if x - 1 >= 0  and self.board.get_tile((y-1,x-1)).value != MINE and self.board.get_tile((y-1,x-1)).hidden:
                self.board.get_tile((y-1,x-1)).set_parent(curr_tile)
                tiles.append(self.board.get_tile((y-1,x-1)))
            
            # directly above
            if self.board.get_tile((y-1,x)).value != MINE and self.board.get_tile((y-1,x)).hidden:
                self.board.get_tile((y-1,x)).set_parent(curr_tile)
                tiles.append(self.board.get_tile((y-1,x)))

            # right
            if x + 1 < self.size[1] and self.board.get_tile((y-1,x+1)).value != MINE and self.board.get_tile((y-1,x+1)).hidden:
                self.board.get_tile((y-1,x+1)).set_parent(curr_tile)
                tiles.append(self.board.get_tile((y-1,x+1)))
        
        # same row
        # left
        if x - 1 >= 0  and self.board.get_tile((y,x-1)).value != MINE and self.board.get_tile((y,x-1)).hidden:
            self.board.get_tile((y,x-1)).set_parent(curr_tile)
            tiles.append(self.board.get_tile((y,x-1)))
        # right
        if x + 1 < self.size[1] and self.board.get_tile((y,x+1)).value != MINE and self.board.get_tile((y,x+1)).hidden:
            self.board.get_tile((y,x+1)).set_parent(curr_tile)
            tiles.append(self.board.get_tile((y,x+1)))

        # bottom
        if y + 1 < self.size[0]:
            # left
            if x - 1 >= 0  and self.board.get_tile((y+1,x-1)).value != MINE and self.board.get_tile((y+1,x-1)).hidden:
                self.board.get_tile((y+1,x-1)).set_parent(curr_tile)
                tiles.append(self.board.get_tile((y+1,x-1)))

            # directly below
            if self.board.get_tile((y+1,x)).value != MINE and self.board.get_tile((y+1,x)).hidden:
                self.board.get_tile((y+1,x)).set_parent(curr_tile)
                tiles.append(self.board.get_tile((y+1,x)))

            # right
            if x + 1 < self.size[1] and self.board.get_tile((y+1,x+1)).value != MINE and self.board.get_tile((y+1,x+1)).hidden:
                self.board.get_tile((y+1,x+1)).set_parent(curr_tile)
                tiles.append(self.board.get_tile((y+1,x+1)))

        return tiles

