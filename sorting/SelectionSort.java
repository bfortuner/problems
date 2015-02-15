package sorting;

public class SelectionSort {

    public static void main(String[] args) {
        int[] a1 = {2,1,4,5,3};
        sort(a1);
        for (int i : a1) {
            System.out.print(i + "");
        }
	
    }

    public static void sort(int[] arr) {
        int i = 0;
        while (i < arr.length-1) {
            int min = i;
            int j = i+1;
            while (j < arr.length) {
                if (arr[j] < arr[min]) {
                    min = j;
                }
                j++;
            }
            int tmp = arr[i];
            arr[i] = arr[min];
            arr[min] = tmp;
            i++;
        }
    };

}
