package searching;

public class BitonicSearch {

    public static void main(String[] args) {
	int[] arr = {1,2,3,4}; //{-3,2,5,8,22,67,89,101};
	System.out.println(binarySearch(arr,1,0,arr.length) == 0);
	System.out.println(binarySearch(arr,4,0,arr.length) == 3);
	System.out.println(binarySearch(arr,2,0,arr.length) == 1);
	System.out.println(binarySearch(arr,-3,0,arr.length) == -1);

	int[] arr2 = {-3,2,5,8,22,67,89,101};
	System.out.println(binarySearch(arr2,-3,0,arr2.length-1) == 0);
	System.out.println(binarySearch(arr2,101,0,arr2.length-1) == arr2.length-1);
	System.out.println(binarySearch(arr2,8,0,arr2.length-1) == 3);
	System.out.println(binarySearch(arr2,99,0,arr2.length-1) == -1);

	int[] arr3 = {1,2,4,1,0};
	System.out.println(getMaxIndex(arr3)==2);
	int[] arr4 = {1,2,0};
	System.out.println(getMaxIndex(arr4)==1);
	int[] arr5 = {1,4,3,2,1,0,0};
	System.out.println(getMaxIndex(arr5)==1);

	System.out.println("Contains Key-------");
	System.out.println(containsKey(arr3,4)==true);
	System.out.println(containsKey(arr3,7)==false);
	System.out.println(containsKey(arr5,0)==true);
	System.out.println(containsKey(arr4,0)==true);
    }

    public static boolean containsKey(int[] arr, int key) {
	int pivot = getMaxIndex(arr);
	int left = binarySearch(arr, key, 0, pivot+1);
	int right = binarySearchDesc(arr, key, pivot-1, arr.length-1);
	return left != -1 || right != -1;
    }

    public static int getMaxIndex(int[] arr) {
	int low = 0;
	int high = arr.length-1;
	int mid = high/2;
	while(mid != low) {
	    if (arr[mid] > arr[mid+1]) {
		high = mid;
	    } else {
		low = mid;
	    }
	    mid = low + (high-low)/2;
	}
	return high;
    }

    /*
     * Return index if int is in Array, else -1
     * [1,3,5,6,7]
     * [1,2,3,4]
     */
    public static int binarySearch(int[] arr, int target, int low, int high) {
	int mid = low + (high-low)/2;
	if (low > high) {
	    return -1;
	} else if (arr[mid] == target) {
	    return mid;
	} else if (arr[mid] > target) {
	    high = mid-1;
	} else {
	    low = mid+1;
	}
	return binarySearch(arr,target,low,high);
    }

    /*
     * Return index if int is in Array, else -1
     * [1,3,5,6,7]
     * [1,2,3,4]
     */
    public static int binarySearchDesc(int[] arr, int target, int low, int high) {
	int mid = low + (high-low)/2;
	if (low > high) {
	    return -1;
	} else if (arr[mid] == target) {
	    return mid;
	} else if (arr[mid] > target) {
	    low = mid+1;
	} else {
	    high = mid-1;
	}
	return binarySearchDesc(arr,target,low,high);
    }
}
