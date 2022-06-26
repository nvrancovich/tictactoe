board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

def display_board():
    print(board[0],"|",board[1],"|",board[2])
    print(board[3],"|",board[4],"|",board[5])
    print(board[6],"|",board[7],"|",board[8])

def turn(player):
    if player == 1:
        marker = "X"
    else:
        marker = "O"
    position = int(input("Selecciona una pocición del 1 al 9: ")) - 1
    while board[position] != "-":
        position = int(input("Esa posición ya esta ocupada, elegí otra: ")) - 1
    board[position] = marker
    return board

def main():
    display_board()
    turn(1)
    display_board()
    turn(1)
    display_board()

main()