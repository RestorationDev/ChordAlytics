import os
from itertools import product
import random
import pandas as pd
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ADJACENCY_DIR = os.path.join(SCRIPT_DIR, 'Adjacency_Matrices')
SONG_FILES = [
    'all_too_well.csv', 'baby.csv', 'yellow.csv',
    'story_of_my_life.csv', 'hey_soul_sister.csv', 'riptide.csv'
]
CHORDS = ["C", "Am", "G", "F"]
CHORD_MATRIX = [a + b + c for a, b, c in product(CHORDS, repeat=3)]

matrices = [pd.read_csv(os.path.join(ADJACENCY_DIR, f), header=None) for f in SONG_FILES]


def preprocess_matrix(matrix):
    return matrix.iloc[1:, 1:].astype(float)


def normalize_matrix(matrix):
    matrix_np = matrix.to_numpy()
    row_sums = np.sum(matrix_np, axis=1, keepdims=True)
    transition_np = np.divide(matrix_np, row_sums, where=row_sums != 0)
    zero_rows = row_sums.flatten() == 0
    if np.any(zero_rows):
        transition_np[zero_rows, :] = 1 / matrix.shape[1]
    return pd.DataFrame(transition_np, index=matrix.index, columns=matrix.columns)


def n_markov_walk(transition_matrix, beginning_chord, n_steps):
    state_sequence = [beginning_chord]
    state_curr = beginning_chord
    for _ in range(n_steps):
        probability_list = transition_matrix[state_curr].values
        n_states = len(probability_list)
        state_next = random.choices(range(1, n_states + 1), weights=probability_list)[0]
        state_sequence.append(state_next)
        state_curr = state_next
    return state_sequence


if __name__ == "__main__":
    preprocessed = [preprocess_matrix(m) for m in matrices]
    average_matrix = sum(preprocessed) / len(preprocessed)
    transformed_average = normalize_matrix(average_matrix)

    for _ in range(10):
        walk_indices = n_markov_walk(transformed_average, 34, 30)
        walk_chords = [CHORD_MATRIX[i - 1] for i in walk_indices]
        print(walk_chords)

    transformed_average.to_csv(os.path.join(ADJACENCY_DIR, 'transformed_average_matrix.csv'), index=False, header=False)
