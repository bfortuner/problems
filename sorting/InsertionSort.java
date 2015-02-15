package sorting;

public class InsertionSort {

    public static void main(String[] args) {
        int[] a1 = {2,1,4,5,3};
        sort(a1);
        for (int i : a1) {
            System.out.print(i + "");
        }
	
    }

    public static void sort(int[] arr) {
        int i = 0;
        while (i < arr.length) {
            int j = i-1;
            int tmp = arr[i];
            while (j >= 0 && tmp < arr[j]) {
                arr[j+1] = arr[j];
                j--;
            }
            arr[j+1] = tmp;
            i++;
        }
    };

}
