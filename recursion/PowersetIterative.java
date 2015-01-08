package recursion;

import java.util.ArrayList;
import java.util.Arrays;

public class PowersetIterative {
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
	set2 = "abcde";
        ArrayList<String> pset = getPowerset(set2, "");
	printArrayList(pset, set2);
    }

    public static ArrayList<String> getPowerset(String set, String subset) {
	ArrayList<String> list = new ArrayList();
	if (set.length() == 0) {
	    list.add(subset);
	    return list;
	} else {
	    ArrayList<String> with = getPowerset(set.substring(1,set.length()), subset + set.substring(0,1));
	    ArrayList<String> withOut = getPowerset(set.substring(1,set.length()), subset);
	    list.addAll(with);
	    list.addAll(withOut);
	    return list;
	}
    }

    public static void printArrayList(ArrayList<String> list, String set) {
	System.out.println("================");
	System.out.println("Set: " + set);
	System.out.println("Length: " + set.length());
	System.out.println("Pset: " + list.size() + " subsets");
        for (String s : list) {
            System.out.print(s + " ");
        }
	System.out.println("\n================");
    }

}
