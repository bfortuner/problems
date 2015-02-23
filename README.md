boring-stuff
==================

Boring Problems and Solutions :)

##Resources
- http://beust.com/algorithms.pdf
- http://www.codewars.com/dashboard
- http://www.geeksforgeeks.org/
- http://www.problee.com
- http://codingbat.com
- http://codepad.org
- http://crazyforcode.com
- http://www.cs.usfca.edu/~galles/visualization/Algorithms.html

##Problems

###Sorting

1. Selection Sort - Implement and describe complexity
2. [Sort Array012] - Sort an array that contains only the integers 0, 1, and 2 in linear time. (e.g. [1,0,2,2,1] == [0,1,1,2,2]) 
3. Insertion Sort - Implement and describe complexity
4. Bubble Sort - Implement and describe complexity
5. Counting Sort - Implement and describe complexity
6. [Bucket Sort] - Implement and describe complexity
7. Merge Sort - Implement and describe complexity
8. Quick Sort - Implement and describe complexity
9. Heap Sort - Implement and describe complexity
10. Shell Sort - Implement and describe complexity

###Searching

1. Binary Search - Write method to return True if integer is in array
2. Binary Search w Pivot - An element in a sorted array can be found in O(log n) time via binary search. But suppose I rotate the sorted array at some pivot unknown to you beforehand. So for instance, 1 2 3 4 5 might become 3 4 5 1 2. Devise a way to find an element in the rotated array in O(log n) time. If not found, return -1.

###Arrays

1. Sum3EqualsZero - Given array of integers, return true if any 3 elements in array sum to zero
2. [MaxContigSumArray] - Given array of integers, return max sum of contiguous elements in array. Write iterative and recursive solutions.
3. MaxSum3Array - Given array of integers, return max sum of 3 element subset
4. SetMatrixToZero - If an element in a M x N matrix is zero, set its entire row and column to zero.
5. FindOnesInMatrix - Given a 2D SORTED matrix, return the row index with the most ones
6. MajorityElement - given a array of integers, print out the element that appears more than n/2 times. Otherwise print not found.
7. [Platforms Train Station] - Given arrival and departure times of all trains that reach a railway station, find the minimum number of platforms required for the railway station so that no train waits. We are given two arrays which represent arrival and departure times of trains that stop. Input:  arr[]  = {9:00,  9:40, 9:50,  11:00, 15:00, 18:00}, dep[]  = {9:10, 12:00, 11:20, 11:30, 19:00, 20:00}, Output: 3. There are at-most three trains at a time (time between 11:00 to 11:20)

###Strings

1. IsAnagram - Return true if two strings are anagrams (each string contains the exact same alpha-numeric characters and the same count)
2. RemoveDuplicates - Given String of alpha-numeric characters, return String of distinct characters
3. ReverseString - Given String, return String with characters in reverse order
4. ReplaceSpaces - Given String, replace all spaces with HTML '%20'
5. IsRotation - Return true if str2 is rotation of str1
6. ReverseStringInplace - Reverses a string inplace
7. [FindFirstUniqueChar] - Return the first non-repeated character in a string. If not found, return null. Assume the string is NOT sorted. 
8. ReverseWords - Given a sentence, return the sentence in reverse order. (e.g. "I am a student" == "student a am I")

###Math

1. PowersOfTwo - Compute 2^2^n in linear time
2. Swap Integers - Swap two integers in an array without using temporary variables
3. [Sum Two Arrays] - Write method to sum 2 arrays and return a new array. Arrays can be of different lengths. e.g. [1,3] + [1,0,0] == [1,1,3]
4. Smallest Number > k - Write method to find the smallest number which is greater than a given number k and has SAME SET OF DIGITS as given number
5. [Find Missing Integer] - Given an array of sorted consecutive integers, return the missing integer (or -1 if no integer is missing). E.g. [3,4,6,7] == 4. Complete solutions in both O(n) and O(log n) time. Follow-up: write a method that handles an unsorted array of integers between 0 and N in O(N) time. e.g. [3,5,7,4] == 6 
6. [P99 Website Latency] - Given an unsorted array of floats between 0 and 1, representing website latency times, return the 99th percentile time (the time that is greater than 99% of other times). This is an important metric in software development to identify worst case issues for users. Follow-up: Instead of an array, assume you are receiving an infinite stream of latency times and can't store them all. Create a Class to return the P99 at any given moment (methods void putTime(double time), double getP99()). Follow-up: Update your methods to handle variable percentiles (60th, 85th) and latency ranges (3 - 7 seconds).  

###Hash Tables

1. Open Addressing - Write a HashTable class that uses "linear probing" to resolve collisions (methods Get, Put, Remove)
2. [Chaining] - Write a HashTable class that uses LinkedLists to resolve collisions (methods Get, Put, Remove)
3. Dynamic Resizing - Add dynamic resizing to either above implementations

###Linked Lists

1. Double Linked List - Implement a Doubly Linked List
2. Remove Duplicates - Remove duplicates from an unsorted Single Linked List
3. Delete Node - Delete node in middle of Single Linked List given access to only that node
4. [Is Circular] - Return true if single linked list is circular (corrupted)
5. Circular Node - Find the first node in a circular single linked list
6. Sum Two Lists - Add two numbers together. Each number's digits are stored in a Single Linked List in reverse order (e.g. 134 == 4 --> 3 --> 1) ** also done in c++ ** 
7. Find Intersection of Two lists - Given two lists, find the node at which they intersect and become one list
8. Linked List Basics - Series of easy problems that cover linked lists    
9. [Reverse Linked List] - Write Iterative and Recursive Solutions that reverse a linked list and return the new first node

