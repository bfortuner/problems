package arrays;

import java.util.*;

public class IntersectionTwoArrays {
    
    public static void main(String[] args) {
	IntersectionTwoArrays two = new IntersectionTwoArrays();
	int[] a1 = {1,2,4,7,9};
	int[] a2 = {0,1,3,5,7};
	Integer[] answer = {1,7};
	Integer[] b1 = two.getIntersection1(a1,a2);
	System.out.println(Arrays.equals(answer,b1));
	Integer[] b2 = two.getIntersection1(a1,a2);
	System.out.println(Arrays.equals(answer,b2));
	Integer[] b3 = two.getIntersection1(a1,a2);
	System.out.println(Arrays.equals(answer,b3));
    }


    /*
     * Naive - O(n^2)
     */
    public Integer[] getIntersection1(int[] a1, int[] a2) {
	List<Integer> list = new ArrayList();
	for (int i=0; i<a1.length; i++) {
	    for (int j=0; j<a2.length; j++) {
		if (a1[i] == a2[j] && !list.contains(a1[i])) {
		    list.add(a1[i]);
		}
	    }
	}
	Integer[] arr = list.toArray(new Integer[list.size()]);	
	return arr;
    }
    /*
     * Linear Search - O(n + m)
     */
    public Integer[] getIntersection2(int[] a1, int[] a2) {
	List<Integer> list = new ArrayList();
	int i=0;
	int j=0;
	while (i<a1.length && j<a2.length) {
	    if (a1[i] == a2[j]) {
		if (!list.contains(a1[i])) {
		    list.add(a1[i]);
		}
		i++;
		j++;
	    } else if (a1[i] < a2[j]) {
		i++;
	    } else {
		j++;
	    }	    
	}
	Integer[] arr = list.toArray(new Integer[list.size()]);	
	return arr;
    }


    /*
     * Hash Map - O(n + m) Time, O(n) Space
     */
    public Integer[] getIntersection3(int[] a1, int[] a2) {
	List<Integer> list = new ArrayList();
	Map<Integer,Integer> map = new HashMap();
	for (int i=0; i<a1.length; i++) {
	    map.put(a1[i],a1[i]);
	}
	for (int j=0; j<a2.length; j++) {
	    if (map.containsKey(a2[j])) {
		list.add(a2[j]);
	    }
	}
	Integer[] arr = list.toArray(new Integer[list.size()]);	
	return arr;
    }

}
