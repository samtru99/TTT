import pprint

#import data_transfer_files import Data_Transfer
import recursion
from recursion import Recurison

def main():
    move_1 = {}
    move_3 = {}
    move_5 = {}
    move_7 = {}

    board = ["_","_","_","_","_","_","_","_","_"]

    all_moves = [move_1,move_3,move_5,move_7]

    recur = Recurison()

    recur.dummy_function(all_moves,1,board)

    print("after generating ")
    recur.total_plays()
    #pprint.pprint(all_moves)


if __name__ == "__main__":
    main()