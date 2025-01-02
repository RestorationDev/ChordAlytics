import Data_Generator
import sys
print(sys.executable)
print(sys.path)
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt



test_file = 'data_generator_test.tsv'
test_df = pd.read_csv(test_file, header=None, skiprows=1, delimiter='\t')

# Convert dataframe to numeric, coerce errors, and fill NaN values with 0
test_df_numeric = test_df.apply(pd.to_numeric, errors='coerce').fillna(0)

# Print number of nodes and edges
print("Number of nodes: ", test_df_numeric.shape[0])
print("Number of edges: ", test_df_numeric.sum().sum())

# Create a graph from the pandas adjacency matrix
G = nx.from_pandas_adjacency(test_df_numeric)

# Print graph nodes and edges
print("G nodes: ", G.nodes())
print("G edges: ", G.edges())


# If the graph has edges, plot it with a more aesthetic layout
if G.number_of_edges() > 0:
    plt.figure(figsize=(12, 8))

    # Use a layout for the graph
    pos = nx.spring_layout(G, k=0.3)  # Adjust k for more spacing if needed

    # Draw the graph with nicer layout and styling
    nx.draw(G, pos, with_labels=True, node_size=800, node_color='lightblue', font_size=12)

    # Set a title for the plot and show it
    plt.title("Graph Visualization")
    plt.show()
else:
    print("The graph is empty. No edges to display.")