###Recursion

1. Fibonacci - Write method to generate the nth fibonacci number
2. Robot Squares - Imagine a robot sitting on the upper left hand corner of an NxN grid. The robot can only move in 2 directions: right and down. How many possible paths are there for the robot?
3. String Permutations - Compute all permutations of a given string
4. [Powerset] - Return all possible subsets of a set (Recursive solution, Iterative, Bit Manipulation no loops)
5. [PowersetM] - Return all subsets of a set having M elements (Recursive, Iterative)
6. Valid Parentheses Pairs - Print all valid (e.g. properly opened and closed) combinations of n-pairs of parentheses. Input: 3, Output: ((())), (()()), (())(), ()(()), ()()()
7. Cents Combos - Given an infinite number of coins (25 cents, 10, 5, 1), return the number of possible ways of representing N cents.
8. Paint Fill - Implement the "paint fill" function one might see on an image editing program. Given a 2 dimensional matrix array of Colors, fill in the surrounding area until you hit a border or another filled-in square.

###Trees
1. Count Nodes at k distance - Given a binary tree, print the nodes k distance away from a target node
2. Implement Tree - That stores integers and has methods getParent(), setParent(), getChildren(), addChild(), removeChild(), getValue(), setValue()
3. Implement BinaryTree - That stores Strings with methods setParent, setValue, setLeftChild, setRightChild
4. Parse Tree Equation - Use BinaryTree to implement a mathematical equation parser. From equations list this, (3 + (4 * 5)), return a Binary tree that holds this equation
5. Tree Traversals - Write methods to print out root nodes using PreOrder, InOrder, and PostOrder algorithms
6. First Common Ancestor - Find the first common ancestor of two nodes in a binary tree. Avoid using additional data structures if possible. *** Java and CPP solutions
7. Min Height Tree - Given a sorted Array of Strings build the Binary Search Tree of minimal height.
8. Binary Search Tree - Implement a Binary Search Tree with methods Get(), Put(), and Delete()
9. Sub Tree of Binary Tree - Given two binary trees, S and T, determine if S is a subtree of T.
10. In Order Traversal of binary tree
11. Sum of 2 Nodes in BST- Given a binary search tree and an integer k, find two nodes whose values sum up to k.
12. Is Subtree - Assume you have two Binary Trees--t1 has millions of nodes and t2 has hundreds of nodes. Return true if t2 is a subtree of t1 (i.e. root of t2 is a node in t1)
13. Find_paths - Given a binary tree and an integer k, print all paths that sum up to k
14. Build Binary Search Tree - Given an array of strings, build a binary search tree. You can use the BinaryTree helper class.
15. Print Path To Key - You are given a Binary Search Tree. Write an algorithm to print the Path Array of a given key. PATH ARRAY:
a) If the given key is not present in the tree than the Path Array is equal to “-1”
b) If the given key is present in the BST, path array tells you the path (in terms of left & right direction) that you take from root to reach the given key. If you go towards right add “0” to the path array and if you go towards left add “1” to Path Array.
16. [Expression Tree] - Implement a method that builds a binary tree given an infix expression like (7+3)*2. Write a second method to return the expression String given a binary tree. Write a third method that takes a postfix expression like 73+2* and returns a binary tree. Terms in the expression are separated by spaces.
17. [Mirror Tree] - Write a method that takes a Binary Tree and returns a mirror image of that tree (i.e. all the left sides are on the right and vis versa). 
18. [Max Weight Subtree] - Given a BinaryTree, write a method that returns the substree of maximum weight. Each node in the subtree carries an integer (+/-) value which represents that node's weight.

###Stacks
1. Implement Stack - Push and Pop methods
2. Single Array - Implement 3 stacks using a single array
3. Set of Stacks - Consider a Stack of plates. If one stack gets too high, create a new stack of plates. Implement a special stack that holds these multiple stacks. When the first stack passes some threshold, the class creates a new stack and continues. Implement both Push and Pop methods.
4. Towers of Hanoi - 
5. Sort Stack - Write a method to sort a stack in ascending order using Push, Pop, Peek, and IsEmpty.

###Queues
1. Implement Queue - Enqueue and Dequeue methods
2. Queue With Stacks - Implement a queue using 2 Stacks

###Heaps
1. Binary Heap - Implement a Binary Heap of integers with methods - isEmpty(), getSize(), getMin(), deleteMin(), buildBinaryTreeFromList(), insertElement()
2. Binary Heap in CPP - ""

###Graphs
1. Implement a Directed Graph using the Adjacent List technique
2. BFS - Find the Vertex in a Graph that holds the key "E" using Breadth First Search.
3. DFS - Implement Recursive and Iterative versions of Depth-First Search, which visit and print out every Vertex in Graph
4. Topological Sort - Implement Recursive (DFS) and Iterative versions of Topological Sort
5. [Chess Moves] - Write a class that calculates the minimum number of moves required to move from point A to point B on a 10x10 chess board. Implement methods to handle moves for Rook, Queen, King, and Knight.
6. [Amazon Locker] - Write a method to find the nearest Amazon locker, given a starting Vertex, which has methods getNeighbors() and isLocker(). The graph can be infinitely big, and you don't know the location of the amazon lockers. 


###Design
1. [Parking Lot] - Model an OOP design for an attendant-less parking lot. To start, walk through the entire customer experience, keeping track of each time software is required.


*[Brackets] highlight questions that we were asked in an interview 