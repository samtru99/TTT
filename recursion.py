import checker
from checker import Checker

class Recurison:
    def __init__(self):
        self.draws = 0
        self.x_wins = 0
        self.o_wins = 0

    '''
        all_moves_list: list of dictionaries
        level_nums: to know what dictionary to store the move in 
        board: the game to keep track of changes 
    '''

    def total_plays(self):
        print("total draws are ", self.draws)
        print("total x wins are ", self.x_wins)
        print("total y wins are ", self.o_wins)
        print("total plays are ", self.draws + self.x_wins + self.o_wins)
    
    def dummy_function(self, all_moves_list, level_num, board):
        print("all_moves_list is ", all_moves_list)
        
        for i in range(len(board)):
            temp = board
            s = "".join(temp)
            new_moves = list(s)
            new_moves[i] = 'X'
            new_move_recur = "".join(new_moves)
            self.find_moves(all_moves_list,0,new_move_recur)
        
    def find_moves(self,all_moves_list, level, board):
        '''
            Base Cases
            1. Full Board
            2. Winner on X moves
        '''
        winner = Checker()
        if winner.check(board) or winner.tie(board):
            if winner.check(board):
                self.x_wins += 1
            else:
                self.draws += 1
        else:

            '''
                1. Insert the X's new move into the correct dictionary by using 'level'
            '''
            all_moves_list[level]["".join(board)] = []

            '''
                2. Generate all O's next moves
            '''
            O_turn = board
            for i in range(len(board)):
                if board[i] == '_':
                    new_move = list(O_turn)
                    new_move[i] = 'O'
                    new_move_str = "".join(new_move)
                    '''
                        3. Insert the new O move into the 1. list 
                    '''
                    all_moves_list[level]["".join(board)].append([new_move_str])
                    '''
                        4. Check if O won, if not iterativelly call all possible moves
                        recursively
                    '''
                    if winner.check(new_move):
                        self.o_wins += 1
                    else:
                        for new_x in range(len(new_move)):
                            if new_move[new_x] == '_':
                                new_x_recur = list(new_move)
                                new_x_recur[new_x] = 'X'
                                self.find_moves(all_moves_list,level+1,new_x_recur)
