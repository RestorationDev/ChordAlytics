import Song_Parser
import pandas as pd

CHORD_POSSIBILITIES = [
    "CCC", "CCG", "CCF", "CCAm", "CGC", "CGG", "CGF", "CGAm",
    "CFC", "CFG", "CFF", "CFAm", "CAmC", "CAmG", "CAmF", "CAmAm",
    "GCC", "GCG", "GCF", "GCAm", "GGC", "GGG", "GGF", "GGAm",
    "GFC", "GFG", "GFF", "GFAm", "GAmC", "GAmG", "GAmF", "GAmAm",
    "FCC", "FCG", "FCF", "FCAm", "FGC", "FGG", "FGF", "FGAm",
    "FFC", "FFG", "FFF", "FFAm", "FAmC", "FAmG", "FAmF", "FAmAm",
    "AmCC", "AmCG", "AmCF", "AmCAm", "AmGC", "AmGG", "AmGF", "AmGAm",
    "AmFC", "AmFG", "AmFF", "AmFAm", "AmAmC", "AmAmG", "AmAmF", "AmAmAm"
]


def three_chord_arr(chord_sequence_array):
    """Build a 65x65 transition matrix from 3-chord sequences."""
    df = pd.DataFrame(index=range(65), columns=range(65))
    df.iloc[1:65, 0] = CHORD_POSSIBILITIES[:64]
    df.iloc[0, 1:65] = CHORD_POSSIBILITIES[:64]
    df.fillna(0, inplace=True)

    for i in range(len(chord_sequence_array) - 1):
        entry = chord_sequence_array[i]
        next_entry = chord_sequence_array[i + 1]
        entry_index = df.iloc[:, 0][df.iloc[:, 0] == entry].index
        next_entry_index = df.iloc[:, 0][df.iloc[:, 0] == next_entry].index
        if not entry_index.empty and not next_entry_index.empty:
            df.iloc[next_entry_index[0], entry_index[0]] += 1

    return df


if __name__ == "__main__":
    test_df = three_chord_arr(Song_Parser.chord_sequence).T
    test_df.to_csv('data_generator_test1.csv', sep='\t', index=False)
