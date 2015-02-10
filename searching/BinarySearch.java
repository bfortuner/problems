package searching;

public class BinarySearch {

    public static void main(String[] args) {
	int[] arr = {1,2,3,4}; //{-3,2,5,8,22,67,89,101};
	for (int i : arr) {
	    System.out.println(i);
	}
	System.out.println(binarySearch(arr,1) == true);
	System.out.println(binarySearch(arr,4) == true);
	System.out.println(binarySearch(arr,2) == true);
	System.out.println(binarySearch(arr,-3) == false);
	//System.out.println(binarySearch(arr,101) == true);
    }

    /*
     * Return true if int is in Array
     * [1,3,5,6,7]
     * [1,2,3,4]
     */
    public static boolean binarySearch(int[] arr, int target) {
	int high = arr.length-1;
	int low = 0;
	int mid = (high - low) / 2;
	while (high >= low) {
	    if (arr[mid] == target) {
		return true;
	    } else if (target > arr[mid]) {
		low = mid+1;
	    } else {
		high = mid-1;
	    }
	    mid = low + (high - low) / 2;
	}
	return false;
    }


}
