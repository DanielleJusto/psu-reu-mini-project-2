from pylab import *
import networkx as nx
import random as rd


# Initialize a random graph with N nodes and C edges and return
def initialize(N, C):
    # Used Copilot to figure out how to ensure generated graph is always connected
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
    visited = set([current_node])
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

    return path

def main():
    G = initialize(20,30)
    path  = random_walk(G)
    print(path)
    print(len(path))

main()