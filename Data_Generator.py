import Song_Parser
import numpy as np
import pandas as pd


# A sample song string for our tasks
song_str = "CCGGAmAmFFCCGGAmAmFFCCGGAmFGCCGGAmAmFFCCGGAmFGCCGGAmAmFFCCGGAmFGFFGCGFFGCGFFGCGFFGGCCGGAmAmFFCCGGAmAmFFCCGGAmFGCCGGAmAmFFCCGGAmFGCCGGAmAmFFCCGGAmFGFFGCGFFGCGFFGCGFFGGCCGGAmAmAmAmGGGGAmGFGFFGCGFFGCFFFGCGFFGCGFFGCGFFGGGCCGGAmAmFGCCGGAmAmFG"



def three_chord_arr(chord_sequence_array):

    # An ordered list of possiblities for 3 chord sequences (4^3 possibilities)
    chord_possibilities = [
    "CCC", "CCG", "CCF", "CCAm",
    "CGC", "CGG", "CGF", "CGAm",
    "CFC", "CFG", "CFF", "CFAm",
    "CAmC", "CAmG", "CAmF", "CAmAm",
    "GCC", "GCG", "GCF", "GCAm",
    "GGC", "GGG", "GGF", "GGAm",
    "GFC", "GFG", "GFF", "GFAm",
    "GAmC", "GAmG", "GAmF", "GAmAm",
    "FCC", "FCG", "FCF", "FCAm",
    "FGC", "FGG", "FGF", "FGAm",
    "FFC", "FFG", "FFF", "FFAm",
    "FAmC", "FAmG", "FAmF", "FAmAm",
    "AmCC", "AmCG", "AmCF", "AmCAm",
    "AmGC", "AmGG", "AmGF", "AmGAm",
    "AmFC", "AmFG", "AmFF", "AmFAm",
    "AmAmC", "AmAmG", "AmAmF", "AmAmAm"]

    # Initialize a dataframe
    df = pd.DataFrame(index=range(65), columns=range(65))

    # Populate dataframe with chord possibilities
    df.iloc[1:65, 0] = chord_possibilities[:64]  
    df.iloc[0, 1:65] = chord_possibilities[:64]
    

    
    df.iloc[1:65, 1:65]

    i = 0

    df.fillna(0,inplace=True)


    for entry in chord_sequence_array:
        #Find the row index of th current entry
        entry_index = df.iloc[:,0][df.iloc[:, 0] == entry].index

        if not entry_index.empty:
            entry_index = entry_index[0]

            i+=1
            
            if i ==len(chord_sequence_array):
                break

            next_entry_index = df.iloc[:, 0][df.iloc[:, 0] == chord_sequence_array[i]].index

            if not next_entry_index.empty:
                next_entry_index = next_entry_index[0]
                
                df.iloc[next_entry_index, entry_index] += 1

    return df


test_df = three_chord_arr(Song_Parser.chord_sequence)

test_df = test_df.T

test_df.to_csv('data_generator_test1.csv', sep='\t', index=False)