# -*- coding: utf-8 -*-
# @Time    : 2017/5/11 下午5:09
# @Author  : Yuhsuan
# @File    : matrix.py
# @Software: PyCharm Community Edition

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# 從csv中讀檔
csv = np.genfromtxt('data/SNA.csv', delimiter=',')
# 將CSV的資料放入matrix
matrix = np.asmatrix(csv)
# 轉致matrix，就是one_mode
matrix_t = matrix.T

# print(matrix)
# print(matrix_t)
# 算出matrix乘績
one_mode = np.dot(matrix,matrix_t)
print(one_mode)

print(one_mode[1,1])

# 取得多少node
matrix_len = len(matrix)
print(matrix_len)

G = nx.from_numpy_matrix(one_mode)
pos=nx.spring_layout(G)

# 增加node
nodelist = []
for node in range(0,matrix_len):
    nodelist.append(node)

# 增加node的名稱
labels = {}
for label in range(0,matrix_len):
    labels[label] = "%s" %(label)

# 將node標出來
nx.draw_networkx_nodes(G,pos,nodelist=nodelist,node_color='r',node_size=500,alpha=0.8)

# 將node的名稱標出來
nx.draw_networkx_labels(G,pos,labels=labels,font_size=8)

# 將edges畫出來
nx.draw_networkx_edges(G,pos,width=1.0,alpha=0.5,edge_color='k')

# 將所有的資訊列出來
print(nx.info(G))

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
# 存檔
plt.savefig("pictures/Matrix_Output.png")

plt.show()