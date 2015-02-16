package sorting;

import java.util.*;

public class QuickSort {

    public static void main(String[] args) {
        int[] a1 = {1,2,13,9,5,6,10,5};
        sort(a1,0,a1.length-1);
        for (int i : a1) {
            System.out.print(i + " ");
        }
        System.out.println();
        int[] a2 = {1,2,-13,9,50,6,10,5};
        sort(a2,0,a2.length-1);
        for (int i : a2) {
            System.out.print(i + " ");
        }
    }

    public static void sort(int[] arr, int low, int high) {
        if (high - low < 1) {
            //skip
        } else {
            int split = partition(arr, low, high);
            sort(arr,low,split-1);
            sort(arr,split,high);
        }
    };

    public static int partition(int[] arr, int low, int high) {
        int pivot = arr[low + ((high - low) / 2)];
        int i = low;
        int j = high;
        while (i <= j) {
            if (arr[i] >= pivot && arr[j] <= pivot) {
                int tmp = arr[i];
                arr[i] = arr[j];
                arr[j] = tmp;
                i++;
                j--;
            } else if (arr[i] < pivot) {
                i++;
            } else {
                j--;
            }
        }
        return i;
    }

    public static void print(int[] arr) {
        System.out.println();
        for (int i : arr) {
            System.out.print(i + " ");
        }
    }
}
