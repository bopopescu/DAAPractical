from collections import defaultdict
import mysql.connector
import networkx as nx
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

class Graph:

    def __init__(self, vertices):
        self. v = vertices
        self. ListVertices = []

    def AddEdge(self,rows):

        for row in rows:
            rm1 = [row[0], row[1], row[2]]
            self.ListVertices.append(rm1)
        return(self.ListVertices)

    def printArr(self, dist):
        print("Vertex   Distance from Source")
        for i in range(self.v):
            print("% d \t\t % d" % (i, dist[i]))

    def BellmanAndFord(self, src):

        dist = [float('inf')] * self.v

        dist[src] = 0
        s = []
        for i in range(0,self.v-1):

            for u,v,w in self.ListVertices:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    s.append([u,v,dist[v]])
        for u, v, w in self.ListVertices:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                print("Graph Contain a Negative Cycle")
        return s
        #self.printArr(dist)
print("Malika Jain \n1706465\n")

g = Graph(5)
sql = "select * from bellmanford"
con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="daa")
cursor = con.cursor()
cursor.execute(sql)
rows = cursor.fetchall()
row=[]
for i in range(len(rows)):
    row.append(list(rows[i]))

dict={"Basant Avenue":0, "Janta Enclave":1 , "Dhandra Road":2,"Gill Chownk":3,"GNE College":4}
list=[]
for i in range (len(row)):
    innerList=[]
    innerList.append(dict[row[i][0]])
    innerList.append(dict[row[i][1]])
    innerList.append(row[i][2])
    list.append(innerList)
g.AddEdge(list)

df1 = pd.DataFrame(row, columns = ['Source Node', 'Destination Node','Weight'])
print("Before Applying BellmanFord Algorithm :")
print(df1)


plt.figure(figsize=(8,5))
edgeLables={}
for i in range(0,len(row)):
    key=(row[i][0],row[i][1])
    value=row[i][2]
    edgeLables[key]=value


spanningTree = nx.from_pandas_edgelist(df1, source='Source Node', target='Destination Node', edge_attr=True)
pos = nx.circular_layout(spanningTree)
nx.draw(spanningTree,pos,with_labels=True)
nx.draw_networkx_edge_labels(spanningTree,pos,edge_labels=edgeLables)

plt.show()
dict={0:"Basant Avenue",1: "Janta Enclave" ,2: "Dhandra Road",3:"Gill Chownk",4:"GNE College"}

d = g.BellmanAndFord(0)
list=[]
for i in range (len(d)):
    innerList=[]
    innerList.append(dict[d[i][0]])
    innerList.append(dict[d[i][1]])
    innerList.append(d[i][2])
    list.append(innerList)
minLables={}
totalWeight=0
for i in range(0,len(d)):
    key=(list[i][0],list[i][1])
    value=list[i][2]
    #print(value)
    totalWeight+=list[i][2]
    minLables[key] = value

#print(minLables)
df2 = pd.DataFrame(list, columns = ['Source Node', 'Destination Node','Weight'])
print("\nAfter Applying Bellman Ford Algorithm :")
print(df2)
print("Total Weight : ",totalWeight)
Dgraph = nx.from_pandas_edgelist(df2, source='Source Node', target='Destination Node', edge_attr=True)
# pos = nx.circular_layout(Dgraph)
nx.draw(Dgraph,pos,with_labels=True)
nx.draw_networkx_edge_labels(Dgraph,pos,edge_labels=minLables)
plt.show()