package searching;

public class BinarySearchPivot {

    public static void main(String[] args) {
	int[] arr = {3,4,5,1,2};
	System.out.println(binarySearchPivot(arr,1) == 3);
	System.out.println(binarySearchPivot(arr,4) == 1);
	System.out.println(binarySearchPivot(arr,2) == 4);
	System.out.println(binarySearchPivot(arr,-3) == -1);
	int[] arr2 = {2,3,1};
	System.out.println(binarySearchPivot(arr,1) == 2);
	System.out.println(binarySearchPivot(arr,3) == 1);
	System.out.println(binarySearchPivot(arr,2) == 0);
	System.out.println(binarySearchPivot(arr,-3) == -1);
	int[] arr3 = {7,1,2,3,6};
	System.out.println(binarySearchPivot(arr,1) == 1);
	System.out.println(binarySearchPivot(arr,3) == 3);
	System.out.println(binarySearchPivot(arr,7) == 0);
	System.out.println(binarySearchPivot(arr,6) == 4);
    }

    /*
     * Return index of target element in array, else return -1
     */
    public static int binarySearchPivot(int[] arr, int target) {
	int low = 0;
	int high = arr.length;
	while (low < high) {
	    int mid = (high + low) / 2;
	    if (arr[mid] == target) {
		return mid;
	    } else if (target < arr[mid]) {
		if (arr[low] > target && arr[low] < arr[mid]) {
		    low = mid+1;
		} else {
		    high = mid;
		}
	    } else if (target > arr[mid]) {
		if (arr[high-1] < target && arr[high-1] > arr[mid]) {
		    high = mid;
		} else {
		    low = mid+1;
		}
	    }
	}
	return -1;
    }


}
