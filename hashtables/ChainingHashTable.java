package hashtables;
import java.util.ArrayList;
import java.util.List;
import java.util.LinkedList;
import java.util.Arrays;


public class ChainingHashTable implements HashTable {

	public Pair[] table;
	public static int BUCKETS = 10;

    public ChainingHashTable() {
    	table = new Pair[BUCKETS];
    }

    public void put(String key, String val) {
        Pair p = new Pair(key, val);
    	int bucket = getBucketFromKey(key);    	
        if (table[bucket] == null) {
            table[bucket] = p;
        } else {
            Pair next = table[bucket];
            while (next.getNext() != null) {
                next = next.getNext();
            }
            next.setNext(p);
        }
    }
    
    public String get(String key) {
    	int bucket = getBucketFromKey(key);
        if (table[bucket] == null) {
            return null;
        } else {    
            Pair tmp = table[bucket];
            while (tmp.getKey() != key) {
                tmp = tmp.getNext();
            }
            if (tmp == null) {
                return null;
            } else {
                return tmp.getValue();
            }
        }
    }

    public void remove(String key) {
    	int bucket = getBucketFromKey(key);
        Pair prior = table[bucket];
        Pair cur = table[bucket];
        if (cur.getKey() == key) {
            table[bucket] = cur.getNext();
        } else {
            while (cur.getKey() != key) {
                prior = cur;
                cur = cur.getNext();
           }
           prior.setNext(cur.getNext());
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
