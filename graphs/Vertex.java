package graphs;

import java.util.Map;
import java.util.HashMap;
import java.util.Set;
import java.util.List;
import java.util.ArrayList;

public class Vertex {

    String key;
    Map<String,Integer> edges = new HashMap(); 
    List<Vertex> incomingEdges = new ArrayList(); 
    int totalEdges = 0;
    int distance;
    String color = "white";
    Vertex predecessor;
    

    public Vertex(String key) {
        this.key = key;
    }
    public String getKey() {
	return this.key;
    }
    public void addNeighbor(String key, int weight) {
	this.edges.put(key,weight);
	totalEdges++;
    }
    public Set<String> getNeighbors() {
	return this.edges.keySet();  //returns set of Keys
    }
    public Integer getCost(String neighbor) {
	return this.edges.get(neighbor);
    }
    public int getDistance() {
	return this.distance;
    }
    public String getColor() {
	return this.color;
    }
    public Vertex getPredecessor() {
	return this.predecessor;
    }
    public void setDistance(int distance) {
	this.distance = distance;
    }
    public void setColor(String color) {
	this.color = color;
    }
    public void setPredecessor(Vertex pred) {
	this.predecessor = pred;
    }
    public void addIncomingEdge(Vertex v) {
	this.incomingEdges.add(v);
    }
    public void removeIncomingEdge(Vertex v) {
	this.incomingEdges.remove(v);
    }
    public List<Vertex> getIncomingEdges() {
	return this.incomingEdges;
    }

}
