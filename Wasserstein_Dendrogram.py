import os
from scipy.stats import wasserstein_distance
from scipy.cluster import hierarchy
import pandas as pd
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ADJACENCY_DIR = os.path.join(SCRIPT_DIR, 'Adjacency_Matrices')
SONG_NAMES = ['All Too Well', 'Baby', 'Yellow', 'Story of My Life', 'Hey Soul Sister', 'Riptide']
SONG_FILES = [
    'all_too_well.csv', 'baby.csv', 'yellow.csv',
    'story_of_my_life.csv', 'hey_soul_sister.csv', 'riptide.csv'
]


def preprocess_matrix(matrix):
    numerical = matrix.iloc[1:, 1:].astype(float)
    flat = numerical.values.flatten()
    flat /= flat.sum()
    return flat


if __name__ == "__main__":
    matrices = [pd.read_csv(os.path.join(ADJACENCY_DIR, f), header=None) for f in SONG_FILES]
    preprocessed = [preprocess_matrix(m) for m in matrices]
    n = len(preprocessed)

    result_matrix = pd.DataFrame(index=range(1, n + 1), columns=range(1, n + 1))
    for i in range(n):
        for j in range(n):
            result_matrix.iloc[i, j] = 0 if i == j else wasserstein_distance(preprocessed[i], preprocessed[j])

    print(result_matrix)
    condensed = hierarchy.distance.squareform(result_matrix.values.astype(float))
    Z = hierarchy.linkage(condensed, 'average')
    plt.figure()
    hierarchy.dendrogram(Z, labels=SONG_NAMES)
    plt.show()
