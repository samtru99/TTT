


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
o = 0
c = 0
def main():
    print("hello world")
    board = ['_','_','_','_','_','_','_','_','_']
    
    '''
        innner function for easy debugging
    '''
    def dfs(board, turn,x,c,o):
        #check if X won 
        if winner(board,'X'):
            x += 1
        #check if cat scratch
        if turn == 9 and board.count("_") == 0:
            #print("cat scratch")
            c += 1
            return
        for i in range(9):
            if board[i] == '_':
                temp = board.copy()
                temp[i] = 'O'
                if winner(temp, 'O'):
                    #print("o won")
                    o += 1
                else:
                    for j in range(9):
                        if board[j] == '_':
                            temp_x_moves = temp.copy()
                            temp_x_moves[j] = 'X'
                            x_p, o_p, c_p = x, c, o
                            x,c,o = dfs(temp_x_moves,turn + 2, x_p, o_p,c_p)
        return x, c, o
    for i in range(9):
        print(f"i is {i}")
        temp = board.copy()
        temp[i] = 'X'
        x,c,o = dfs(temp, 1,0,0,0)
        print("done with {i}")
    
    print("RESULTS ARE ")
    print("x = ", x)
    print("o = ", o)
    print("c = ", c)
    print("total = ", x + o + c)

if __name__ == "__main__":
    main()