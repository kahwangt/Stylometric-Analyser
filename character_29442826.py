# Tan Kah Wang
# 2944 2826
# Start Date - 170518
# Last Modified Date - 250518
import pandas as pd
class CharacterAnalyser:
    
    def __init__(self):
        self.character_count = pd.DataFrame(index=['Count']) # define pandas dataframe to store character count
        
    def __str__(self):
        char_str = ""
        for each in self.character_count:
            char_str += str(each) + " has count of " + str(self.character_count.loc["Count",each]) + "\n"
        return char_str
    
    def analyse_characters(self, tokenised_list):
        for each in ''.join(tokenised_list):      # join the tokenised list together as one whole string
            if each not in self.character_count:
                self.character_count[each] = 1
            else:
                self.character_count[each] += 1
        
        self.character_count=self.character_count.reindex(sorted(self.character_count.columns), axis=1) # sort the dataframe in ascending
        return self.character_count
        
    def get_punctuation_frequency(self):
        punctuation_count=pd.DataFrame() # define pandas dataframe to store punctuation count
        alphabet_number_list=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W',
                             'X','Y','Z','0','1','2','3','4','5','6','7','8','9'] # define a list of all alphabets and all numbers
        punctuation_count = self.character_count.loc[:, ~self.character_count.columns.isin(alphabet_number_list)] 
        return punctuation_count # return only the dataframe of instance variable that do not contain alphabets and numbers, i.e. punctuations