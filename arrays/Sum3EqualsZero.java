public class Sum3EqualsZero {

    public static void main(String[] args) {
		int[] arr1 = {-3,-2,1,2,5};
		boolean found1 = foundZeroSum(arr1);
		System.out.println(found1);
    
		int[] arr2 = {-3,-1,0,2,3};
		boolean found2 = foundZeroSum(arr2);
		System.out.println(found2);
    }

    public static boolean foundZeroSum(int[] arr) {
		int len = arr.length;
		int curSum;
		for (int i=0; i<len-2; i++) {
			int j = i+1;
			int k = len-1;
			while (k>j) {
				curSum = arr[i] + arr[j] + arr[k];
				if (curSum == 0) {
					return true;
				} else if (curSum < 0) {
					j++;
				} else {
					k--;
				}
			}
		}
		return false;
    }

}
