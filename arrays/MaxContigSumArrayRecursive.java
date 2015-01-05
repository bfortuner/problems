import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.lang.Math;

public class MaxContigSumArrayRecursive {

    public static void main(String[] args) {
        System.out.println("Starting Tests!");
	testGetMaxContigSum();
	testGetMaxContigSum2();

	List<Integer> left = new ArrayList();
	left.add(-1);
	left.add(-2);
	left.add(5);
	left.add(-2);
	List<Integer> right = new ArrayList();
	right.add(1);
	right.add(2);
	right.add(-6);
	right.add(4);
	int maxSum = getCombo(left,right);
	//System.out.println(maxSum);

	List<Integer> combined = new ArrayList(left);
	combined.addAll(right);
	printArrayList(combined);
	maxSum = getMaxContigSum2(combined);
	System.out.println(maxSum);
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

    public static int getMaxContigSum2(List<Integer> nums) {
	if ( nums.size() == 1 ) {
	    return nums.get(0);
	} else {
	    List<Integer> left = nums.subList(0,nums.size()/2);
	    List<Integer> right = nums.subList(nums.size()/2, nums.size());
	    int leftMax = getMaxContigSum2(left);
	    int rightMax = getMaxContigSum2(right);
	    int combo = getCombo(left,right);
	    return Math.max(Math.max(leftMax, rightMax), combo);
	}
    }

    public static int getCombo(List<Integer> left, List<Integer> right) {
	int leftMax = 0;
	int i = left.size()-1;
	int leftSum = 0;
	while (i >= 0) {
	    leftSum += left.get(i);
	    if (leftSum > leftMax) {
		leftMax = leftSum;
	    }
	    i--;
	}

	int rightMax = 0;
	int rightSum = 0;
	int j = 0;
	while (j < right.size()) {
	    rightSum += right.get(j);
	    if (rightSum > rightMax) {
		rightMax = rightSum;
	    }
	    j++;
	}
	return leftMax + rightMax;
    }

    public static void printArrayList(List<Integer> list) {
	System.out.print("[");
	for (int i : list) {
	    System.out.print("" + i + " ");
	}
	System.out.print("]\n");	
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

    public static void testGetMaxContigSum2() {
	List<Integer> nums1 = new ArrayList();
	nums1.add(0);
	nums1.add(4);
	nums1.add(-2);
	nums1.add(1);
	nums1.add(4);
	System.out.println(getMaxContigSum2(nums1) == 7);

	nums1.clear();

	nums1.add(-7);
	System.out.println(getMaxContigSum2(nums1) == -7);

	nums1.clear();

	nums1.add(1);
	nums1.add(1);
	nums1.add(1);
	
	System.out.println(getMaxContigSum2(nums1) == 3);

	nums1.clear();

	nums1.add(0);
	nums1.add(4);
	nums1.add(-6);
	nums1.add(8);
	
	System.out.println(getMaxContigSum2(nums1) == 8);

	nums1.clear();

	nums1.add(1);
	nums1.add(1);
	nums1.add(1);
	nums1.add(-3);
	nums1.add(1);
	nums1.add(1);
	nums1.add(1);

	System.out.println(getMaxContigSum2(nums1) == 3);

	nums1.clear();

	nums1.add(0);
	nums1.add(-2);
	nums1.add(5);
	nums1.add(-4);
	nums1.add(-3);

	System.out.println(getMaxContigSum2(nums1) == 5);

    }


}
