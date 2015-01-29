package graphs;

import java.util.List;
import java.util.ArrayList;
import java.util.Queue;
import java.util.LinkedList;
import java.util.Set;

public class BFS {

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

	Vertex ans = BFS(g1,v1,"E");
	System.out.println(ans.getKey().equals("E"));
	System.out.println(ans.getDistance() == 3);

    }

    public static Vertex BFS(Graph G, Vertex start, String val) {
	Queue<Vertex> queue = new LinkedList<Vertex>();
	start.setDistance(0);
	queue.add(start);
	Vertex curVertex = start;
	while (queue.size() > 0) {
	    curVertex = queue.poll();
	    if (curVertex.getKey() == val) {
		return curVertex;
	    }
	    for (String key : curVertex.getNeighbors()) {
		Vertex tmp = G.getVertex(key);
		if (tmp.getColor() == "white") {
		    tmp.setColor("gray");
		    tmp.setDistance(curVertex.getDistance() + 1);
		    queue.add(tmp);
		}
	    }
	}
	return null;
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
