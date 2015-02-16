package sorting;

public class ShellSort {

    public static void main(String[] args) {
        int[] a1 = {2,1,4,5,3};
        sort(a1);
        for (int i : a1) {
            System.out.print(i + "");
        }
	System.out.println("\n================");
        int[] a2 = {54,26,93,17,77,31,44,55,20};
        sort(a2);
        for (int i : a2) {
            System.out.print(i + "");
        }
	
    }

    public static void sort(int[] arr) {
	int gap = 3;
	while (gap > 0) {
	    int start = 0;
	    while (start < gap) {
		insertionSort(arr, start, gap);
		start++;
	    }
	    gap--;
	}
    }

    public static void insertionSort(int[] arr, int start, int gap) {
        int i = start + gap;
        while (i < arr.length) {
            int j = i;
            while (j > start && arr[j] < arr[j-gap]) {
		int tmp = arr[j];
		arr[j] = arr[j-gap];
		arr[j-gap] = tmp;
		j = j - gap;
            }
            i = i + gap;
        }
    };

}
