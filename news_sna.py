# -*- coding: utf-8 -*-
# @Time    : 2017/5/14 下午2:07
# @Author  : Yuhsuan
# @File    : news_sna.py
# @Software: PyCharm Community Edition


import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# 從csv中讀檔
# csv = np.genfromtxt('SNA.csv', delimiter=',')
csv = np.genfromtxt('data/combinematrix.csv', delimiter=',')
# 將CSV的資料放入matrix
matrix = np.asmatrix(csv)

print(matrix)
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

# criema 306
nodelist_1=[]
# sewol 188
nodelist_2=[]
# hk 268
nodelist_3=[]
for node in range(0,306):
    nodelist_1.append(node)

nx.draw_networkx_nodes(G,pos,nodelist=nodelist_1,node_color='r',node_size=30,alpha=0.8)

for node in range(306,494):
    nodelist_2.append(node)

nx.draw_networkx_nodes(G,pos,nodelist=nodelist_2,node_color='g',node_size=30,alpha=0.8)

for node in range(494,762):
    nodelist_3.append(node)

nx.draw_networkx_nodes(G,pos,nodelist=nodelist_3,node_color='b',node_size=30,alpha=0.8)

# 增加node的名稱
labels = {}
for label in range(0,matrix_len):
    labels[label] = "%s" %(label)

# # 將node的名稱標出來
# nx.draw_networkx_labels(G,pos,labels=labels,font_size=8)
#
# print(nx.info(G))
#
# # nx.draw(G)
#
# # 將edges畫出來
# nx.draw_networkx_edges(G,pos,width=1.0,alpha=0.5,edge_color='k')

# # 將中心度列出來
# print('\nbetweenness')
# print(nx.betweenness_centrality(G))

# # 將G的資料列出來
# print('\ninfo G')
# print(nx.info(G))

# # 將各edges列出來
# print('\nedge G')
# print(nx.edges(G))

# 將matplotlib的座標關閉
plt.axis('off')
# 存檔
# plt.savefig("picture_sna_room.png")

# print(nx.number_of_cliques(G))
plt.show()