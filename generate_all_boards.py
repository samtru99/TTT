'''
    by Samuel Trujillo - 9/29
'''
import copy

def winner(board, player):
    #Won across
    if board[0] == board[1] == board[2] == player:
        return True
    if board[3] == board[4] == board[5] == player:
        return True
    if board[6] == board[7] == board[8] == player:
        return True

    #won columnly 
    if board[0] == board[3] == board[6] == player:
        return True
    if board[1] == board[4] == board[7] == player:
        return True
    if board[2] == board[5] == board[8] == player:
        return True
    
    #won diagonaly
    if board[0] == board[4] == board[8] == player:
        return True
    if board[6] == board[4] == board[2] == player:
        return True
    
    return False

x = 0
c = 0 
o = 0
def main():
    
    '''
        innner function for easy debugging
    '''
   
    def dfs(game, turn):
        #check if X won 
        if winner(game,'X'):
            global x
            x += 1
            return
        #check if cat scratch
        if turn == 9 and game.count("_") == 0:
            global c
            c += 1
            return
        for i in range(9):
            #O's turn to go 
            if game[i] == '_':
                temp = copy.deepcopy(game)
                temp[i] = 'O'
                #if O won
                if winner(temp, 'O'):
                    global o
                    o += 1
                else:
                    '''
                        This two step process makes it easier on dealing with recurison
                    '''
                    for j in range(9):
                        if temp[j] == '_':
                            temp_x_moves = copy.deepcopy(temp)
                            temp_x_moves[j] = 'X'
                            dfs(temp_x_moves,turn + 2)
    

    board = ['_','_','_','_','_','_','_','_','_']
    for i in range(9):
        temp = copy.deepcopy(board)
        temp[i] = 'X'
        dfs(temp, 1)
    
    print("RESULTS ARE ")
    print("x = ", x)
    print("o = ", o)
    print("c = ", c)
    print("total = ", x + c + o)

if __name__ == "__main__":
    main()