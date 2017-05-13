# -*- coding: utf-8 -*-
# @Time    : 2017/5/12 下午6:08
# @Author  : Yuhsuan
# @File    : Centrality.py
# @Software: PyCharm Community Edition

# https://networkx.github.io/documentation/development/reference/algorithms.centrality.html

import networkx as nx
import matplotlib.pyplot as plt
import community

G = nx.erdos_renyi_graph(30, 0.05)

#first compute the best partition
partition = community.best_partition(G)

#drawing
size = float(len(set(partition.values())))
pos = nx.spring_layout(G)
count = 0.
for com in set(partition.values()) :
    count = count + 1.
    list_nodes = [nodes for nodes in partition.keys()
                                if partition[nodes] == com]
    nx.draw_networkx_nodes(G, pos, list_nodes, node_size = 20,
                                node_color = str(count / size))


nx.draw_networkx_edges(G,pos, alpha=0.5)
plt.show()