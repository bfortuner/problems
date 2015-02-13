package sorting;

import java.util.*;

public class SortArray012 {

    public static void main(String[] args) {

	List<Integer> l1 = new ArrayList();
	l1.add(2);
	l1.add(0);
	l1.add(2);
	l1.add(0);
	l1.add(1);
	
	sort(l1);
	for (int i : l1) {
	    System.out.print(i + " ");
	}
    }

    public static void sort(List<Integer> list) {
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

}
