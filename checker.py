class Checker:
    def check(self,list):
        row_win = self.rows(list)
        col_win = self.cols(list)
        diagonals_win = self.digonals(list)
        #print(f"{row_win} or {col_win} or {diagonals_win}")
        if row_win == True or col_win == True or diagonals_win == True:
            return True
        else:
            return False 
    def rows(self, board):
        wins = False
        if board[0] == board[1] == board[2] != '_':
            wins = True
        if board[3] == board[4] == board[5] != '_':
            wins = True
        if board[6] == board[7] == board[8] != '_':
            wins = True
        return wins
    
    def cols(self,board):
        wins = False
        if board[0] == board[3] == board[6] != '_':
            wins =  True
        if board[1] == board[4] == board[7] != '_':
            wins =  True
        if board[2] == board[5] == board[8] != '_':
            wins =  True
        
        return wins
    
    def digonals(self,board):
        wins = False
        if board[0] == board[4] == board[8] != '_':
            wins =  True
        if board[6] == board[4] == board[2] != '_':
            wins =  True
        return wins

    def tie(self, board):
        game_over = True
        for i in range(len(board)):
            if board[i] == '_':
                game_over = False
        return game_over