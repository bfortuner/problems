package graphs;

import java.util.List;
import java.util.ArrayList;
import java.util.Queue;
import java.util.Stack;
import java.util.LinkedList;
import java.util.Set;
import java.util.Map;
import java.util.HashMap;
import java.util.Collection;


public class TopologicalSort {

    public static void main(String[] args) {
	Graph g1 = new Graph();
	Vertex v1 = g1.addVertex("A");
	Vertex v2 = g1.addVertex("B");
	Vertex v3 = g1.addVertex("C");
	Vertex v4 = g1.addVertex("D");
	Vertex v5 = g1.addVertex("E");
	Vertex v6 = g1.addVertex("F");
	Vertex v7 = g1.addVertex("G");
	Vertex v8 = g1.addVertex("H");
	Vertex v9 = g1.addVertex("I");

	g1.addEdge(v1.getKey(),v2.getKey(),2);
	g1.addEdge(v1.getKey(),v3.getKey(),2);
	g1.addEdge(v2.getKey(),v3.getKey(),2);
	g1.addEdge(v2.getKey(),v4.getKey(),2);
	g1.addEdge(v3.getKey(),v4.getKey(),2);
	g1.addEdge(v4.getKey(),v5.getKey(),2);
	g1.addEdge(v9.getKey(),v1.getKey(),2);
	g1.addEdge(v8.getKey(),v1.getKey(),2);
	g1.addEdge(v6.getKey(),v5.getKey(),2);
	g1.addEdge(v4.getKey(),v6.getKey(),2);
	g1.addEdge(v1.getKey(),v7.getKey(),2);
	printGraph(g1);

	System.out.println("---------------");
	List<Vertex> ans = sortIterative(g1);
	for (Vertex ver1 : ans) {
	    System.out.println(ver1.getKey());
	}
	System.out.println("---------------");
	List<Vertex> ans1 = sortRecursive(g1);
	for (Vertex ver2 : ans1) {
	    System.out.println(ver2.getKey());
	}
	System.out.println("---------------");

	List<Vertex> roots = getRootVertices(g1);
	System.out.println(roots.contains(v8) == true);
	System.out.println(roots.contains(v9) == true);
	System.out.println(roots.contains(v1) == false);
	System.out.println("---------------");

    }

    /*
     * Return List of sorted Vertices given Graph G - Iterative
     * Must be directed acyclic graph with no cycles 
     * (i.e. must have at least 1 vertex with no incoming edges)
     */
    public static List<Vertex> sortIterative(Graph G) {
	List<Vertex> sortedList = new ArrayList();
	List<Vertex> L = getRootVertices(G);
	while(L.size() > 0) {
	    Vertex cur = L.get(0);
	    sortedList.add(cur);
	    L.remove(cur);
	    for (String outgoingEdge : cur.getNeighbors()) {
		Vertex out = G.getVertex(outgoingEdge);
		out.removeIncomingEdge(cur);
		if (out.getIncomingEdges().size() == 0) {
		    L.add(out);
		}
	    }
	}

	return sortedList;
    }

    /*
     * Return List of sorted Vertices given Graph G - Recursive
     */
    public static List<Vertex> sortRecursive(Graph G) {
	List<Vertex> L = new ArrayList();
	return L;
    }

    public static List<Vertex> getRootVertices(Graph G) {
	Collection<Vertex> vertices = G.getVerticesVals();
	Map<String,String> edges = new HashMap(); //<To, From>
	List<Vertex> roots = new ArrayList();
	for (Vertex v : vertices) {
	    Set<String> neighbors = v.getNeighbors();
	    for (String n : neighbors) {
		edges.put(n,v.getKey()); //to, from
	    }
	}
	for (Vertex v: vertices) {
	    if ( !edges.containsKey(v.getKey()) ) {
		roots.add(v);
	    }
	}
	return roots;
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
