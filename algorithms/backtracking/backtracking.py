def is_valid(graph, vertex, color, assignment):
    for neighbor in graph[vertex]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def graph_coloring(graph, num_colors, assignment, vertex):
    if vertex not in graph:
        return True  # All vertices colored

    for color in range(num_colors):
        if is_valid(graph, vertex, color, assignment):
            assignment[vertex] = color
            if graph_coloring(graph, num_colors, assignment, vertex + 1):
                return True
            assignment[vertex] = None  # Backtrack if no valid coloring found

    return False  # No valid coloring for the current assignment

def backtracking_graph_coloring(graph, V):
    if V==0 or V==1:
        return {}, V 
    num_colors = 1
    while True:
        assignment = {}
        if graph_coloring(graph, num_colors, assignment, 0):
            return assignment, num_colors
        num_colors += 1

# Example usage:
# graph = {
#     0: [1, 2],
#     1: [0, 2],
#     2: [0, 1]
# }

# chromatic_number, coloring = backtracking_graph_coloring(graph)
# if coloring:
#     print(f"Chromatic number of the graph: {chromatic_number}")
#     print("Graph coloring solution:")
#     for vertex, color in coloring.items():
#         print(f"Vertex {vertex}: Color {color}")
# else:
#     print("No valid coloring exists for the given graph.")