from tkinter import *
from tkinter import messagebox as mb
import random


def win(player):
    global board

    if player == 1:
        msg = "I win!"
    elif player == 2:
        msg = "You win!"
    elif player == 0:
        msg = "Nobody win!"
    print(msg)
    mb.showinfo("info", msg)
    canv.delete(ALL)
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    draw_field()
    first_move()


def win_check(player):
    global board

    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        win(player)
    elif board[1][0] == player and board[1][1] == player and board[1][2] == player:
        win(player)
    elif board[2][0] == player and board[2][1] == player and board[2][2] == player:
        win(player)
    elif board[0][0] == player and board[1][0] == player and board[2][0] == player:
        win(player)
    elif board[0][1] == player and board[1][1] == player and board[2][1] == player:
        win(player)
    elif board[0][2] == player and board[1][2] == player and board[2][2] == player:
        win(player)
    elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
        win(player)
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        win(player)
    elif len([i for i in (board[0] + board[1] + board[2]) if i == 0]) == 0:
        win(0)


def draw_zero(x, y):
    global canv
    global window_height, window_width, height_indent

    width_size = window_width / 3
    height_size = window_height / 3
    print("zero", x, y)
    canv.create_oval(y * width_size, x * height_size + height_indent, y * width_size + width_size,
                     x * height_size + height_size + height_indent)
    win_check(1)


def draw_cross(x, y):
    global canv
    global window_height, window_width, height_indent

    width_size = window_width / 3
    height_size = window_height / 3
    print("cross", x, y)
    canv.create_line(y * width_size, x * height_size + height_indent, y * width_size + width_size,
                     x * height_size + height_size + height_indent)
    canv.create_line(y * width_size + width_size, x * height_size + height_indent, y * width_size,
                     x * height_size + height_size + height_indent)
    win_check(2)


def b1(event):
    global window_height, window_width, height_indent, board

    width_size = window_width / 3
    height_size = window_height / 3

    graph_x = event.x
    graph_y = event.y - height_indent
    y = int(graph_x / width_size)
    x = int(graph_y / height_size)

    print("Press", x, y)

    if board[x][y] == 0:
        board[x][y] = 2
        draw_cross(x, y)
        get_move()


def get_move():
    global board

    while True:
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        if board[x][y] == 0:
            board[x][y] = 1
            draw_zero(x, y)
            break


def draw_field():
    # Draw vertical lines
    canv.create_line(window_width / 3, height_indent, window_width / 3, window_height + height_indent)
    canv.create_line(window_width / 3 * 2, + height_indent, window_width / 3 * 2, window_height + height_indent)

    # Draw header underline
    canv.create_line(0, height_indent, window_width, height_indent)

    # Draw horizontal lines
    canv.create_line(0, window_height / 3 + height_indent, window_width, window_height / 3 + height_indent)
    canv.create_line(0, window_height / 3 * 2 + height_indent, window_width, window_height / 3 * 2 + height_indent)


def first_move():
    who_start = random.randint(0, 1)
    if who_start:
        get_move()


window_width = 600
window_height = 600
window_xpos = 100
window_ypos = 100
height_indent = 30
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

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
