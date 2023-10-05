import Training_Class
import data_transfer_files
from Training_Class import Training
from data_transfer_files import Data_Transfer


def main():


    #Train the model 
    dict_1 = {}
    dict_2 = {}
    dict_3 = {}
    dict_4 = {}

    list_of_moves = [dict_1,dict_2,dict_3,dict_4]
    dataTransfer = Data_Transfer()
    print("Extracting Q-Tables")
    dataTransfer.read_in(list_of_moves)


    epsilon = .3
    learning_rate = .1
    gamma = .9
    num_of_games = 10000
    print("Training the model")
    Model = Training(epsilon, learning_rate, gamma)
    Model.train_for_q_values(num_of_games,list_of_moves)
    
    print("Testing the model")
    loss = Model.test_model(num_of_games,list_of_moves)

    print(f"Model lost {loss} out of {num_of_games} games")
    print("loss rate is ", (loss / num_of_games) * 100)

    print("Storing Model Data")
    dataTransfer.write_out(list_of_moves)



if __name__ == '__main__':
    main()