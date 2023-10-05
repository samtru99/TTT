import checker
from checker import Checker

import pprint
import data_transfer_files
from data_transfer_files import Data_Transfer
import random

class Training:
    def __init__(self, epsilon, learning_rate, gamma):
        self.EPSILON = epsilon
        self.LEARNING_RATE = learning_rate
        self.GAMMA = gamma
    '''
        all_moves - list of all the dictionaries possible moves
    '''

    def train_for_q_values(self,num_of_games,all_moves):
        '''
            Initialize
        '''
        game = Checker()
        
        #Number of games to train through
        while num_of_games > 0:
            won = False
            tie = False

            x_play_count = 0
            episode = []
            reward = 0

            board = ["_","_","_","_","_","_","_","_","_"]
            choices = [1,2,3,4,5,6,7,8,9]
            #print("playing game ", num_of_games)
            while won != True and tie != True:
                next_state = []
                '''
                    X turn
                '''
                val = random.randint(0, len(choices)-1)
                position = choices[val]
                del choices[val]

                board[position-1] = 'X'

                #Check if X won or if it's a tie
                if game.check(board) == True:
                    #print("X won")
                    won = True
                    reward = -1
                    break
                if game.tie(board) == True:
                    #print("tie")
                    tie = True
                    reward = 1
                    break

                #find the right dictionary and x play 

                x_play_str = "".join(board)
                next_state.append(x_play_str)
                '''
                    Exploit vs Explore
                '''
                O_play = ""
                
                '''
                    Explore route
                '''
                if random.uniform(0,1) < self.EPSILON:
                    num_of_options = len(all_moves[x_play_count][x_play_str])
                    explore_val = random.randint(0,num_of_options-1)
                    O_play = all_moves[x_play_count][x_play_str][explore_val][0]
                
                #   Exploit 
                else:
                    highest_q_list = []
                    highest_q = all_moves[x_play_count][x_play_str][0][1]
                    highest_q_list.append(0)

                    exploit_move = ""
                    for o_play in range(1, len(all_moves[x_play_count][x_play_str])):
                        if all_moves[x_play_count][x_play_str][o_play][1] > highest_q:
                            highest_q_list.clear()
                            highest_q_list.append(o_play)
                            highest_q = all_moves[x_play_count][x_play_str][o_play][1]
                            continue
                        if all_moves[x_play_count][x_play_str][o_play][1] == highest_q:
                            highest_q_list.append(o_play)
                    '''
                        If there are 2 or more highest equal q values, then randomly pick one
                    '''
                    if len(highest_q_list) > 1:
                        ran_exploit = random.randint(0,len(highest_q_list))
                        exploit_move = all_moves[x_play_count][x_play_str][highest_q_list[ran_exploit-1]][0]
                    else:
                        exploit_move = all_moves[x_play_count][x_play_str][highest_q_list[0]][0]
                    O_play = exploit_move

                next_state.append(O_play)

                '''
                    update the board
                '''
                difference_board = list(O_play)
                for diff_pos in range(len(difference_board)):
                    if difference_board[diff_pos] != board[diff_pos]:
                        for find_pos in range(len(choices)):
                            if choices[find_pos] == diff_pos+1:
                                del choices[find_pos]
                                break
                
                        board = difference_board
                        break

                '''
                    Check if O won
                '''
                episode.append(next_state)
                if game.check(board) == True:
                    reward = 1
                    #print("O won")
                    break
                x_play_count += 1
            
            self.update_q_vals(episode,reward, all_moves)
            num_of_games -= 1

    '''
        Episode - A Stack ADT to udate the values

        Eq = Q(S,A) + lr * (R(S,A) + gamma * max() - Q(S,A))
    '''
    def update_q_vals(self, epsidoe,reward, all_moves):
        
        for i in range(len(epsidoe)):
            o_play = 0
            while all_moves[i][epsidoe[i][0]][o_play][0] != epsidoe[i][1]:
                o_play+=1

            o_move_str = all_moves[i][epsidoe[i][0]][o_play][0]

            #Set up the base Q Val
            new_q_val = all_moves[i][epsidoe[i][0]][o_play][1]

            #For Non-Terminal State
            if i != len(epsidoe) - 1:
                max_val = self.max_val(i+1, epsidoe[i+1][0], all_moves)
                new_q_val += self.LEARNING_RATE * (self.GAMMA * max_val - new_q_val)

            #For Terminal
            else:
                new_q_val += self.LEARNING_RATE * (reward - new_q_val)
            all_moves[i][epsidoe[i][0]][o_play][1] = new_q_val
    
    def max_val(self, dict_ct, x_move, all_moves):
        max_val = 0
        for o_play in range((len(all_moves[dict_ct][x_move]))):
            if all_moves[dict_ct][x_move][o_play][1] > max_val:
                max_val = all_moves[dict_ct][x_move][o_play][1]
        return max_val

    def test_model(self, num_of_games, all_moves):
        lose = 0
        game = Checker()
        while num_of_games > 0:
            won = False
            tie = False

            x_play_count = 0

            board = ["_","_","_","_","_","_","_","_","_"]
            choices = [1,2,3,4,5,6,7,8,9]
            #print("playing game ", num_of_games)
            while won != True and tie != True:
                '''
                    X turn
                '''
                val = random.randint(0, len(choices)-1)
                position = choices[val]
                del choices[val]
                board[position-1] = 'X'

                #Check if X won or if it's a tie
                if game.check(board) == True:
                    lose += 1
                    break
                if game.tie(board) == True:
                    break

                #find the right dictionary and x play 
                x_play_str = "".join(board)

                '''
                    -O turn, iterate through the Q-Table to find
                    the highest Q-Vale
                '''

                o_turn_str = ""

                highest_q_val = all_moves[x_play_count][x_play_str][0][1]
                highest_q_pos = 0

                for o_play in range(1, len(all_moves[x_play_count][x_play_str])):
                    if all_moves[x_play_count][x_play_str][o_play][1] > highest_q_val:
                        highest_q_pos = o_play
                        highest_q_val = all_moves[x_play_count][x_play_str][o_play][1]
                
                o_turn_str = all_moves[x_play_count][x_play_str][highest_q_pos][0]
                '''
                    update the board
                '''
                #print("o_turn_str is ", o_turn_str)
                difference_board = list(o_turn_str)
                for diff_pos in range(len(difference_board)):
                    if difference_board[diff_pos] != board[diff_pos]:
                        for find_pos in range(len(choices)):
                            if choices[find_pos] == diff_pos+1:
                                del choices[find_pos]
                                break
                
                        board = difference_board
                        break

                '''
                    Check if O won
                '''
                if game.check(board) == True:
                    break
                x_play_count += 1
            num_of_games -= 1
        return lose
            