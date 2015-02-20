package strings;

import java.util.*;

public class ReverseWords {
    
    public static void main(String[] args) {
	String in = "I am a student";
	String out = "student a am I";
	System.out.println(out.equals(reverseSentence(in)));
	System.out.println(out.equals(reverseSentenceArray(in)));
    }

    public static String reverseSentence(String str) {
	String reverse = "";
	int i = 0;
	while(i < str.length()) {
	    int j=i;
	    while (j<str.length() && str.charAt(j) != ' ') {
		j++;
	    }
	    reverse = " " + str.substring(i,j) + reverse;
	    i=j+1;
	}
	return reverse.substring(1,reverse.length());
    }

    public static String reverseSentenceArray(String str) {
	String reverse = "";
	String[] arr = str.split(" ");
	int i = arr.length-1;
	while (i >= 0) {
	    reverse = reverse + arr[i] + " ";
	    i--;
	}
	return reverse.substring(0,reverse.length()-1);
    }


}
