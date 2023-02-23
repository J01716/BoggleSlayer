
#fills a given 4x4 board with user inputs for each cell of the board
def fill_board(board):
    for j in range(4):
        for i in range(4):
            board[i][j] = input("Please enter " + get_ordinal_word(i) + " column and " + get_ordinal_word(j) + " row letter:  ")
    return board

#returns the ordinal number string matching the number received as parameter.
# If no cardinal number is assigned to the number send as param, the function
# will return "forty second" since it's the answer to everything
def get_ordinal_word(order):
    if order == 0:
        return "first"
    elif order == 1:
        return "second"
    elif order == 2:
        return "third"
    elif order == 3:
        return "fourth"
    else:
        return "forty second"

#prints a board for testing and verification purposes
def print_board(board):
    for j in range(len(board)):
        if board[0]:
            line = ""
            for i in range(len(board[0])):
                line += board[i][j] + " "
            print(line)

            