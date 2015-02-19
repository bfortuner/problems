package javalang;

import java.util.ArrayList;
import java.util.List;
import java.io.*;  //InputStream, InputStreamReader, BufferedReader
import math.Counter;
import java.util.*;

public class Hello {
    
    public int count = 0;

    public static void main(String[] args) {

        System.out.println("Hello World!");
	System.out.println(Integer.toBinaryString(8));

	List<String> l1 = new ArrayList();
	l1.add("A");
	l1.add("B");
	l1.add("C");
	List<String> l2 = new ArrayList(l1);
	for (String s : l2) {
	    System.out.println(s);
	}

	int i = 4;
	String iStr = String.valueOf(i);
	System.out.println(iStr instanceof String);

	Integer iInt = Integer.parseInt(iStr);
	System.out.println(iInt instanceof Integer);

	Double j = 4.5;
	String dStr = Double.toString(i);
	System.out.println(dStr instanceof String);

	Double doub = Double.parseDouble(dStr);
	System.out.println(doub instanceof Double);

	String f = "README.md";
	readFile(f);

	System.out.println("=====================");
	
	String s = "A";
	changeStr(s);
	System.out.println(s.equals("A"));

	Counter c = new Counter();
	increment(c);
	System.out.println(c.count);

	testGetListSublist();

	testArrayEquality();
    }

    public static void changeStr(String s) {
	s = "e";
    }

    public static void increment(Counter c) {
	c.count = 3;
    }

    public static void readFile(String filename) {
	try {
	     InputStream input = new FileInputStream(filename);
	     InputStreamReader reader = new InputStreamReader(input);
	     BufferedReader buffer = new BufferedReader(reader);
	     String line = buffer.readLine();
	     while (line != null) {
		 System.out.println(line);
		 line = buffer.readLine();
	     }
	} catch (IOException e) {
	    //do nothing
	}	
    }

    public static void testAutoBoxing() {
	//This will generate an error
	//List<int> list = new ArrayList();
    }

    public static void testCreateGenericArray() {
	List<String>[] list = (List<String>[]) new ArrayList[10];
	//need to case the list first
    }

    public static void testGetListSublist() {
	List<String> list = new ArrayList();
	list.add("a");
	list.add("b");
	list.add("c");
	list.add("d");
       
	List<String> sublist = list.subList(1,3);
	System.out.println(sublist.size() == 2);
    }

    public static void testArrayEquality() {
	System.out.println("Testing Array Equality -----");
	int[] arr1 = {1,2,3};
	int[] arr2 = {1,2,3};
	System.out.println((arr1 == arr2) == false);
	System.out.println(arr1.equals(arr2) == false);
	System.out.println(Arrays.equals(arr1,arr2) == true);

    }

}
