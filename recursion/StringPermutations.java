package recursion;
import java.util.ArrayList;
import java.util.List;

public class StringPermutations {

    public static List<String> perms = new ArrayList();

    public static void main(String[] args) {
	getPermutations("ABC","");
	printArrayList(perms);
	System.out.println(perms.size()==6);

	perms.clear();
	getPermutations("ABCD","");
	//printArrayList(perms);
	System.out.println(perms.size()==24);

	perms.clear();
	getPermutations("ABCDE","");
	//printArrayList(perms);
	System.out.println(perms.size()==120);
    }

    /*
     *
     */
    public static void getPermutations(String str, String cur) {
	if (str.length() == 0) {
	    perms.add(cur);
	} else {
	    for (int i=0; i<str.length(); i++) {
		String tmp = cur + str.substring(i,i+1);
		getPermutations(str.substring(0,i) + str.substring(i+1,str.length()), tmp);
	    }
	}
    }

    public static void printArrayList(List<String> arr) {
	for (String s : arr) {
	    System.out.println(s);
	}
    }

}
