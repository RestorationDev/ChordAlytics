test_str = "CCGGAmAmFFCCGGAmAmFFCCGGAmAmFFCCGGAmFGCCGGAmAmFFCCGGAmFGCCGGAmAmFFCCGGAmFGFFGCGFFGCGFFGCGFFGGCCGGAmAmFFCCGGAmAmFFCCGGAmFGCCGGAmAmFFCCGGAmFGCCGGAmAmFFCCGGAmFGFFGCGFFGCGFFGCGFFGGCCGGAmAmAmAmGGGGAmGFGFFGCGFFGCFFFGCGFFGCGFFGCGFFGGGCCGGAmAmFGCCGGAmAmFG"


def song_to_matrix(test_string):
    """Convert a chord string to a list of 3-chord sequences."""
    chord_array = []
    i = 0
    while i < len(test_string):
        if test_string[i] in ["C", "G", "F"]:
            chord_array.append(test_string[i])
        elif test_string[i] == "A" and i + 1 < len(test_string):
            chord_array.append(test_string[i] + test_string[i + 1])
            i += 1
        i += 1

    three_chord_array = [
        chord_array[j] + chord_array[j + 1] + chord_array[j + 2]
        for j in range(len(chord_array) - 2)
    ]
    return three_chord_array


chord_sequence = song_to_matrix(test_str)

if __name__ == "__main__":
    print(chord_sequence)
