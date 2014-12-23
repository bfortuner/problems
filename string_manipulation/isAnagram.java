public class isAnagram {

    public static void main(String[] args) {
        String in1 = "abcd";
        String in2 = "dcab";
        System.out.println(isAnagram(in1, in2));

        String in3 = "acdbb";
        String in4 = "dcab";
        System.out.println(isAnagram(in3, in4));

        String in5 = "acd";
        String in6 = "cada";
        System.out.println(isAnagram(in5, in6));

    }

    public static boolean isAnagram(String str1, String str2) {
        for (int i=0; i<str1.length(); i++) {
            boolean found = false;
            int j = 0;
            while ( !found && j < str2.length() ) {
                if ( str2.charAt(j) == str1.charAt(i) ) {
                    found = true;
                } else {
                    j++;
                }
            }
            if (!found) {
                return false;
            } else {
                str2 = str2.substring(0,j) + str2.substring(j+1,str2.length());
            }
        }
        
        if ( str2.length() > 0 ) {
            return false;
        } else {
            return true;
        }   
   }


}
