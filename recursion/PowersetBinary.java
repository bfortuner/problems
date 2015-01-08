package recursion;

import java.util.ArrayList;
import java.util.Arrays;

public class PowersetBinary {
    public static String[] set1;

    public static void main(String[] m) {
        set1 = new String[6];
        set1[0] = "a";
        set1[1] = "b";
        set1[2] = "c";
        set1[3] = "d";
        set1[4] = "e";
        set1[5] = "f";
	String set2 = "abc";
	String set3 = "abcde";
        ArrayList<Integer> pset = getPowerset(set2);
	printArrayList(pset, set2);
        pset = getPowerset(set3);
	printArrayList(pset, set3);
    }

    public static ArrayList<Integer> getPowerset(String set) {
	int i = 0;
	ArrayList<Integer> subsets = new ArrayList();
	while (i < Math.pow(2,set.length())) {
	    subsets.add(i);
	    i++;
	}
	return subsets;
    }

    public static void printArrayList(ArrayList<Integer> list, String set) {
	System.out.println("================");
	System.out.println("Set: " + set);
	System.out.println("Length: " + set.length());
	System.out.println("Pset: " + list.size() + " subsets");
        for (Integer i : list) {
	    String s = intToNBitBinaryStr(i, set.length());
            System.out.println(s);
        }
	System.out.println("\n================");
    }

    /*
     * Convert integer, i, to binary string of min digits, pad
     */
    public static String intToNBitBinaryStr(int i, int n) {
        String binStr = Integer.toBinaryString(i);  // get x-digit binary string from int
        binStr = String.format("%" + Integer.toString(n) + "s", binStr).replace(' ', '0');   //add minimum zero-padding to always return n-bit string
        binStr = binStr.substring(binStr.length()-n, binStr.length());  //grab last n digits b/c java represents binary in 64 digits

        return binStr;
    }


}
