import plotly.plotly as py
from plotly.graph_objs import *

import networkx as nx
import numpy as np
import plotly
plotly.tools.set_credentials_file(username='moveurbody', api_key='GVYrJPREM9I2vzNcqSkF')

plotly.tools.set_config_file(world_readable=False,
                             sharing='private')



# coding: utf-8

# In[1]:

import networkx as nx
import plotly.plotly as py
from plotly.graph_objs import *
import matplotlib.pyplot as plt


def test1():

    G=nx.random_geometric_graph(200,0.125)


    # In[3]:

    # add the edges in as disconnected lines in a single trace
    edge_trace = Scatter(x=[], y=[], mode='lines')
    for edge in G.edges():
        x0, y0 = G.node[edge[0]]['pos']
        x1, y1 = G.node[edge[1]]['pos']
        edge_trace['x'] += [x0, x1, None]
        edge_trace['y'] += [y0, y1, None]

    # add the nodes in as a scatter
    node_trace = Scatter(x=[], y=[], mode='markers', marker=Marker(size=[]))
    for node in G.nodes():
        x, y = G.node[node]['pos']
        node_trace['x'].append(x)
        node_trace['y'].append(y)

    # size the node points by the number of connections
    for node, adjacencies in enumerate(G.adjacency_list()):
        node_trace['marker']['size'].append(len(adjacencies))


    # In[4]:

    # create a figure so we can customize a couple more things
    fig = Figure(data=Data([edge_trace, node_trace]),
                 layout=Layout(title='random geometric graph from networkx', plot_bgcolor="rgb(217, 217, 217)",
                               showlegend=False, xaxis=XAxis(showgrid=False, zeroline=False, showticklabels=False),
                               yaxis=YAxis(showgrid=False, zeroline=False, showticklabels=False)))

    # send the figure to Plotly and embed an iframe in this notebook
    plotly.offline.plot(fig)
    # py.iplot(fig, filename='networkx')

def test2():
    import networkx as nx
    import random
    import pylab as py
    from math import floor

    G = nx.complete_graph(20)

    for edge in G.edges():
        if floor(edge[0] / 5.) != floor(edge[1] / 5.):
            if random.random() < 0.95:
                G.remove_edge(edge[0], edge[1])

    nx.draw_spring(G)
    py.show()

    fixedpos = {1: (0, 0), 6: (1, 1), 11: (1, 0), 16: (0, 1)}
    pos = nx.spring_layout(G, fixed=fixedpos.keys(), pos=fixedpos)

    nx.draw_networkx(G, pos=pos)

    py.show()

def test3():
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3)])
    G.add_node("spam")  # adds node "spam"
    nx.connected_components(G)
    sorted(nx.degree(G).values())
    nx.clustering(G)
    nx.degree(G)
    nx.degree(G, 1)
    nx.degree(G, 1)
    G.degree([1, 2])
    sorted(G.degree([1, 2]).values())
    sorted(G.degree().values())
    nx.draw(G)
    plt.show()

def test4():
    # 一定要建立一個物件，這物件就是包含所有的node跟edge
    G = nx.random_graphs.binomial_graph(100,10)
    labels={}
    for i in range(0,100):
        labels[i]=i

    POS = nx.spectral_layout(G)
    res = nx.number_of_cliques(G)
    nx.draw(G, POS)
    group=[]
    for i in res:
        group.append(res[i])
        print(i,res[i])

    max_group=max(group)
    for group_num in range(1,max_group+1):
        group_list=[]
        for i in res:
            if res[i]==group_num:
                group_list.append(i)
        if group_num!=1:
            nx.draw_networkx_nodes(G,pos=POS,nodelist=group_list,node_color='b')
        else:
            nx.draw_networkx_nodes(G, pos=POS, nodelist=group_list, node_color='r')

    nx.draw_networkx_labels(G,POS,labels)
    # nx.draw_circular(G)
    # nx.draw_spectral(G)
    plt.show()

def test5():
    # 從csv中讀檔
    # csv = np.genfromtxt('SNA.csv', delimiter=',')
    csv = np.genfromtxt('data/combine_relation.csv', delimiter=',')
    # 將CSV的資料放入matrix
    matrix = np.asmatrix(csv)

    print(matrix)
    # 轉致matrix，就是one_mode
    one_mode = matrix
    print(one_mode)

    print(one_mode[1, 1])

    # 取得多少node
    matrix_len = len(matrix)
    print(matrix_len)

    G = nx.from_numpy_matrix(one_mode)
    pos = nx.spring_layout(G)

    # criema 306
    nodelist_1 = []
    # sewol 188
    nodelist_2 = []
    # hk 268
    nodelist_3 = []
    for node in range(0, 306):
        nodelist_1.append(node)

    nx.draw_networkx_nodes(G, pos, nodelist=nodelist_1, node_color='r', node_size=300, alpha=0.8)

    for node in range(306, 494):
        nodelist_2.append(node)

    nx.draw_networkx_nodes(G, pos, nodelist=nodelist_2, node_color='g', node_size=300, alpha=0.8)

    for node in range(494, 762):
        nodelist_3.append(node)

    nx.draw_networkx_nodes(G, pos, nodelist=nodelist_3, node_color='b', node_size=300, alpha=0.8)

    # 增加node的名稱
    labels = {}
    for label in range(0, matrix_len):
        labels[label] = "%s" % (label)

    # # 將node的名稱標出來
    nx.draw_networkx_labels(G,pos,labels=labels,font_size=8)
    #
    # print(nx.info(G))
    #
    # # nx.draw(G)
    #
    # # 將edges畫出來
    nx.draw_networkx_edges(G,pos,width=1.0,alpha=0.8,edge_color='k')

    # # 將中心度列出來
    # print('\nbetweenness')
    # print(nx.betweenness_centrality(G))

    # # 將G的資料列出來
    # print('\ninfo G')
    # print(nx.info(G))

    # 將各edges列出來
    print('\nedge G')
    print(nx.edges(G))

    # 將matplotlib的座標關閉
    plt.axis('off')
    # 存檔
    # plt.savefig("picture_sna_room.png")

    # print(nx.number_of_cliques(G))
    plt.show()

if __name__=="__main__":
    test5()