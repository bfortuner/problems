package graphs;

import java.util.Map;
import java.util.HashMap;
import java.util.Set;
import java.util.List;
import java.util.ArrayList;
import java.util.Collection;


public class Graph {

    Map<String,Vertex> vertices = new HashMap(); 
    int numVertices = 0;


    public static void main(String[] args) {
	Graph g1 = new Graph();
	Vertex v1 = g1.addVertex("A");
	Vertex v2 = g1.addVertex("B");
	Vertex v3 = g1.addVertex("C");
	Vertex v4 = g1.addVertex("D");

	g1.addEdge(v1.getKey(),v2.getKey(),9);
	g1.addEdge(v1.getKey(),v3.getKey(),2);
	printGraph(g1);
	System.out.println(v3.getIncomingEdges().size() == 1);
	v3.removeIncomingEdge(v1);
	System.out.println(v3.getIncomingEdges().size() == 0);
	
    }

    public Vertex addVertex(String key) {
	Vertex newVertex = new Vertex(key);
	vertices.put(key, newVertex);
	numVertices++;
	return newVertex;
    }

    public Vertex getVertex(String key) {
	return vertices.get(key);
    }
    
    public Set<String> getVertices() {
	return vertices.keySet();
    }

    public Collection<Vertex> getVerticesVals() {
	return vertices.values();
    }

    public void addEdge(String from, String to, int cost) {
	if (!vertices.containsKey(to)) {
	    addVertex(to);
	}
	Vertex toVertex = getVertex(to);
	Vertex fro = vertices.get(from);
	fro.addNeighbor(to, cost);
	toVertex.addIncomingEdge(fro);
    } 

    public static void printGraph(Graph g) {
	Set<String> vertices = g.getVertices();
	for ( String vertex : vertices ) {
	    System.out.print(vertex + " --> [ ");
	    Vertex v = g.getVertex(vertex);
	    for ( String neighbor : v.getNeighbors() ) {
		System.out.print("(" + neighbor + "," + v.getCost(neighbor) + ") ");
	    }
	    System.out.println("]\n");
	}
    }

}
