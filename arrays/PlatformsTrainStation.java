package arrays;

import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;

public class PlatformsTrainStation {

    // Train station hours and interval
    static final int OPEN = 900;
    static final int CLOSE = 2000;
    static final int INTERVAL = 10;
    
    public static void main(String[] args) {
	System.out.println("Testing Has Overlap -----");
	System.out.println(hasOverlap(900,910,910,920) == false);
	System.out.println(hasOverlap(900,950,910,920) == true);
	System.out.println(hasOverlap(910,920,900,910) == false);
	System.out.println(hasOverlap(1100,1200,900,1130) == true);
	
	System.out.println("Testing maxplatforms basic ------");
	int[] arr1 = {900, 940, 950, 1100, 1500, 1800};
	int[] dep1 = {910, 1200, 1120, 1130, 1900, 2000};
	System.out.println(maxPlatformsBasic(arr1,dep1) == 3);
	System.out.println(maxPlatformsFaster(arr1,dep1) == 3);

    }
    
    /*
     * Given two arrays of arrival times and departure times for trains
     * Return the maximum number of platforms needed to support
     * those trains (e.g. max trains at station at one time)
     *
     * Assume the train station is open between 9:00 and 20:00
     * and the minimum stop is 10 minutes (departure - arrival)
     *
     * O(n^2)
     */
    public static int maxPlatformsBasic(int[] arr, int[] dep) {
	int maxPlatforms = 0;
	int curTime = OPEN;
	while (curTime < CLOSE) {
	    int reqPlatforms = 0;
	    for (int i=0; i<arr.length; i++) {
		if (hasOverlap(curTime, curTime+INTERVAL, arr[i], dep[i])) {
		    reqPlatforms++;
		}
	    }
	    maxPlatforms = Math.max(maxPlatforms,reqPlatforms);
	    curTime += INTERVAL;
	}
	return maxPlatforms;
    }

    /*
     * O(n Log n) - Sorts list, then loops 1x through result
     */
    public static int maxPlatformsFaster(int[] arr, int[] dep) {
	int maxPlatforms = 0;
	Arrays.sort(arr);
	Arrays.sort(dep);
	int reqPlatforms = 0;
	int a = 0;
	int d = 0;
	while (a < arr.length) {
	    if (arr[a] == dep[d]) {
		a++;
		d++;
	    } else if (arr[a] < dep[d]) {
		reqPlatforms++;
		a++;
	    } else {
		reqPlatforms--;
		d++;
	    }
	    maxPlatforms = Math.max(maxPlatforms,reqPlatforms);
	}
	return maxPlatforms;
    }

    /*
     * Return true if 2 time ranges overlap
     */
    public static boolean hasOverlap(int start1, int end1, int start2, int end2) {
	if (start1 > start2 && start1 < end2) {
	    return true;
	} else if (end1 > start2 && end1 < end2) {
	    return true;
	} else if (start2 > start1 && start2 < end1) {
	    return true;
	} else if (end2 > start1 && end2 < end1) {
	    return true;
	} else {
	    return false;
	}
    }

}
