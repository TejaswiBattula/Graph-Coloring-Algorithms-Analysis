import input
from algorithms.greedy.greedy_sequential import greedyColoring
from algorithms.greedy.welsh_powell import welshPowellColoring
from algorithms.greedy.DSatur import dsatur
from algorithms.backtracking.backtracking import backtracking_graph_coloring
from algorithms.backtracking.forward_checking import ForwardChecking 
from algorithms.backtracking.constraint_satisfaction import ConstraintSatisfaction 
import time
import random
import plot
import math

def execute_sorting_algorithms(array, n):
    algorithms = [
        ("Greedy Sequential", greedyColoring),
        ("Welsh Powell", welshPowellColoring),
        ("DSatur", dsatur),
        ("Backtracking", backtracking_graph_coloring),
        ("Forward Checking", ForwardChecking),
        ("Constraint Satisfaction", ConstraintSatisfaction)
    ]

    results = {}

    for algorithm_name, algorithm_func in algorithms:
        array_copy = array.copy()
        start_time = time.time()
        result, chromatic_number = algorithm_func(array_copy, n)
        end_time = time.time()
        duration = end_time - start_time
        results[algorithm_name] = {"duration": duration, "chromatic_number": chromatic_number}

        print(algorithm_name)
        print(result)
        print(chromatic_number)
    return results

def generateGraph():
    print("started")
    scenarios = [input.linear_graph, input.dense_graph, input.sparse_graph, input.regular_graph, input.bipartite_graph, input.planar_graph, input.disconnected_graph, input.graph_with_bridges_and_cut_vertices, input.crown_graph]
    #[input.linear_graph, input.dense_graph, input.sparse_graph, input.regular_graph, input.bipartite_graph, input.planar_graph, input.disconnected_graph, input.graph_with_bridges_and_cut_vertices, input.crown_graph]
    points = 20
    n = 10
    results = []

    while points:
        print(f"Point: {points}")
        for scenario in scenarios:
            print(scenario)
            graph = scenario(n)
            #print(graph)
            results.append({"Length": n, "Scenario": scenario.__name__, **execute_sorting_algorithms(graph, n)})
        n += 50000
        points -= 1

    # Plot both time vs input and chromatic number vs input
    plot.plot_results(results, 'duration')
    plot.plot_results(results, 'chromatic_number')

generateGraph()