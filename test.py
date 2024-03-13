import input
import output
from algorithms.greedy.greedy_sequential import greedyColoring
from algorithms.greedy.welsh_powell import welshPowellColoring
from algorithms.greedy.DSatur import dsatur 
from algorithms.backtracking.backtracking import backtracking_graph_coloring
from algorithms.backtracking.forward_checking import ForwardChecking 

V = 10
dense_graph_adjacency = input.dense_graph(V)
result, chromatic_number = ForwardChecking(dense_graph_adjacency, V)
print(chromatic_number)
print(result)
output.draw_graph(dense_graph_adjacency, result)
