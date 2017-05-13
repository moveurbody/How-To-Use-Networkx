import matplotlib.pyplot as plt
import networkx as nx

# G = nx.random_graphs.barabasi_albert_graph(100,2)
G=nx.Graph()
H = nx.path_graph(10)
G.add_nodes_from(H)
nx.draw(G,pos=nx.spectral_layout(G),node_size = 30, with_label = True)
print(nx.info(G))
plt.show()