from tkinter import *
from tkinter import messagebox as mb
import random


def win(player):
    """ Function display WIN message window, clean graphical view and gaming board, and make random first move"""
    global board

    if player == 1:
        msg = "I win!"
    elif player == 2:
        msg = "You win!"
    elif player == 0:
        msg = "Nobody win!"

    mb.showinfo("info", msg)
    canv.delete(ALL)
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    draw_field()
    first_move()


def win_check(player):
    """ Function check field for win situation and return 1 if this situation appeared"""
    global board

    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        win(player)
        return 1
    elif board[1][0] == player and board[1][1] == player and board[1][2] == player:
        win(player)
        return 1
    elif board[2][0] == player and board[2][1] == player and board[2][2] == player:
        win(player)
        return 1
    elif board[0][0] == player and board[1][0] == player and board[2][0] == player:
        win(player)
        return 1
    elif board[0][1] == player and board[1][1] == player and board[2][1] == player:
        win(player)
        return 1
    elif board[0][2] == player and board[1][2] == player and board[2][2] == player:
        win(player)
        return 1
    elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
        win(player)
        return 1
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        win(player)
        return 1
    elif len([i for i in (board[0] + board[1] + board[2]) if i == 0]) == 0:
        win(0)
        return 1
    else:
        return 0

def draw_zero(x, y):
    """Draw zero function"""
    global canv
    global window_height, window_width, height_indent

    width_size = window_width / 3
    height_size = window_height / 3
    canv.create_oval(y * width_size, x * height_size + height_indent, y * width_size + width_size,
                     x * height_size + height_size + height_indent)
    return win_check(1)


def draw_cross(x, y):
    """Draw cross function"""
    global canv
    global window_height, window_width, height_indent

    width_size = window_width / 3
    height_size = window_height / 3
    canv.create_line(y * width_size, x * height_size + height_indent, y * width_size + width_size,
                     x * height_size + height_size + height_indent)
    canv.create_line(y * width_size + width_size, x * height_size + height_indent, y * width_size,
                     x * height_size + height_size + height_indent)
    return win_check(2)


def b1(event):
    """On left mouse click on gaming window"""
    global window_height, window_width, height_indent, board

    width_size = window_width / 3
    height_size = window_height / 3

    #Get mouse position on game window
    graph_x = event.x
    graph_y = event.y - height_indent
    #Calculate mouse pointer to board position
    y = int(graph_x / width_size)
    x = int(graph_y / height_size)
    #Check move for empty field
    if board[x][y] == 0:
        board[x][y] = 2
        if not draw_cross(x, y): #if game not in win situation - take move
            get_move()


def get_move():
    """Make computer move"""
    global board

    while True:
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        # Check move for empty field
        if board[x][y] == 0:
            board[x][y] = 1
            draw_zero(x, y)
            break


def draw_field():
    """Function draw gaming field"""
    # Draw vertical lines
    canv.create_line(window_width / 3, height_indent, window_width / 3, window_height + height_indent)
    canv.create_line(window_width / 3 * 2, + height_indent, window_width / 3 * 2, window_height + height_indent)

    # Draw header underline
    canv.create_line(0, height_indent, window_width, height_indent)

    # Draw horizontal lines
    canv.create_line(0, window_height / 3 + height_indent, window_width, window_height / 3 + height_indent)
    canv.create_line(0, window_height / 3 * 2 + height_indent, window_width, window_height / 3 * 2 + height_indent)


def first_move():
    """Function make who start game, and if Comp - make move"""
    who_start = random.randint(0, 1)
    if who_start:
        get_move()


#Game windows parameters
window_width = 600
window_height = 600
window_xpos = 100
window_ypos = 100
height_indent = 30
#init gaming voard
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

#Make GUI
root = Tk()
root.title("Tic tac toe")
win_geo = str(window_width) + "x" + str(window_height + height_indent) + "+" + str(window_xpos) + "+" + str(window_ypos)
root.geometry(win_geo)
root.resizable(width=False, height=False)
canv = Canvas(bg="white", width=1000, height=1000)
canv.grid()

draw_field()
first_move()

root.bind('<Button-1>', b1)

root.mainloop()
