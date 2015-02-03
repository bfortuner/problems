#include <iostream>
#include <stdlib.h>
#include <math.h>

using namespace std;

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

struct Node* find_intersection(Node *L1, Node *L2){
	if (L1 == NULL || L2 == NULL)
		return NULL;
	int size1=0;
	int size2=0;
	
	Node* tmp1 = L1;
	Node* tmp2 = L2;
	// find sizes of the lists
	while (tmp1->next != NULL){
		tmp1=tmp1->next;
		size1++;
	}
	while (tmp2->next != NULL){
		tmp2=tmp2->next;
		size2++;
	}
	tmp1=L1;
	tmp2=L2;
	int difference = abs(size1-size2);
	//make the lists the same size 
	if (size1 > size2){
		for (int x=0;x<difference;x++)
			tmp1=tmp1->next;
	}
	if (size2 > size1){
		for (int x=0;x<difference;x++)
			tmp2=tmp2->next;
	}
	// move both pointers through lists until they are the same node
	while (tmp1->next!=NULL && tmp2->next!= NULL){
		if (tmp1 == tmp2){
			cout << "success!\n";
			return tmp1;
		}
		tmp1=tmp1->next;
		tmp2=tmp2->next;
	}

	cout << "no intersection found" << endl;
	return NULL;
}

int main(){
	// create 2 Linked lists using Nodes 
	struct Node *head1 = new struct Node;
	struct Node *head2 = new struct Node;
	// Construct linked list 1->0->1->8
	head2 = newNode(1);
	head2->next = newNode(0); 
	head2->next->next = newNode(1);
	head2->next->next->next = newNode(8);

		// Construct linked list 1->2->1->8
		// where the second 1 is the intersection
	head1 = newNode(1);
	head1->next = newNode(2);
	head1->next->next = head2->next->next;

	find_intersection(head1,head2);

	return 0;
}