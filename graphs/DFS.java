package graphs;

import java.util.List;
import java.util.ArrayList;
import java.util.Queue;
import java.util.Stack;
import java.util.LinkedList;
import java.util.Set;

public class DFS {

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
	//visitDFSRecursive(g1,v1);
	System.out.println("---------------");
	visitDFSIterative(g1,v1);

    }

    /*
     * Find Vertex in Graph with Value val
     */
    public static Vertex DFS(Graph G, Vertex start, String val) {
	if (start.getKey().equals(val)) {
	    return start;
	} else {
	    Set<String> edges = start.getNeighbors();
	    for (String edge: edges) {
		Vertex v = DFS(G, G.getVertex(edge), val);
		if (v != null) {
		    return v;
		}
	    }
	}
	return null;
    }

    /*
     * Visit + Print all Vertices in Graph G - Recursive
     */
    public static void visitDFSRecursive(Graph G, Vertex start) {
	System.out.println(start.getKey());
	start.setColor("gray");
	Set<String> edges = start.getNeighbors();
	for (String edge: edges) {
	    Vertex v = G.getVertex(edge);
	    if (v.getColor() == "white") {
		visitDFSRecursive(G, v);
	    }
	}
    }

    /*
     * Visit + Print all Vertices in Graph G - Iterative
     */
    public static void visitDFSIterative(Graph G, Vertex start) {
	Stack<Vertex> stack = new Stack();
	stack.push(start);
	while (stack.size() > 0) {
	    Vertex cur = stack.pop();
	    if (cur.getColor() == "white") {
		System.out.println(cur.getKey());
		cur.setColor("gray");
		Set<String> edges = cur.getNeighbors();
		for (String edge: edges) {
		    Vertex v = G.getVertex(edge);
		    stack.push(v);
		}
	    }
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
