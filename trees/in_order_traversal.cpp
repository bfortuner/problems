#include <iostream>
#include <stdlib.h>
#include <stack>
using namespace std;


// Structure of tree node
struct Node
{
    char key;
    struct Node *left, *right;
};
 
// A utility function to create a new BT node
Node *newNode(char item)
{
    Node *temp =  new Node;
    temp->key = item;
    temp->left = temp->right = NULL;
    return temp;
}


// function for in-order traversal of a tree
// prints out the contents (Assume each node has 1 piece of content which is an integer). 
 // recursive
void print_inorder(Node *root){
	if (root == NULL)
		return;
	print_inorder(root->left);
	cout << root->key << endl;
	print_inorder(root->right);
}

// // iterative using stacks
// void print_inorder_iter(Node *root){
// 	if (root == NULL)
// 		return;

// 	stack<Node> *tmp = new stack<Node>;
// 	while (tmp->size() > 0 || root != NULL){
// 		if (root == NULL){
// 			Node parent = tmp->Pop();
// 			cout << parent->key << endl;
// 			root = parent->right;
// 		}
// 		else
// 		{
// 			tmp.push(root);
// 			root = root->left;
// 		}
// 	}

// }

int main(){

	Node *T = newNode('a');						//     a
    T->left = newNode('b');						//   b   d
    T->right = newNode('d');					// c       e
    T->left->left = newNode('c');
    T->right->right = newNode('e');

    print_inorder(T);

    cout << "*****************\n";
    cout << "and now iteratively\n";
    cout << "*****************\n";

    //print_inorder_iter(T);	

	return 0;
}