#include <iostream>
#include <stdlib.h>

using namespace std;

// FUll node class 
// template <class T>
// class Node {
// public:
//   Node() : next_(NULL), prev_(NULL) {}
//   Node(const T& v) : value_(v), next_(NULL), prev_(NULL) {}

//   // REPRESENTATION
//   T value_;
//   Node<T>* next_;
//   Node<T>* prev_;
// };

// Quick node class
struct Node {
	int value;
	Node *next;
};
// Creates new nodes
struct Node* newNode(int data)
{
	struct Node* temp = new struct Node;
	temp->value = data;
	temp->next = NULL;
}

// Function to find the size of a list
int find_size(Node *n) {
	int length = 0;
	while(n) {
		length++;
		n=n->next;
	}
	return length;
}

// helper function
Node* add_util(Node* list1, Node* list2, int&carry, int state){
	// if both are NULL we are at end
	if ( list1 == NULL && list2 == NULL) 
		return NULL;
	// create new node to return
	struct Node* new_list = new struct Node;
	new_list = newNode(0);

	// list1 is longer than list2
	if (state > 0){
		// advance list1 and decrease state...then call add_util again
		new_list->next = add_util(list1->next,list2,carry,state-1); 
		// add carry and list1 value
		new_list->value = carry + list1->value; 
	}
	// list2 is longer than list1
	else if (state < 0){
		// only advance list2's pointer and increase state
		new_list->next = add_util(list1,list2->next,carry,state+1);
		new_list->value = carry + list2->value;
	}
	// list1 and list 2 are same length
	else {
		// advance both pointers
		new_list->next = add_util(list1->next, list2->next, carry, 0);
		new_list->value = carry + list1->value + list2->value;
	}

	carry = new_list->value/10;	// calculate new carry
	new_list->value %= 10;		// update current value to be smaller than 10
	return new_list;			// return new node
}


// Function to add two link lists as if they represented numbers
Node* add_lists(Node* list1, Node* list2){
	// find size of lists to determine which condition to use
	int state = find_size(list1) - find_size(list2);
	// variable in case of carry
	int carry = 0;
	Node* new_list = add_util(list1,list2,carry,state);
	if ( carry > 0 ) {
		struct Node* temp = new struct Node;
		temp = newNode(carry);
		temp->next = new_list;
		new_list = temp;
	}
	return new_list;
}

int main(){

	// create 2 Linked lists using Nodes 
	struct Node *head1 = new struct Node;
	struct Node *head2 = new struct Node;

	// Construct linked list 1->2->3
	head1 = newNode(1);
	head1->next = newNode(2);
	head1->next->next = newNode(3);

	// Construct linked list 1->0->1->8
	head2 = newNode(1);
	head2->next = newNode(0);
	head2->next->next = newNode(1);
	head2->next->next->next = newNode(8);

	struct Node * final = add_lists(head1,head2);

	while (final){
		cout << final->value << endl;
		final = final->next;
	}
	// solution should be 1141 
	return 0;
}