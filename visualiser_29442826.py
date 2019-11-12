# Tan Kah Wang
# 2944 2826
# Start Date - 240518
# Last Modified Date - 260518
import pandas as pd

class AnalysisVisualiser:
    def __init__ (self,all_text_stats):
        # char count relative freq, obtained by dividing by total count of characters in each text
        char_df=all_text_stats.T.loc[:,all_text_stats.T.columns.str.len()==1]
        char_df_rel=char_df.divide(char_df.loc[:,char_df.columns.str.len()==1].sum(axis=1),axis=0).T

        # word length count relative freq, obtained by dividing by total count of words in each text
        word_length_df=all_text_stats.T.loc[:,all_text_stats.T.columns.str.len()>1].loc[:,all_text_stats.T.loc[:,all_text_stats.T.columns.str.len()>1].columns.str.contains('Word Length:')].T
        word_length_df_rel=word_length_df.divide(word_length_df.sum())

        # stopword count relative freq, obtained by dividing by total count of words in each text
        alphabet_number_list=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W',
                            'X','Y','Z','0','1','2','3','4','5','6','7','8','9']
        stopword_df=all_text_stats.T.loc[:,all_text_stats.T.columns.str.len()>1].loc[:,~all_text_stats.T.loc[:,all_text_stats.T.columns.str.len()>1].columns.str.contains('Word Length:')].T
        stopword_df_rel=stopword_df.divide(word_length_df.sum())
        
        # instance variable containing the relative frequencies
        # note the punctuation relative frequency can be found as well in character relative frequency
        self.overall_df_rel=pd.concat([char_df_rel,stopword_df_rel,word_length_df_rel],axis=0)
    
    def visualise_character_frequency(self):
        # define alphabets and numeral list, get relative frequencies of only those found in the list and return them as bar chart
        alphabet_number_list=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W',
                              'X','Y','Z','0','1','2','3','4','5','6','7','8','9']
        return self.overall_df_rel.T.loc[:, self.overall_df_rel.T.columns.isin(alphabet_number_list)].T.plot(kind='bar',title='Character Relative Frequency',figsize=(15,8));
        
    def visualise_punctuation_frequency(self):
        # define alphabets and numeral list, get relative frequencies of punctuations only and return them as bar chart
        # i.e. those not in the alphabet number list and is of length 1 only
        alphabet_number_list=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W',
                              'X','Y','Z','0','1','2','3','4','5','6','7','8','9',' ']
        return self.overall_df_rel.T.loc[:, ~self.overall_df_rel.T.columns.isin(alphabet_number_list)].loc[:,self.overall_df_rel.T.loc[:, ~self.overall_df_rel.T.columns.isin(alphabet_number_list)].columns.str.len()==1].T.plot(kind='bar',title='Punctuation Relative Frequency',figsize=(15,8));

    def visualise_stopword_frequency(self):
        # return only stopwords found in the instance variable
        # i.e. those of length > 1 and those that do not contain the string "Word Length"
        return self.overall_df_rel.T.loc[:,self.overall_df_rel.T.columns.str.len()>1].loc[:,~self.overall_df_rel.T.loc[:,self.overall_df_rel.T.columns.str.len()>1].columns.str.contains('Word Length:')].T.plot(kind='bar',title='Stopword Relative Frequency',figsize=(20,8),fontsize=5);
        
    def visualise_word_length_frequency(self):
        # return the relative frequencies of word length
        # i.e. those containing the string "Word Length"
        return self.overall_df_rel.T.loc[:,self.overall_df_rel.T.columns.str.len()>1].loc[:,self.overall_df_rel.T.loc[:,self.overall_df_rel.T.columns.str.len()>1].columns.str.contains('Word Length:')].T.plot(kind='barh',title='Word Length Relative Frequency',figsize=(15,8));
        
    def return_relative_frequency(self):
        # defined to return the instance variable
        return self.overall_df_rel