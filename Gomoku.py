class Game:
    def __init__(self):
    
        self.board = [[0] * 15 for i in range(15)]

        self.turn = 1     
        self.winner = 0  
        self.win_x1 = self.win_y1 = None 
        self.win_x2 = self.win_y2 = None  
    
    dirs = [(1, -1), (1, 0), (1, 1), (0, 1)]

   
    def five_in_a_row(self, x, y, dx, dy):
        def at(x, y):
            return self.board[x][y] if 0 <= x < 15 and 0 <= y < 15 else None
        p = self.board[x][y]
        return (p > 0 and
                at(x - dx, y - dy) != p and
                all([at(x + i * dx, y + i * dy) == p for i in range(5)]) and
                at(x + 5 * dx, y + 5 * dy) != p)

    
    def check_win(self):
        for x in range(15):
            for y in range(15):
                for dx, dy in self.dirs:
                    if self.five_in_a_row(x, y, dx, dy):
                        self.win_x1, self.win_y1 = x,y
                        self.win_x2, self.win_y2 = x + 4 * dx, y + 4 * dy
                        self.winner = self.turn
                        return True
        return False
                                       
                        

  
    def play(self, x, y):
        if self.board[x][y] == 0:
            self.board[x][y] = self.turn
            self.turn = 3 - self.turn
            return True
        return False
            

from tkinter import *
root = Tk()
root.title('Gomoku by Tural')
canvas = Canvas(root, width = 800, height = 800, bg = "cadet blue")
canvas.grid()
for i in range (50,800, 50):
    column = canvas.create_line(i,50,i,750)
for j in range (50,800, 50):
    lines = canvas.create_line(50,j,750,j)
game = Game()

stones = []
finished = False


def on_click(event):
    global finished, game
    if finished:
        for i in stones:
            canvas.delete(i)
        finished = False
        game = Game()
    else:
        
        a = round((event.x - 50) / 50)
        b = round((event.y - 50) / 50)
        if a < 0:
            a = 0
        if a > 14:
            a = 14
        if b < 0:
            b = 0
        if b > 14:
            b = 14
        if game.play(a, b):
        
            color = 'lavender' if game.turn == 1 else 'red4'
            stone = canvas.create_oval(a*50+30, b*50+30,a*50+70, b*50+70, fill = color)
            stones.append(stone)
        
            if game.check_win():
                stones.append(canvas.create_line(game.win_x1*50+50, game.win_y1*50+50, game.win_x2*50+50, game.win_y2*50+50, width=5,fill='light slate gray'))
                finished = True
    

canvas.bind("<Button>", on_click)

    
root.mainloop()