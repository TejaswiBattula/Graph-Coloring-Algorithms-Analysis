# take the graph output from algorithms with color and generate the graph.
# pip install networkx matplotlib
# pip install seaborn


import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns

def draw_graph(adjacency_list, indices):
    G = nx.Graph(adjacency_list)
    pos = nx.spring_layout(G)

    unique_indices = set(indices.values())
    colors = sns.color_palette('deep', len(unique_indices))
    color_map = {value: colors[i] for i, value in enumerate(unique_indices)}

    node_color = [color_map[indices[node]] for node in G.nodes()]

    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color=node_color, font_size=8)
    plt.show()

# Example usage for a dense graph
# V = 10
# dense_graph_adjacency = input.linear_graph(V)
# draw_graph(dense_graph_adjacency)
