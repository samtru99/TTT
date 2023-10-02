class Checker:
    def check(self,list):
        row_win = self.rows(list)
        col_win = self.cols(list)
        diagonals_win = self.digonals(list)

    def rows(self, board):
        wins = False
        if board[0] == board[1] == board[2] != '-':
            wins = True
        if board[3] == board[4] == board[5] != '-':
            wins = True
        if board[6] == board[7] == board[8] != '-':
            wins = True
        return wins
    
    def cols(self,board):
        wins = False
        if board[0] == board[3] == board[6] != '-':
            wins =  True
        if board[1] == board[4] == board[7] != '-':
            wins =  True
        if board[2] == board[5] == board[8] != '-':
            wins =  True
        
        return wins
    
    def tie(self, board):
        game_over = True
        for i in range(len(board)):
            if board[i] == '_':
                game_over = False
        return game_over