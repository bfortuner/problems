package graphs;

import java.util.Map;
import java.util.HashMap;
import java.util.Set;

public class Vertex {

    String key;
    Map<String,Integer> edges = new HashMap(); 
    int totalEdges = 0;

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
}
