package sorting;

import java.util.*;
import lists.Node;

public class BucketSort {

    public static void main(String[] args) {
        int[] a1 = {1,2,13,9,5,6,10,5};
        sort(a1);
        for (int i : a1) {
            System.out.print(i + "");
        }
	
    }

    public static void sort(int[] arr) {
        Node<Integer>[] buckets = new Node[10];
        double max = getMax(arr);
        double bucketSize = max / buckets.length;
        for (int i=0; i<arr.length; i++) {
            put(arr[i],buckets,bucketSize);
        }
        int i = 0;
        for (int j=0; j<buckets.length; j++) {
            while(buckets[j] != null) {
                arr[i] = buckets[j].getValue();
                buckets[j] = buckets[j].getNext();
                i++;
            }
        }
    };

    public static void put(int val, Node<Integer>[] buckets, double bucketSize) {
        int index = (int) (val / bucketSize);
        index = Math.max(0,index-1);
        Node<Integer> n = new Node(val);
        Node<Integer> cur = buckets[index];
        if (cur == null) {
            buckets[index] = n;
        } else if (val <= cur.getValue()) {
            n.setNext(cur);
            buckets[index] = n;
        } else {
            while (cur.getNext() != null && val > (Integer) cur.getNext().getValue()) {
                cur = cur.getNext();
            }
            n.setNext(cur.getNext());
            cur.setNext(n);
        }
    }

    private static int getMax(int[] arr) {
        int max = arr[0];
        for (int i=0; i<arr.length; i++) {
            max = Math.max(max,arr[i]);
        }
        return max;
    }

}
