class Data_Transfer:

    def __init__(self):
        self.move_1_file = "move_1.txt"
        self.move_3_file = "move_3.txt"
        self.move_5_file = "move_5.txt"
        self.move_7_file = "move_7.txt"
        self.list_of_files= [self.move_1_file,self.move_3_file,self.move_5_file,self.move_7_file,]
    
    def read_in(self, list_of_moves):
        for file_number in range(len(self.list_of_files)): 
            f = open(self.list_of_files[file_number],"r")
            for first_move in f:
                l = first_move.split(":")
                list_of_moves[file_number][str(l[0])] = []
                next_play = l[1].split(" | ")
                for plays in range(len(next_play)):
                    plays_stats = next_play[plays].split(" ")
                    o_move = plays_stats[0]
                    q_val_str = plays_stats[1]
                    q_val = float(q_val_str)

                    list_of_moves[file_number][l[0]].append([o_move,q_val])
    
    def write_out(self, list_of_moves):
        size = 0
        for file_number in range(len(self.list_of_files)):
            with open(self.list_of_files[file_number], 'w') as f:
                for key, value in list_of_moves[file_number].items():
                    f.write(key)
                    f.write(":")
                    for i in range(len(value)):
                        for x in range(len(value[i])):
                            if x != 0:
                                f.write(" ")
                                '''
                                    format the float value to be 4 decimal points
                                '''
                            if type(value[i][x]) != str:
                                value[i][x] = round(value[i][x],4)
                                
                            f.write(str(value[i][x]))
                        if i != len(value) -1:
                            f.write(" | ")
                    if size != len(list_of_moves[file_number])-1:
                        f.write("\n")
                    size += 1
                            