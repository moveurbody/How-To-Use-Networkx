import networkx as nx
import matplotlib.pyplot as plt
import datetime

# https://segmentfault.com/a/1190000000527216#articleHeader0

def write():
    g = nx.Graph()
    g.add_edge(1,2)
    g.add_edge(2,3)
    g.add_edge(3,1)

    print(nx.info(g))
    nx.write_edgelist(g,'sample_data.txt')

def read():
    g = nx.read_edgelist('sample_data.txt',create_using=nx.Graph(),nodetype=int)
    print(nx.info(g))
    nx.draw(g)
    # nx.draw_networkx(g)
    # nx.draw_networkx_nodes(g)
    nx.draw_circular(g)
    plt.show()

try:
    print(datetime.datetime.now())
    write()
    read()
except Exception as e:
    print(e)