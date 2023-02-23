from board_util import *






def check_for_two_letter_words(board):
    for j in range(len(board)):
        if board[0]:
            for i in range(len(board[0])):
                if board[i-1] and board[j-1]:
                    #check
                    print("test1of8")
                if board[i] and board[j-1]:
                    #check
                    print("test2of8")
                if board[i+1] and board[j-1]:
                    #check
                    print("test3of8")
                if board[i-1] and board[j]:
                    #check
                    print("test4of8")
                if board[i+1] and board[j]:
                    #check
                    print("test5of8")
                if board[i-1] and board[j+1]:
                    #check
                    print("test6of8")
                if board[i] and board[j+1]:
                    #check
                    print("test7of8")
                if board[i+1] and board[j+1]:
                    #check
                    print("test8of8")


                




def main():
    board = [["","","",""],["","","",""],["","","",""],["","","",""]]

    board = fill_board(board)
    
    print_board(board)









main()