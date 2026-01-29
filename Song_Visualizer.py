import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

TEST_FILE = 'data_generator_test.tsv'

test_df = pd.read_csv(TEST_FILE, header=None, skiprows=1, delimiter='\t')
test_df_numeric = test_df.apply(pd.to_numeric, errors='coerce').fillna(0)

print("Number of nodes:", test_df_numeric.shape[0])
print("Number of edges:", test_df_numeric.sum().sum())

G = nx.from_pandas_adjacency(test_df_numeric)
print("G nodes:", G.nodes())
print("G edges:", G.edges())

if G.number_of_edges() > 0:
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G, k=0.3)
    nx.draw(G, pos, with_labels=True, node_size=800, node_color='lightblue', font_size=12)
    plt.title("Graph Visualization")
    plt.show()
else:
    print("The graph is empty. No edges to display.")
