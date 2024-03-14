# https://github.com/gadgil-devashri/csp-map-coloring/blob/main/code/mapcoloring.py
import random
import copy
from datetime import datetime


# Function to inilialize assigned colors
def initColorDict(states):
    assignedColor = {}
    for state in states:
        assignedColor[state] = 'Nil'
    return assignedColor

# Function to initialize domain
def initDomain(states, noOfColors):
    domain = {}
    for state in states:
        domain[state] = list(range(0, noOfColors))
    return domain

def Forwardcheck(states, neighbours, colors, domain):
    if all(value != 'Nil' for value in colors.values()):
        return "Success"
    currentState = states[0]
    currentNeighbors = neighbours[currentState]
    output = 'Success'
    occupiedColors = list(map(colors.get, currentNeighbors))
    if 'Nil' in occupiedColors:
        occupiedColors.remove('Nil')
    for color in domain[currentState]:
        if color not in occupiedColors:
            # assign consistent color
            colors[currentState] = color
            # Temporarily remove currentState
            states.remove(currentState)
            # check if domain can be reduced
            result = check(color, currentNeighbors, colors, domain)
            if not result:
                prevDomain = copy.deepcopy(domain)
                # Reduce domain
                reduceDomain(color, currentNeighbors, colors, domain)
                output = Forwardcheck(states, neighbours, colors, domain)
                if output != "Failure":
                    return "Success"
                # Restore the domain
                domain = prevDomain
            colors[currentState] = 'Nil'
            # Add the state back since it was a failed assignment
            states.append(currentState)
    if colors[currentState] == 'Nil':
        return "Failure"

def reduceDomain(color, currentNeighbors, colors, domain):
    for neighbor in currentNeighbors:
        if colors[neighbor] == 'Nil' and color in domain[neighbor]:
            domain[neighbor].remove(color)

def check(color, currentNeighbors, colors, domain):
    for neighbor in currentNeighbors:
        if colors[neighbor] == 'Nil' and color in domain[neighbor]:
            if len(domain[neighbor]) == 1:
                return True
    return False

# Function to get the minimum chromatic number of the map
def ForwardChecking(graph, V):
    states = list(range(len(graph)))
    neighbours = graph
    copyStates = copy.deepcopy(states)
    count = 0
    color_assignments = {}
    while 1:
        count = count + 1
        copyStates = copy.deepcopy(states)
        colors = initColorDict(states)
        domain = initDomain(states, count)
        result = Forwardcheck(copyStates, neighbours, colors, domain)
        if result == 'Success':
            color_assignments = colors
            break
    return color_assignments, count                   

# G2 = {0: [1, 2], 1: [0, 2, 3], 2: [0, 1, 3], 3: [1, 2, 4], 4: [3]}
# G2 = {
#     0: [1, 2],   # Node A is connected to nodes B and C
#     1: [0, 3],   # Node B is connected to nodes A, C, and D
#     2: [0, 3],   # Node C is connected to nodes A, B, and D
#     3: [1, 2, 4],   # Node D is connected to nodes B, C, and E
#     4: [3]    # Node E is connected to node D
# }
# min_number = ForwardChecking(G2, 5)
# print("Minimum no of colors required for Australia map: ", min_number)