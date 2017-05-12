# -*- coding: utf-8 -*-
# @Time    : 2017/5/10 下午5:33
# @Author  : Yuhsuan
# @File    : basic_network.py
# @Software: PyCharm Community Edition
import networkx as nx
import matplotlib.pyplot as plt


def sample1():
    # 一定要建立一個物件，這物件就是包含所有的node跟edge
    G = nx.random_graphs.barabasi_albert_graph(100,1)
    # nx.draw(G)
    nx.draw_random(G)
    # nx.draw_circular(G)
    # nx.draw_spectral(G)
    plt.savefig("test.png")
    plt.show()

def sample2():
    G = nx.Graph()
    G.add_node("test")
    G.add_nodes_from([2, 3])
    G.add_nodes_from([2, 4])
    # 就是用來畫點的
    nx.draw(G)
    plt.show()

def sample3():
    G = nx.Graph()
    # 增加一個連線點
    G.add_edge(3, 1)
    # 增加第二個連線點
    e = (2, 4)
    G.add_edge(*e)
    # 就是用來畫點的
    nx.draw(G)
    plt.show()

def sample4():
    G = nx.Graph()

    G.add_edge(1, 2)
    e = (2, 3)
    G.add_edge(*e)
    G.add_edges_from([(1, 2), (2, 3)])

    # 計算node數
    print(G.number_of_nodes())
    # 計算邊緣數
    print(G.number_of_edges())

    nx.draw(G)
    plt.show()

def sample5():
    # 修改顏色
    G = nx.Graph()
    G.add_node(2)
    G.add_edge(1, 3)
    pos = nx.spring_layout(G)
    nx.draw(G)
    nx.draw_networkx_edges(G,pos,edgelist=[(1,3)], edge_color='b')
    plt.show()

def sample6():

    G = nx.cubical_graph()
    pos = nx.spring_layout(G)  # positions for all nodes

    # nodes
    # nx.draw_networkx_nodes(G, pos,
    #                        nodelist=[0, 1, 2, 3],
    #                        node_color='r',
    #                        node_size=500,
    #                        alpha=0.8)
    # nx.draw_networkx_nodes(G, pos,
    #                        nodelist=[4, 5, 6, 7],
    #                        node_color='b',
    #                        node_size=500,
    #                        alpha=0.8)

    # edges
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
    nx.draw_networkx_edges(G, pos,
                           edgelist=[(0, 1), (1, 2), (2, 3), (3, 0)],
                           width=8, alpha=0.5, edge_color='r')
    nx.draw_networkx_edges(G, pos,
                           edgelist=[(4, 5), (5, 6), (6, 7), (7, 4)],
                           width=8, alpha=0.5, edge_color='b')
    
    # some math labels
    labels = {}
    labels[0] = r'$a$'
    labels[1] = r'$b$'
    labels[2] = r'$c$'
    labels[3] = r'$d$'
    labels[4] = r'$\alpha$'
    labels[5] = r'$\beta$'
    labels[6] = r'$\gamma$'
    labels[7] = r'$\delta$'
    nx.draw_networkx_labels(G, pos, labels, font_size=16)

    plt.axis('off')
    plt.axis('on')
    plt.savefig("labels_and_colors.png")  # save as png
    plt.show()  # display

if __name__ =="__main__":
    sample6()