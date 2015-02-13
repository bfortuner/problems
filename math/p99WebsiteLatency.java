package math;

import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;

public class p99WebsiteLatency {
    
    static int NUM_BUCKETS = 10;
    static int[] BUCKETS = new int[NUM_BUCKETS];
    static int SIZE = 0;
    static int MIN_RANGE = 0;
    static int MAX_RANGE = 1;
    static double BUCKET_SIZE = (double) (MAX_RANGE-MIN_RANGE) / NUM_BUCKETS;

    public static void main(String[] args) {

	double[] a1 = {1.12,3.4,5.6,6.3,7.1};
	System.out.println(getP99FromArray(a1,99) == 6.3);
	System.out.println(getP99FromArray(a1,100) == 7.1);
	System.out.println(getP99FromArray(a1,40) == 3.4);
	System.out.println(getP99FromArray(a1,1) == 1.12);

	double[] a2 = {.002,.123,.42,.522,.125,.643};
	for (double d : a2) {
	    putLatencyTimeDynamic(d);
	}
	for (int i : BUCKETS) {
	    System.out.println(i);
	}
	System.out.println(getP99(90) == .5);
	System.out.println(getP99(99) == .5);
	System.out.println(getP99(100));
	System.out.println(getP99(20) == .0);
	System.out.println(getP99(40) == .1);
    }

    /*
     * Given unsorted array of integers, and percentile from 0-100, 
     * return the integer value that represents that percentile
     * 99th percentile = value >= 99% of other values 
     */
    public static double getP99FromArray(double[] arr, int percentile) {
	Arrays.sort(arr);
	int count = arr.length;
	int pos = (int) (percentile / 100.0 * count);
	if (pos == 0) {
	    return arr[0];
	} else {
	    return arr[pos-1];
	}
    }

    /* 
     * Add time from stream to buckets array
     * Times range from 0 to 1
     */
    public static void putLatencyTime(double time) {
	int bucket = (int) (time * 10);
	BUCKETS[bucket]++;
	SIZE++;
    }

    /* 
     * Add time from stream to array of N buckets
     * Times range from MIN to MAX
     * 10 buckets, range 2 - 7, size = .5
     * val 2.75 placed in bucket 1, 6.9 placed in bucket 9
     */
    public static void putLatencyTimeDynamic(double time) {
	double bucket_size = (double) (MAX_RANGE-MIN_RANGE) / NUM_BUCKETS;
	
	int bucket = (int) ((time - MIN_RANGE) / bucket_size);
	BUCKETS[bucket]++;
	SIZE++;
    }

    /*
     * Calculate and return the Nth percentile value (0 - 100)
     * From the buckets array
     */
    public static double getP99(int percentile) {
	int elementPos = (int) (percentile / 100.0 * SIZE);
	int bucket = 0;
	while (elementPos > 0) {
	    elementPos -= BUCKETS[bucket];
	    if (elementPos <= 0) {
		return Math.round(bucket * BUCKET_SIZE * 100.0) / 100.0;  //necessary to catch small rounding differences
	    }
	    bucket++;
	}
	return Math.round(bucket * BUCKET_SIZE * 100.0) / 100.0;  //necessary to catch
    }

}
