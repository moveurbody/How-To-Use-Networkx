import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_node(1, time='5pm')
G.add_nodes_from([3], time='2pm')

G.node[1]['room'] = 714
print(G.node[1])
print(G.nodes(data=True))
G.add_edge(1, 2, weight=4.7 )
G.add_edges_from([(3,4),(4,5)], color='blue')
G.add_edges_from([(1,2,{'color':'blue'}), (2,3,{'weight':8})])

nx.draw(G)
plt.show()