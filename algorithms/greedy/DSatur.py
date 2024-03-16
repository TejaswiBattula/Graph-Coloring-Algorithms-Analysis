# https://www.codingninjas.com/studio/library/dsatur-algorithm-for-graph-coloring
# Import necessary modules
from collections import defaultdict
from heapq import heappush, heappop

# Define a class to store vertex information with saturation degree, degree, and vertex index
class VertexInfo:
    def __init__(self, sat, deg, vertex):
        self.sat = sat
        self.deg = deg
        self.vertex = vertex

    def __lt__(self, other):
        # Custom comparison method for the priority queue
        return (self.sat, self.deg, self.vertex) > (other.sat, other.deg, other.vertex)

# # Function to add an edge between two vertices in the graph
# def add_edge_between(graph, a, b):
#     graph[a].append(b)
#     graph[b].append(a)

# Main DSatur algorithm function for graph coloring
def dsatur(graph, V):
    u = 0
    use = [False] * V  # Keep track of colors used by adjacent vertices
    color = [-1] * V  # Colors assigned to vertices
    d = [len(graph[u]) for u in range(V)]  # Degree of each vertex
    adj_cols = [set() for _ in range(V)]  # Colors used by adjacent vertices
    Q = []  # Priority queue for vertices based on saturation degree and degree

    # Initialize the priority queue with vertices and their information
    for u in range(V):
        color[u] = -1
        d[u] = len(graph[u])
        adj_cols[u] = set()
        heappush(Q, VertexInfo(0, d[u], u))

    while Q:
        # Extract vertex with maximum saturation degree and degree
        max_ptr = heappop(Q)
        u = max_ptr.vertex

        # Check colors used by adjacent vertices
        for v in graph[u]:
            if color[v] != -1:
                use[color[v]] = True

        # Find the first available color
        i = 0
        while i != len(use):
            if not use[i]:
                break
            i += 1

        # Reset the 'use' array
        for v in graph[u]:
            if color[v] != -1:
                use[color[v]] = False

        # Assign the found color to the current vertex
        color[u] = i

        # Update information for adjacent vertices
        for v in graph[u]:
            if color[v] == -1:
                new_vertex_info = VertexInfo(len(adj_cols[v]), d[v], v)
                # Remove the old information from the priority queue
                Q = [v_info for v_info in Q if v_info != new_vertex_info]
                adj_cols[v].add(i)
                d[v] -= 1
                # Push the updated information back into the priority queue
                heappush(Q, VertexInfo(len(adj_cols[v]), d[v], v))
    
    return color, len(set(color))
    # ans = set(color)

    # Print the colors assigned to each vertex
    # print_color(color)
    # print("The Chromatic number is :", len(ans))
    # return len(ans)

# Function to print the colors assigned to each vertex
# def print_color(color):
#     for i in range(len(color)):
#         print("The Color of the vertex", i, "is", color[i])

# Function to get the chromatic number of a graph
# def get_chromatic_number(graph):
#     V = len(graph)
#     return dsatur(graph, V)

# Example usage of the algorithm with two sample graphs G1 and G2
# if __name__ == "__main__":
#     G1 = [[1, 2], [0, 2, 3], [0, 1, 3], [1, 2, 4], [3]]
#     G2 = [[1, 2], [0, 2, 4], [0, 1, 4], [4], [1, 2, 3]]
#     # G2 = {0: [1, 2], 1: [0, 2, 3], 2: [0, 1, 3], 3: [1, 2, 4], 4: [3]}

#     print("Coloring of graph G1 ")
#     get_chromatic_number(G1)

#     print("\nColoring of graph G2 ")
#     get_chromatic_number(G2)
