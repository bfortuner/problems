package sorting;

public class CountingSort {

    public static void main(String[] args) {
        int[] a1 = {1,2,13,9,5,6,10,5};
        int[] newArr = sort(a1);
        for (int i : newArr) {
            System.out.print(i + "");
        }
	
    }

    private static int getMax(int[] arr) {
        int max = arr[0];
        for (int i=0; i<arr.length; i++) {
            max = Math.max(max,arr[i]);
        }
        return max;
    }
    public static int[] sort(int[] arr) {
        //Create buckets array (count)
        int[] count = new int[getMax(arr)+1];

        //Loop through values in array and map to bucket
        for (int i=0; i<arr.length; i++) {
            int countIndex = arr[i];
            count[countIndex]++;
        }

        //Transform count array values into cumulative sums of counts
        int last = 0;
        for (int i=0; i<count.length; i++) {
            count[i] += last;
            last = count[i];
        }

        //Create new array and map sorted values
        int[] sorted = new int[arr.length];
        for (int i=0; i<arr.length; i++) {
            int index = count[arr[i]]-1;
            sorted[index] = arr[i];
            count[arr[i]]--;
        }
        return sorted;
    };

}
