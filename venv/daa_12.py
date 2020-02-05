from graphviz import Digraph
import numpy as np

print("Jasmanjot Singh- 1706448")
INF = float('Inf')
graph = [
    [0,   5,  INF, 10],
    [INF,  0,  3,  INF],
    [INF, INF, 0,   1],
    [INF, INF, INF, 0]
]
def floyd_warshall(graph):
    V = len(graph)
    cost = np.array(graph)
    for k in range(V):
        for i in range(V):
            for j in range(V):
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
    
    return cost
cost = floyd_warshall(graph)
print ("Shortest distance cost matrix:-")
print (cost)
dot = Digraph()
for i,item in enumerate(graph):
    for j in range(i,len(item)):
        if item[j] != INF:
            dot.edge(str(i),str(j),label=str(graph[i][j]))

dot.render('floyd_warshall')
#
# dot_path = Digraph()
# for i in range(1,len(path)):
#     dot_path.edge(str(path[i-1]), str(path[i]))
# dot_path.render('floyd_warshall_Path')