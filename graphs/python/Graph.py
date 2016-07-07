from Vertex import Vertex

class Graph(object):
    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        vertex = Vertex(key)
        self.vertices[vertex.id] = vertex
        self.num_vertices+=1
        return vertex

    def get_vertex(self, key):
        return self.vertices.get(key) #returns None if not found
    
    def add_edge(self, fro, to, weight):
        if fro not in self.vertices:
            nv = self.add_vertex(fro)
        if to not in self.vertices:
            nv = self.add_vertex(to)
        fv = self.get_vertex(fro)
        fv.add_neighbor(to, weight)

    def get_keys(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())

    def __contains__(self, n):
        return n in self.vertices


if __name__ == "__main__":
    g = Graph()
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")

    g.add_edge("A","B",5)
    g.add_edge("A","C",10)
    g.add_edge("B","A",2)
    g.add_edge("A","F",20)
    g.add_edge("J","K",99)

    print g.vertices
    assert len(g.get_keys()) == 6
    assert g.num_vertices == 6
    assert g.get_vertex("A").id == "A"
