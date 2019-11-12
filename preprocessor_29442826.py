# Tan Kah Wang
# 2944 2826
# Start Date - 170518
# Last Modified Date - 250518
class Preprocesser:
    
    def __init__(self):
        self.token_list = []
        
    def __str__(self):
        return "Total number of tokens: " + str(len(self.token_list))
    
    def tokenise(self,input_sequence):
        for each in input_sequence.upper().split(" "):  #change all to upper cases and split the spaces
            self.token_list.append(each)
            
    def get_tokenised_list(self):
        return self.token_list