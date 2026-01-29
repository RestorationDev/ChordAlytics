import os
import pandas as pd
import numpy as np

FOLDER_PATH = "/Users/kunalkulkarni/Desktop/DEs/Code/Music Project"
ADJACENCY_DIR = os.path.join(FOLDER_PATH, "Adjacency_Matrices")
SONG_FILES = {
    'All Too Well': 'all_too_well.csv',
    'Baby': 'baby.csv',
    'Hey Soul Sister': 'hey_soul_sister.csv',
    'Riptide': 'riptide.csv',
    'Story of My Life': 'story_of_my_life.csv',
    'Yellow': 'yellow.csv',
}


def _load_matrix(path):
    df = pd.read_csv(path, header=None)
    chord_names = df.iloc[1:, 0].values
    matrix = df.iloc[1:, 1:].apply(pd.to_numeric, errors='coerce').to_numpy()
    return chord_names, matrix


def chord_centrality_list(matrix_path):
    """Compute eigenvalue centrality and return chords ranked by centrality."""
    chord_names, matrix = _load_matrix(matrix_path)
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    max_idx = np.argmax(eigenvalues)
    centrality = np.abs(eigenvectors[:, max_idx])
    centrality /= np.sum(centrality)
    ranked_indices = np.argsort(-centrality)
    ranked_list = chord_names[ranked_indices].tolist()
    for rank, idx in enumerate(ranked_indices):
        print(f"Rank {rank + 1}: Number {idx}: Chords: {chord_names[idx]}")
    return ranked_list


def frequency_list(matrix_path):
    """Compute frequency rankings from row sums."""
    chord_names, matrix = _load_matrix(matrix_path)
    row_sums = np.sum(matrix, axis=1)
    ranked_indices = np.argsort(row_sums)[::-1]
    ranked_list = chord_names[ranked_indices].tolist()
    for rank, idx in enumerate(ranked_indices):
        print(f"Rank {rank + 1}: Number {idx}: Sum: {row_sums[idx]} Chords: {chord_names[idx]}")
    return ranked_list


if __name__ == "__main__":
    paths = {name: os.path.join(ADJACENCY_DIR, f) for name, f in SONG_FILES.items()}

    print("Centrality Rankings:")
    for name, path in paths.items():
        ranking = chord_centrality_list(path)
        print(f"{name}: {ranking}\n")

    print("Frequency Rankings:")
    for name, path in paths.items():
        ranking = frequency_list(path)
        print(f"{name}: {ranking}\n")
