import numpy as np
import pandas as pd

# Load your matrices
matrix_1 = pd.read_csv('/Users/kunalkulkarni/Desktop/DEs/Code/Music Project/Adjacency_Matrices/all_too_well.csv', header=None)
matrix_2 = pd.read_csv('/Users/kunalkulkarni/Desktop/DEs/Code/Music Project/Adjacency_Matrices/baby.csv', header=None)
matrix_3 = pd.read_csv('/Users/kunalkulkarni/Desktop/DEs/Code/Music Project/Adjacency_Matrices/yellow.csv', header=None)
matrix_4 = pd.read_csv('/Users/kunalkulkarni/Desktop/DEs/Code/Music Project/Adjacency_Matrices/story_of_my_life.csv', header=None)
matrix_5 = pd.read_csv('/Users/kunalkulkarni/Desktop/DEs/Code/Music Project/Adjacency_Matrices/hey_soul_sister.csv', header=None)
matrix_6 = pd.read_csv('/Users/kunalkulkarni/Desktop/DEs/Code/Music Project/Adjacency_Matrices/riptide.csv', header=None)

matrices = [matrix_1, matrix_2, matrix_3, matrix_4, matrix_5, matrix_6]

# Function to normalize a matrix (element-wise normalization to [0, 1])
def normalize_matrix(matrix):
    '''
       input: matrix of numbers
       processes: ?/
       returns:
    '''
    min_val = matrix.min().min()  # Find the overall min value
    max_val = matrix.max().max()  # Find the overall max value
    return (matrix - min_val) / (max_val - min_val)  # Normalize to [0, 1]

# Preprocessing the matrices and normalizing them
def preprocess_and_normalize_matrix(matrix):
    numerical_matrix = matrix.iloc[1:, 1:].astype(float)  # Remove the first row and column and convert to float
    normalized_matrix = normalize_matrix(numerical_matrix)  # Apply normalization
    return normalized_matrix

# Preprocess and normalize all matrices
preprocessed_normalized_matrices = [preprocess_and_normalize_matrix(m) for m in matrices]

# Multiply two matrices
def multiply_matrices(m1, m2):
    return np.dot(m1, m2)

# Iterate over each unique pair of matrices and multiply them in both orders
for i in range(len(preprocessed_normalized_matrices)):
    for j in range(i + 1, len(preprocessed_normalized_matrices)):
        # Multiply matrices in one order
        product_matrix_ij = multiply_matrices(preprocessed_normalized_matrices[i].values, preprocessed_normalized_matrices[j].values)
        product_df_ij = pd.DataFrame(product_matrix_ij)
        filename_ij = f'normalized_matrix_{i+1}_x_normalized_matrix_{j+1}.csv'
        product_df_ij.to_csv(filename_ij, header=None, index=None)
        print(f'Saved multiplication of normalized matrix {i+1} and matrix {j+1} to {filename_ij}')

        # Multiply matrices in reverse order
        product_matrix_ji = multiply_matrices(preprocessed_normalized_matrices[j].values, preprocessed_normalized_matrices[i].values)
        product_df_ji = pd.DataFrame(product_matrix_ji)
        filename_ji = f'normalized_matrix_{j+1}_x_normalized_matrix_{i+1}.csv'
        product_df_ji.to_csv(filename_ji, header=None, index=None)
        print(f'Saved multiplication of normalized matrix {j+1} and matrix {i+1} to {filename_ji}')