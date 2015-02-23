package strings;

public class RotateString {
    
    public static void main(String[] args) {
	RotateString rot = new RotateString();
	String s1 = "abcd";
	System.out.println("cdab".equals(rot.rotate(s1,2)));
	System.out.println("dabc".equals(rot.rotate(s1,5)));
    }

    //Rotate String to the right
    public String rotate(String str, int n) {
	while (n > 0) {
	    str = str.substring(str.length()-1,str.length()) + str.substring(0,str.length()-1);
	    n--;
	}
	return str;
    }


}
