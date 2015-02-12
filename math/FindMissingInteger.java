package math;

public class FindMissingInteger {
    
    public static void main(String[] args) {
	int[] a1 = {1,2,3,4,5};
	int[] a2 = {1,2,4,5,6};
	int[] a3 = {0,2,3,4};
	int[] a4 = {0};
	System.out.println(getMissingInt(a1) == -1);
	System.out.println(getMissingInt(a2) == 3);
	System.out.println(getMissingInt(a3) == 1);
	System.out.println(getMissingInt(a4) == -1);

	System.out.println(binarySearchMissingInt(a1) == -1);
	System.out.println(binarySearchMissingInt(a2) == 3);
	System.out.println(binarySearchMissingInt(a3) == 1);
	System.out.println(binarySearchMissingInt(a4) == -1);

	System.out.println(unsortedMissingInt(a1) == -1);
	System.out.println(unsortedMissingInt(a2) == 3);
	System.out.println(unsortedMissingInt(a3) == 1);
	System.out.println(unsortedMissingInt(a4) == -1);
    }

    /*
     * Naive Solution - O(n)
     */
    public static int getMissingInt(int[] arr) {
	if (arr.length <= 1) {
	    return -1;
	}
	int last = 0;
	for (int i = 1; i<arr.length; i++) {
	    if (arr[i] > arr[last]+1) {
		return arr[last]+1;
	    }
	    last++;
	}
	return -1;
    }

    /*
     * arr = [4,5,6,8]
     * binary search - O(log n)
     */
    public static int binarySearchMissingInt(int[] arr) {
	if (arr.length <= 1) {
	    return -1;
	}
	int base = arr[0]; //all comparisons subtract start, 2
	int low = 1;
	int high = arr.length;
	while (low < high) {
	    int mid = low + ((high-low) / 2);
	    if (arr[mid]-1 != arr[mid-1]) {
		return arr[mid]-1;
	    } else if (arr[mid]-base > mid) { //
		high = mid;
	    } else {
		low = mid+1;
	    }
	}
	return -1;
    }

    /*
     * arr = [4,5,3,7,8]
     * sum=27, min=3, max=8
     * baseSum=3, expectedSum=33, missingInt=6
     * binary search - O(log n)
     * sum of consecutive integers from 0 to N
     * sum = N * (N-1) / 2
     */
    public static int unsortedMissingInt(int[] arr) {
	if (arr.length <= 1) {
	    return -1;
	}
	int sum = 0;
	int min = arr[0];
	int max = arr[0];
	for (int i=0; i<arr.length;i++) {
	    sum += arr[i];
	    if (arr[i] > max) {
		max = arr[i];
	    }
	    if (arr[i] < min) {
		min = arr[i];
	    }
	}
	min-=1;
	int baseSum = min * (min+1) / 2;
	int expectedSum = (max * (max+1) / 2) - baseSum;
	if (expectedSum == sum) {
	    return -1;
	} else {
	    return expectedSum - sum;
	}
    }

}




