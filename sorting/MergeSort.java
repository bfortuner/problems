package sorting;

import java.util.*;

public class MergeSort {

    public static void main(String[] args) {
        int[] a1 = {1,2,13,9,5,6,10,5};
        a1 = sort(a1);
        for (int i : a1) {
            System.out.print(i + "");
        }

        int[] a2 = {1,2,-13,9,50,6,10,5};
        a2 = sort(a2);
        for (int i : a2) {
            System.out.print(i + "");
        }
    }

    public static int[] sort(int[] arr) {
        if (arr.length <= 1) {
            return arr;
        } else {
            int[] left = Arrays.copyOfRange(arr, 0, arr.length/2);
            int[] right = Arrays.copyOfRange(arr, arr.length/2, arr.length);
            left = sort(left);
            right = sort(right);
            return merge(left, right);
        }
    };

    public static int[] merge(int[] arr1, int[] arr2) {
        int[] sorted = new int[arr1.length + arr2.length];
        int a = 0;
        int b = 0;
        for (int i=0; i<sorted.length; i++) {
            if (a >= arr1.length) {
                sorted[i] = arr2[b];
                b++;
            } else if (b >= arr2.length) {
                sorted[i] = arr1[a];
                a++;
            } else if (arr1[a] < arr2[b]) {
                sorted[i] = arr1[a];
                a++;
            } else {
                sorted[i] = arr2[b];
                b++;
            }
        }
        return sorted;
    }

}
