class Graph(object):

    def __init__(self, graph_dict=None):

        if graph_dict == None:
            graph_dict = {}
        self.graph_dict = graph_dict

    @staticmethod
    def add_vertex(self, vertex):
        if vertex not in self.graph_dict.keys():
            self.graph_dict[vertex] = []

    def remove_vertex(self, vertex):
        if vertex in self.graph_dict.keys():
            del self.graph_dict[vertex]

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph_dict.keys() and vertex2 in self.graph_dict.keys():
            if vertex1 not in self.graph_dict[vertex2] and vertex2 not in self.graph_dict[vertex1]:
                self.graph_dict[vertex1].append(vertex2)
                self.graph_dict[vertex2].append(vertex1)

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph_dict[vertex2] and vertex2 in self.graph_dict[vertex1]:
            self.graph_dict[vertex1].remove(vertex2)
            self.graph_dict[vertex2].remove(vertex1)

    def get_neighbours(self, vertex):
        if vertex in self.graph_dict.keys():
            return self.graph_dict[vertex]
