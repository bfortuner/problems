package arrays;

import java.util.*;

public class MaxIncrementalSubsequence {
    
    public static void main(String[] args) {
	MaxIncrementalSubsequence max = new MaxIncrementalSubsequence();
	int[] a1 = {0,2,1,3,4,5,0,1};
	System.out.println(max.getMaxLength(a1) == 4);
	int[] b1 = max.getMaxLengthSubsequence(a1);
	int[] sub = {1,3,4,5};
	System.out.println(Arrays.equals(sub,b1));
    }
    public int getMaxLength(int[] arr) {
	int max = 0;
	int curStart = 0;
	int curEnd = 1;
	for (int i=0; i<arr.length-1; i++) {
	    if (arr[i] <= arr[i+1]) {
		curEnd++;
		if (curEnd-curStart > max) {
		    max = curEnd-curStart;
		}
	    } else {
		curStart = i+1;
		curEnd = i+2;
	    }
	}
	return max;
    }

    public int[] getMaxLengthSubsequence(int[] arr) {
	if (arr == null || arr.length == 0) {
	    return null;
	}
	int maxStart = 0;
	int maxEnd = 1;
	int curStart = 0;
	int curEnd = 1;
	for (int i=0; i<arr.length-1; i++) {
	    if (arr[i] <= arr[i+1]) {
		curEnd++;
		if (curEnd-curStart > maxEnd-maxStart) {
		    maxStart = curStart;
		    maxEnd = curEnd;
		}
	    } else {
		curStart = i+1;
		curEnd = i+2;
	    }
	}
	return Arrays.copyOfRange(arr,maxStart,maxEnd);
    }


}
