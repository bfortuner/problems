import java.util.ArrayList;
import java.util.List;

public class MaxContigSumArrayIterative {

    public static void main(String[] args) {

        System.out.println("Starting Tests!");
	testGetMaxContigSum();

    }

    public static int getMaxContigSum(List<Integer> nums) {
	int maxSum = nums.get(0);
	int curSum = 0;

	for (int e : nums) {

	    if (curSum + e < e) {
		curSum = e;
	    } else {
		curSum = curSum + e;
	    }

	    if (curSum > maxSum) {
		maxSum = curSum;
	    }	    
	}

	return maxSum;
    }

    public static void testGetMaxContigSum() {
	List<Integer> nums1 = new ArrayList();
	nums1.add(0);
	nums1.add(4);
	nums1.add(-2);
	nums1.add(1);
	nums1.add(4);
	System.out.println(getMaxContigSum(nums1) == 7);

	nums1.clear();

	nums1.add(-7);
	System.out.println(getMaxContigSum(nums1) == -7);

	nums1.clear();

	nums1.add(1);
	nums1.add(1);
	nums1.add(1);
	
	System.out.println(getMaxContigSum(nums1) == 3);

	nums1.clear();

	nums1.add(0);
	nums1.add(4);
	nums1.add(-6);
	nums1.add(8);
	
	System.out.println(getMaxContigSum(nums1) == 8);

	nums1.clear();

	nums1.add(1);
	nums1.add(1);
	nums1.add(1);
	nums1.add(-3);
	nums1.add(1);
	nums1.add(1);
	nums1.add(1);

	System.out.println(getMaxContigSum(nums1) == 3);

	nums1.clear();

	nums1.add(0);
	nums1.add(-2);
	nums1.add(5);
	nums1.add(-4);
	nums1.add(-3);

	System.out.println(getMaxContigSum(nums1) == 5);

    }
}
