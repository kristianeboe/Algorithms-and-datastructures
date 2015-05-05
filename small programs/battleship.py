from random import randint
from sys import stdin

board = []
number_of_ships = int(input("How many ships do you want?(Max 4)"))
different_size = bool(input("Different size on the ships?(True/False)"))
size = 5
ships = []

while len(ships) != number_of_ships:
    x = randint(0, len(board) - 1)
    y = randint(0, len(board[0]) - 1)
    if (x,y) not in ships:
        ships.append((x,y))

ship_row, ship_col = random_row_and_col(board)

if different_size:
    size = round(size*1.5)


for x in range(size):
    board.append(["O"] * size)

def print_board(board):
    for row in board:
        print (" ".join(row))

print ("Let's play Battleship!")
print_board(board)


print (ship_row, ship_col)

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(4):
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col:
        print ("Congratulations! You sunk my battleship!")
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print ("Oops, that's not even in the ocean.")
        elif(board[guess_row][guess_col] == "X"):
            print ("You guessed that one already.")
        else:
            print ("You missed my battleship!")
            board[guess_row][guess_col] = "X"
        if turn == 3:
            print ("Game Over")
            break
        print (turn + 1)
        print_board(board)
