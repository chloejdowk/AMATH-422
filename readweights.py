import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

print("Just got here")
adj_mat = np.loadtxt('network_13.csv', delimiter=',')

adj_mat[adj_mat <1] = 0
adj_mat[adj_mat >1] = 1

print(adj_mat)

network = nx.from_numpy_array(adj_mat, create_using=nx.DiGraph)

print("I'm on it boss!")

avg_length = nx.average_shortest_path_length(network)
print(avg_length)

clustering = nx.average_clustering(network)
print(clustering)