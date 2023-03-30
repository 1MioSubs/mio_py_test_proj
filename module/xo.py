import random

# создаем пустую игровую доску
board = [" " for i in range(9)]

# выводим игровую доску
def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

# проверяем, есть ли победитель
def winner(board):
    # варианты победы
    winning_options = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6))

    # проходим по вариантам победы
    for i in winning_options:
        if board[i[0]] == board[i[1]] == board[i[2]] != " ":
            winner = board[i[0]]
            return winner

    # проверяем, заполнена ли доска
    if " " not in board:
        return "Ничья"

    # если никто не победил и есть пустые клетки, игра продолжается
    return None

# проверяем, является ли ход допустимым
def is_valid(move):
    if move >= 0 and move <= 8 and board[move] == " ":
        return True
    else:
        return False

# делаем ход компьютера
def computer_move():
    # проверяем, есть ли выигрышные комбинации
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if winner(board) == "O":
                print("Компьютер выиграл!")
                print_board()
                return
            else:
                board[i] = " "

    # проверяем, есть ли выигрышные комбинации для игрока
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            if winner(board) == "X":
                board[i] = "O"
                print_board()
                return
            else:
                board[i] = " "

    # если нет выигрышных комбинаций, делаем случайный ход
    while True:
        move = random.randint(0, 8)
        if board[move] == " ":
            board[move] = "O"
            print_board()
            break

# делаем ход игрока
def player_move():
    valid = False
    while not valid:
        move = int(input("Введите число от 0 до 8: "))
        if is_valid(move):
            board[move] = "X"
            valid = True
        else:
            print("Недопустимый ход. Попробуйте еще раз.")
    print_board()

# игра
def game():
    print_board()
    while not winner(board):
        player_move()
        computer_move()
    else:
        if winner(board) == "X":
            print("Вы выиграли!")
        elif winner(board) == "O":
            print("Компьютер выиграл!")
        elif winner(board) == "Ничья":
            print("Ничья!")

game()