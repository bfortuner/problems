package queues;

import java.util.*;

public class QueueWithArray<T> {

    public static void main(String[] args) {
        QueueWithArray<String> queue = new QueueWithArray();
        queue.enqueue("A");
        queue.enqueue("B");
        queue.enqueue("C");

	queue.printQueue();
        queue.dequeue();
        queue.dequeue();
        queue.dequeue();
	queue.printQueue();

        queue.enqueue("A");
        queue.enqueue("B");
        queue.enqueue("C");

	queue.printQueue();

        queue.enqueue("A");
        queue.enqueue("B");
        queue.enqueue("C");
        queue.enqueue("A");
        queue.enqueue("B");
        queue.enqueue("C");
        queue.enqueue("A");
        queue.enqueue("B");
        queue.enqueue("C");

	queue.printQueue();

	queue.dequeue();
	queue.dequeue();
	queue.dequeue();
	queue.dequeue();
	queue.dequeue();
	queue.dequeue();
	queue.dequeue();
	queue.dequeue();
	queue.dequeue();
	queue.printQueue();
    }

    T[] arr = (T[]) new Object[1];
    int first;
    int last;

    public void printQueue() {
	System.out.println("First = " + first + " Last = " + last + " Size = " + size());
	for (T t : arr) {
	    System.out.println(t);
	}
	System.out.println("-----------");
    }

    public void enqueue(T val) {
        if (size() == 0) {
	    arr[last] = val;
        } else if (last == arr.length-1) {
	    resize();
	    last++;
	    arr[last] = val;
	} else {
	    last++;
	    arr[last] = val;
	}
    }

    public T dequeue() {
	if (size() == 0) {
	    first = 0;
	    last = 0;
	    return null;
	}
	T val = arr[first];
	arr[first] = null;
	if (first == last) {
	    first = 0;
	    last = 0;
	    return val;
	}
	first++;

	if(last-first < arr.length/4) {
	    resize();
	}
	return val;
    }
    
    public int size() {
        if (arr[first] == null) {
	    return 0;
	}
	return last-first + 1;
    }

    private void resize() {
	T[] newArr = getNewArr();
	int i = 0;
	for (int j=first; j<=last; j++) {
	    newArr[i] = arr[j];
	    i++;
	}
	first = 0;
	last = i-1;
	arr = newArr;
    }

    private T[] getNewArr() {
	if (last-first == arr.length-1) {
	    T[] newArr = (T[]) new Object[arr.length*2];
	    return newArr;
	} else if (last-first < arr.length/4) {
	    T[] newArr = (T[]) new Object[arr.length/2];
	    return newArr;
	} else {
	    T[] newArr = (T[]) new Object[arr.length];
	    return newArr;
	}

    }
}

