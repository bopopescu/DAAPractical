import networkx as nx

class Vertex(object):
    def __init__(self, name, category):
        self.name = name
        self.category = category
    def __hash__(self):
        return hash((self.name, self.category))
    def __eq__(self, other):
        if isinstance(other, Vertex):
            return other.name == self.name and other.category == self.category
    def __str__(self):
        return '{}-{}'.format(self.name, self.category)
    def __repr__(self):
        return str(self)

d = {
    Vertex('A','red') : {Vertex('B','red') : {'weight':1}},
    Vertex('B','red') : {Vertex('C','blu') : {'weight':1}},
    Vertex('C','blu') : {Vertex('D','ylw') : {'weight':1}, Vertex('X','grn') : {'weight':-1}},
    Vertex('D','ylw') : {Vertex('A','red') : {'weight':1}},
    Vertex('X','grn') : {Vertex('D','ylw') : {'weight':-3}},
}
G = nx.DiGraph(d)

pos = nx.circular_layout(G)
nx.draw_networkx(G,pos, arrows=True, with_labels=True)
labels = nx.get_edge_attributes(G,'weight')
print(labels)
nx.draw_networkx_edge_labels(G,pos, edge_labels=labels);