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

	System.out.println("===========");
	int[] arr4 = {1,2,3,4,0};
	int[] arr5 = {1,2,3,4};
	int[] arr6 = {4,5,1,2,3,4};
	System.out.println(findPivot(arr,0,arr.length-1) == 2);
	System.out.println(findPivot(arr2,0,arr2.length-1) == 1);
	System.out.println(findPivot(arr3,0,arr3.length-1) == 0);
	System.out.println(findPivot(arr4,0,arr4.length-1) == 3);
	System.out.println(findPivot(arr5,0,arr5.length-1) == -1);
	System.out.println(findPivot(arr6,0,arr6.length-1) == 1);
    }

    /*
     * Return index of target element in array, else return -1
     */
    public static int binarySearchPivot(int[] arr, int target) {
	int pivot = findPivot(arr,0,arr.length-1);
	System.out.println(pivot);
	if (pivot == -1) {
	    return BinarySearch.binarySearchRecursive(arr,target,0,arr.length);
	} else if (pivot == target) {
	    return pivot;
	} else {
	    int left = BinarySearch.binarySearchRecursive(arr,target,0,pivot);
	    int right = BinarySearch.binarySearchRecursive(arr,target,pivot+1,arr.length);
	    if (left != -1) {
		return left;
	    } else {
		return right;
	    }
	}
    }

    //	int[] arr = {3,4,5,1,2};
    //	int[] arr3 = {7,1,2,3,6};
    //	int[] arr4 = {1,2,3,4,0};
    //  int[] arr5 = {1,2,3,4};
    //  int[] arr6 = {4,5,1,2,3,4};
    public static int findPivot(int[] arr, int low, int high) {
	int mid = (high+low) / 2;
	if (low > high || mid+1 > high) {
	    return -1;
	} else if (arr[mid] > arr[mid+1]) {
	    return mid;
	} else if (arr[mid] < arr[high]) {
	    high = mid;
	} else if (arr[mid] > arr[high]) {
	    low = mid+1;
	} else if (arr[mid] > arr[low]) {
	    low = mid+1;
	} else if (arr[mid] < arr[low]) {
	    high = mid;
	}
	return findPivot(arr,low,high);
    }



}
