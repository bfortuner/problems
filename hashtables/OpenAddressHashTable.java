package hashtables;
import java.util.ArrayList;
import java.util.List;
import java.util.LinkedList;
import java.util.Arrays;


public class OpenAddressHashTable implements HashTable {

	public Pair[] table;
	public static int BUCKETS = 10;

    public OpenAddressHashTable() {
    	table = new Pair[BUCKETS];
    }

    public void put(String key, String val) {
        Pair p = new Pair(key, val);
    	int bucket = getBucketFromKey(key);
        while (table[bucket] != null && table[bucket].getKey() != "DELETED") {
            bucket++;
        }
        table[bucket] = p;
    }
    
    public String get(String key) {
    	int bucket = getBucketFromKey(key);
        while (table[bucket] != null && table[bucket].getKey() != key) {
            bucket++;
        }
        if (table[bucket] == null) {
            return null;
        } else {
            return table[bucket].getValue();
        }
    }

    public void remove(String key) {
    	int bucket = getBucketFromKey(key);
        while (table[bucket] != null && table[bucket].getKey() != key) {
            bucket++;
        }
        if (table[bucket] != null) {
            Pair deleted = new Pair("DELETED","DELETED");
            table[bucket] = deleted;
        }
    }

    public int getBucketFromKey(String key) {
    	int sum = 0;
    	int ascii;
    	for (int i=0; i<key.length(); i++) {
    		ascii = (int) key.charAt(i);
    		sum = sum + ascii;
    	}
    	return sum % BUCKETS;
    }


}
