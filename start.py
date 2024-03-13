import input
from algorithms.greedy.greedy_sequential import greedyColoring
from algorithms.greedy.welsh_powell import welshPowellColoring
from algorithms.greedy.DSatur import dsatur
import time
import random
import plot
import math

def execute_sorting_algorithms(array, n):
    algorithms = [
        ("Greedy Sequential", greedyColoring),
        ("Welsh Powell", welshPowellColoring),
        ("DSatur", dsatur)
    ]

    results = {}

    for algorithm_name, algorithm_func in algorithms:
        array_copy = array.copy()
        start_time = time.time()
        result, chromatic_number = algorithm_func(array_copy, n)
        end_time = time.time()
        duration = end_time - start_time
        results[algorithm_name] = {"duration": duration, "chromatic_number": chromatic_number}

    return results

def generateGraph2():
    print("started")
    scenarios = [input.linear_graph, input.dense_graph]
    points = 5
    n = 10
    results = []

    while points:
        for scenario in scenarios:
            graph = scenario(n)
            results.append({"Length": n, "Scenario": scenario.__name__, **execute_sorting_algorithms(graph, n)})

        print(f"Point: {points}")
        n += 10
        points -= 1

    # Plot both time vs input and chromatic number vs input
    plot.plot_results(results, 'duration')
    plot.plot_results(results, 'chromatic_number')

generateGraph2()
