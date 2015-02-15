package sorting;

public class BubbleSort {

    public static void main(String[] args) {
        int[] a1 = {2,1,4,5,3};
        sort(a1);
        for (int i : a1) {
            System.out.print(i + "");
        }
	
    }

    public static void sort(int[] arr) {
	    boolean sorted = false;
        while (!sorted) {
            sorted = true;
            for (int i=0; i<arr.length-1; i++) {
                if (arr[i] > arr[i+1]) {
                    int tmp = arr[i];
                    arr[i] = arr[i+1];
                    arr[i+1] = tmp;
                    sorted = false;
                }
            }
        }
    };

}
