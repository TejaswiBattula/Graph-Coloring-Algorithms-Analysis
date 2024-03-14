import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import numpy as np

def plot_results(results, ylabel):
    # Create a color map for different algorithms
    color_map = mcolors.ListedColormap(['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown'])

    for i, (scenario, group) in enumerate(group_by_scenario(results)):
        lengths = [result["Length"] for result in group]

        # Separate values for each algorithm
        algorithm_values = {algorithm: np.array([result[algorithm][ylabel] for result in group]) for algorithm in ["Greedy Sequential", "Welsh Powell", "DSatur"]}
        # "Backtracking", "Forward Checking", "Constraint Satisfaction"

        # Plot for each algorithm with a different color
        for j, (algorithm, values) in enumerate(algorithm_values.items()):
            plt.plot(lengths, values, label=f"{algorithm}", marker='o', markersize=2, color=color_map(j))

        # Add labels and title
        plt.xlabel('Length')
        plt.ylabel(ylabel)

        plt.title(f'Size of Input vs {ylabel} for Algorithms - {scenario}')

        # Add a legend
        plt.legend()

        # Save the plot to a file
        plt.savefig(f'output/{scenario}_{ylabel.replace(" ", "_")}.png')

        # Show the plot
        plt.show()

def group_by_scenario(results):
    results.sort(key=lambda x: (x["Scenario"], x["Length"]))

    current_scenario = None
    grouped_results = []

    for result in results:
        if result["Scenario"] != current_scenario:
            if current_scenario is not None:
                grouped_results.append((current_scenario, current_group))
            current_scenario = result["Scenario"]
            current_group = []
        current_group.append(result)

    if current_scenario is not None:
        grouped_results.append((current_scenario, current_group))

    return grouped_results
