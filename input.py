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

def bipartite_graph(V):
    if V % 2 != 0:
        raise ValueError("The number of nodes must be even for a bipartite graph.")
    
    partition_size = V // 2
    adjacency_list = {i: [(i + j) % partition_size + partition_size] for i in range(partition_size) for j in range(1, partition_size)}
    adjacency_list.update({i + partition_size: [(i + j) % partition_size] for i in range(partition_size) for j in range(1, partition_size)})
    return adjacency_list

def crown_graph(n):
    if(n%2!=0):
        print("crown graph can not be generated with odd vertices.")
        return
    n = n//2
    adj_list = {}
    for i in range(n):
        adj_list[i] = [j + n for j in range(n) if j != i]
    for j in range(n):
        adj_list[j + n] = [i for i in range(n) if i != j]
    return adj_list

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
def disconnected_graph(V, isolation_probability=0.5):
    components = []
    remaining_vertices = V

    # Randomly assign isolated nodes based on the default probability
    isolated = [random.random() < isolation_probability for _ in range(V)]
    isolated_count = sum(isolated)
    remaining_vertices -= isolated_count

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

    # Randomly add edges between non-isolated nodes
    non_isolated_nodes = [i for i in range(V) if not isolated[i]]
    for node in non_isolated_nodes:
        neighbors = random.sample(non_isolated_nodes, random.randint(0, len(non_isolated_nodes) - 1))
        adjacency_list[node] = neighbors

    # Add isolated nodes to the adjacency list
    isolated_nodes = [i for i in range(V) if isolated[i]]
    for node in isolated_nodes:
        adjacency_list[node] = []

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
