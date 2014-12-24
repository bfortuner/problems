public class ReverseString {

    public static void main(String[] args) {
		String in = "abcd";
		String out1 = reverse1(in);
		String out2 = reverse2(in);
		System.out.println(out1);
		System.out.println(out2);
    }

    public static String reverse1(String str) {
		String newStr = "";
		for (int i=str.length()-1; i>=0; i--) {
		    newStr = newStr + str.substring(i,i+1);
		}
		return newStr;
    };
	
    public static String reverse2(String str) {
 		int start = 0;
		int end = str.length()-1;
		String tmp;
		while (start < end) {
			tmp = str.substring(start,start+1);
			str = str.substring(0,start) + str.substring(end,end+1) + 
				str.substring(start+1,end) + tmp + str.substring(end+1,str.length());
			start++;
			end--;
		}
		return str;
    };

}
