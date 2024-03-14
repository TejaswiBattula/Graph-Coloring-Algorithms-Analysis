# input


import random


# linear graph 
def linear_graph(V):
    adjacency_list = {i: [i - 1, i + 1] for i in range(V)}
    adjacency_list[0] = [1]
    adjacency_list[V - 1] = [V - 2]
    return adjacency_list

# dense graph
def dense_graph(V, edge_probability=0.5):
    adjacency_list = {i: [] for i in range(V)}
    for i in range(V):
        for j in range(i + 1, V):
            if random.uniform(0, 1) < edge_probability:
                adjacency_list[i].append(j)
                adjacency_list[j].append(i)
    return adjacency_list


# Sparse Graph
def sparse_graph(V, edge_probability=0.1):
    adjacency_list = {i: [] for i in range(V)}
    for i in range(V):
        for j in range(i + 1, V):
            if random.uniform(0, 1) < edge_probability:
                adjacency_list[i].append(j)
                adjacency_list[j].append(i)
    return adjacency_list

# Regular Graph
def regular_graph(V):
    degree = random.randint(2, V // 2) * 2
    if V % 2 != 0 or degree % 2 != 0:
        raise ValueError("The number of nodes and degree must be even for a regular graph.")
    
    adjacency_list = {i: [(i + j) % V for j in range(1, degree // 2 + 1)] +
                        [(i - j) % V for j in range(1, degree // 2 + 1)] for i in range(V)}
    return adjacency_list

# Bipartite Graph
def bipartite_graph(V):
    if V % 2 != 0:
        raise ValueError("The number of nodes must be even for a bipartite graph.")
    
    partition_size = V // 2
    adjacency_list = {i: [i + partition_size] for i in range(partition_size)}
    adjacency_list.update({i + partition_size: [i] for i in range(partition_size)})
    return adjacency_list

# Planar Graphs
def planar_graph(V):
    # Generating a simple planar graph for illustration
    if V < 3:
        raise ValueError("A planar graph must have at least 3 nodes.")
    
    adjacency_list = {i: [(i + 1) % V, (i + 2) % V] for i in range(V)}
    adjacency_list[V - 1].append(0)
    adjacency_list[V - 2].append(0)
    return adjacency_list

# Disconnected Graph
def disconnected_graph(V):
    components = []
    remaining_vertices = V

    while remaining_vertices > 0:
        size = random.randint(1, remaining_vertices)  # Randomly select component size
        components.append(size)
        remaining_vertices -= size

    start = 0
    adjacency_list = {}

    for size in components:
        component = list(range(start, start + size))
        start += size
        adjacency_list.update({i: [] for i in component})

    return adjacency_list

# Graphs with Bridges and Cut Vertices
def graph_with_bridges_and_cut_vertices(V):
    if V < 3:
        raise ValueError("A graph with bridges and cut vertices must have at least 3 nodes.")
    
    # Initialize an empty adjacency list
    adjacency_list = {i: [] for i in range(V)}
    
    # Add random edges to form a connected graph
    for i in range(V - 1):
        j = random.randint(i + 1, V - 1)
        adjacency_list[i].append(j)
        adjacency_list[j].append(i)
    
    # Add an extra edge to create a cycle
    j = random.randint(0, V - 1)
    adjacency_list[0].append(j)
    adjacency_list[j].append(0)
    
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
