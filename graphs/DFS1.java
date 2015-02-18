package graphs;

import java.util.List;
import java.util.ArrayList;
import java.util.Queue;
import java.util.Stack;
import java.util.LinkedList;
import java.util.Set;
import java.util.Stack;

public class DFS1 {

    public static void main(String[] args) {
	Graph g1 = new Graph();
	Vertex v1 = g1.addVertex("A");
	Vertex v2 = g1.addVertex("B");
	Vertex v3 = g1.addVertex("C");
	Vertex v4 = g1.addVertex("D");
	Vertex v5 = g1.addVertex("E");

	g1.addEdge(v1.getKey(),v2.getKey(),2);
	g1.addEdge(v1.getKey(),v3.getKey(),2);
	g1.addEdge(v2.getKey(),v3.getKey(),2);
	g1.addEdge(v2.getKey(),v4.getKey(),2);
	g1.addEdge(v3.getKey(),v4.getKey(),2);
	g1.addEdge(v4.getKey(),v5.getKey(),2);
	printGraph(g1);

	Vertex ans = DFS(g1,v1,"E");
	System.out.println(ans.getKey().equals("E"));
	System.out.println("---------------");

    }

    /*
     * Find Vertex in Graph with Value val
     */
    public static Vertex DFS(Graph G, Vertex v, String target) {
	if (v.getKey() == target) {
	    return v;
	} else {
	    Set<String> friends = v.getNeighbors();
	    for (String friend : friends) {
		Vertex friendVertex = G.getVertex(friend);
		return DFS(G,friendVertex,target);
	    }
	    return null;
	}
    }

    /*
     * Find Vertex in Graph with Value val
     */
    public static Vertex DFS(Graph G, Vertex v, String target) {
	if (v.getKey() == target) {
	    return v;
	} else {
	    Set<String> friends = v.getNeighbors();
	    for (String friend : friends) {
		Vertex friendVertex = G.getVertex(friend);
		return DFS(G,friendVertex,target);
	    }
	    return null;
	}
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
