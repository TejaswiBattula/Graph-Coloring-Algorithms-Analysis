# input


# linear graph 
# dense graph
# Sparse Graph
# Regular Graph
# Bipartite Graph
# Power Law Graphs
# Planar Graphs
# Graphs with Cliques
# Graphs with Independent Sets
# Disconnected Graph
# Graphs with Bridges and Cut Vertices


import random

def linear_graph(V):
    adjacency_list = {i: [i - 1, i + 1] for i in range(V)}
    adjacency_list[0] = [1]
    adjacency_list[V - 1] = [V - 2]
    return adjacency_list

def dense_graph(V, edge_probability=0.5):
    adjacency_list = {i: [] for i in range(V)}
    for i in range(V):
        for j in range(i + 1, V):
            if random.uniform(0, 1) < edge_probability:
                adjacency_list[i].append(j)
                adjacency_list[j].append(i)
    return adjacency_list

def sparse_graph(V, edge_probability=0.1):
    adjacency_list = {i: [] for i in range(V)}
    for i in range(V):
        for j in range(i + 1, V):
            if random.uniform(0, 1) < edge_probability:
                adjacency_list[i].append(j)
                adjacency_list[j].append(i)
    return adjacency_list

def regular_graph(V, degree):
    if V % 2 != 0 or degree % 2 != 0:
        raise ValueError("The number of nodes and degree must be even for a regular graph.")
    
    adjacency_list = {i: [(i + j) % V for j in range(1, degree // 2 + 1)] +
                        [(i - j) % V for j in range(1, degree // 2 + 1)] for i in range(V)}
    return adjacency_list

def bipartite_graph(V):
    if V % 2 != 0:
        raise ValueError("The number of nodes must be even for a bipartite graph.")
    
    partition_size = V // 2
    adjacency_list = {i: [i + partition_size] for i in range(partition_size)}
    adjacency_list.update({i + partition_size: [i] for i in range(partition_size)})
    return adjacency_list

def power_law_graph(V, m=3, seed=None):
    random.seed(seed)
    degrees = [random.paretovariate(m) for _ in range(V)]
    adjacency_list = {i: random.sample(range(V), int(degrees[i])) for i in range(V)}
    return adjacency_list

def planar_graph(V):
    # Generating a simple planar graph for illustration
    if V < 3:
        raise ValueError("A planar graph must have at least 3 nodes.")
    
    adjacency_list = {i: [(i + 1) % V, (i + 2) % V] for i in range(V)}
    adjacency_list[V - 1].append(0)
    adjacency_list[V - 2].append(0)
    return adjacency_list

def graph_with_cliques(V, clique_sizes):
    if sum(clique_sizes) != V:
        raise ValueError("The sum of clique sizes must be equal to the number of nodes.")
    
    start = 0
    adjacency_list = {}
    for size in clique_sizes:
        clique = list(range(start, start + size))
        adjacency_list.update({i: clique for i in clique})
        start += size
    return adjacency_list

def graph_with_independent_sets(V, set_sizes):
    if sum(set_sizes) != V:
        raise ValueError("The sum of set sizes must be equal to the number of nodes.")
    
    start = 0
    adjacency_list = {}
    for size in set_sizes:
        node = start
        for _ in range(size - 1):
            adjacency_list[node] = [node + 1]
            node += 1
        start += size
    return adjacency_list

def disconnected_graph(V, components):
    if sum(components) != V:
        raise ValueError("The sum of component sizes must be equal to the number of nodes.")
    
    start = 0
    adjacency_list = {}
    for size in components:
        component = list(range(start, start + size))
        start += size
        adjacency_list.update({i: [] for i in component})
    return adjacency_list

def graph_with_bridges_and_cut_vertices(V):
    if V < 3:
        raise ValueError("A graph with bridges and cut vertices must have at least 3 nodes.")
    
    adjacency_list = {0: [1], 1: [0, 2], 2: [1]}
    return adjacency_list

# # Example usage:
# V = 10
# print("Linear Graph:", linear_graph(V))
# print("\nDense Graph:", dense_graph(V))
# print("\nSparse Graph:", sparse_graph(V))
# print("\nRegular Graph:", regular_graph(V, 4))
# print("\nBipartite Graph:", bipartite_graph(V))
# print("\nPower Law Graph:", power_law_graph(V))
# print("\nPlanar Graph:", planar_graph(V))
# print("\nGraph with Cliques:", graph_with_cliques(V, [3, 4, 3]))
# print("\nGraph with Independent Sets:", graph_with_independent_sets(V, [2, 3, 5]))
# print("\nDisconnected Graph:", disconnected_graph(V, [2, 4, 4]))
# print("\nGraph with Bridges and Cut Vertices:", graph_with_bridges_and_cut_vertices(V))
