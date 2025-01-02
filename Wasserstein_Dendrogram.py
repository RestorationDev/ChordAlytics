from scipy.stats import wasserstein_distance
from scipy.cluster import hierarchy
import pandas as pd
import matplotlib.pyplot as plt

# Remove labels and normalize
def preprocess_matrix(matrix):
    numerical_matrix = matrix.iloc[1:, 1:].astype(float)
    flat_matrix = numerical_matrix.values.flatten()
    flat_matrix /= flat_matrix.sum()
    return flat_matrix

matrix_1 = pd.read_csv('/Users/kunalkulkarni/Desktop/DEs/Code/Music Project/Adjacency_Matrices/all_too_well.csv', header=None)
matrix_2 = pd.read_csv('/Users/kunalkulkarni/Desktop/DEs/Code/Music Project/Adjacency_Matrices/baby.csv', header=None)
matrix_3 = pd.read_csv('/Users/kunalkulkarni/Desktop/DEs/Code/Music Project/Adjacency_Matrices/yellow.csv', header=None)
matrix_4 = pd.read_csv('/Users/kunalkulkarni/Desktop/DEs/Code/Music Project/Adjacency_Matrices/story_of_my_life.csv', header=None)
matrix_5 = pd.read_csv('/Users/kunalkulkarni/Desktop/DEs/Code/Music Project/Adjacency_Matrices/hey_soul_sister.csv', header=None)
matrix_6 = pd.read_csv('/Users/kunalkulkarni/Desktop/DEs/Code/Music Project/Adjacency_Matrices/riptide.csv', header=None)

matrices = [matrix_1, matrix_2, matrix_3, matrix_4, matrix_5, matrix_6]

# Add song names corresponding to the matrices
song_names = ['All Too Well', 'Baby', 'Yellow', 'Story of My Life', 'Hey Soul Sister', 'Riptide']

# Preprocess all matrices
preprocessed_matrices = [preprocess_matrix(m) for m in matrices]

n = len(preprocessed_matrices)
result_matrix = pd.DataFrame(index=range(1, n+1), columns=range(1, n+1))

for i in range(n):
    for j in range(n):
        if i == j:
            result_matrix.iloc[i, j] = 0
        else:
            result_matrix.iloc[i, j] = wasserstein_distance(preprocessed_matrices[i], preprocessed_matrices[j])
            
print(result_matrix)

condensed_matrix = hierarchy.distance.squareform(result_matrix)

# Perform hierarchical clustering using the condensed distance matrix
Z = hierarchy.linkage(condensed_matrix, 'average')

# Add song names as labels in the dendrogram
plt.figure()
dn = hierarchy.dendrogram(Z, labels=song_names)

plt.show()