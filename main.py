from tkinter import *
from tkinter import messagebox as msg_box
from board import Board
from explore import Explore

# explored: E
# free: O
# mine: X
# flagged: F

# fonts
font1 = ('Poppins-Regular', 15)
font2 = ('Poppins-Regular', 20)
font3 = ('Poppins-SemiBold', 20)
font4 = ('Poppins-ExtraBold', 30)

class App():
    def __init__(self, root):
        # gui
        # self.board_list -> Board object
        self.root = root
        self.widgets()

    def widgets(self):
        self.bg = Frame(self.root, background='#292a30',width=self.root.winfo_screenwidth(),height=self.root.winfo_screenheight())
        self.bg.pack()
        self.label = Label(self.bg, text='CHOOSE A LEVEL', fg='#dfdfe0', bg='#292a30', font=font4).place(x=270,y=100)

        # buttons for levels
        self.buttons = Frame(self.bg, background='#292a30',width=self.root.winfo_screenwidth(),height=self.root.winfo_screenheight())
        self.buttons.place(x=0, y=200)
        self.btn_easy = Button(self.buttons, command=lambda:self.start_game(10), text='EASY', width=10, font=font3, height=2, bg='#ffffff', border=1,borderwidth=1).place(x=300,y=0)
        self.btn_medium = Button(self.buttons, command=lambda:self.start_game(32), text='MEDIUM', font=font3, width=10, height=2, bg='#ffffff', border=1, borderwidth=1).place(x=300,y=100)
        self.btn_hard = Button(self.buttons, command=lambda:self.start_game(60), text='HARD', font=font3, width=10, height=2, bg='#ffffff', border=1, borderwidth=1).place(x=300,y=200)

    def start_game(self, no_of_mines):
        size = '9x9'
        self.scale = 1
        if no_of_mines == 32: 
            size = '16x16'
            self.scale = 0.75
        if no_of_mines == 60: 
            size = '16x30'
            self.scale = 0.5
        self.board_list = Board(size)
        self.explore = Explore(size)
        self.remove_widgets(self.buttons)
        self.display_board()

    def display_board(self):
        self.grid = Frame(self.bg, background='#292a30', width=self.bg.winfo_screenwidth(), height=self.bg.winfo_screenheight())
        self.grid.pack()
        self.tiles = [[0 for _ in range(0,self.board_list.size[1])] for _ in range(0,self.board_list.size[0])]
        for y in range(0, self.board_list.size[0]):
            for x in range(0,self.board_list.size[1]):
                pos_x = (x*40) + self.board_list.size[0]
                pos_y = (y*35) + self.board_list.size[0]
                self.tiles[y][x] = Button(self.grid, font=font3, bg='#ffffff', command=lambda y=y, x=x:self.click_tile((y,x)), width=1, height=1, padx=0, pady=0)
                self.tiles[y][x].place(x=pos_x,y=pos_y)

    def update_board(self, explored):
        for tile in explored:
            if tile.hidden == False:
                self.tiles[tile.pos[0]][tile.pos[1]]['state'] = DISABLED
                self.tiles[tile.pos[0]][tile.pos[1]].config(text=tile.value)
                self.tiles[tile.pos[0]][tile.pos[1]].config(disabledforeground='#292a2f')

    def click_tile(self,pos):
        print('tile clicked')
        y = pos[0]
        x = pos[1]
        self.explore.set_board(self.board_list)
        result = self.explore.bfs(self.board_list.get_tile((y,x)))
        if (result == -1): self.game_over()
        else:
            # result is all the explored tiles
            self.update_board(result)

    def remove_widgets(self, widget):
        for each in widget.winfo_children():
            each.destroy()

    def game_over(self):
        msg_box.showerror(message="GAME OVER!")
        self.try_again()

    def try_again(self):
        self.remove_widgets(self.grid)
        self.remove_widgets(self.bg)
        self.remove_widgets(self.root)
        self.widgets()

def main():
    root = Tk()
    root.title("MINESWEEPER")
    root.resizable(False,False)
    x = root.winfo_screenwidth()
    y = root.winfo_screenheight()
    width = 1250
    height = 600
    center_x = (x//2)-(width//2)
    center_y = (y//2)-(height//2)
    root.geometry(f'{width}x{height}+{center_x}+{center_y}')
    App(root)
    root.mainloop()

if __name__ == "__main__":
    main()