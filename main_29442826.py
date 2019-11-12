# Tan Kah Wang
# 2944 2826
# Start Date - 250518
# Last Modified Date - 260518
import pandas as pd
from preprocessor_29442826 import Preprocesser
from character_29442826 import CharacterAnalyser
from word_29442826 import WordAnalyser
from visualiser_29442826 import AnalysisVisualiser

def main():
    # read in the 6 text files
    edward_str=read_input('Edward_II_Marlowe.tok')
    jew_str=read_input('Jew_of_Malta_Marlowe.tok')
    ric_str=read_input('Richard_II_Shakespeare.tok')
    ham_str=read_input('Hamlet_Shakespeare.tok')
    hen1_str=read_input('Henry_VI_Part1_Shakespeare.tok')
    hen2_str=read_input('Henry_VI_Part2_Shakespeare.tok')
    
    # get the dataframes for edward text
    edward_pre = Preprocesser()
    edward_pre.tokenise(edward_str)
    edward_char = CharacterAnalyser()
    edward_char_count = edward_char.analyse_characters(edward_pre.get_tokenised_list()) #character count dataframe
    edward_punc_count = edward_char.get_punctuation_frequency() #punctuation count dataframe
    edward_word = WordAnalyser()
    edward_word_count = edward_word.analyse_words(edward_pre.get_tokenised_list())#word count dataframe
    edward_stop_count = edward_word.get_stopword_frequency() #stopword count dataframe
    edward_word_len = edward_word.get_word_length_frequency() #word length count dataframe
    
    # get the dataframes for jew text
    jew_pre = Preprocesser()
    jew_pre.tokenise(jew_str)
    jew_char = CharacterAnalyser()
    jew_char_count = jew_char.analyse_characters(jew_pre.get_tokenised_list()) #character count dataframe
    jew_punc_count = jew_char.get_punctuation_frequency() #punctuation count dataframe
    jew_word = WordAnalyser()
    jew_word_count = jew_word.analyse_words(jew_pre.get_tokenised_list())#word count dataframe
    jew_stop_count = jew_word.get_stopword_frequency() #stopword count dataframe
    jew_word_len = jew_word.get_word_length_frequency() #word length count dataframe
    
    # get the dataframes for richard text
    ric_pre = Preprocesser()
    ric_pre.tokenise(ric_str)
    ric_char = CharacterAnalyser()
    ric_char_count = ric_char.analyse_characters(ric_pre.get_tokenised_list()) #character count dataframe
    ric_punc_count = ric_char.get_punctuation_frequency() #punctuation count dataframe
    ric_word = WordAnalyser()
    ric_word_count = ric_word.analyse_words(ric_pre.get_tokenised_list())#word count dataframe
    ric_stop_count = ric_word.get_stopword_frequency() #stopword count dataframe
    ric_word_len = ric_word.get_word_length_frequency() #word length count dataframe
    
    # get the dataframes for hamlet text
    ham_pre = Preprocesser()
    ham_pre.tokenise(ham_str)
    ham_char = CharacterAnalyser()
    ham_char_count = ham_char.analyse_characters(ham_pre.get_tokenised_list()) #character count dataframe
    ham_punc_count = ham_char.get_punctuation_frequency() #punctuation count dataframe
    ham_word = WordAnalyser()
    ham_word_count = ham_word.analyse_words(ham_pre.get_tokenised_list())#word count dataframe
    ham_stop_count = ham_word.get_stopword_frequency() #stopword count dataframe
    ham_word_len = ham_word.get_word_length_frequency() #word length count dataframe
    
    # get the dataframes for henry part 1 text
    hen1_pre = Preprocesser()
    hen1_pre.tokenise(hen1_str)
    hen1_char = CharacterAnalyser()
    hen1_char_count = hen1_char.analyse_characters(hen1_pre.get_tokenised_list()) #character count dataframe
    hen1_punc_count = hen1_char.get_punctuation_frequency() #punctuation count dataframe
    hen1_word = WordAnalyser()
    hen1_word_count = hen1_word.analyse_words(hen1_pre.get_tokenised_list())#word count dataframe
    hen1_stop_count = hen1_word.get_stopword_frequency() #stopword count dataframe
    hen1_word_len = hen1_word.get_word_length_frequency() #word length count dataframe
    
    # get the dataframes for henry part 2 text
    hen2_pre = Preprocesser()
    hen2_pre.tokenise(hen2_str)
    hen2_char = CharacterAnalyser()
    hen2_char_count = hen2_char.analyse_characters(hen2_pre.get_tokenised_list()) #character count dataframe
    hen2_punc_count = hen2_char.get_punctuation_frequency() #punctuation count dataframe
    hen2_word = WordAnalyser()
    hen2_word_count = hen2_word.analyse_words(hen2_pre.get_tokenised_list())#word count dataframe
    hen2_stop_count = hen2_word.get_stopword_frequency() #stopword count dataframe
    hen2_word_len = hen2_word.get_word_length_frequency() #word length count dataframe
    
    # merging the 18 dataframes to get my_all_text_stats
    # note, punctuation dataframe not included as it has already been shown in character dataframe
    edward_overall = pd.concat([edward_char_count,edward_stop_count,edward_word_len], axis=1)
    edward_overall.index=["Edward_II_Marlowe"]
    jew_overall = pd.concat([jew_char_count,jew_stop_count,jew_word_len], axis=1)
    jew_overall.index=["Jew_of_Malta_Marlowe"]
    ric_overall = pd.concat([ric_char_count,ric_stop_count,ric_word_len], axis=1)
    ric_overall.index=["Richard_II_Shakespeare"]
    ham_overall = pd.concat([ham_char_count,ham_stop_count,ham_word_len], axis=1)
    ham_overall.index=["Hamlet_Shakespeare"]
    hen1_overall = pd.concat([hen1_char_count,hen1_stop_count,hen1_word_len], axis=1)
    hen1_overall.index=["Henry_VI_Part1_Shakespeare"]
    hen2_overall = pd.concat([hen2_char_count,hen2_stop_count,hen2_word_len], axis=1)
    hen2_overall.index=["Henry_VI_Part2_Shakespeare"]
    
    # concatenate all dataframes into one (my_all_text_stats)
    my_all_text_stats=pd.concat([edward_overall.T,jew_overall.T,ric_overall.T,ham_overall.T,hen1_overall.T,hen2_overall.T])
    my_all_text_stats=my_all_text_stats.groupby(my_all_text_stats.index,as_index=True).sum().astype(int)

    # calling class AnalysisVisualiser by passing through my_all_text_stats
    visualiser=AnalysisVisualiser(my_all_text_stats)
    # calling the method for character frequency and saving the plot as an output file
    char_plot=visualiser.visualise_character_frequency()
    char_plot_fig=char_plot.get_figure()
    char_plot_fig.savefig("charplot.png")
    # calling the method for punctuation frequency and saving the plot as an output file
    punc_plot=visualiser.visualise_punctuation_frequency()
    punc_plot_fig=punc_plot.get_figure()
    punc_plot_fig.savefig("puncplot.png")
    # calling the method for stopword frequency and saving the plot as an output file
    stop_plot=visualiser.visualise_stopword_frequency()
    stop_plot_fig=stop_plot.get_figure()
    stop_plot_fig.savefig("stopplot.png")
    # calling the method for word length and saving the plot as an output file
    len_plot=visualiser.visualise_word_length_frequency()
    len_plot_fig=len_plot.get_figure()
    len_plot_fig.savefig("lenplot.png")
    # calling the method to return the relative frequency dataframe and output to a csv file
    visualiser.return_relative_frequency().to_csv("relativefrequency.csv")
    
    # return all the __str__ method defined in task 1, 2, 3
    # Edward_II_Marlowe
    print ("Analysis of Edward_II_Marlowe:","\n")
    print (edward_pre ,"\n")
    print (edward_char)
    print (edward_word)
    # Jew_of_Malta_Marlowe
    print ("Analysis of Jew_of_Malta_Marlowe:","\n")
    print (jew_pre ,"\n")
    print (jew_char)
    print (jew_word)
    # Richard_II_Shakespeare
    print ("Analysis of Richard_II_Shakespeare:","\n")
    print (ric_pre ,"\n")
    print (ric_char)
    print (ric_word)
    # Hamlet_Shakespeare
    print ("Analysis of Hamlet_Shakespeare:","\n")
    print (ham_pre ,"\n")
    print (ham_char)
    print (ham_word)
    # Henry_VI_Part1_Shakespeare
    print ("Analysis of Henry_VI_Part1_Shakespeare:","\n")
    print (hen1_pre ,"\n")
    print (hen1_char)
    print (hen1_word)
    # Henry_VI_Part2_Shakespeare
    print ("Analysis of Henry_VI_Part2_Shakespeare:","\n")
    print (hen2_pre ,"\n")
    print (hen2_char)
    print (hen2_word)
    
def read_input(file_name):
    try:
        input_handle = open(file_name, 'r')
    except FileNotFoundError:
        print(file_name ,"not found")
    except IOError:
        print("Cannot open", file_name)
    except RuntimeError:
        print("A run-time error has occured")
    else:
        temp_str=""
        for line in input_handle:
            temp_str += line
        input_handle.close()
        # return a string with the newline at the end of each line stripped
        return (temp_str.replace("\n",''))
    
if __name__ == "__main__":
    main()