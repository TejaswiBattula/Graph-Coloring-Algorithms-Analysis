# def addEdge(adj, v, w):
#     adj[v].append(w)
#     adj[w].append(v)

def welshPowellColoring(adjacencyList, numberOfVertices):
    # Step 1: Create a list of vertices sorted by their degrees
    sortedVertices = sorted(range(numberOfVertices), key=lambda x: len(adjacencyList[x]), reverse=True)

    # Step 2: Initialize the colors and assignedColors set
    colors = [-1] * numberOfVertices
    assignedColors = set()

    # Step 3: Assign colors to the vertices
    for vertex in sortedVertices:
        # Step 3.1: Check for available colors
        neighbors_with_colors = []
        for neighbor in adjacencyList[vertex]:
            if colors[neighbor] != -1:
                neighbors_with_colors.append(colors[neighbor])
        availableColors = assignedColors.difference(set(neighbors_with_colors))

        # Step 3.2: If there are available colors, assign the minimum color
        if availableColors:
            colors[vertex] = min(availableColors)
        else:
            # Step 3.3: If no available colors, assign a new color
            newColor = max(colors) + 1
            colors[vertex] = newColor
            assignedColors.add(newColor)
    
    return colors, len(set(colors))

    # # Step 4: Print the result
    # for vertex in range(numberOfVertices):
    #     print("Vertex", vertex, " --->  Color", colors[vertex])

# # Example usage:
# if __name__ == "__main__":
#     g = [[] for _ in range(5)]
#     addEdge(g, 0, 1)
#     addEdge(g, 0, 2)
#     addEdge(g, 1, 2)
#     addEdge(g, 1, 3)
#     addEdge(g, 2, 3)
#     addEdge(g, 3, 4)

#     print("Coloring of the graph using Welsh-Powell Algorithm:")
#     welshPowellColoring(g, 5)
