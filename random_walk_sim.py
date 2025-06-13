from pylab import *
import networkx as nx
import random as rd
import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import csv

# Initialize a random graph with N nodes and C edges and return
# Used Copilot to figure out how to ensure generated graph is always connected
def initialize(N, C):
    while True:
        G = nx.gnm_random_graph(N, C)
        if nx.is_connected(G):
            break
    for i in G.nodes():
        G.nodes[i]['state'] = 0
    return G

# Simulate a random walk until all nodes are visited, return path 
# Generated with help from Copilot 
def random_walk(G):
    start_node = rd.choice(list(G.nodes()))
    current_node = start_node
    path = [current_node]
    visited = set([start_node])
    G.nodes[start_node]['state'] = 1
 
    while len(visited) < len(G.nodes()):
        # Get unvisited neighbors
        unvisited_neighbors = [n for n in G.neighbors(current_node) if G.nodes[n]['state'] == 0]
        if unvisited_neighbors:
            next_node = rd.choice(unvisited_neighbors)
        else:
            # If all neighbors are visited, pick any neighbor (allows revisiting)
            next_node = rd.choice(list(G.neighbors(current_node)))
        
        current_node = next_node
        path.append(current_node)
        G.nodes[current_node]['state'] = 1
        visited.add(current_node)

    return len(path)

def main():
    results = []
    xs = []  # store n values for plotting
    ys = []  # store c values for plotting
    zs = []  # store average random walk lengths for plotting

    # iterate through different values of n
    for n in range(0, 40, 5):
        # iterate through different values of c
        for c in range(n, n*2, 5):
            avg_walk_lengths = [] 
            for i in range (5):
                G = initialize(n, c)
                path = random_walk(G)
                avg_walk_lengths.append(path)
            mean_walk = np.mean(avg_walk_lengths)
            results.append([n, c, mean_walk])
            xs.append(n)
            ys.append(c)
            zs.append(mean_walk)

    print(results)

    # Export results to a CSV file
    with open('results.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write header row
        writer.writerow(['Number of Nodes (n)', 'Number of Connections (c)', 'Average Random Walk Length'])
        # Write each result row
        writer.writerows(results)
    
    # Plot the results in a 3D scatter plot
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    sc = ax.scatter(xs, ys, zs, c=zs, cmap='viridis', s=50)
    ax.set_xlabel('Number of Nodes (n)')
    ax.set_ylabel('Number of Connections (c)')
    ax.set_zlabel('Average Random Walk Length')
    ax.set_title('3D Visualization of Random Walk Length vs. n and c')
    fig.colorbar(sc, ax=ax, label='Walk Length')
    
    plt.show()

main()
