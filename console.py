import random


def win(player):
    global board

    if player == 1:
        msg = "I win!"
    elif player == 2:
        msg = "You win!"
    elif player == 0:
        msg = "Nobody win!"
    draw_board()
    print(msg)
    exit()


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


def player_move():
    global board

    while True:
        while True:
            x = input("Enter line A-C")
            if x == "A" or x == "B" or x == "C":
                x = ord(x) - ord("A")
                break
            else:
                print("Wrong enter, try again")

        while True:
            y = input("Enter row 1-3")
            if y == "1" or y == "2" or y == "3":
                y = int(y) - 1
                break
            else:
                print("Wrong enter, try again")

        if board[x][y] == 0:
            board[x][y] = 2
            break
        else:
            print("Field not empty, try again")


def get_move():
    global board

    while True:
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        if board[x][y] == 0:
            board[x][y] = 1
            break


def draw_board():
    print("  1 2 3")
    print(" -------")
    for c, line in enumerate(board):
        p_line = chr(ord("A") + c) + "|" + "|".join(map(str, line)) + "|"
        p_line = p_line.replace("0", " ")
        p_line = p_line.replace("1", "O")
        p_line = p_line.replace("2", "X")
        print(p_line)
        print(" -------")


def first_move():
    who_start = random.randint(0, 1)
    if who_start:
        get_move()


game = 1
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

print("Tic tac toe")
first_move()
while game:
    draw_board()
    player_move()
    win_check(2)
    get_move()
    win_check(1)
