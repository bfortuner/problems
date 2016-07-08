from Vertex import Vertex

class Graph(object):
    def __init__(self, vertices={}):
        self.vertices = vertices
        self.num_vertices = len(vertices)

    def add_vertex(self, key):
        vertex = Vertex(key)
        self.vertices[vertex.key] = vertex
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

    def __str__(self):
        g = ""
        for v in self.vertices.values():
            g += v.key + ": " + str([n.key for n in v.neighbors]) + "\n"
        return g
            

def build_test_graph():
	"""
	A --> B <->
	^     |    |
	D <-> C -> E
	"""
	v1 = Vertex("A")
	v2 = Vertex("B")
	v3 = Vertex("C")
	v4 = Vertex("D")
	v5 = Vertex("E")

	v1.add_neighbor(v2)
	v2.add_neighbors([v3,v5])
	v3.add_neighbors([v2,v4,v5])
	v4.add_neighbors([v1,v3])
	v5.add_neighbors([v2])
        
	return Graph({"A":v1,"B":v2,"C":v3,"D":v4,"E":v5})

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
    assert g.get_vertex("A").key == "A"

    g2 = build_test_graph()
    print g2.vertices
    print g2.num_vertices
