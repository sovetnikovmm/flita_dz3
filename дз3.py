import networkx as nx
import matplotlib.pyplot as plt

with open('list_of_edges.txt', 'r') as file:
    edges = [line.strip().split() for line in file]
    print(edges)

G = nx.Graph()
for edge in edges:
    if len(edge) == 1:
        G.add_node(edge[0])
    elif len(edge) == 2:
        G.add_edge(edge[0], edge[1])
    else:
        print('Invalid input of edges')
        break

nx.draw(G, with_labels=True)
plt.show()
print("By the graph connectivity theorem:")
if len(G.edges) > (len(G.nodes)-1)*(len(G.nodes)-2)*0.5:
    print("Graph is connected")
else:
    print("Graph is not connected")
