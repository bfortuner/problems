import java.util.HashMap;
import java.util.Map;

public class RemoveDuplicates {

    public static void main(String[] args) {
	String in = "aaabddaeg";
	String out = removeDuplicates(in);
	System.out.println(out);
    }
 
    public static String removeDuplicates(String str) {
	Map<Character,Character> map = new HashMap<Character,Character>();
	String newStr = "";
	for (int i=0; i<str.length(); i++) {
	    char c = str.charAt(i);
	    if (map.get(c) == null) {
		map.put(c,c);
		newStr = newStr + String.valueOf(c);
	    }
	}
	return newStr;
    }

}
