# Tan Kah Wang
# 2944 2826
# Start Date - 170518
# Last Modified Date - 260518
import pandas as pd
import urllib.request
class WordAnalyser:
    
    def __init__(self):
        self.word_count = pd.DataFrame(index=['Count']) # define pandas dataframe to store word count
        
    def __str__(self):
        word_str = ""
        for each in self.word_count:
            word_str += str(each) + " has count of " + str(self.word_count.loc["Count",each]) + "\n"
        return word_str
    
    def analyse_words(self, tokenised_list):
        for each in tokenised_list:
            if each not in self.word_count:
                self.word_count[each] = 1
            else:
                self.word_count[each] += 1
                
        self.word_count=self.word_count.reindex(sorted(self.word_count.columns), axis=1) # sort the dataframe in alphabetical order
        return self.word_count
        
    def get_stopword_frequency(self):
        url="http://www.lextek.com/manuals/onix/stopwords1.html"
        data=urllib.request.urlopen("http://www.lextek.com/manuals/onix/stopwords1.html")
        data=data.read().decode('utf-8')
        data=data.split("\n")
        # slice the data list from the word index of about to word index of yours
        data=data[data.index("about"):data.index("yours")+1]
        stopword_list=[]
        for each in data:
            # remove blanks and single character in data list
            if len(each) !=1 and len(each) !=0:
                stopword_list.append(each.upper())
        stopword_list_count=pd.DataFrame()
        # match word list to stopword list and return their counts
        stopword_list_count=self.word_count.loc[:,self.word_count.columns.isin(stopword_list)]
        return stopword_list_count
    
    def get_word_length_frequency(self):
        # define an empty dataframe to store the word length frequency
        word_length_count=pd.DataFrame(index=['Count'])
        for each in self.word_count:
            if len(each) not in word_length_count:
                # set count of that particular word length frequency to frequency of that particular words
                word_length_count[len(each)] = self.word_count[each]
            else:
                word_length_count[len(each)] += self.word_count[each]
        
        # return dataframe with ascending sorted word length frequency and adding prefix Word Length to prevent clashing with
        # analyse_character in Task 2
        word_length_count=word_length_count.sort_index(axis=1).add_prefix('Word Length: ')
        return word_length_count