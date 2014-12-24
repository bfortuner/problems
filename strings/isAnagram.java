import java.util.Arrays;

public class isAnagram {

    public static void main(String[] args) {
        String in1 = "abcd";
        String in2 = "dcab";
        System.out.println(isAnagram(in1, in2));
        System.out.println(isAnagramArray(in1, in2));
        System.out.println(isAnagramBitwise(in1, in2));
        System.out.println(isAnagramSort(in1, in2));

        String in3 = "acdbb";
        String in4 = "dcab";
        System.out.println(isAnagram(in3, in4));
        System.out.println(isAnagramArray(in3, in4));
        System.out.println(isAnagramBitwise(in3, in4));
        System.out.println(isAnagramSort(in3, in4));

        String in5 = "acd";
        String in6 = "cada";
        System.out.println(isAnagram(in5, in6));
        System.out.println(isAnagramArray(in5, in6));
        System.out.println(isAnagramBitwise(in5, in6));
        System.out.println(isAnagramSort(in5, in6));

        String in7 = "aaabbbef";
        String in8 = "bbbbeeef";
        System.out.println(isAnagram(in7, in8));
        System.out.println(isAnagramArray(in7, in8));
        System.out.println(isAnagramBitwise(in7, in8));
        System.out.println(isAnagramSort(in7, in8));

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

    public static boolean isAnagramArray(String str1, String str2) {
        int[] arr = new int[256];
        for (int i=0; i<str1.length(); i++) {
            int ascii = (int) str1.charAt(i);
            arr[ascii]++;
        }
        for (int j=0; j<str2.length(); j++) {
            int ascii = (int) str2.charAt(j);
            arr[ascii]--;
        }
        for (int k : arr) {
            if (k != 0) {
                return false;
            }
        }
        return true;
    }

    public static boolean isAnagramBitwise(String str1, String str2) {
        if (str1.length() != str2.length()) {
            return false;
        }
        int x = 0;
        for (int i=0; i<str1.length(); i++) {
            int a1 = (int) str1.charAt(i);
            int a2 = (int) str2.charAt(i);
            x = x ^ a1;
            x = x ^ a2;
        }
        return x == 0;
    }

    public static boolean isAnagramSort(String str1, String str2) {
        //convert String to array
        char[] arr1 = str1.toCharArray();
        char[] arr2 = str2.toCharArray();

        //sort array
        java.util.Arrays.sort(arr1);
        java.util.Arrays.sort(arr2);

        //convert back to String
        str1 = new String(arr1);
        str2 = new String(arr2);

        return str1.equals(str2);
    }

}
