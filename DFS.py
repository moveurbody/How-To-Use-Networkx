import networkx as nx

G = nx.Graph()
G.add_edges_from([(1, 5), (1, 2), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5), (5, 3)])
stack = [1]  # Start from node1
visit_list = []

while len(stack) > 0:
    # nonlocal visit_list
    # nonlocal stack
    vnode = stack.pop()
    if vnode not in visit_list:
        print("\t[Info] Visit {0}...".format(vnode))
        visit_list.append(vnode)
    nbs = G.neighbors(vnode)
    for nb in nbs:
        if nb not in visit_list:
            print("\t[Info] Put {0} in stack...".format(nb))
            stack.append(nb)
    print("\tStack list={0}".format(stack))
    print("\tVisit list={0}".format(visit_list))
    if len(visit_list) == len(G.nodes()): break

print("\t[Info] Deep First Search has {0}".format(visit_list))