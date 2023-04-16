import networkx as nx
import matplotlib.pyplot as plt

with open('list_of_edges.txt', 'r') as file:
    edges = [line.strip().split() for line in file]

G = nx.Graph()
for edge in edges:
    if len(edge) == 1:
        G.add_node(edge[0])
    else:
        G.add_edge(edge[0], edge[1])

nx.draw(G, with_labels=True)
plt.show()

if nx.is_connected(G):
    print("Граф связный")
else:
    print("Граф несвязный")
