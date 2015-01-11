package math;

public class SwapIntegers {

    public static void main(String[] args) {
        int[] arr = new int[5];
        int a = 4;
        int b = 3;
        arr[1] = a;
        arr[3] = b;
        arr = swapIntegers(arr, 1, 3);
        System.out.println(arr[1] == b && arr[3] == a);

        arr[1] = -7;
        arr[3] = -3;
        arr = swapIntegers(arr, 1, 3);
        System.out.println(arr[1] == -3 && arr[3] == -7);
	}

    /*
     * Swap two integers in an array without using tmp variables
     */
    public static int[] swapIntegers(int[] arr, int a, int b) {
        arr[a] = arr[a] + arr[b];   //4 + 3 = 7
        arr[b] = arr[a] - arr[b];   //7 - 3 = 4
        arr[a] = arr[a] - arr[b];   //7 - 4 = 3
        return arr;
    }

}
