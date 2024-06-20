class Tile():
    def __init__(self, pos, value) -> None:
        self.pos = pos # (y, x)
        self.value = value # X, no. of bombs around it, F
        self.hidden = True

    def reveal(self):
        self.hidden = False
    
    def print_details(self):
        print(f"pos: {self.pos}\nvalue: {self.value}\nhidden: {self.hidden}")

    def set_parent(self, parent):
        self.parent = parent