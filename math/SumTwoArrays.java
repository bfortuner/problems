package math;

import java.util.Arrays;
import java.lang.Math;

public class SumTwoArrays {

    public static void main(String[] args) {
	int[] a1 = {6,8,3};
	int[] a2 = {3,5,4};
	
	int[] res = sumArrays1(a1, a2);
	int[] ans = {1,0,3,7};
	System.out.println(Arrays.equals(res,ans));

	int[] a3 = {1,6,8,3};
	int[] a4 = {3,5,4};
	
	int res2[] = sumArrays1(a3, a4);
	int ans2[] = {0,2,0,3,7};
	System.out.println(Arrays.equals(res2,ans2));

	int[] a5 = {4,3,2,1};
	int res3 = extractNumFromArr(a5);
	System.out.println(res3 == 4321);

	int[] res4 = sumArrays2(a3, a4);
	int[] ans4 = sumArrays2(a3, a4);
	System.out.println(Arrays.equals(res4,ans4));

    }

    /*
     * Finds larger array and loops through adding both
     * until it reaches end of array. Uses carry int variable
     */
    public static int[] sumArrays1(int[] arr1, int[] arr2) {
	int stop = Math.max(arr1.length, arr2.length);
	int[] arr3 = new int[stop+1]; //3
	int tmp = 0;
	int carry = 0;
	int i = 1;
	while (i <= stop) {
	    tmp = carry;
	    if (i <= arr1.length) {
		tmp = tmp + arr1[arr1.length-i];
	    }
	    if (i <= arr2.length) {
		tmp = tmp + arr2[arr2.length-i];
	    }
	    if (tmp >= 10) {
		carry = 1;
		tmp = tmp % 10;
	    } else {
		carry = 0;
	    }
	    arr3[stop-i+1] = tmp;
	    i++;
	}
	if (carry > 0) {
	    arr3[0] = carry;
	}
	return arr3;
    }

    /*
     * Uses helper methods sumArray() and countDigits() to 
     * first find the sum, and then build an array of the 
     * correct length
     */

    public static int[] sumArrays2(int[] arr1, int[] arr2) {
	int sum = extractNumFromArr(arr1) + extractNumFromArr(arr2); //4552
	int digits = countDigits(sum);
	int[] arr3 = new int[digits]; //4
	int place = (int) Math.pow(10, digits-1); //1000
	for (int i=0; i<digits; i++) {	    
	    arr3[i] = sum / place;
	    sum = sum % place;
	    place = place / 10;
	}
	return arr3;
    }

    public static int countDigits(int num) {
	int count = 0;
	while (num > 0) {
	    count++;
	    num = num / 10;
	}
	return count;
    }

    //[4,5,5,2] == 4,5,5,2
    public static int extractNumFromArr(int[] arr) {
	int sum = 0;
	int place = arr.length-1;
	for (int i=0; i<arr.length; i++) {
	    sum += (arr[i] * Math.pow(10,place));
	    place--;
	}
	return sum;
    }

}
