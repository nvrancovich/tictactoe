empty_board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

def display_board(board):
    print(board[0],"|",board[1],"|",board[2])
    print(board[3],"|",board[4],"|",board[5])
    print(board[6],"|",board[7],"|",board[8])

def turn(player, board):
    if player == 1:
        marker = "X"
    else:
        marker = "O"
    display_board(board)
    print(f"Es el turno del jugador {player}.")
    position = int(input("Selecciona una pocición del 1 al 9: ")) - 1
    while board[position] != "-":
        position = int(input("Esa posición ya esta ocupada, elegí otra: ")) - 1
    board[position] = marker
    if check_rows(board):
        return 1, board
    elif check_columns(board):
        return 1, board
    elif check_diagonals(board):
        return 1, board
    elif check_tie(board):
        return 2, board
    else:
        return 0, board

def check_rows(board):
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    if row1 or row2 or row3:
        return True

def check_columns(board):
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"
    if col1 or col2 or col3:
        return True

def check_diagonals(board):
    diag1 = board[0] == board[4] == board[8] != "-"
    diag2 = board[2] == board[4] == board[6] != "-"
    if diag1 or diag2:
        return True

def check_tie(board):
    for slot in board:
        if slot == "-":
            return False
    return True

def main(board):
    player = 1
    result = 0
    board = empty_board
    while result == 0:
        result, board= turn(player, board)
        if result == 1:
            print(f"El jugador {player} ganó!")
            break
        elif result == 2:
            print("Hubo un empate!")
            break
        if player == 1:
            player = 2
        else:
            player = 1

main(empty_board)

# Test