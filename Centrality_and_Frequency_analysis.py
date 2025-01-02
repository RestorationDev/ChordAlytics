import pandas as pd
import numpy as np

# Function to calculate eigenvalue centrality and rank chords
def chord_centrality_list(matrix_1):
    # Read the adjacency matrix
    matrix_1 = pd.read_csv(matrix_1, header=None)

    # Extract the chord names (first column, skipping the header)
    array_values = matrix_1.iloc[:, 0].values
    array_values = array_values[1:]

    # Remove the first row/column (headers) for numeric processing
    matrix_1 = matrix_1.iloc[1:, 1:]

    # Convert matrix to numeric values
    matrix_1 = matrix_1.apply(pd.to_numeric, errors='coerce').to_numpy()

    # Compute eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(matrix_1)

    # Find the eigenvector corresponding to the largest eigenvalue
    max_eigenvalue_index = np.argmax(eigenvalues)
    eigenvector_centrality = np.abs(eigenvectors[:, max_eigenvalue_index])

    # Normalize the centrality scores
    eigenvector_centrality /= np.sum(eigenvector_centrality)

    # Rank the nodes based on centrality scores (descending order)
    node_indices_ranked = np.argsort(-eigenvector_centrality)
    ranked_list = []

    # Create and print the ranked list
    for rank, node_index in enumerate(node_indices_ranked):
        print(f"Rank {rank + 1}: Number {node_index}: Chords: {array_values[node_index]}")
        ranked_list.append(array_values[node_index])

    return ranked_list


# Function to calculate frequency rankings based on row sums
def frequency_list(matrix_1):
    # Read the adjacency matrix
    matrix_1 = pd.read_csv(matrix_1, header=None)

    # Extract the chord names
    array_values = matrix_1.iloc[:, 0].values
    array_values = array_values[1:]

    # Remove the first row/column (headers) for numeric processing
    matrix_1 = matrix_1.iloc[1:, 1:]
    matrix_1 = matrix_1.apply(pd.to_numeric, errors='coerce').to_numpy()

    # Compute the sum of each row
    row_sums = np.sum(matrix_1, axis=1)

    # Rank the rows based on their sums (descending order)
    ranked_row_indices = np.argsort(row_sums)[::-1]
    ranked_list = []

    # Create and print the ranked list
    for rank, node_index in enumerate(ranked_row_indices):
        print(f"Rank {rank + 1}: Number {node_index}: Sum: {row_sums[node_index]} Chords: {array_values[node_index]}")
        ranked_list.append(array_values[node_index])

    return ranked_list


# Paths to adjacency matrix files
folder_path = "/Users/kunalkulkarni/Desktop/DEs/Code/Music Project"
all_too_well = folder_path + "/Adjacency_Matrices/all_too_well.csv"
baby = folder_path + "/Adjacency_Matrices/baby.csv"
hey_soul_sister = folder_path + "/Adjacency_Matrices/hey_soul_sister.csv"
riptide = folder_path + "/Adjacency_Matrices/riptide.csv"
story_of_my_life = folder_path + "/Adjacency_Matrices/story_of_my_life.csv"
yellow = folder_path + "/Adjacency_Matrices/yellow.csv"

# Get centrality rankings for each song
atw_centrality = chord_centrality_list(all_too_well)
baby_centrality = chord_centrality_list(baby)
hss_centrality = chord_centrality_list(hey_soul_sister)
rt_centrality = chord_centrality_list(riptide)
soml_centrality = chord_centrality_list(story_of_my_life)
ylw_centrality = chord_centrality_list(yellow)

# Get frequency rankings for each song
atw_ranked = frequency_list(all_too_well)
baby_ranked = frequency_list(baby)
hss_ranked = frequency_list(hey_soul_sister)
rt_ranked = frequency_list(riptide)
soml_ranked = frequency_list(story_of_my_life)
ylw_ranked = frequency_list(yellow)

# Print results for centrality rankings
print("Centrality Rankings: ")
print("All too well: ", atw_centrality)
print()
print("Baby: ", baby_centrality)
print()
print("Hey soul sister: ", hss_centrality)
print()
print("Riptide: ", rt_centrality)
print()
print("Story of My Life: ", soml_centrality)
print()
print("Yellow: ", ylw_centrality)

# Print results for frequency rankings
print()
print("Frequency Rankings: ")
print("All too well: ", atw_ranked)
print()
print("Baby: ", baby_ranked)
print()
print("Hey soul sister: ", hss_ranked)
print()
print("Riptide: ", rt_ranked)
print()
print("Story of My Life: ", soml_ranked)
print()
print("Yellow: ", ylw_ranked)