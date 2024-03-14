import input
import output
from algorithms.greedy.greedy_sequential import greedyColoring
from algorithms.greedy.welsh_powell import welshPowellColoring
from algorithms.greedy.DSatur import dsatur 
from algorithms.backtracking.backtracking import backtracking_graph_coloring
from algorithms.backtracking.forward_checking import ForwardChecking 
from algorithms.backtracking.constraint_satisfaction import ConstraintSatisfaction 

V = 11
dense_graph_adjacency = input.graph_with_bridges_and_cut_vertices(V)
result, chromatic_number = ConstraintSatisfaction(dense_graph_adjacency, V)
print(chromatic_number)
print(result)
output.draw_graph(dense_graph_adjacency, result)
