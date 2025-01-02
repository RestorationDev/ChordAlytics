import pandas as pd
import numpy as np
import random


# Take adjacency matrices
# Turn them into transition matrices
# Average these transition matrices

matrix_1 = pd.read_csv('/Users/kunalkulkarni/Desktop/DEs/Code/Music Project/Adjacency_Matrices/all_too_well.csv', header=None)
matrix_2 = pd.read_csv('/Users/kunalkulkarni/Desktop/DEs/Code/Music Project/Adjacency_Matrices/baby.csv', header=None)
matrix_3 = pd.read_csv('/Users/kunalkulkarni/Desktop/DEs/Code/Music Project/Adjacency_Matrices/yellow.csv', header=None)
matrix_4 = pd.read_csv('/Users/kunalkulkarni/Desktop/DEs/Code/Music Project/Adjacency_Matrices/story_of_my_life.csv', header=None)
matrix_5 = pd.read_csv('/Users/kunalkulkarni/Desktop/DEs/Code/Music Project/Adjacency_Matrices/hey_soul_sister.csv', header=None)
matrix_6 = pd.read_csv('/Users/kunalkulkarni/Desktop/DEs/Code/Music Project/Adjacency_Matrices/riptide.csv', header=None)

chord_matrix = [
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

def preprocess_matrix(matrix):
    numerical_matrix = matrix.iloc[1:, 1:].astype(float)
    return numerical_matrix




def normalize_matrix(matrix):
    # Convert the matrix to a NumPy array for sum computation with keepdims
    matrix_np = matrix.to_numpy()
    
    # Compute row sums with keepdims
    row_sums = np.sum(matrix_np, axis=1, keepdims=True)
    
    # Normalize rows (avoid division by zero)
    transition_matrix_np = np.divide(matrix_np, row_sums, where=row_sums != 0)
    
    # Handle rows with zero sums (uniform distribution for zero rows)
    zero_rows = row_sums.flatten() == 0
    if np.any(zero_rows):
        transition_matrix_np[zero_rows, :] = 1 / matrix.shape[1]
    
    # Convert back to a pandas DataFrame for consistency
    transition_matrix = pd.DataFrame(transition_matrix_np, index=matrix.index, columns=matrix.columns)
    
    return transition_matrix

def n_markov_walk(average_transition_matrix, beginning_chord, n_steps):
    
    state_sequence = [beginning_chord]

    state_curr = beginning_chord

    for i in range(n_steps):

        probability_list = average_transition_matrix[state_curr]

        indexing_list = range(1, len(probability_list)+1)

        state_next = random.choices(indexing_list, weights=probability_list)[0]

        state_sequence.append(state_next)

        state_curr = state_next
    
    return state_sequence

matrices = [matrix_1, matrix_2,
            matrix_3, matrix_4,
            matrix_5, matrix_6]


preprocessed_matrices = [preprocess_matrix(m) for m in matrices]

# # Calculate the average matrix
average_matrix = sum(preprocessed_matrices) / len(preprocessed_matrices)


transformed_average_matrix = normalize_matrix(average_matrix)

for i in range(10):
    stimulated_walk_indices = n_markov_walk(transformed_average_matrix,34, 30)

    stimulated_walk = []

    stimulated_walk.append([chord_matrix[index-1] for index in stimulated_walk_indices])

    print(stimulated_walk)

#transformed_average_matrix.to_csv('/Users/kunalkulkarni/Desktop/DEs/Code/Music Project/Adjacency_Matrices/transformed_average_matrix.csv', index=False, header=False)













