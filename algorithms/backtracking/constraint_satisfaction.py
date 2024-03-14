import random
import copy
import pandas as pd

noOfBacktracks = 0

#Function to inilialize assigned colors
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
    
def reduceSingletonDomain(currentNeighbors, neighbors, colors, domain):
    reduceStates = []
    for neighbor in currentNeighbors:
        if len(domain[neighbor]) == 1 and colors[neighbor] == 'Nil':
            reduceStates.append(neighbor)
    
    while reduceStates:
        state = reduceStates.pop(0)
        for neighbor in neighbors[state]:
            if colors[neighbor] == 'Nil' and domain[state][0] in domain[neighbor]:
                domain[neighbor].remove(domain[state][0])
                if len(domain[neighbor]) == 0:
                    return False
                if len(domain[neighbor]) == 1:
                    reduceStates.append(neighbor)
    return True

def minRemainingValueHeuristic(states, domain, neighbours):    
    states.sort(key=lambda x: (len(domain[x]),-len(neighbours[x])))
    currentSelection = states[0]
    return currentSelection

def leastConstrainingValueHeuristic(currentState, domain, neighbors):
    currentDomain = domain[currentState]
    currentNeighbors = neighbors[currentState]
    orderedDomain ={}
    for color in currentDomain:
        count = 0
        for neighbor in currentNeighbors:
            if color in domain[neighbor]:
                count = count + 1
        orderedDomain[color] = count
    
    # Sort 
    orderedDomain = dict(sorted(orderedDomain.items(), key=lambda item: item[1]))
    return list(orderedDomain.keys())

            
def ForwardcheckWithSingletonPropogationAndHeuristics(states, neighbours, colors, domain):
    global noOfBacktracks
    if all(value != 'Nil' for value in colors.values()):
        return "Success"
    # Use minimum heuristics( and degree heuristics ) to select next unassigned variable 
    currentState = minRemainingValueHeuristic(states, domain, neighbours)
    currentNeighbors = neighbours[currentState]
    output = 'Success'
    occupiedColors = list( map(colors.get, currentNeighbors))
    if 'Nil' in occupiedColors:
        occupiedColors.remove('Nil')
    # Use LCV heuristic to get the color
    orderedDomain = leastConstrainingValueHeuristic(currentState, domain, neighbours)
    for color in orderedDomain:
        if color not in occupiedColors:
            # assign consistent color
            colors[currentState] = color
            # Temporarily remove currentState
            states.remove(currentState)
            # check if any domain can be reduced
            result = check(color,currentNeighbors, colors, domain)
            if not result:
                prevDomain = copy.deepcopy(domain)
                # Reduce domain
                reduceDomain(color, currentNeighbors, colors, domain)
                # Aplly singleton propogation
                singleton = reduceSingletonDomain(currentNeighbors, neighbours, colors, domain)
                if singleton:
                    output = ForwardcheckWithSingletonPropogationAndHeuristics(states, neighbours, colors, domain)
                    if output != "Failure":
                        return "Success"
                # Rsstore domain if filure occurs
                domain = prevDomain
            colors[currentState] = 'Nil'
            # add currentState back since assignment failed
            states.append(currentState)
    if colors[currentState] == 'Nil':
        noOfBacktracks = noOfBacktracks + 1
        return "Failure"

#Function to get the minimum chromatic number of the map
def ConstraintSatisfaction(graph, V):
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
        result = ForwardcheckWithSingletonPropogationAndHeuristics(copyStates, neighbours, colors, domain)
        if result == 'Success':
            color_assignments = colors
            break
    return color_assignments, count                     


# G2 = {0: [1, 2], 1: [0, 2, 3], 2: [0, 1, 3], 3: [1, 2, 4], 4: [3]}
# min_number = ConstraintSatisfaction(G2)
# print("Minimum no of colors required for Australia map: ", min_number)
