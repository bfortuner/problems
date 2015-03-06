package sorting;

import java.util.*;

public class SortArray012 {

    public static void main(String[] args) {
	SortArray012 arr = new SortArray012();
	List<Integer> l1 = new ArrayList();
	l1.add(2);
	l1.add(0);
	l1.add(2);
	l1.add(0);
	l1.add(1);
	
	arr.sortList(l1);
	for (int i : l1) {
	    System.out.print(i + " ");
	}
	System.out.println();
	int[] a1 = {1,0,2,1,0,2,1};
	arr.sortArray(a1);
	for (int i : a1) {
	    System.out.print(i + " ");
	}
	System.out.println();
    }

    public void sortList(List<Integer> list) {
	int elemCount = list.size();
	int listPos = 0;
	while (elemCount > 0) {
	    int elem = list.get(listPos);
	    if (elem == 0) {
		list.remove(listPos);
		list.add(0,0);
		listPos++;
	    } else if (elem == 2) {
		list.remove(listPos);
		list.add(2);
	    } else {
		listPos++;
	    }
	    elemCount--;
	}
    };

    public void sortArray(int[] arr) {
	int[] buckets = new int[3]; //0,0,0
	for (int i=0; i<arr.length; i++) {
	    buckets[arr[i]]++;
	}
	int pos = 0;
	for (int i=0; i<3; i++) {
	    while (buckets[i] > 0) {
		arr[pos] = i;
		pos++;
		buckets[i]--;
	    }
	}
    };

}
