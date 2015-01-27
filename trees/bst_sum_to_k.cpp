#include <iostream>
#include <stdlib.h>

using namespace std;

//http://www.careercup.com/question?id=5767892626833408

// Program to find two nodes in a BST that sum to input k

// assumes that nodes have parent pointers
// assumes no duplicates in the bst

// Structure of tree node
struct Node
{
    int value;
    struct Node *left, *right;
};
 
// A utility function to create a new BT node
Node *newNode(char item)
{
    Node *temp =  new Node;
    temp->value = item;
    temp->left = temp->right = NULL;
    return temp;
}


void sum_2_nodes(Node* r1, Node* r2, int k){
	if (r1 == NULL || r2 == NULL)
		return;
	else {
		int i = r1->value + r2->value;
		if (i == k){
			cout << r1->value << "+" << r2->value << endl;
			exit(1);
		}
		else if (i > k)
			sum_2_nodes(r1->left,r2,k);
		else if (i < k)
			sum_2_nodes(r1,r2->right,k);
	}
}

	
void treeSum(Node *root,int k){
	if ((root == NULL) || (root->left == NULL && root->right == NULL))
		return;
	else if (root->left != NULL)
		sum_2_nodes(root->left,root,k);
	else if (root->right != NULL)
		sum_2_nodes(root,root->right,k);
}


int main() {
	int k = 0;
	cout << "Enter a number" << endl;
	cin >> k;

	Node *T = newNode(5);						
    T->left = newNode(3);				
    T->right = newNode(7);	
    T->left->left = newNode(2);
    T->left->right = newNode(4);
    T->right->right = newNode(9);
    T->right->left = newNode(6);

    treeSum(T,k);

	return 0;
}