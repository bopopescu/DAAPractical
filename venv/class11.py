from graphviz import Digraph

print("Jasmanjot Singh- 1706448")


inf = float('Inf')
graph = [
    [inf,1,2,5,inf,inf,inf,inf],
    [inf,inf,inf,inf,4,11,inf,inf],
    [inf,inf,inf,inf,9,5,16,inf],
    [inf,inf,inf,inf,inf,inf,2,inf],
    [inf,inf,inf,inf,inf,inf,inf,18],
    [inf,inf,inf,inf,inf,inf,inf,13],
    [inf,inf,inf,inf,inf,inf,inf,2],
    [inf,inf,inf,inf,inf,inf,inf,inf]
]

def multi_stage_graph(graph, source, dest):
    cost = [float('Inf')] * len(graph)
    path = [[] for i in range(len(graph))]
    cost[source] = 0
    path[source] = [source]
    for i in range(len(graph)):
        for j in range(i):
            if graph[j][i] == float('Inf'):
                continue
            if cost[i] > graph[j][i] + cost[j]:
                path[i] = path[j] + [i]
                cost[i] = graph[j][i] + cost[j]
    return cost[dest],path[dest]

cost,path = multi_stage_graph(graph,0,7)

print (('Minimum Cost:'),cost)
print(( 'Shortest path to follow:'),path)

dot = Digraph()
for i,item in enumerate(graph):
    for j in range(i,len(item)):
        if item[j] != inf:
            dot.edge(str(i),str(j),label=str(graph[i][j]))

dot.render('multi_graph')

dot_path = Digraph()
for i in range(1,len(path)):
    dot_path.edge(str(path[i-1]), str(path[i]))
dot_path.render('Path')
