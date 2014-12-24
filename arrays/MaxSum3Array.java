public class MaxSum3Array {

    public static void main(String[] args) {
	int[] arr1 = {1,3,5,-3,2};
	int max1 = getMaxSum(arr1);
	System.out.println(max1);
    }

    public static int getMaxSum(int[] arr) {
	int len = arr.length;
	Integer maxSum = null;
	for (int i=0; i<len-2; i++) {
	    for (int j=i+1; j<len-1; j++) {
		for (int k=j+1; k<len; k++) {
		    int curSum = arr[i] + arr[j] + arr[k];
		    if (maxSum == null || curSum > maxSum) {
			maxSum = curSum;
		    }
		}
	    }
	}

	return maxSum;
    }

}
