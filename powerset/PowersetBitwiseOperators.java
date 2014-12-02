import java.util.List;
import java.util.ArrayList;
import java.lang.Math;

public class PowersetBitwiseOperators {

    public static void main(String[] args) {
	testNextMCalc();
    }

    public static void testNextMCalc() {
	List<String> vals = new ArrayList<String>();
	List<String[]> clumpVals = new ArrayList<String[]>();
	String[] array = {"00000100","00001000"};
	clumpVals.add(array);
	String[] array1 = {"00001111","00010111"};
	clumpVals.add(array1);
	String[] array2 = {"00000110","00001001"};
	clumpVals.add(array2);
	String[] array3 = {"00110100","00111000"};
	clumpVals.add(array3);
	String[] array4 = {"00101010","00101100"};
	clumpVals.add(array4);
	String[] array5 = {"01100000","10000001"};
	clumpVals.add(array5);
	String[] array6 = {"01100111","01101011"};
	clumpVals.add(array6);
	String[] array7 = {"00000001","00000010"};
	clumpVals.add(array7);
	String[] array8 = {"01100110","01101001"};
	clumpVals.add(array8);
	String[] array9 = {"00100101","00100110"};
	clumpVals.add(array9);
	String[] array10 = {"00111110","01001111"};
	clumpVals.add(array10);
	String[] array11 = {"00100101","00100110"};
	clumpVals.add(array11);
	String[] array12 = {"01101110","01110011"};
	clumpVals.add(array12);
        String[] array13 = {"01110110","01111001"};
        clumpVals.add(array13);

	for (String[] clump : clumpVals) {
            String in = clump[0];
            String out = clump[1];
	    System.out.print(in + " -> ");
	    String answer = getNextSetM(in); 
            System.out.println("\n" + answer + " == " + answer.equals(out) + "\n========");
	}
    }


    public static String getNextSetM(String bitsStr) {
	int num = binaryStrToInt(bitsStr);
	
	// Get lowest bit
	// 01101110
	// 01101101 unset lowest bit
	// 00000010 get XOR with num to get unset bit
	int lowBit = ( num & (num-1) ) ^ num;
	
	// Get highest bit of lowest clump
	// 01101110
	// 01001000  // get highest bits of all clumps
	int highBit = ~(num>>1) & num;
	// 00001000  // get lowest remaining bit
	highBit = ( highBit & (highBit-1) ) ^ highBit;
	
	// Get Right side of new set
	// find starting point of new set's bottom clump select everything to right
	// 00001010 // 18 / 2 == 4
	// 00000011 // 4 - 1 == 3
	int rightSide = (highBit / lowBit)-1;  //division returns size of clump
	
	// Get Left Side of new Set
	// create left mask to clear everything right of highBit
	// and return everything to the left of highBit<<1
	// 01010011
	// 01100000
	int leftSide = highBit<<1 | ( ~((highBit<<1) - 1) & num );
	
	return intToNBitBinaryStr(leftSide | rightSide, 8);
    }


    /* 
     * Convert integer, i, to binary string of min digits, pad
     */
    public static String intToNBitBinaryStr(int i, int n) {
	String binStr = Integer.toBinaryString(i);  // get x-digit binary string from int
	binStr = String.format("%" + Integer.toString(n) + "s", binStr).replace(' ', '0');   //add minimum zero-padding to always return n-bit string
	binStr = binStr.substring(binStr.length()-n, binStr.length());  //grab last n digits b/c java represents binary in 64 digits
        
        return binStr;
    }

    
    /*
     * Convert binary string to base 10 integer
     */
    public static int binaryStrToInt(String binStr) {
	int newInt = Integer.parseInt(binStr, 2);
	
	return newInt;
    }    


}
