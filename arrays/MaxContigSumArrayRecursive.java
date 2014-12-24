import java.util.ArrayList;
import java.util.List;

public class MaxContigSumArrayRecursive {

    public static void main(String[] args) {
        System.out.println("Starting Tests!");
	testGetMaxContigSum();
    }

    public static int getMaxContigSum(List<Integer> nums, int maxSum, int curSum) {
	if ( nums.size() == 0 ) {
	    return maxSum;
	} else if ( curSum + nums.get(0) < nums.get(0) ) {
	    curSum = nums.get(0);
	} else {
	    curSum = curSum + nums.get(0);
	}
	
	if ( curSum > maxSum ) {
	    return getMaxContigSum(nums.subList(1, nums.size()), curSum, curSum);
	} else {
	    return getMaxContigSum(nums.subList(1, nums.size()), maxSum, curSum);
	}

    }

    public static void testGetMaxContigSum() {
	List<Integer> nums1 = new ArrayList();
	nums1.add(0);
	nums1.add(4);
	nums1.add(-2);
	nums1.add(1);
	nums1.add(4);
	System.out.println(getMaxContigSum(nums1, nums1.get(0), 0) == 7);

	nums1.clear();

	nums1.add(-7);
	System.out.println(getMaxContigSum(nums1, nums1.get(0), 0) == -7);

	nums1.clear();

	nums1.add(1);
	nums1.add(1);
	nums1.add(1);
	
	System.out.println(getMaxContigSum(nums1, nums1.get(0), 0) == 3);

	nums1.clear();

	nums1.add(0);
	nums1.add(4);
	nums1.add(-6);
	nums1.add(8);
	
	System.out.println(getMaxContigSum(nums1, nums1.get(0), 0) == 8);

	nums1.clear();

	nums1.add(1);
	nums1.add(1);
	nums1.add(1);
	nums1.add(-3);
	nums1.add(1);
	nums1.add(1);
	nums1.add(1);

	System.out.println(getMaxContigSum(nums1, nums1.get(0), 0) == 3);

	nums1.clear();

	nums1.add(0);
	nums1.add(-2);
	nums1.add(5);
	nums1.add(-4);
	nums1.add(-3);

	System.out.println(getMaxContigSum(nums1, nums1.get(0), 0) == 5);

    }
}
