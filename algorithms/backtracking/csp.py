from constraint import Problem

def graph_coloring_csp(graph):
    problem = Problem()

    # Add variables for each vertex
    for vertex in graph:
        problem.addVariable(vertex, range(1, len(graph) + 1))

    # Add constraints to ensure neighboring vertices have different colors
    for vertex, neighbors in graph.items():
        for neighbor in neighbors:
            problem.addConstraint(lambda color1, color2: color1 != color2, (vertex, neighbor))

    # Solve the CSP problem
    solution = problem.getSolutions()

    print("All solutions:", solution)

    if solution:
        chromatic_number = max(max(sol.values()) for sol in solution)
        return chromatic_number
    else:
        return None

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

result = graph_coloring_csp(graph)
if result:
    print("Chromatic number:", result)
else:
    print("No solution found.")