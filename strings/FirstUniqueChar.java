package strings;

import java.util.*;

public class FirstUniqueChar {
    
    public static void main(String[] args) {
	String s1 = "abacb";
	String s2 = "";
	String s3 = null;
	String s4 = "a";
	String s5 = "aabbccc";
	String s6 = "abbccc";
	System.out.println("HashMap----");
	System.out.println(findHashMap(s1) == 'c');
	System.out.println(findHashMap(s2) == null);
	System.out.println(findHashMap(s3) == null);
	System.out.println(findHashMap(s4) == 'a');
	System.out.println(findHashMap(s5) == null);
	System.out.println(findHashMap(s6) == 'a');
	System.out.println("Double Loop----");
	System.out.println(findDoubleLoop(s1) == 'c');
	System.out.println(findDoubleLoop(s2) == null);
	System.out.println(findDoubleLoop(s3) == null);
	System.out.println(findDoubleLoop(s4) == 'a');
	System.out.println(findDoubleLoop(s5) == null);
	System.out.println(findDoubleLoop(s6) == 'a');
	System.out.println("Sorted----");
	System.out.println(findSorted(s1) == 'c');
	System.out.println(findSorted(s2) == null);
	System.out.println(findSorted(s3) == null);
	System.out.println(findSorted(s4) == 'a');
	System.out.println(findSorted(s5) == null);
	System.out.println(findSorted(s6) == 'a');

    }
    

    // Log Linear Time - O(n Log n)
    // aadee
    public static Character findSorted(String str) {
	if (str == null || str.length() == 0) {
	    return null;
	} else if (str.length() == 1) {
	    return str.charAt(0);
	}
	Character[] charArr = new Character[str.length()];
	for (int i=0; i<str.length(); i++) {
	    charArr[i] = str.charAt(i);
	}
	Arrays.sort(charArr);
	int i=0;
	while (i<charArr.length) {
	    char cur = charArr[i];
	    if (i == charArr.length-1 || charArr[i+1] != cur) {
		return charArr[i];
	    }
	    while (i<charArr.length && charArr[i] == cur) {
		i++;
	    }
	}
	return null;
	
    }

    // Quadratic Time - O(n^2)
    public static Character findDoubleLoop(String str) {
	if (str == null || str.length() == 0) {
	    return null;
	}
	for (int i=0; i<str.length(); i++) {
	    int j = 0;
	    boolean foundDupe = false;
	    while (!foundDupe && j<str.length()) {
		if (str.charAt(i) == str.charAt(j) && i != j) {   //need to check if already tried this char
		    foundDupe = true;
		} else {
		    j++;
		}
	    }
	    if (!foundDupe) {
		return str.charAt(i);
	    }
	}
	return null;	   
    }

    // Linear Time - O(n), Space O(n)
    public static Character findHashMap(String str) {
	if (str == null || str.length() == 0) {
	    return null;
	} else if (str.length() == 1) {
	    return str.charAt(0);
	}
	// Build HashMap to store count of each char
	Map<Character,Integer> map = new HashMap();
	for (int i=0; i<str.length(); i++) {
	    if ( map.containsKey(str.charAt(i)) ) {
		map.put(str.charAt(i),map.get(str.charAt(i))+1);
	    } else {
		map.put(str.charAt(i),1);
	    }
	}

	// Loop through initial str, checking if count == 1
	for (int i=0; i<str.length(); i++) {
	    if (map.get(str.charAt(i)) == 1) {
		return str.charAt(i);
	    }
	}

	return null; // no unique characters

    }


}
