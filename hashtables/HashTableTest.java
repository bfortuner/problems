package hashtables;
import java.util.ArrayList;
import java.util.List;
import java.util.LinkedList;
import java.util.Arrays;

public class HashTableTest {

    public static void main(String[] args) {

    	ChainingHashTable hash = new ChainingHashTable();
    	String key = "KEY1";
    	int bucket = hash.getBucketFromKey(key);
    	hash.put(key, "VAL1");
    	hash.put(key, "VAL2");
    	hash.put("KEY3", "VAL3");

		System.out.println("\n------");
		String val1 = hash.get("KEY1");
		System.out.println(val1);

		//hash.remove(key);
		//hash.remove(key);
		System.out.println("------");
		String val2 = hash.get("KEY1");
		System.out.println(val2);

		System.out.println("\n------");
		for (int i=0; i<hash.table.length; i++) {
			Pair tmp = hash.table[i]; 
			if (tmp == null) {
				System.out.println("[ ]");
			}
			while (tmp != null) {
				System.out.print(tmp.getKey() + ":" + tmp.getValue() + " ---> ");
				tmp = tmp.getNext();
			} 
		}
		System.out.println("\n------");

    }


}
