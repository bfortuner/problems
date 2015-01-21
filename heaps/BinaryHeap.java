package heaps;

import java.util.List;
import java.util.ArrayList;


public class BinaryHeap {

    public static void main(String[] args) {
	BinaryHeap h1 = new BinaryHeap();
	System.out.println(h1.size() == 0);
	System.out.println(h1.isEmpty() == true);
	h1.insert(5);
	h1.insert(2);
	h1.insert(1);
	h1.insert(8);
	printList(h1.heap);

	h1.delMin();
	h1.delMin();
	printList(h1.heap);
    }

    public List<Integer> heap;
    public int size;

    public BinaryHeap() {
	this.heap = new ArrayList<Integer>();
	this.heap.add(0);    //default value needed to ensure calculations are correct
	this.size = 0;
    }

    public void insert(int k) {
	this.heap.add(k);
	this.size = this.size + 1;
	percUp(this.size);
    }

    public int findMin() {
	return this.heap.get(1);
    }

    public void delMin() {
	this.heap.set(1, this.heap.get(this.size));
	this.heap.remove(this.size);
	this.size = this.size - 1;
	percDown(1);
    }

    public boolean isEmpty() {
	return this.size == 0;
    }

    public int size() {
	return this.size;
    }

    //Need To Implement
    public BinaryHeap buildHeap(List<Integer> list) {
	return new BinaryHeap();
    }

    /*
     *  1. If element < parent, swap with parent (2n)
     *  2. Continue swapping up until parent < element
     */
    private void percUp(int i) {
	while (i / 2 > 0) {
	    if ( this.heap.get(i) < this.heap.get(i / 2) ) {
		int tmp = this.heap.get(i / 2);
		this.heap.set(i / 2, this.heap.get(i));
		this.heap.set(i, tmp);
	    }
	    i = i / 2;
	}
    }

    private void percDown(int i) {
	while (i*2 <= this.size) {
	    int min = minChild(i);
	    if (this.heap.get(min) < this.heap.get(i)) {
		int tmp = this.heap.get(i);
		this.heap.set(i,this.heap.get(min));
		this.heap.set(min,tmp);
	    }
	    i = min;
	}
    }

    private int minChild(int i) {
	if ( (i*2 + 1) > this.size ) {
	    return i*2;
	} else if (this.heap.get(i*2) < this.heap.get(i*2 + 1)) {
	    return i*2;
	} else {
	    return i*2 + 1;
	}
    }

    public static void printList(List<Integer> list) {
        System.out.print("[");
        for (int i : list) {
            System.out.print("" + i + " ");
        }
        System.out.print("]\n");
    }


}
