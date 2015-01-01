package hashtables;
import java.util.ArrayList;
import java.util.List;
import java.util.LinkedList;
import java.util.Arrays;

public class OpenAddressHashTableTest {

    public static void main(String[] args) {

        OpenAddressHashTable hash = new OpenAddressHashTable();
    	hash.put("KEY1", "VAL1");
        hash.put("KEY1", "VAL2");
    	hash.put("KEY3", "VAL3");

		System.out.println("\n------");
		String val1 = hash.get("KEY1");
		System.out.println(val1);

		hash.remove("KEY1");
		hash.remove("KEY1");
		System.out.println("------");
		String val2 = hash.get("KEY1");
		System.out.println(val2);
        System.out.println("------");
        String val3 = hash.get("KEY3");
        System.out.println(val3);
        System.out.println("------");
        String val4 = hash.get("KEY1");
        System.out.println(val4);

		System.out.println("\n------");
		for (int i=0; i<hash.table.length; i++) {
			Pair tmp = hash.table[i]; 
			if (tmp == null) {
				System.out.println("[ ]");
			} else {
				System.out.println(tmp.getKey() + ":" + tmp.getValue());
			}
		}
		System.out.println("\n------");

    }


}
