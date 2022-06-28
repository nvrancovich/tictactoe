from anyio import BusyResourceError


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
        return True, board
    elif check_columns(board):
        return True, board
    elif check_diagonals(board):
        return True, board
    else:
        return False, board

def check_rows(board):
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    if row1 or row2 or row3:
        return True

def check_columns(board):
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[3] == board[8] != "-"
    if col1 or col2 or col3:
        return True

def check_diagonals(board):
    diag1 = board[0] == board[4] == board[8] != "-"
    diag2 = board[2] == board[4] == board[6] != "-"
    if diag1 or diag2:
        return True

def main(board):
    player = 1
    winner = False
    board = empty_board
    while not winner:
        winner, board= turn(player, board)
        if winner:
            break
        if player == 1:
            player = 2
        else:
            player = 1
    print(f"El jugador {player} ganó!")

main(empty_board)