public class IsRotation {

    public static void main(String[] args) {
        String str1 = "abcd";
        String str2 = "cdab";

        String str3 = "abcd";
        String str4 = "cdba";

        String str5 = "abcd";
        String str6 = "cccc";

        System.out.println(isRotation(str1, str2));
        System.out.println(isRotation(str3, str4));
        System.out.println(isRotation(str5, str6));

    }

    /*
     * Return true if str1 is a rotation of str1
     */
    public static boolean isRotation(String str1, String str2) {
        int start = 0;
        while (start < str2.length()) {
            if (str1.charAt(0) == str2.charAt(start)) {
                boolean found = true;
                int i = 0;
                int j = start;
                while (i < str1.length()) {
                    if (str1.charAt(i) != str2.charAt(j)) {
                        return false;
                    } else if (j + 1 == str1.length()) {
                        j = 0;
                        i++;
                    } else {
                        j++;
                        i++;
                    }
                }
                if (found) {
                    return true;
                }
            }
            start++;
        }
        return false;

    }

}
