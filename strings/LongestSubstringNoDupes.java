package strings;

import java.util.*;

public class LongestSubstringNoDupes {
    
    public static void main(String[] args) {
	LongestSubstringNoDupes sub = new LongestSubstringNoDupes();
	String s1 = "ababc";
	String s2 = "ab";
	String s3 = "a";
	String s4 = "";
	System.out.println(sub.getMaxSubstringLength(s1) == 3);
	System.out.println(sub.getMaxSubstringLength(s2) == 2);
	System.out.println(sub.getMaxSubstringLength(s3) == 1);
	System.out.println(sub.getMaxSubstringLength(s4) == 0);
    }

    /*
     * Complexity - O(n^2) ? But average case looks much better
     */
    public int getMaxSubstringLength(String str) {
	Map<Character,Character> map = new HashMap();
	int maxLength = 0;
	int curLength = 0;
	for (int i=0; i<str.length(); i++) {
	    int j = i;
	    while (j < str.length() && !map.containsKey(str.charAt(j))) {
		map.put(str.charAt(j),str.charAt(j));
		curLength++;
		j++;
	    }
	    if (curLength > maxLength) {
		maxLength = curLength;
	    }
	    curLength = 0;
	    map.clear();
	}
	return maxLength;
    }


}
