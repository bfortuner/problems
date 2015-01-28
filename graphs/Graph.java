package graphs;

import java.util.Map;
import java.util.HashMap;
import java.util.Set;
import java.util.List;
import java.util.ArrayList;


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

    public void addEdge(String from, String to, int cost) {
	if (!vertices.containsKey(to)) {
	    addVertex(to);
	}
	Vertex fro = vertices.get(from);
	fro.addNeighbor(to, cost);
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
