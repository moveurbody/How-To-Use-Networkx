# -*- coding: utf-8 -*-
# @Time    : 2017/5/11 下午5:09
# @Author  : Yuhsuan
# @File    : matrix.py
# @Software: PyCharm Community Edition

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# 從csv中讀檔
csv = np.genfromtxt('SNA.csv', delimiter=',')
# 將CSV的資料放入matrix
matrix = np.asmatrix(csv)
# 轉致matrix，就是one_mode
matrix_t = matrix.T

print(matrix)
print(matrix_t)
# 算出matrix乘績
one_mode = np.dot(matrix,matrix_t)
print(one_mode)

print(one_mode[1,1])

# 取得多少node
print(len(matrix))

G = nx.from_numpy_matrix(one_mode)
pos=nx.spring_layout(G)

# 增加node
nodelist = []
for node in range(0,len(matrix)):
    nodelist.append(node)

# 增加node的名稱
labels = {}
for label in range(0,len(matrix)):
    labels[label] = "%s" %(label)

print(nx.info(G))

# nx.draw(G)
# 將node標出來
nx.draw_networkx_nodes(G,pos,nodelist=nodelist,node_color='r',node_size=500,alpha=0.8)
# 將node的名稱標出來
nx.draw_networkx_labels(G,pos,labels=labels,font_size=8)
# 將edges畫出來
nx.draw_networkx_edges(G,pos,width=1.0,alpha=0.5,edge_color='b')

# 將中心度列出來
print('\nbetweenness')
print(nx.betweenness_centrality(G))
# 將G的資料列出來
print('\ninfo G')
print(nx.info(G))
# 將各edges列出來
print('\nedge G')
print(nx.edges(G))
# 將matplotlib的座標關閉
plt.axis('off')

plt.show()
