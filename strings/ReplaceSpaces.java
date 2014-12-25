public class ReplaceSpaces {

    public static void main(String[] args) {
    	String in = "This is a space";
    	String out = "This%20is%20a%20space";
    	System.out.println(insertHtmlSpaces(in).equals(out));
    	System.out.println(insertHtmlSpaces2(in).equals(out));
    	System.out.println(insertHtmlSpaces2(in).equals(out));
    }

    public static String insertHtmlSpaces(String str) {
    	return str.replaceAll("[ ]+", "%20");
 	}	

    public static String insertHtmlSpaces2(String str) {
    	return str.replace(" ", "%20");
 	}	

    public static String insertHtmlSpaces3(String str) {
    	String newStr = "";
    	for (int i=0; i<str.length(); i++) {
    		if (newStr.charAt(i) == ' ') {
    			newStr = newStr + "%20";
    		} else {
    			newStr = newStr + str.substring(i,i+1);
    		}
    	}

    	return newStr;
 	}	

}
