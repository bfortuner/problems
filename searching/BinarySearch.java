package searching;

public class BinarySearch {

    public static void main(String[] args) {
	int[] arr = {1,2,3,4}; //{-3,2,5,8,22,67,89,101};
	System.out.println(binarySearchIterative(arr,1) == true);
	System.out.println(binarySearchIterative(arr,4) == true);
	System.out.println(binarySearchIterative(arr,2) == true);
	System.out.println(binarySearchIterative(arr,-3) == false);

	System.out.println(binarySearchRecursive(arr,1,0,arr.length) == 0);
	System.out.println(binarySearchRecursive(arr,4,0,arr.length) == 3);
	System.out.println(binarySearchRecursive(arr,2,0,arr.length) == 1);
	System.out.println(binarySearchRecursive(arr,-3,0,arr.length) == -1);

	int[] arr2 = {-3,2,5,8,22,67,89,101};
	System.out.println(binarySearchIterative(arr2,101) == true);
	System.out.println(binarySearchIterative(arr2,-3) == true);
	System.out.println(binarySearchIterative(arr2,8) == true);
	System.out.println(binarySearchIterative(arr2,99) == false);

	System.out.println(binarySearchRecursive(arr2,-3,0,arr2.length-1) == 0);
	System.out.println(binarySearchRecursive(arr2,101,0,arr2.length-1) == arr2.length-1);
	System.out.println(binarySearchRecursive(arr2,8,0,arr2.length-1) == 3);
	System.out.println(binarySearchRecursive(arr2,99,0,arr2.length-1) == -1);

    }

    /*
     * Return true if int is in Array
     * [1,3,5,6,7]
     * [1,2,3,4]
     */
    public static boolean binarySearchIterative(int[] arr, int target) {
	int low = 0;
	int high = arr.length;
	while (low < high) {
	    int mid = (high + low) / 2;
	    if (arr[mid] == target) {
		return true;
	    } else if (target < arr[mid]) {
		high = mid;
	    } else {
		low = mid+1;
	    }
	}
	return false;
    }

    /*
     * Return index if int is in Array, else -1
     * [1,3,5,6,7]
     * [1,2,3,4]
     */
    public static int binarySearchRecursive(int[] arr, int target, int low, int high) {
	int mid = (high + low) / 2;
	if (low > high) {
	    return -1;
	} else if (arr[mid] == target) {
	    return mid;
	} else if (target < arr[mid]) {
	    return binarySearchRecursive(arr, target, low, mid-1);
	} else {
	    return binarySearchRecursive(arr, target, mid+1, high);
	}
    }


}
