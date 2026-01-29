import os
import numpy as np
import pandas as pd

ADJACENCY_DIR = 'Adjacency_Matrices'
SONG_FILES = [
    'all_too_well.csv', 'baby.csv', 'yellow.csv',
    'story_of_my_life.csv', 'hey_soul_sister.csv', 'riptide.csv'
]

matrices = [pd.read_csv(os.path.join(ADJACENCY_DIR, f), header=None) for f in SONG_FILES]


def normalize_matrix(matrix):
    min_val = matrix.min().min()
    max_val = matrix.max().max()
    return (matrix - min_val) / (max_val - min_val)


def preprocess_and_normalize_matrix(matrix):
    numerical = matrix.iloc[1:, 1:].astype(float)
    return normalize_matrix(numerical)


def multiply_matrices(m1, m2):
    return np.dot(m1, m2)


preprocessed = [preprocess_and_normalize_matrix(m) for m in matrices]
output_dir = 'Multiplied_matrices'
os.makedirs(output_dir, exist_ok=True)

for i in range(len(preprocessed)):
    for j in range(i + 1, len(preprocessed)):
        product_ij = pd.DataFrame(multiply_matrices(preprocessed[i].values, preprocessed[j].values))
        product_ji = pd.DataFrame(multiply_matrices(preprocessed[j].values, preprocessed[i].values))
        name_ij = f'normalized_matrix_{i+1}_x_normalized_matrix_{j+1}.csv'
        name_ji = f'normalized_matrix_{j+1}_x_normalized_matrix_{i+1}.csv'
        product_ij.to_csv(os.path.join(output_dir, name_ij), header=None, index=False)
        product_ji.to_csv(os.path.join(output_dir, name_ji), header=None, index=False)
        print(f'Saved {name_ij} and {name_ji}')
