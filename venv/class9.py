import mysql.connector
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

def createAdjMatrix(V, G):
    adjMatrix = []
    for i in range(0, V):
        adjMatrix.append([])
        for j in range(0, V):
            adjMatrix[i].append(0)
    for i in range(0, len(G)):
        adjMatrix[G[i][0]][G[i][1]] = G[i][2]
        adjMatrix[G[i][1]][G[i][0]] = G[i][2]
    return adjMatrix

def minDistance(dist, sptSet):
    min = float('inf')
    V = 5
    for v in range(V):
        if dist[v] < min and sptSet[v] == False:
            min = dist[v]
            min_index = v
    return min_index

def dijkstra(vertices,src,graph):
    dist = [float('inf')] * vertices
    dist[src] = 0
    sptSet = [False] * vertices
    V = 5
    s = []
    t = []

    for cout in range(vertices):
        u = minDistance(dist, sptSet)
        sptSet[u] = True

        for v in range(vertices):
            if graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]
                s.append([u,v,dist[v]])
    return s

def fetchAllVertices():
    sql = "select * from dijikstra"
    con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="daa")
    cursor = con.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    # list=[]
    row = []
    for i in range(len(rows)):
        row.append(rows[i])
    dict = {"Basant Avenue": 0, "Janta Enclave": 1, "Dhandra Road": 2, "Gill Chownk": 3, "GNE College": 4}
    df1 = pd.DataFrame(row, columns=['Source Node', 'Destination Node', 'Weight'])
    print("Before Applying Dijikstra's  Algorithm :")
    print(df1)

    plt.figure(figsize=(8, 5))
    edgeLables = {}
    for i in range(0, len(row)):
        key = (row[i][0], row[i][1])
        value = row[i][2]
        edgeLables[key] = value

    spanningTree = nx.from_pandas_edgelist(df1, source='Source Node', target='Destination Node', edge_attr=True)
    pos = nx.circular_layout(spanningTree)
    nx.draw(spanningTree, pos, with_labels=True)
    nx.draw_networkx_edge_labels(spanningTree, pos, edge_labels=edgeLables)

    plt.show()
    list = []
    for i in range(len(row)):
        innerList = []
        innerList.append(dict[row[i][0]])
        innerList.append(dict[row[i][1]])
        innerList.append(row[i][2])
        list.append(innerList)
    return list

print("Ishpreet Kaur Gulati")
print("1706443")
print("CSE A2")
G = fetchAllVertices()

a = createAdjMatrix(5,G)
d = dijkstra(5,3,a)
#print(d)
dict={0:"Basant Avenue",1: "Janta Enclave" ,2: "Dhandra Road",3:"Gill Chownk",4:"GNE College"}
list=[]
for i in range (len(d)):
    innerList=[]
    innerList.append(dict[d[i][0]])
    innerList.append(dict[d[i][1]])
    innerList.append(d[i][2])
    list.append(innerList)

minLables={}
totalWeight=0
for i in range(0,len(list)):
    key=(list[i][0],list[i][1])
    value=list[i][2]
    totalWeight+=list[i][2]
    minLables[key] = value
df2 = pd.DataFrame(list, columns = ['Source Node', 'Destination Node','Weight'])
print("\nAfter Applying dijikstra Algorithm :")
print(df2)
print("Total Weight : ",totalWeight)
Dgraph = nx.from_pandas_edgelist(df2, source='Source Node', target='Destination Node', edge_attr=True)
pos = nx.planar_layout(Dgraph)
nx.draw(Dgraph,pos,with_labels=True)
nx.draw_networkx_edge_labels(Dgraph,pos,edge_labels=minLables)
plt.show()

